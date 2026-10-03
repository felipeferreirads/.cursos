# Aula 03: Cartografia hidrogeológica — sistemas de fluxo, recarga, descarga e relação rio-aquífero

**ID:** geologia-avancado-m01-a03
**Módulo:** [[01-hidrogeologia-recursos-hidricos-modulo|Módulo 01 — Hidrogeologia e recursos hídricos]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** interpretar um mapa potenciométrico e uma rede de fluxo para identificar áreas de recarga e descarga, reconhecer os sistemas de fluxo local, intermediário e regional de Tóth, e classificar a interação entre um rio e o aquífero adjacente.

## Antes de começar, você precisa saber

- Carga hidráulica h = z + ψ, lei de Darcy e o sentido do fluxo de carga alta para carga baixa — Aula 02 deste módulo.
- Curvas de nível topográficas e a lógica de um mapa de contorno (isolinhas).
- Noção de bacia hidrográfica como divisor de águas superficial.

## Conteúdo

### O mapa potenciométrico: a topografia invisível que comanda o fluxo

Um **mapa potenciométrico** (ou mapa de isopotenciais) contorna a carga hidráulica h medida em uma rede de poços/piezômetros num mesmo aquífero, num mesmo instante (ou média de um período). É o equivalente hidrogeológico de um mapa topográfico: as **linhas equipotenciais** unem pontos de igual carga, exatamente como curvas de nível unem pontos de igual altitude. E, como a água flui de carga alta para carga baixa, o fluxo em meio isotrópico é sempre **perpendicular às equipotenciais**, apontando da carga maior para a menor — permitindo desenhar **linhas de fluxo** diretamente sobre o mapa.

A construção de um mapa potenciométrico confiável exige que todos os poços amostrem o **mesmo aquífero** (ou intervalo confinado equivalente) e, idealmente, sejam medidos em condição de equilíbrio (sem bombeamento ativo nas proximidades) e no mesmo intervalo de tempo — cargas de estações diferentes do ano podem diferir vários metros num mesmo poço e produzir um mapa artificialmente distorcido se misturadas.

> [!important] Mapa potenciométrico não é mapa de profundidade do nível d'água
> São dois produtos diferentes, com usos diferentes. O mapa de profundidade do nível d'água (distância do solo até a água) serve para planejar perfuração e para avaliar vulnerabilidade a contaminação (Módulo 03). O mapa potenciométrico (carga hidráulica absoluta, referida a um datum) é o que revela a direção e o sentido do fluxo — o gradiente da carga, não a profundidade em si.

### Anisotropia e o desvio do fluxo em relação ao gradiente

A perpendicularidade estrita entre linhas de fluxo e equipotenciais só vale em meio **isotrópico** (K igual em todas as direções). Em meio **anisotrópico** — a regra, não a exceção, em sedimentos estratificados, onde Kh > Kv (Aula 01) — as linhas de fluxo se desviam da perpendicular às equipotenciais, tanto mais quanto maior a razão de anisotropia e mais oblíquo o gradiente em relação às direções principais de K. Ignorar esse desvio ao traçar linhas de fluxo à mão é um erro sistemático em aquíferos estratificados com contraste de K forte entre camadas.

### O modelo de Tóth: fluxo local, intermediário e regional

József Tóth (1963) formalizou, com solução analítica de um domínio de bacia sedimentar com topografia ondulada, um resultado que reorganizou a hidrogeologia regional: **a topografia do terreno controla a hierarquia dos sistemas de fluxo subterrâneo.** Em uma bacia com relevo suave, coexistem tipicamente três escalas de fluxo, superpostas:

- **Sistema de fluxo local**: recarrega numa elevação topográfica local e descarrega na depressão topográfica adjacente (o vale mais próximo) — percurso curto, tempo de trânsito curto (dias a décadas), sensível a variações sazonais de recarga.
- **Sistema de fluxo intermediário**: atravessa uma ou mais ondulações topográficas menores antes de descarregar — percurso e tempo de trânsito intermediários.
- **Sistema de fluxo regional**: recarrega no divisor topográfico principal da bacia e descarrega no ponto topográfico mais baixo de toda a bacia (o rio principal, um lago terminal, a linha de costa) — percurso longo, tempo de trânsito longo (séculos a dezenas de milhares de anos), pouco sensível a variações sazonais.

> [!note] Consequência prática direta
> Um poço posicionado numa mesma área de superfície pode captar água de sistemas de fluxo completamente diferentes dependendo da profundidade: raso, capta o sistema local (química mais jovem, mais reativa à recarga recente, mais vulnerável a contaminação de superfície); profundo, pode captar o sistema regional (água mais antiga, quimicamente mais evoluída, tipicamente mais protegida — tema desenvolvido no Módulo 02 de hidrogeoquímica). Um mesmo local geográfico não implica uma mesma "água subterrânea".

A razão física por trás da hierarquia é geométrica: relevo de pequena amplitude e curto comprimento de onda gera predominantemente sistemas locais rasos; relevo de grande amplitude relativa à espessura da bacia favorece o desenvolvimento de sistema regional profundo que pode até suprimir os sistemas locais (condição de "recarga através", em que praticamente toda a área é de recarga para o sistema regional). A razão profundidade-da-bacia/comprimento-da-bacia e o contraste de K entre camadas (aquíferos-aquitardos alternados favorecem sistemas mais compartimentados e locais) são os dois parâmetros de controle mais citados na literatura subsequente a Tóth (Freeze & Witherspoon, 1967).

### Identificando áreas de recarga e de descarga no mapa

Áreas de **recarga** apresentam, tipicamente: nível d'água mais profundo, componente de fluxo com direção descendente (carga hidráulica decrescendo com a profundidade em poços aninhados no mesmo local), e posição topográfica relativamente elevada. Áreas de **descarga** apresentam o padrão espelhado: nível d'água raso ou aflorante (nascentes, banhados, o próprio leito de um rio ganhador), componente de fluxo ascendente, e posição topográfica baixa.

O critério mais robusto em campo é o de **poços aninhados** (nested piezometers): dois ou mais piezômetros no mesmo local geográfico, com trechos filtrantes a profundidades diferentes no mesmo aquífero ou em aquíferos empilhados. Se a carga cai com a profundidade, o fluxo vertical é descendente → recarga. Se a carga sobe com a profundidade, o fluxo é ascendente → descarga. Esse teste é mais confiável que inferir recarga/descarga só pela topografia, porque condições geológicas locais (janelas em camadas confinantes, falhas condutoras) podem inverter o padrão esperado.

### A relação rio-aquífero

Um curso d'água superficial e o aquífero adjacente trocam água por um dos três regimes, definidos pela relação entre a carga hidráulica do aquífero junto à margem e o nível da lâmina d'água do rio:

- **Rio efluente (ganhador, gaining stream)**: a carga do aquífero é maior que o nível do rio → água subterrânea flui *para* o rio, alimentando o **escoamento de base** (baseflow) que sustenta a vazão em período seco. É o regime dominante em climas úmidos e em trechos de vale profundamente entalhados no aquífero.
- **Rio influente (perdedor, losing stream)**: o nível do rio é maior que a carga do aquífero adjacente → água do rio infiltra e recarrega o aquífero. Comum em regiões áridas/semiáridas e em trechos onde o rio corre sobre um cone aluvial ou terraço elevado em relação ao nível freático regional.
- **Rio desconectado**: quando o rebaixamento do nível freático (natural, por bombeamento intensivo, ou por incisão do canal) supera a espessura saturada abaixo do leito, forma-se uma zona não saturada contínua entre a base do rio e o topo do nível freático. Nesse regime, a taxa de infiltração deixa de depender da carga do aquífero (que caiu abaixo do controle) e passa a depender só da carga do próprio rio e da condutividade do leito — a infiltração atinge um valor máximo, praticamente constante, mesmo que o aquífero continue rebaixando. É o estágio mais avançado (e mais difícil de reverter) de estresse hídrico induzido por bombeamento excessivo perto de um rio.

Um mesmo rio frequentemente alterna entre efluente e influente ao longo do seu curso, e mesmo sazonalmente no mesmo trecho — efluente na estação chuvosa (nível freático alto), influente na seca (nível freático rebaixado abaixo do nível do rio). A **separação de hidrograma** (base-flow separation), técnica que decompõe a vazão de um rio numa componente de escoamento superficial rápido e numa componente de escoamento de base sustentado pelo aquífero, é a ferramenta quantitativa padrão para estimar a contribuição subterrânea à vazão fluvial ao longo do ano — e, por extensão, para estimar a taxa de recarga de bacia por balanço hídrico (retomado na Aula 06).

## Exemplo trabalhado

**Situação:** um mapa potenciométrico de um aquífero livre mostra equipotenciais que descrevem uma curva fechada, tipo domo, em torno de uma serra, e outra curva fechada, tipo depressão, coincidindo com um vale onde há brejos permanentes. Dois piezômetros aninhados na base da serra (30 m e 90 m de profundidade, mesmo aquífero) registram cargas de 210 m e 205 m, respectivamente. Classifique as duas feições e o regime de fluxo vertical na base da serra.

**Raciocínio.** O domo de carga sobre a serra é uma área de **recarga**: carga hidráulica máxima coincide com a maior cota topográfica, e o fluxo diverge radialmente dali (perpendicular às equipotenciais, apontando para fora do domo, de carga alta para carga baixa). A depressão de carga no vale com brejos é uma área de **descarga**: carga mínima, convergência das linhas de fluxo, nível d'água aflorante compatível com brejo permanente — assinatura clássica de descarga subterrânea sustentando um ecossistema úmido topograficamente baixo. Na base da serra, o piezômetro raso (30 m) tem carga de 210 m e o profundo (90 m) tem 205 m — a carga *diminui* com a profundidade, logo o fluxo vertical ali é **descendente**, consistente com estar ainda dentro (ou na borda) da área de recarga, água ainda descendo para se juntar ao sistema de fluxo mais profundo antes de eventualmente convergir para a descarga do vale.

**A lição:** a mesma lógica de "carga alta → carga baixa" que organiza o mapa em planta organiza também o perfil vertical num par de poços aninhados; os dois são a mesma pergunta (onde está a carga maior?) aplicada em dimensões diferentes.

## Erros comuns

- **Inferir recarga/descarga só pela topografia, sem verificar poços aninhados.** Estruturas geológicas locais (falhas, janelas em confinantes) podem inverter o padrão esperado pela topografia simples.
- **Traçar linhas de fluxo estritamente perpendiculares às equipotenciais em meio conhecidamente anisotrópico.** Introduz erro sistemático de direção proporcional à razão de anisotropia.
- **Assumir que um rio é sempre efluente ou sempre influente ao longo de todo o seu curso e do ano todo.** A relação rio-aquífero é local e sazonal; classificar um rio inteiro com um único rótulo ignora essa variabilidade.
- **Misturar medições de cargas de épocas diferentes do ano na mesma malha de contorno**, produzindo um mapa que mistura condições de recarga e de estiagem e não representa nenhum estado real.

### Rio desconectado: um caso à parte

Um erro conceitual específico merece destaque: tratar um rio desconectado como "muito influente" — na verdade ele atingiu um regime onde bombear mais o aquífero adjacente **não aumenta mais a infiltração**, porque ela já está no seu valor máximo controlado pela condutividade do leito, não pela carga do aquífero. Isso muda o cálculo de gestão: rebaixar ainda mais o aquífero perto de um rio já desconectado só aprofunda o cone de rebaixamento, sem trazer água adicional do rio — informação central para a Aula 06 (vazão sustentável) e para o Módulo 04 (dimensionamento de campos de poços).

## O que não concluir

- **Que um mapa potenciométrico de boa aparência visual (equipotenciais suaves, bem espaçadas) é necessariamente confiável.** A qualidade depende de os poços amostrarem de fato o mesmo aquífero e de as medições serem contemporâneas — um mapa "bonito" construído com dados inconsistentes é mais perigoso que um mapa reconhecidamente esparso.
- **Que o sistema de fluxo regional é sempre o mais importante para o abastecimento.** Em muitas bacias, o sistema local, mais raso, é o que efetivamente supre poços domésticos e pequenas captações — o regional importa mais para hidrogeoquímica de longo prazo e para aquíferos profundos de grande escala.
- **Que a existência de um sistema de fluxo regional profundo torna a superfície imune a contaminação.** Contaminação lançada numa área de recarga pode, em princípio, entrar no sistema regional; o que muda é a escala de tempo até se manifestar na descarga, não a possibilidade em si.

## Recap relâmpago

- **Mapa potenciométrico** contorna carga hidráulica (não profundidade do nível d'água); fluxo é perpendicular às equipotenciais só em meio isotrópico.
- **Modelo de Tóth**: topografia controla sistemas de fluxo **local, intermediário e regional**, superpostos, com tempos de trânsito crescentes; um mesmo ponto em planta pode captar águas de sistemas distintos conforme a profundidade.
- **Recarga**: carga decrescente com a profundidade (fluxo descendente), nível profundo, cota alta. **Descarga**: padrão espelhado — o critério mais robusto é o par de poços aninhados.
- **Rio efluente** (recebe água do aquífero, sustenta baseflow), **influente** (recarrega o aquífero) e **desconectado** (infiltração no valor máximo, independente do rebaixamento adicional do aquífero) — regime pode variar ao longo do curso e da estação.

## Próxima aula

[[01-hidrogeologia-recursos-hidricos-aula-04-pocos-tubulares-e-de-monitoramento|Aula 04 — Poços tubulares e de monitoramento: projeto, perfuração, construção e manutenção]]

## Anterior

[[01-hidrogeologia-recursos-hidricos-aula-02-lei-de-darcy-e-zona-nao-saturada|Aula 02 — Lei de Darcy e o movimento da água subterrânea; água na zona não saturada]]

## Fontes

- Mapas potenciométricos, equipotenciais e linhas de fluxo: Fetter, C. W. (2001), *Applied Hydrogeology*, 4ª ed., Prentice-Hall, cap. 5 e 8.
- Modelo de sistemas de fluxo local, intermediário e regional controlado pela topografia: Tóth, J. (1963), "A theoretical analysis of groundwater flow in small drainage basins", *Journal of Geophysical Research*, 68(16), 4795–4812; Freeze, R. A. & Witherspoon, P. A. (1967), "Theoretical analysis of regional groundwater flow: 2", *Water Resources Research*, 3(2), 623–634.
- Poços aninhados, identificação de recarga e descarga, relação rio-aquífero (efluente, influente, desconectado): Freeze, R. A. & Cherry, J. A. (1979), *Groundwater*, Prentice-Hall, cap. 6.
- Separação de hidrograma e escoamento de base: Fetter (2001), cap. 6.

<!--
nivel: avancado
palavras_corpo: ~1800

mapa_objetivo_secao:
  geologia-avancado-m01-oa02: "O mapa potenciométrico: a topografia invisível que comanda o fluxo" + "Anisotropia e o desvio do fluxo em relação ao gradiente" + "O modelo de Tóth: fluxo local, intermediário e regional" + "Identificando áreas de recarga e de descarga no mapa" + "A relação rio-aquífero" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: HIDRO-M01-A03-POTENCIOMETRICO-001
    claim: "Um mapa potenciométrico contorna a carga hidráulica medida numa rede de poços do mesmo aquífero; em meio isotrópico o fluxo é perpendicular às linhas equipotenciais, apontando de carga maior para carga menor."
    risk: fato
    source: "Fetter 2001, cap. 5 e 8"
  - claim_id: HIDRO-M01-A03-TOTH-002
    claim: "Tóth (1963) demonstrou que a topografia de uma bacia sedimentar controla o desenvolvimento hierárquico de sistemas de fluxo subterrâneo local, intermediário e regional, com tempos de trânsito crescentes do local para o regional."
    risk: fato
    source: "Tóth 1963, Journal of Geophysical Research 68(16); Freeze & Witherspoon 1967"
  - claim_id: HIDRO-M01-A03-NESTED-003
    claim: "Poços aninhados (piezômetros a diferentes profundidades no mesmo ponto) identificam recarga quando a carga hidráulica diminui com a profundidade (fluxo descendente) e descarga quando a carga aumenta com a profundidade (fluxo ascendente)."
    risk: fato
    source: "Freeze & Cherry 1979, cap. 6"
  - claim_id: HIDRO-M01-A03-RIO-004
    claim: "Um rio é efluente (ganhador) quando a carga do aquífero adjacente é maior que o nível do rio, influente (perdedor) quando o nível do rio é maior que a carga do aquífero, e desconectado quando existe zona não saturada contínua entre a base do rio e o nível freático, caso em que a taxa de infiltração atinge um valor máximo independente de rebaixamento adicional do aquífero."
    risk: fato
    source: "Freeze & Cherry 1979, cap. 6"
-->
