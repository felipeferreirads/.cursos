# Aula 04: Amostragem representativa, métodos analíticos, limites de detecção e padrões de qualidade

**ID:** geologia-avancado-m02-a04
**Módulo:** [[02-hidrogeoquimica-modulo|Módulo 02 — Hidrogeoquímica]]
**Duração estimada:** ~28 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** planejar uma campanha de amostragem de água subterrânea que produza amostras representativas e avaliar o controle de qualidade analítico de um boletim de resultados.

## Antes de começar, você precisa saber

- Balanço iônico e unidades de concentração (Aula 01 deste módulo).
- Construção e desenvolvimento de poços de monitoramento (Módulo 01, Aula 04).

## Conteúdo

### Por que a amostragem, não só a análise, decide a qualidade do dado

Um laboratório pode analisar uma amostra com exatidão perfeita e o resultado ainda ser inútil — ou pior, enganoso — se a amostra não representa a água do aquífero no ponto e no instante de interesse. Os erros de amostragem são, na prática, a fonte dominante de dado hidrogeoquímico ruim, mais frequente que erro analítico de laboratório (Appelo & Postma, 2005; Custodio & Llamas, 1983). Duas fontes de não representatividade dominam:

- **Água estagnada no poço** (a coluna de água dentro do revestimento, entre bombeamentos, troca lentamente com o aquífero e pode ter composição alterada por reações com o próprio poço — oxidação de ferro no filtro, absorção de CO₂ atmosférico, mudança de temperatura).
- **Alteração da amostra entre a coleta e a análise** (perda de gases dissolvidos, oxidação, precipitação, atividade biológica) se a amostra não for tratada corretamente no campo.

### Purga: removendo a água que não representa o aquífero

Antes de coletar, é preciso **purgar** o poço — remover a água estagnada da coluna do poço até que chegue água representativa do aquífero. Dois critérios equivalentes, escolhidos conforme a vazão do poço e o objetivo do monitoramento:

