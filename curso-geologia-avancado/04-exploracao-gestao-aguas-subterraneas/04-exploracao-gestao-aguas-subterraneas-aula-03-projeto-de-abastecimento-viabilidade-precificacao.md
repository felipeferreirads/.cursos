# Aula 03: Projeto de abastecimento por água subterrânea: etapas, viabilidade e precificação da água

**ID:** geologia-avancado-m04-a03
**Módulo:** [[04-exploracao-gestao-aguas-subterraneas-modulo|Módulo 04 — Exploração, explotação e gestão dos recursos hídricos subterrâneos]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** estruturar as etapas de um projeto de abastecimento por água subterrânea, avaliar sua viabilidade técnica e econômica, e precificar a água produzida distinguindo tarifa de serviço e cobrança pelo uso da água bruta.
**Pré-requisito:** Aulas 01 e 02 deste módulo (fases de desenvolvimento do aquífero, dimensionamento de campos de poços) e Módulo 01, Aula 06 (vazão sustentável, outorga).

## Antes de começar, você precisa saber

- As três fases de desenvolvimento de um aquífero — exploração, avaliação, explotação — Aula 01 deste módulo.
- Dimensionamento hidráulico de um campo de poços e vazão sustentável do campo — Aula 02 deste módulo.
- Outorga de direito de uso de água subterrânea no Brasil (Lei 9.433/1997) — Módulo 01, Aula 06.

## Conteúdo

### O ciclo de vida de um projeto de abastecimento

Um projeto de abastecimento por água subterrânea segue o mesmo ciclo de vida de qualquer projeto de infraestrutura hídrica, com as fases hidrogeológicas das Aulas 01 e 02 embutidas nas etapas iniciais:

1. **Estudo de viabilidade** — reúne a avaliação hidrogeológica (Aula 01) e o dimensionamento preliminar do campo de poços (Aula 02) para responder três perguntas: é tecnicamente possível atender à demanda projetada? É economicamente justificável frente a alternativas? É ambiental e legalmente viável (outorga, licenciamento)?
2. **Projeto básico** — detalha o arranjo do campo de poços, o traçado da adução, a necessidade (ou não) de tratamento, e consolida os quantitativos de obra o suficiente para orçamento com precisão de projeto (não mais de viabilidade).
3. **Projeto executivo** — especificações técnicas completas para licitação e construção: diâmetros de revestimento e filtro por poço, especificação de bombas, materiais de adução, instrumentação de monitoramento.
4. **Implantação** — perfuração, construção e testes de aceitação dos poços (Módulo 01, Aula 04), montagem de bombas e adução, comissionamento do sistema.
5. **Operação e manutenção** — a fase de explotação (Aula 01), incluindo monitoramento contínuo, manutenção preventiva de poços e bombas, e revisão periódica de outorga.

O erro estrutural mais comum em projetos malsucedidos é comprimir ou pular a primeira etapa: avançar para projeto executivo e obra sem uma avaliação hidrogeológica robusta compromete todas as etapas seguintes, pois os quantitativos de obra e os custos operacionais dependem diretamente dos parâmetros hidráulicos e da vazão sustentável estimados na avaliação.

### Viabilidade técnica: a demanda como ponto de partida

A viabilidade técnica confronta a **demanda projetada** — vazão necessária ao longo do horizonte de projeto (tipicamente 20 anos para sistemas de abastecimento público), estimada a partir de população atendida, consumo per capita e perdas de distribuição — contra a vazão sustentável do campo de poços (Aula 02) e da bacia (Módulo 01, Aula 06). Um projeto é tecnicamente viável quando o campo dimensionado atende à demanda de pico do horizonte de projeto sem exceder a vazão sustentável — não apenas a demanda do ano de implantação. Subdimensionar o horizonte de crescimento populacional é um erro recorrente: um campo dimensionado só para a demanda inicial exige expansão prematura, frequentemente mais cara por unidade de capacidade adicional que se tivesse sido prevista desde o início.

### Viabilidade econômica: CAPEX, OPEX e custo nivelado da água

A avaliação econômica de um projeto de água subterrânea separa dois tipos de custo:

- **CAPEX** (capital expenditure, investimento inicial): perfuração e construção dos poços, revestimento e filtro, bomba e motor, casa de bomba, rede de adução, e — quando necessário — unidade de tratamento (Módulo 03 trata da qualidade que pode exigir tratamento).
- **OPEX** (operational expenditure, custo operacional recorrente): energia elétrica de bombeamento (tipicamente o maior componente recorrente, proporcional ao produto vazão × altura manométrica total, que inclui o rebaixamento operacional discutido na Aula 02), manutenção preventiva e corretiva de poços e equipamentos, monitoramento, e taxas de outorga/cobrança pelo uso da água bruta onde aplicável.

Dois instrumentos de engenharia econômica traduzem CAPEX e OPEX projetados ao longo da vida útil em uma decisão comparável:

- **Valor Presente Líquido (VPL):** traz todos os fluxos de caixa futuros (investimento inicial negativo, custos operacionais anuais, eventualmente receita tarifária) a valor presente, usando uma taxa de desconto que reflete o custo de capital do investidor; um VPL positivo (ou, no caso de comparação entre alternativas de fornecimento sem receita associada, o menor valor presente de custos) indica a opção economicamente preferível.
- **Custo nivelado da água (levelized cost of water, LCOW):** análogo ao custo nivelado de energia (LCOE) usado em projetos energéticos, o LCOW divide o valor presente de todos os custos (CAPEX + OPEX ao longo da vida útil) pelo volume total de água produzida ao longo do mesmo período, também trazido a valor presente — resultando num custo médio por metro cúbico que permite comparar diretamente fontes de naturezas distintas (água subterrânea, adução de manancial superficial distante, dessalinização, reúso de água) numa mesma unidade.

> [!note] Por que o custo por m³ de água subterrânea costuma favorecer projetos de pequeno e médio porte
> A relação entre CAPEX e vazão de um sistema de água subterrânea tende a ser menos sensível a economia de escala que sistemas de captação superficial com grandes barragens e adutoras longas — um campo de poços pode ser expandido incrementalmente, poço a poço, próximo ao ponto de demanda, o que frequentemente torna o LCOW de água subterrânea competitivo para municípios de pequeno e médio porte, mesmo quando teria custo por m³ mais alto que um grande sistema superficial regional em escala metropolitana.

### Precificação da água: dois instrumentos que não devem ser confundidos

A cobrança sobre um sistema de abastecimento por água subterrânea envolve, na prática brasileira, dois instrumentos distintos, com finalidades e beneficiários diferentes:

- **Tarifa de serviço de abastecimento:** cobrada pela concessionária ou órgão prestador (companhia estadual de saneamento, serviço autônomo municipal) ao usuário final, remunerando o custo do serviço prestado — captação, tratamento quando houver, distribuição, manutenção do sistema. Estrutura tarifária costuma ser progressiva ou em faixas de consumo, com tarifa social para consumo mínimo essencial, buscando equilíbrio entre **recuperação de custos** (cost recovery, princípio geral de sustentabilidade financeira do prestador) e acesso universal.
- **Cobrança pelo uso da água bruta:** instrumento da Política Nacional de Recursos Hídricos (Lei 9.433/1997), cobrada pelo órgão gestor de recursos hídricos (estadual, no caso de água subterrânea — Módulo 01, Aula 06) diretamente sobre o volume extraído do aquífero, independente de quem opera o sistema de distribuição. Seu objetivo declarado na lei não é recuperar custo de serviço, mas **reconhecer a água como bem econômico dotado de valor** e gerar receita destinada, entre outros usos, ao financiamento de ações de gestão de recursos hídricos na própria bacia.

Confundir os dois instrumentos é comum na comunicação pública de projetos: o valor pago na conta de água ao consumidor final embute a tarifa de serviço, mas não necessariamente a cobrança pelo uso da água bruta em separado — em muitas bacias brasileiras, a cobrança pelo uso ainda não está implementada ou é cobrada apenas simbolicamente, o que reduz seu efeito pretendido como instrumento econômico de gestão da demanda.

### Comparando fontes: água subterrânea como uma opção de portfólio

A decisão final de projeto raramente é "água subterrânea sim ou não" isoladamente — é, mais frequentemente, uma decisão de **portfólio de fontes** frente a alternativas (manancial superficial existente, nova captação superficial, dessalinização em áreas costeiras, reúso de água). O LCOW oferece a métrica comum para essa comparação, mas a decisão de portfólio também pesa fatores não capturados diretamente no custo por m³: a resiliência a secas (aquíferos, sobretudo os de grande volume de armazenamento, amortecem melhor a variabilidade interanual de precipitação que reservatórios superficiais rasos), o tempo de implantação (um campo de poços costuma ser implantado mais rápido que uma barragem), e o risco de conflito de uso com outros usuários da mesma bacia — antecipando a discussão de uso conjuntivo e governança da Aula 04.

## Exemplo trabalhado

**Situação:** um projeto de abastecimento por água subterrânea tem CAPEX de R$ 2,4 milhões (poços, adução, casa de bombas) e OPEX anual estimado de R$ 180 mil (energia, manutenção, monitoramento), operando por 20 anos e produzindo 1.200.000 m³/ano de água (vazão média de aproximadamente 38 L/s). Simplificando sem trazer a valor presente (aproximação de custo médio simples, adequada para uma primeira ordem de grandeza):

Custo total ao longo de 20 anos = CAPEX + (OPEX × 20) = 2.400.000 + (180.000 × 20) = 2.400.000 + 3.600.000 = R$ 6.000.000

Volume total produzido em 20 anos = 1.200.000 × 20 = 24.000.000 m³

Custo médio por m³ ≈ 6.000.000 / 24.000.000 = **R$ 0,25/m³**

**Interpretação:** essa aproximação simples (sem desconto temporal) subestima o LCOW real, porque não pondera o fato de que o CAPEX é desembolsado integralmente no início, enquanto o OPEX se espalha ao longo de 20 anos — trazer os fluxos a valor presente com uma taxa de desconto positiva aumentaria o peso relativo do CAPEX inicial no cálculo, elevando ligeiramente o LCOW efetivo. Ainda assim, o valor aproximado de R$ 0,25/m³ já serve para uma comparação de ordem de grandeza contra o custo de uma alternativa de captação superficial distante, cujo CAPEX de adutora longa tenderia a ser proporcionalmente maior para a mesma vazão.

## Erros comuns

- **Avançar para projeto executivo e obra sem uma avaliação hidrogeológica robusta** (Aula 01), comprometendo os quantitativos de obra e os custos operacionais projetados por todo o restante do ciclo de vida.
- **Dimensionar o campo de poços apenas para a demanda do ano de implantação**, ignorando o horizonte de crescimento populacional do projeto e forçando expansão prematura mais cara por unidade de capacidade adicional.
- **Confundir tarifa de serviço de abastecimento com cobrança pelo uso da água bruta**, tratando-as como o mesmo instrumento ou assumindo que uma implica automaticamente a outra.
- **Comparar CAPEX de alternativas de fonte sem levar OPEX a valor presente**, favorecendo indevidamente opções de baixo investimento inicial mas custo operacional elevado ao longo da vida útil.

## O que não concluir

- **Que o menor CAPEX inicial é sempre a melhor escolha de fonte.** A comparação correta é pelo custo nivelado (LCOW), que pondera CAPEX e OPEX ao longo de toda a vida útil trazidos a valor presente — uma opção de CAPEX baixo mas OPEX elevado (por exemplo, bombeamento de rebaixamento muito profundo) pode ter LCOW pior que uma alternativa de investimento inicial maior.
- **Que a existência de cobrança pelo uso da água bruta, por si, garante gestão eficaz da demanda.** Seu efeito pretendido como instrumento econômico depende do valor cobrado ser suficiente para influenciar decisões de uso — cobrança simbólica ou não implementada, situação ainda comum em bacias brasileiras, não produz esse efeito.

## Recap relâmpago

- O ciclo de vida de um projeto de abastecimento por água subterrânea segue **viabilidade → projeto básico → projeto executivo → implantação → operação e manutenção**, com as fases hidrogeológicas das Aulas 01–02 embutidas na viabilidade.
- **Viabilidade técnica** confronta a demanda projetada (horizonte de 20 anos) contra a vazão sustentável do campo e da bacia; **viabilidade econômica** compara CAPEX e OPEX via VPL ou custo nivelado da água (LCOW).
- **Tarifa de serviço** (remunera o prestador) e **cobrança pelo uso da água bruta** (Lei 9.433/1997, instrumento de gestão de recursos hídricos) são dois instrumentos distintos, com beneficiários e finalidades diferentes.
- A decisão de fonte é, em geral, uma decisão de **portfólio** — o LCOW dá a métrica comum de comparação, mas resiliência a secas, tempo de implantação e risco de conflito de uso também pesam.

## Próxima aula

[[04-exploracao-gestao-aguas-subterraneas-aula-04-superexplotacao-uso-conjuntivo-governanca|Aula 04 — Superexplotação, uso conjuntivo e governança dos recursos hídricos subterrâneos]]

## Anterior

[[04-exploracao-gestao-aguas-subterraneas-aula-02-hidraulica-interferencia-campos-de-pocos|Aula 02 — Hidráulica de aquíferos aplicada ao projeto: interferência entre poços e dimensionamento de campos de poços]]

## Fontes

- Ciclo de projeto de sistemas de abastecimento de água e estimativa de demanda: Todd, D. K. & Mays, L. W. (2005), *Groundwater Hydrology*, 3ª ed., Wiley, cap. 8.
- Avaliação econômica de projetos de água subterrânea (CAPEX/OPEX, custo nivelado): Driscoll, F. G. (1986), *Groundwater and Wells*, 2ª ed., Johnson Screens, cap. 18.
- Instrumentos da Política Nacional de Recursos Hídricos (outorga e cobrança pelo uso da água): Lei Federal 9.433/1997, arts. 5º, 12 e 19–22.
- Custo nivelado como métrica de comparação entre fontes de água: Banco Mundial / World Bank Group, *Guidance Note on Water Tariffs and Subsidies* (metodologia de custo nivelado adaptada de LCOE para água).

<!--
nivel: avancado
palavras_corpo: ~1750

mapa_objetivo_secao:
  geologia-avancado-m04-oa03: "O ciclo de vida de um projeto de abastecimento" + "Viabilidade técnica: a demanda como ponto de partida" + "Viabilidade econômica: CAPEX, OPEX e custo nivelado da água" + "Precificação da água: dois instrumentos que não devem ser confundidos" + "Comparando fontes: água subterrânea como uma opção de portfólio" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: EXPLOT-M04-A03-CICLO-001
    claim: "O ciclo de vida de um projeto de abastecimento por água subterrânea segue as etapas de estudo de viabilidade, projeto básico, projeto executivo, implantação e operação/manutenção, com a avaliação hidrogeológica e o dimensionamento do campo de poços embutidos na etapa de viabilidade."
    risk: fato (prática consolidada de engenharia de projetos de infraestrutura hídrica)
    source: "Todd & Mays 2005, cap. 8"
  - claim_id: EXPLOT-M04-A03-LCOW-002
    claim: "O custo nivelado da água (LCOW) é calculado dividindo o valor presente de todos os custos de capital e operacionais de um sistema de fornecimento de água pelo volume total de água produzido ao longo da vida útil, também trazido a valor presente, permitindo comparar fontes de naturezas distintas numa métrica comum de custo por metro cúbico."
    risk: fato (metodologia consolidada, adaptação do LCOE)
    source: "World Bank Group, Guidance Note on Water Tariffs and Subsidies"
  - claim_id: EXPLOT-M04-A03-COBRANCA-003
    claim: "No Brasil, a Lei Federal 9.433/1997 distingue a tarifa de serviço de abastecimento (cobrada pelo prestador do serviço) da cobrança pelo uso de recursos hídricos (instrumento da Política Nacional de Recursos Hídricos, cobrada pelo órgão gestor de recursos hídricos sobre o volume de água bruta extraído, com finalidade de reconhecer a água como bem econômico e financiar a gestão da bacia)."
    risk: fato
    source: "Lei 9.433/1997, arts. 5º, 12 e 19-22"
-->
