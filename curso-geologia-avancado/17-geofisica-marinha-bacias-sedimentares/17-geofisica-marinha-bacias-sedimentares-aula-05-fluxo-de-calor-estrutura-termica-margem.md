# Aula 05: Fluxo de calor e a estrutura térmica de uma margem divergente

**ID:** geologia-avancado-m17-a05
**Módulo:** [[17-geofisica-marinha-bacias-sedimentares-modulo|Módulo 17 — Geofísica marinha e de bacias sedimentares]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** interpretar mapas de fluxo de calor de bacias sedimentares e margens continentais, aplicando o padrão de decaimento térmico da litosfera oceânica à avaliação da maturação térmica de uma bacia.
**Ao final você vai conseguir:** explicar por que o fluxo de calor decai sistematicamente com a idade da litosfera oceânica e aplicar as duas equações do modelo GDH1 para calcular esse decaimento; distinguir a quebra interna do modelo (55 Ma) da idade de selamento da circulação hidrotermal (~65 Ma), que têm origens diferentes e não devem ser fundidas; e usar réguas de fluxo de calor de referência (oceânico jovem, oceânico antigo, cratônico, médias globais) para julgar se um valor medido numa bacia é alto, baixo ou típico.
**Pré-requisito:** [[17-geofisica-marinha-bacias-sedimentares-aula-04-gravimetria-magnetometria-campos-potenciais|Aula 04 deste módulo — Gravimetria e magnetometria marinhas em margens divergentes]], cujo zoneamento crustal (crosta continental, limite crosta continental-oceânica, crosta oceânica) esta aula acrescenta um terceiro critério independente para reconhecer; e, mais adiante no texto, a **Aula 01** (mecanismo de subsidência térmica) e a **Aula 02** (fase rifte e fase sag da margem atlântica brasileira), cujo raciocínio térmico esta aula retoma diretamente.

## Conteúdo

### Fluxo de calor: definição e o mecanismo de resfriamento da litosfera oceânica

O **fluxo de calor** — a taxa de transferência de energia térmica do interior da Terra para a superfície, tipicamente expresso em miliwatts por metro quadrado (mW/m²) — é diretamente ligado ao mecanismo de subsidência térmica introduzido na Aula 01: a litosfera oceânica recém-formada numa dorsal é quente e tem fluxo de calor superficial alto; à medida que se afasta da dorsal e envelhece, ela esfria por condução (e, nos primeiros dezenas de milhões de anos, também por circulação hidrotermal ativa na crosta superior), e o fluxo de calor decai sistematicamente com a idade da litosfera.

### O modelo GDH1: duas equações, dois regimes

O modelo de referência atual é o **GDH1** (*Global Depth and Heat flow model 1*) de **Stein & Stein (1992)**, um modelo de placa em resfriamento ajustado conjuntamente a dados de batimetria e de fluxo de calor, que substituiu como padrão o modelo de placa anterior de **Parsons & Sclater (1977)** — a diferença prática é que o GDH1 implica uma placa mais fina e mais quente em profundidade, e ajusta muito melhor os dados de litosfera antiga (>70 Ma), antes tratados como anômalos. Ele descreve o decaimento aproximadamente como proporcional ao inverso da raiz quadrada da idade (fluxo de calor ∝ 1/√idade) **enquanto a litosfera é jovem** — essa é a lei do resfriamento de semiespaço, e é justamente onde o modelo de placa se afasta dela, em idade alta, que os dois modelos se distinguem. Em números, o GDH1 é uma função definida por partes, com *q* em mW/m² e *t* em Ma:

> *q*(*t*) = 510 · *t*^(−1/2), para *t* ≤ 55 Ma
> *q*(*t*) = 48 + 96 · e^(−0,0278·*t*), para *t* > 55 Ma

Para litosfera oceânica muito antiga o modelo não continua caindo indefinidamente: o segundo ramo tende a um **patamar assintótico de 48 mW/m²**. Aplicando a equação a uma crosta oceânica de 60 Ma, por exemplo, 48 + 96 · e^(−1,668) ≈ **66 mW/m²**.

### Duas idades que não devem ser confundidas

Duas idades diferentes costumam ser confundidas aqui, e convém separá-las: **55 Ma é a quebra interna do próprio GDH1**, o ponto em que a lei de semiespaço deixa de valer e o comportamento de placa assume; **~65 Ma é a "idade de selamento" da circulação hidrotermal** (Stein & Stein, 1994), até a qual o fluxo de calor *medido* fica sistematicamente abaixo do previsto pela condução pura, porque a água circulante remove calor adicional da crosta superior. São números de origem distinta e não devem ser fundidos num só.

### Réguas de fluxo de calor: da crosta jovem ao cráton

Vale ter na cabeça algumas réguas de ordem de grandeza, porque é por comparação com elas que um valor medido numa bacia vira interpretação:

| Domínio | Fluxo de calor típico |
|---|---|
| Crosta oceânica de ~60 Ma (pelo GDH1) | ~66 mW/m² |
| Litosfera oceânica muito antiga (patamar do GDH1) | 48 mW/m² |
| Cráton arqueano estável | ~41 mW/m² |
| Cráton proterozoico | ~48 mW/m² |
| Média de **todos** os continentes (inclui áreas tectonicamente ativas) | 65 mW/m² |
| Média oceânica global | 101 mW/m² |

Leia a tabela de baixo para cima e o padrão salta: **crosta continental estável é o extremo frio do planeta** (40-50 mW/m²), e a média oceânica global é mais que o dobro disso — porque o oceano é, em média, muito mais jovem que o continente. O contraste com o fluxo de calor elevado sobre litosfera oceânica jovem próxima a dorsais ativas é, portanto, grande.

### Fluxo de calor na margem continental estirada e a maturação térmica

Essa mesma lógica térmica se aplica à margem continental estirada: durante a fase rifte (Aula 02), o afinamento litosférico traz astenosfera relativamente mais quente para mais perto da superfície, elevando temporariamente o fluxo de calor sobre a bacia; ao longo da fase sag e da margem divergente subsequente, esse fluxo de calor decai progressivamente à medida que a litosfera estirada retorna ao equilíbrio térmico — o mesmo processo de resfriamento que governa a subsidência térmica pós-rifte. Esse decaimento térmico tem consequência direta para a avaliação de recursos: o fluxo de calor ao longo da história de soterramento de uma bacia controla a **maturação térmica** da matéria orgânica nas rochas geradoras (os folhelhos lacustres sin-rifte discutidos na Aula 02), determinando se, quando e onde essa matéria orgânica atingiu temperatura suficiente para gerar hidrocarbonetos líquidos ou gás — o tema central da Aula 06.

## Exemplo trabalhado

**Situação:** um levantamento de fluxo de calor ao longo de um perfil perpendicular a uma antiga dorsal meso-oceânica extinta mostra valores decrescendo progressivamente da porção mais próxima ao eixo de espalhamento original (crosta com ~5 Ma na época da medida) para a porção mais distante (crosta com ~60 Ma). Um levantamento gravimétrico e magnético complementar (Aula 04) já havia identificado essas duas porções como crosta oceânica, uma mais jovem que a outra.

**Pergunta:** (a) calcule, pelo GDH1, o fluxo de calor esperado em cada uma das duas idades; (b) compare os dois valores com a régua de referência do cráton estável e da média oceânica global; (c) explique por que o padrão de decaimento observado é consistente, de forma independente, com o zoneamento crustal já obtido por gravimetria e magnetometria na Aula 04.

**Resolução:**

**(a) Cálculo pelo GDH1:**

Para a crosta de 5 Ma (dentro do regime jovem, *t* ≤ 55 Ma, lei de semiespaço):
*q*(5) = 510 · 5^(−1/2) = 510 / √5 = 510 / 2,236 ≈ **228 mW/m²**.

Para a crosta de 60 Ma (regime de placa, *t* > 55 Ma):
*q*(60) = 48 + 96 · e^(−0,0278×60) = 48 + 96 · e^(−1,668) ≈ **66 mW/m²**.

**(b) Comparação com as réguas de referência:** os 228 mW/m² esperados na crosta de 5 Ma são mais que o **dobro** da média oceânica global (101 mW/m²) e cerca de **cinco vezes** o fluxo cratônico estável (41-48 mW/m²) — coerente com o fato de que a litosfera está a apenas alguns milhões de anos de sua formação na dorsal, ainda perdendo grande parte do calor acumulado na origem. Os 66 mW/m² esperados na crosta de 60 Ma já estão abaixo da média oceânica global e se aproximam do patamar assintótico do modelo (48 mW/m²), mas ainda são maiores que qualquer valor cratônico — a litosfera oceânica de 60 Ma já perdeu a maior parte do excesso térmico da origem, mas ainda não esfriou até o regime de crosta continental estável.

**(c) Convergência com o zoneamento crustal:** o fluxo de calor mais alto na porção mais jovem (mais próxima ao eixo de espalhamento) e decrescente em direção à porção mais antiga e mais distante é exatamente o padrão previsto pelo modelo de resfriamento da litosfera com a idade. Esse padrão não depende de nenhum dado magnético ou gravimétrico — é obtido de forma inteiramente independente —, e ainda assim aponta para a mesma conclusão de zoneamento por idade que a Aula 04 já havia estabelecido por faixas magnéticas lineares e por nível regional de Bouguer. É exatamente esse tipo de convergência independente entre métodos de famílias diferentes — campos potenciais e estrutura térmica — que caracteriza a interpretação integrada de margens divergentes.

## Erros comuns

- **Confundir a quebra de 55 Ma do GDH1 com a idade de selamento hidrotermal de ~65 Ma.** A aula é explícita que são números de origem diferente — um é onde a própria equação muda de regime matemático, o outro é até onde a circulação hidrotermal medida difere da condução pura — fundi-los é um erro de origem, não só de arredondamento.
- **Aplicar a equação de semiespaço (t ≤ 55 Ma) a litosfera mais antiga que 55 Ma, ou vice-versa.** O modelo é definido por partes especificamente porque o comportamento muda de regime — usar a fórmula errada para a idade produz um número que "fecha a conta" mas está fisicamente errado.
- **Julgar um valor de fluxo de calor "alto" ou "baixo" sem uma régua de referência explícita.** Como o exemplo trabalhado faz, 228 mW/m² só significa algo quando comparado à média oceânica (101) e ao cráton (41-48) — um número isolado não diz se é anômalo.
- **Achar que fluxo de calor decrescente ao longo de um perfil precisa de confirmação magnética ou gravimétrica para valer.** O próprio exemplo trabalhado enfatiza que o padrão térmico é obtido de forma inteiramente independente — a convergência com outros métodos reforça a confiança, mas cada método sozinho já é evidência válida.

## O que não concluir

- **Que o fluxo de calor continua caindo indefinidamente com a idade.** O GDH1 tende a um patamar assintótico de 48 mW/m² em litosfera muito antiga — não cai a zero nem continua decrescendo sem limite.
- **Que a média continental (65 mW/m²) representa a crosta continental estável.** Essa média inclui áreas tectonicamente ativas; crosta continental estável (cráton) fica bem abaixo, em 40-50 mW/m² — usar a média geral para julgar um cráton específico superestima o valor esperado.
- **Que o decaimento de fluxo de calor na margem estirada é só curiosidade acadêmica.** Ele controla diretamente a maturação térmica da matéria orgânica nas rochas geradoras — é o elo direto entre esta aula e a avaliação de recursos da Aula 06, não um fato isolado sobre litosfera.

## Recap relâmpago

- Fluxo de calor decai sistematicamente com a idade da litosfera oceânica. O modelo de referência é o **GDH1** de Stein & Stein (1992), que substituiu o modelo de placa mais antigo de Parsons & Sclater (1977): *q* = 510·*t*^(−1/2) até 55 Ma (lei de semiespaço, ∝ 1/√idade) e *q* = 48 + 96·e^(−0,0278·*t*) depois, tendendo ao patamar de **48 mW/m²** em litosfera muito antiga.
- **Não confunda os 55 Ma da quebra do modelo com os ~65 Ma da idade de selamento hidrotermal** (Stein & Stein 1994) — são números de origem diferente: um é onde a equação muda de regime, o outro é até onde a circulação hidrotermal mantém o fluxo medido abaixo do previsto pela condução pura.
- Réguas de referência: **~66 mW/m²** em crosta oceânica de ~60 Ma (pela própria equação); 40-50 mW/m² em cráton estável (41 arqueano, 48 proterozoico — Nyblade & Pollack 1993); 65 mW/m² de média continental e 101 mW/m² de média oceânica global (Pollack et al. 1993); crosta jovem próxima a uma dorsal ativa facilmente supera 200 mW/m².
- A mesma lógica térmica governa a subsidência térmica pós-rifte (Aula 01-02): o afinamento litosférico na fase rifte eleva temporariamente o fluxo de calor, que decai progressivamente nas fases sag e margem divergente — e esse decaimento controla a maturação térmica das rochas geradoras, o elo direto com a avaliação de recursos da Aula 06.

## Próxima aula

[[17-geofisica-marinha-bacias-sedimentares-aula-06-recursos-minerais-energeticos-margem-atlantica-sistemas-petroliferos-trapas-estudos-de-caso|Aula 06 — Recursos minerais e energéticos da margem atlântica: sistemas petrolíferos, trapas e estudos de caso]] — como a arquitetura tectonossedimentar (Aula 02) e as assinaturas geofísicas das Aulas 03-05 (métodos sísmicos, campos potenciais e estrutura térmica) se combinam para localizar e avaliar rocha geradora, reservatório, selo e trapa dos principais sistemas petrolíferos da margem brasileira.

## Anterior

[[17-geofisica-marinha-bacias-sedimentares-aula-04-gravimetria-magnetometria-campos-potenciais|Aula 04 — Gravimetria e magnetometria marinhas em margens divergentes]]

## Fontes

- Stein, C. A. & Stein, S. (1992), "A model for the global variation in oceanic depth and heat flow with lithospheric age", *Nature*, 359, 123-129 (modelo de resfriamento de placa GDH1 e as equações de fluxo de calor por idade usadas nesta aula: *q* = 510·*t*^(−1/2) para *t* ≤ 55 Ma e *q* = 48 + 96·e^(−0,0278·*t*) para *t* > 55 Ma).
- Stein, C. A. & Stein, S. (1994), "Constraints on hydrothermal heat flux through the oceanic lithosphere from global heat flow", *Journal of Geophysical Research*, 99(B2), 3081-3095 (idade de selamento da circulação hidrotermal, ~65 Ma — distinta da quebra de 55 Ma do GDH1).
- Parsons, B. & Sclater, J. G. (1977), "An analysis of the variation of ocean floor bathymetry and heat flow with age", *Journal of Geophysical Research*, 82(5), 803-827 (modelo de placa anterior, substituído como padrão pelo GDH1).
- Pollack, H. N., Hurter, S. J. & Johnson, J. R. (1993), "Heat flow from the Earth's interior: analysis of the global data set", *Reviews of Geophysics*, 31(3), 267-280 (médias globais de fluxo de calor continental 65 mW/m² e oceânico 101 mW/m²).
- Nyblade, A. A. & Pollack, H. N. (1993), "A global analysis of heat flow from Precambrian terrains: implications for the thermal structure of Archean and Proterozoic lithosphere", *Journal of Geophysical Research*, 98(B7), 12207-12218 (médias cratônicas: ~41 mW/m² sobre crosta arqueana e ~48 mW/m² sobre crosta proterozoica).
- McKenzie, D. (1978), "Some remarks on the development of sedimentary basins", *Earth and Planetary Science Letters*, 40 (modelo de estiramento litosférico e evolução térmica associada).
- Allen, P. A. & Allen, J. R. (2013), *Basin Analysis*, cap. 9 (fluxo de calor e maturação térmica em bacias de rifte).

<!--
nivel: avancado
palavras_corpo: 1050
origem: 'Esta aula é a metade "fluxo de calor" da antiga Aula 04 (Gravimetria, magnetometria e fluxo de calor), dividida em 2026-09-10 por decisão do orquestrador a partir do achado didático DID-M17-A04-CARGA-003 (revisão didática, não bloqueante). O conteúdo científico da seção de fluxo de calor é integralmente o já auditado e corrigido (auditoria de 2026-09-10, ver 17-geofisica-marinha-bacias-sedimentares-auditoria.md, achados AUD-M17-A04-CRATONFONTE-008, AUD-M17-A04-GDH1VALOR-013 e AUD-M17-A04-GDH1SELAMENTO-014, todos corrigidos), apenas reorganizado em subseções nomeadas (mecanicamente, a partir dos quatro blocos já separados na revisão didática anterior). ATENÇÃO — CONTEÚDO NOVO ALÉM DA DIVISÃO MECÂNICA: o "Exemplo trabalhado" desta aula é NOVO (a aula original tinha um único exemplo trabalhado compartilhado com a parte de campos potenciais, cujo parágrafo final de fluxo de calor era qualitativo). O novo exemplo aplica a equação do GDH1 já auditada a t=5 Ma (cálculo: 510/√5 ≈ 228 mW/m², NÃO estava escrito em nenhuma aula anterior, é aritmética simples aplicada à fórmula já verificada) e reaproveita o cálculo de t=60 Ma (66 mW/m²) que já constava do corpo. RECOMENDA-SE que o geo-arquiteto confirme rapidamente esta única conta nova (228 mW/m²) antes de considerar a aula dispensada de nova auditoria — o restante do conteúdo não foi alterado.'
mapa_objetivo_secao:
  geologia-avancado-m17-oa04: "Fluxo de calor: definição e o mecanismo de resfriamento da litosfera oceânica" + "O modelo GDH1: duas equações, dois regimes" + "Duas idades que não devem ser confundidas" + "Réguas de fluxo de calor: da crosta jovem ao cráton" + "Fluxo de calor na margem continental estirada e a maturação térmica" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOFISMAR-M17-A05-FLUXOCALOR-004
    claim: "O modelo de referência para o resfriamento da litosfera oceânica é o GDH1 (Global Depth and Heat flow model 1) de Stein & Stein (1992), ajustado conjuntamente a batimetria e fluxo de calor, que substituiu como padrão o modelo de placa de Parsons & Sclater (1977) — o GDH1 implica placa mais fina e mais quente em profundidade e ajusta melhor a litosfera antiga (>70 Ma). As equações do GDH1 são q(t) = 510 · t^(-1/2) para t ≤ 55 Ma (lei de semiespaço) e q(t) = 48 + 96 · exp(-0,0278 · t) para t > 55 Ma, com q em mW/m² e t em Ma, tendendo ao patamar assintótico de 48 mW/m² em litosfera muito antiga. A quebra de 55 Ma do modelo NÃO é a mesma coisa que a idade de selamento da circulação hidrotermal, de cerca de 65 Ma (Stein & Stein 1994). Valores de referência: ~66 mW/m² em crosta oceânica de ~60 Ma (48 + 96 · e^-1,668, pela própria equação); ~228 mW/m² em crosta oceânica de ~5 Ma (510/√5, pela própria equação — cálculo novo desta divisão, mesma fórmula já auditada); 40-50 mW/m² em cráton estável (média ~41 mW/m² no Arqueano e ~48 mW/m² no Proterozoico, Nyblade & Pollack 1993); média continental global 65 mW/m² e média oceânica global 101 mW/m² (Pollack, Hurter & Johnson 1993)."
    risk: aproximacao
    source: "Stein, C. A. & Stein, S. (1992), Nature 359, 123-129; Stein, C. A. & Stein, S. (1994), JGR 99(B2), 3081-3095; Parsons, B. & Sclater, J. G. (1977), JGR 82; Pollack, Hurter & Johnson (1993), Reviews of Geophysics 31(3), 267-280; Nyblade, A. A. & Pollack, H. N. (1993), JGR 98(B7), 12207-12218. Herdado sem alteração da auditoria de 2026-09-10 (achados AUD-M17-A04-CRATONFONTE-008, AUD-M17-A04-GDH1VALOR-013, AUD-M17-A04-GDH1SELAMENTO-014, todos corrigidos), exceto o valor de 228 mW/m² a 5 Ma, que é cálculo novo pela mesma equação já auditada — não reverificado em fonte primária separadamente, apenas por aritmética direta da fórmula."
  - claim_id: GEOFISMAR-M17-A05-FLUXOCALOR-BACIA-005
    claim: "O afinamento litosférico durante a fase rifte eleva temporariamente o fluxo de calor sobre a bacia (astenosfera mais próxima da superfície); esse fluxo decai progressivamente durante as fases sag e margem divergente à medida que a litosfera estirada resfria, controlando a maturação térmica das rochas geradoras sin-rifte ao longo da história de soterramento da bacia."
    risk: aproximacao
    source: "McKenzie, D. (1978), Earth and Planetary Science Letters 40; Allen & Allen (2013), Basin Analysis, cap. 9. Herdado sem alteração da auditoria de 2026-09-10."
-->