- **Purga por volume**: remover de 3 a 5 volumes do poço (calculados a partir do diâmetro do revestimento e da altura da coluna d'água) antes de coletar — critério tradicional, robusto, mas pode gerar volume de purga excessivo em poços de diâmetro grande ou coluna longa, e o método pode ainda assim misturar água de diferentes profundidades dentro do poço.
- **Amostragem de baixa vazão** (*low-flow sampling*): bombear a vazão muito baixa (tipicamente <0,5 L/min), monitorando parâmetros de campo (ver adiante) até estabilização, minimizando o rebaixamento e a mistura vertical na coluna do poço — hoje o método preferido para monitoramento de qualidade em poços de investigação ambiental (Módulo 03), por amostrar preferencialmente a água que efetivamente flui através do filtro, não a coluna estagnada acima dele (USEPA; Puls & Barcelona, 1996).

**Critério de estabilização** (aplicável a ambos os métodos, mas central na amostragem de baixa vazão): medir em campo, em intervalos regulares (a cada volume de célula de fluxo), pH, condutividade elétrica (EC), temperatura, potencial redox (Eh/ORP) e oxigênio dissolvido (OD) até que as leituras variem menos que uma tolerância pré-definida (tipicamente ±0,1 unidade de pH, ±3% de EC, ±10 mV de Eh, ±10% de OD entre leituras consecutivas) — a estabilização indica que a água que sai da bomba já reflete o aquífero, não mais a coluna estagnada.

> [!important] Parâmetros de campo são medidos em campo porque mudam ao expor a amostra ao ar
> pH, Eh, OD e, em menor grau, temperatura são grandezas instáveis fora do ambiente do aquífero: o contato com o ar atmosférico altera OD quase instantaneamente, e a perda de CO₂ dissolvido desloca o pH. Medir esses parâmetros em laboratório, horas ou dias depois da coleta, produz valores sistematicamente não representativos — por isso são sempre medidos com sonda multiparâmetro numa célula de fluxo fechada, em campo, no momento da coleta.

### Filtração, preservação e prazo de validade da amostra

Após a coleta, cada grupo de analitos exige tratamento específico para não se alterar antes da análise:

- **Filtração** (membrana de 0,45 µm) é aplicada a amostras destinadas à análise de **cátions dissolvidos** e metais dissolvidos, para separar a fração verdadeiramente dissolvida do material particulado em suspensão — sem filtração, um resultado de "ferro total" pode incluir partículas de óxido de ferro que não representam o ferro efetivamente dissolvido no aquífero.
- **Acidificação** (HNO₃ até pH < 2) de amostras filtradas para cátions/metais previne a precipitação e a adsorção às paredes do frasco durante o transporte e armazenamento.
- **Amostras para ânions** (Cl⁻, SO₄²⁻, NO₃⁻) geralmente não são acidificadas nem filtradas da mesma forma, mas são refrigeradas (4 °C) e analisadas dentro de um prazo curto, sobretudo para nitrato (instável por atividade biológica).
- **Alcalinidade (HCO₃⁻)** é o parâmetro mais sensível ao tempo: idealmente titulada em campo, no mesmo dia da coleta — a perda de CO₂ dissolvido por desgaseificação ao longo do transporte desloca o equilíbrio carbonático e altera o valor medido, uma das causas mais comuns de balanço iônico ruim (Aula 01).
- **Frasco e headspace**: amostras para gases dissolvidos (CO₂, CH₄) e compostos voláteis exigem frascos completamente cheios, sem espaço de ar (*zero headspace*), para impedir a troca de gases com uma bolha de ar residual.

### Limites de detecção e de quantificação

Todo método analítico tem um piso de sensibilidade:

- **Limite de detecção (LOD)**: a menor concentração que o método consegue distinguir de forma confiável do ruído de fundo (branco) — abaixo do LOD, o resultado é reportado como "< LOD", não como zero.
- **Limite de quantificação (LOQ)**: tipicamente 3 a 5 vezes o LOD — a menor concentração que pode ser medida com precisão aceitável para fins quantitativos, não apenas detectada.

> [!warning] "Não detectado" não é o mesmo que "ausente"
> Um resultado "< LOD" significa apenas que a concentração está abaixo da sensibilidade do método usado — pode ser zero, ou pode ser uma concentração real, porém pequena. Ao calcular um balanço iônico ou uma média de série temporal com resultados "< LOD", a prática convencional (e conservadora) é usar metade do valor do LOD, nunca simplesmente zero, para não subestimar sistematicamente a concentração real.

### Controle de qualidade (QA/QC): amostras de verificação

Uma campanha de amostragem robusta inclui amostras adicionais cujo único propósito é verificar a qualidade dos próprios dados, não caracterizar o aquífero:

- **Duplicata de campo**: duas amostras coletadas em sequência no mesmo ponto, analisadas separadamente — mede a precisão combinada de amostragem + análise (variabilidade esperada pequena; diferença grande indica problema de campo ou de heterogeneidade do próprio poço).
- **Branco de campo** (*field blank*): água ultrapura levada ao campo, "amostrada" com o mesmo equipamento e procedimento — detecta contaminação cruzada pelo próprio equipamento de amostragem (crítico em investigações de contaminação, Módulo 03).
- **Branco de viagem** (*trip blank*): água ultrapura que acompanha as amostras desde o laboratório até o campo e de volta, sem ser aberta — detecta contaminação durante transporte e armazenamento, relevante sobretudo para compostos orgânicos voláteis.
- **Amostra cega (branco duplicado ou padrão certificado)**: enviada ao laboratório sem identificação especial, com concentração conhecida — verifica a exatidão do laboratório de forma independente do conhecimento prévio do analista sobre a amostra.
- **Balanço iônico** (Aula 01): embora calculado depois, é também uma ferramenta de QA/QC — a verificação de consistência mais barata e mais amplamente aplicável de todas, porque não exige amostra extra nenhuma.

### Padrões de qualidade de água

A interpretação de uma análise frequentemente compara os resultados contra padrões regulatórios, que têm propósitos distintos e não devem ser confundidos:

- **Padrão de potabilidade** (Brasil: Portaria GM/MS nº 888/2021, que atualizou a antiga Portaria de Consolidação nº 5/2017 do Ministério da Saúde; internacionalmente, as *Guidelines for Drinking-water Quality* da OMS) — define limites máximos para consumo humano direto, com foco em risco à saúde e em padrão organoléptico (sabor, cor, odor).
- **Padrão de qualidade de água subterrânea** (Brasil: Resolução CONAMA nº 396/2008) — estabelece classes de enquadramento da água subterrânea conforme seus usos preponderantes (consumo humano, dessedentação animal, irrigação, recreação, entre outros), distinta da norma de potabilidade porque avalia o corpo hídrico em si, não apenas a água já tratada e distribuída.

> [!note] Padrão de qualidade do aquífero ≠ padrão de potabilidade da torneira
> Uma água subterrânea pode estar em conformidade com o enquadramento da CONAMA 396/2008 para seu uso preponderante e ainda assim exigir tratamento (ex.: desinfecção, remoção de ferro/manganês) antes de atender à Portaria GM/MS 888/2021 para consumo humano direto — são normas com propósitos e etapas da cadeia de uso diferentes, não intercambiáveis na interpretação de um resultado.

## Exemplo trabalhado

**Situação:** durante a purga de baixa vazão de um poço de monitoramento, o técnico registra, a cada 5 minutos: pH 7,1 → 7,3 → 6,9 → 6,8 → 6,8 → 6,8; EC (µS/cm) 620 → 590 → 545 → 520 → 515 → 512; OD (mg/L) 5,2 → 3,8 → 2,1 → 1,4 → 1,2 → 1,2. Quando a amostra deve ser coletada?

**Raciocínio:** os três parâmetros mostram trajetórias de estabilização típicas — a água inicialmente extraída (mais próxima da coluna estagnada, mais exposta a contato com o ar dentro do poço) tem pH mais alto e instável, EC decrescente (a coluna estagnada geralmente concentra solutos por evaporação lenta ou reações com o revestimento) e OD alto (contaminação pelo ar). Por volta da quarta/quinta leitura, os três parâmetros já satisfazem critérios de estabilização convencionais (variação de pH <0,1, de EC <3%, de OD <10% entre leituras consecutivas) — a coleta deve ocorrer **na leitura seguinte à estabilização** (aqui, após a quinta leitura, coletando na sexta), não antes: coletar cedo demais (ex.: na segunda leitura) capturaria água ainda não representativa do aquífero.

## Erros comuns

- **Medir pH, Eh e OD em laboratório em vez de campo.** Esses parâmetros mudam entre a coleta e a chegada ao laboratório — o valor de laboratório não representa mais a condição do aquífero.
- **Coletar sem purgar (ou purgar de menos)** em poços de monitoramento — captura preferencialmente a água estagnada da coluna do poço, não a água do aquífero.
- **Não filtrar amostras de metais/cátions dissolvidos**, confundindo "ferro dissolvido" com "ferro total" (que inclui partículas em suspensão).
- **Tratar resultado "< LOD" como zero** em cálculos de balanço ou de média — subestima sistematicamente a concentração real.
- **Comparar um resultado contra o padrão de potabilidade quando o objetivo é avaliar o enquadramento do corpo hídrico**, ou vice-versa — são normas com finalidades distintas.

## O que não concluir

- **Que amostragem de baixa vazão é sempre superior à purga por volume em qualquer contexto.** Em poços de produção de grande vazão (não poços de monitoramento estreitos), a purga convencional continua sendo o método prático — baixa vazão foi desenvolvida especificamente para poços de monitoramento ambiental de pequeno diâmetro.
- **Que uma única duplicata de campo com boa concordância garante que toda a campanha está livre de erro sistemático.** QA/QC avalia precisão amostra a amostra; erros sistemáticos (viés de calibração do laboratório, por exemplo) exigem verificação contra padrão certificado, não apenas duplicatas.

## Recap relâmpago

- Amostragem inadequada é a causa mais comum de dado hidrogeoquímico ruim — mais frequente que erro de laboratório.
- Purgar (por volume, 3–5 volumes de poço, ou por baixa vazão com estabilização de pH/EC/Eh/OD) remove a água estagnada da coluna do poço antes de coletar.
- Filtração (0,45 µm) e acidificação preservam cátions/metais; alcalinidade deve ser titulada o quanto antes (idealmente em campo).
- LOD é o piso de detecção; "< LOD" não é zero — usar metade do LOD em cálculos, por convenção conservadora.
- QA/QC: duplicata de campo, branco de campo, branco de viagem, amostra cega e o próprio balanço iônico.
- Padrão de potabilidade (Portaria GM/MS 888/2021) e padrão de qualidade de água subterrânea (CONAMA 396/2008) avaliam coisas diferentes — não são intercambiáveis.

## Próxima aula

[[02-hidrogeoquimica-aula-05-diagramas-hidrogeoquimicos-e-modelo-conceitual|Aula 05 — Tratamento e interpretação de dados: diagramas de Piper, Stiff e Schoeller e o modelo hidrogeoquímico conceitual]]

## Anterior

[[02-hidrogeoquimica-aula-03-composicao-quimica-das-aguas|Aula 03 — Composição química das águas de chuva, superficiais, da zona não saturada e subterrâneas; águas minerais]]

## Fontes

- Amostragem de baixa vazão e critérios de estabilização de parâmetros de campo: Puls, R. W. & Barcelona, M. J. (1996), *Low-Flow (Minimal Drawdown) Ground-Water Sampling Procedures*, USEPA/540/S-95/504; Appelo, C. A. J. & Postma, D. (2005), *Geochemical Processes and Applications*, 2ª ed., Balkema, cap. 1.
- Filtração, preservação e prazos de validade de amostra: APHA/AWWA/WEF, *Standard Methods for the Examination of Water and Wastewater*; Custodio, E. & Llamas, M. R. (1983), *Hidrología Subterránea*, Omega, cap. 13.
- Limites de detecção e quantificação: APHA *Standard Methods*, seção de garantia da qualidade.
- Padrões de qualidade brasileiros: Portaria GM/MS nº 888/2021 (Ministério da Saúde, potabilidade); Resolução CONAMA nº 396/2008 (classificação e enquadramento das águas subterrâneas).

<!--
nivel: avancado
palavras_corpo: ~1850

mapa_objetivo_secao:
  geologia-avancado-m02-oa03: "Por que a amostragem, não só a análise, decide a qualidade do dado" + "Purga: removendo a água que não representa o aquífero" + "Filtração, preservação e prazo de validade da amostra" + "Limites de detecção e de quantificação" + "Controle de qualidade (QA/QC): amostras de verificação" + "Padrões de qualidade de água" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: HIDROGEOQ-M02-A04-PURGA-001
    claim: "A purga convencional de poço remove de 3 a 5 volumes de água da coluna do poço antes da coleta; a amostragem de baixa vazão (low-flow, tipicamente menos de 0,5 L/min) monitora pH, condutividade elétrica, Eh e oxigênio dissolvido até estabilização como critério alternativo, sendo o método preferido para poços de monitoramento ambiental."
    risk: fato
    source: "Puls & Barcelona 1996, USEPA/540/S-95/504"
  - claim_id: HIDROGEOQ-M02-A04-PRESERVACAO-002
    claim: "Amostras para cátions/metais dissolvidos são filtradas em membrana de 0,45 micrômetros e acidificadas com HNO3 até pH menor que 2 para prevenir precipitação e adsorção; a alcalinidade é o parâmetro mais sensível ao tempo, idealmente titulada em campo no mesmo dia da coleta."
    risk: fato
    source: "APHA/AWWA/WEF Standard Methods; Custodio & Llamas 1983, cap. 13"
  - claim_id: HIDROGEOQ-M02-A04-LOD-003
    claim: "Limite de detecção (LOD) é a menor concentração distinguível do ruído de fundo; limite de quantificação (LOQ) é tipicamente 3 a 5 vezes o LOD; a prática conservadora recomendada para cálculos é usar metade do LOD para resultados não detectados, em vez de zero."
    risk: fato
    source: "APHA Standard Methods, seção de garantia da qualidade"
  - claim_id: HIDROGEOQ-M02-A04-PADRAO-004
    claim: "No Brasil, a Portaria GM/MS nº 888/2021 do Ministério da Saúde regula o padrão de potabilidade para consumo humano, enquanto a Resolução CONAMA nº 396/2008 estabelece diretrizes de classificação e enquadramento das águas subterrâneas segundo seus usos preponderantes, sendo normas de escopo distinto."
    risk: fato
    source: "Portaria GM/MS 888/2021; Resolução CONAMA 396/2008"
-->
