# Aula 06: Estatística de contagens, propagação de erros e limites de detecção

**ID:** geologia-avancado-m28-a06
**Módulo:** [[28-analise-instrumental-i-modulo|Módulo 28 — Análise instrumental I]]
**Duração estimada:** ~20 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** aplicar o tratamento estatístico de erro — estatística de contagens, propagação de incertezas, limite de detecção e de quantificação — que fecha o módulo e vale para toda técnica instrumental vista nas aulas anteriores.
**Ao final você vai conseguir:** calcular o erro relativo de uma contagem e o tempo de contagem necessário para reduzi-lo; combinar incertezas em somas e em razões; e calcular limite de detecção e limite de quantificação a partir do desvio-padrão do branco e da sensibilidade, julgando se um resultado sustenta ou não a interpretação geológica pretendida.
**Pré-requisito:** Aula 05 (XRF: o que o detector conta; pérola fundida e pastilha prensada), Aula 04 (curva de calibração e sensibilidade) e Aula 02 (branco de procedimento, réplicas). Assume-se noção básica de distribuição de Poisson e de desvio-padrão de graduação.

> [!note] Parte 2 de 2 da antiga Aula 05
> Esta aula e a [[28-analise-instrumental-i-aula-05-fluorescencia-de-raios-x|Aula 05]] eram uma aula só, dividida pela revisão didática de 2026-09-23 por excesso de conceitos independentes. A Aula 05 ficou com a física e a aparelhagem de XRF; esta ficou com o tratamento de erro, que não é específico de XRF.

## Conteúdo

### Estatística de contagens: por que medir raios X é, no fundo, contar fótons

A Aula 05 descreveu como um fóton de raios X é gerado e separado por energia — mas a medição final, no detector, é uma **contagem de eventos discretos** ao longo de um tempo fixo: quantos fótons daquela energia específica chegaram ao detector em, digamos, 10 ou 100 segundos. Contagens de eventos aleatórios discretos e independentes seguem, com excelente aproximação, a **distribuição de Poisson**, cuja propriedade central para esta aula é: se o número esperado de contagens é N, o desvio-padrão dessa contagem é simplesmente √N.

Essa propriedade tem uma consequência prática direta e contraintuitiva: o **erro relativo de uma contagem melhora com a raiz quadrada do tempo de contagem** (ou do número de contagens acumuladas), não linearmente. Se uma medição de 100 segundos acumula 10000 contagens, o desvio-padrão é √10000 = 100, um erro relativo de 1%. Para reduzir esse erro relativo a 0,5% — a metade —, não bastam 200 segundos: são necessárias 40000 contagens (quatro vezes mais), ou seja, 400 segundos de contagem — quatro vezes o tempo, não duas. Esse princípio, embora introduzido aqui no contexto de XRF (onde contagem de fótons é a variável nativa do instrumento), é uma propriedade estatística geral de qualquer processo de contagem de eventos discretos, e reaparece em espectrometria de massa (Aula 04) e em geocronologia (Módulos 26 e 27) sempre que a variável medida for, no fundo, um número de eventos (fótons, íons, decaimentos) contados num intervalo de tempo.

### Propagação de erros: da contagem bruta ao resultado final

O número de contagens medido no detector não é o resultado final reportado — ele passa por uma cadeia de cálculos (subtração de fundo, correção de matriz, conversão para concentração via curva de calibração) até virar um valor em percentual ou em ppm. Cada uma dessas etapas carrega sua própria incerteza, e a regra geral de **propagação de erros** determina como essas incertezas se combinam: para uma soma ou diferença de grandezas independentes, os desvios-padrão absolutos se somam em quadratura (raiz da soma dos quadrados); para um produto ou razão, são os erros relativos que se somam em quadratura. Um resultado final de XRF, portanto, carrega contribuições de erro da contagem do pico (Poisson), da contagem do fundo (também Poisson, subtraída do pico), da calibração (incerteza da inclinação e do intercepto da curva) e da preparação da amostra (Aula 02) — e um laboratório que reporta apenas "erro instrumental" de reinjeção da mesma pérola está, na melhor das hipóteses, subestimando o erro real do resultado, e na pior, escondendo a maior fonte de incerteza, que costuma estar na preparação, não no instrumento.

### Limite de detecção e limite de quantificação: definições que não são intercambiáveis

O módulo inteiro converge, na prática, para uma pergunta central levantada já no ponto de dificuldade do hub: um resultado com três casas decimais representa um sinal real acima do ruído, ou é o próprio ruído do instrumento interpretado como se fosse uma medida? A resposta formal vem das recomendações IUPAC de nomenclatura para avaliação de métodos analíticos (Currie, 1995, *Pure and Applied Chemistry*, 67(10), 1699-1723), que distinguem um **nível crítico** (L_C, o limiar de decisão "detectado / não detectado"), um **limite de detecção** (L_D) e um **limite de quantificação** (L_Q). Na prática de laboratório, os dois últimos se calculam a partir do branco, e é aí que três coisas frequentemente confundidas precisam ser mantidas separadas:

- **Branco de procedimento** (já visto na Aula 02): a medição de uma "amostra" sem o analito de interesse, processada por toda a cadeia analítica, cujo sinal e cujo desvio-padrão (σ_branco) são a base de todo o cálculo seguinte. Não é um limite, é o ponto de partida dos limites.
- **Limite de detecção** (*limit of detection*, LOD): a menor concentração cujo sinal pode ser distinguido, com confiança estatística razoável, do sinal do branco. A convenção mais usada em laboratório — a da IUPAC de 1976/78, discutida por Long & Winefordner (1983) — define LOD como três vezes o desvio-padrão do branco, dividido pela inclinação (sensibilidade) da curva de calibração: LOD = 3·σ_branco / m. A formulação de Currie (1995), que controla ao mesmo tempo falsos positivos e falsos negativos (5% cada), chega a um fator de 3,29 — na prática, o mesmo "cerca de 3". Abaixo do LOD, um resultado não deve ser interpretado como "o elemento está ausente" nem como um valor numérico confiável — apenas como "não detectado com confiança nesta condição de medição".
- **Limite de quantificação** (*limit of quantification*, LOQ): um critério mais rigoroso, geralmente definido como dez vezes o desvio-padrão do branco dividido pela sensibilidade (LOQ = 10·σ_branco / m) — a concentração mínima acima da qual o valor numérico reportado tem precisão relativa aceitável para uso quantitativo, não só para afirmar presença. O fator 10 e o trio nível crítico / limite de detecção / limite de quantificação vêm de Currie (1968, *Analytical Chemistry*, 40, 586-593), consolidados na recomendação IUPAC de 1995. Long & Winefordner (1983), "Limit of Detection: A Closer Look at the IUPAC Definition" (*Analytical Chemistry*, 55, 712A-724A), é a referência clássica que discutiu e popularizou a convenção 3σ para a comunidade de química analítica instrumental.

A distinção prática entre esses conceitos é exatamente o que o hub do módulo já sinaliza como o ponto de dificuldade central: um valor de 0,015% relatado para um elemento cujo LOQ do método é 0,02% não é um dado analítico confiável — é ruído de instrumento vestido de precisão, e tratá-lo como uma anomalia geoquímica real (por exemplo, interpretando-o como evidência de um processo petrogenético específico) é um erro de julgamento analítico, não um erro instrumental.

## Exemplo trabalhado: decidindo se um teor de Nb em um basalto sustenta uma interpretação petrogenética

**Situação.** Um laboratório reporta, por WDXRF sobre pérola de vidro fundido, um teor de Nb de 4 ppm para uma amostra de basalto, com o objetivo de discutir se a razão Nb/Y da amostra é compatível com uma fonte de manto empobrecido (razões baixas de elementos incompatíveis como Nb) ou enriquecido. O boletim do laboratório informa que o LOD do método para Nb, calculado a partir de 3σ do branco de procedimento dividido pela sensibilidade da curva de calibração, é de 3 ppm, e o LOQ (10σ) é de 10 ppm.

**Diagnóstico.** O valor reportado (4 ppm) está **acima do LOD** (3 ppm) — o laboratório pode, com razoável confiança, afirmar que há Nb detectável na amostra, distinto do ruído do branco. Mas está **abaixo do LOQ** (10 ppm) — o valor numérico específico de 4 ppm carrega uma incerteza relativa grande demais para ser usado com confiança num cálculo de razão como Nb/Y, que pretende sustentar uma conclusão petrogenética fina sobre a fonte do magma.

**Quanto é "grande demais".** Os dois números do boletim são coerentes entre si e permitem estimar essa incerteza. Se LOD = 3·σ_branco/m = 3 ppm, então σ_branco/m = 1 ppm, e o LOQ é 10 × 1 = 10 ppm, como informado. Tão perto do branco, é razoável admitir que a incerteza do resultado seja da ordem da do branco: cerca de 1 ppm sobre 4 ppm, ou **~25% de erro relativo** (1σ). Na razão Nb/Y, os erros relativos se somam em quadratura; supondo, só para o cálculo, que o Y foi medido bem acima do seu LOQ com 3% de erro relativo, o erro da razão é √(25² + 3²) ≈ 25%. O Y praticamente não pesa: a incerteza da razão é a do Nb. Uma razão com ±25% dificilmente separa as hipóteses de fonte que o estudo quer distinguir.

**Consequência para a interpretação.** Usar "Nb = 4 ppm" como se fosse um valor quantitativo preciso para calcular Nb/Y e discutir enriquecimento de fonte seria repetir exatamente o erro que o ponto de dificuldade do módulo antecipa: tratar um número que está tecnicamente "detectado, mas não quantificável com confiança" como se tivesse a mesma força probatória de um elemento maior medido a 40% com erro relativo de 1%. A leitura correta é reportar o valor com a ressalva explícita de que está entre LOD e LOQ, e — se a conclusão petrogenética depender criticamente dessa razão — buscar um método com LOD/LOQ mais baixos para Nb. Há duas saídas: repetir o XRF sobre **pastilha de pó prensado**, que não sofre a diluição do fundente (Aula 02) e é a rotina clássica de elementos-traço por XRF (Aula 05), com LOD típico de 1 a 5 ppm; ou usar ICP-MS (Aula 04), que na faixa de poucos ppm costuma ter desempenho superior ao de XRF para elementos-traço incompatíveis como o Nb.

**O que fixar.** "Detectado" e "quantificável com confiança" não são a mesma coisa, e a diferença entre os dois não é um detalhe estatístico acadêmico — é o que separa uma interpretação geológica defensável de uma conclusão construída sobre ruído instrumental.

## Recap relâmpago

- Contagem de fótons segue distribuição de Poisson: o desvio-padrão de uma contagem N é √N, e o erro relativo melhora com a raiz quadrada do tempo de contagem — reduzir o erro relativo à metade exige quadruplicar o tempo de contagem, não dobrá-lo.
- Incertezas independentes se combinam em quadratura: desvios-padrão absolutos em somas e diferenças, erros relativos em produtos e razões. Numa razão, o termo mais incerto domina — e a maior fonte de erro costuma estar na preparação, não na reinjeção instrumental.
- Branco de procedimento é a base do cálculo, não um limite. LOD = 3σ_branco/m (convenção IUPAC 1976/78; Currie 1995 dá 3,29 ao controlar falsos positivos e negativos) e LOQ = 10σ_branco/m (fator de Currie 1968), com m = sensibilidade, a inclinação da curva de calibração.
- Um resultado entre LOD e LOQ é detectável, mas não deve ser tratado como quantitativamente confiável para cálculos que exigem precisão relativa boa, como razões de elementos-traço usadas em interpretação petrogenética.

## Próxima aula

Este é o encerramento do Módulo 28. O Módulo 29 (Granitos no ciclo de Wilson) retoma a discussão de classificação geoquímica e assinatura de fonte de magmas graníticos apoiada diretamente nos dados analíticos — elementos maiores, terras-raras, razões de elementos-traço — cuja obtenção e cujos limites de confiabilidade este módulo acabou de estabelecer.

## Fontes

- Currie, L. A. (1995), "Nomenclature in Evaluation of Analytical Methods including Detection and Quantification Capabilities (IUPAC Recommendations 1995)", *Pure and Applied Chemistry*, 67(10), 1699-1723, doi:10.1351/pac199567101699. VERIFICADO por busca na redação (2026-09-23): título, autor, periódico, volume, páginas e DOI confirmados.
- Long, G. L. & Winefordner, J. D. (1983), "Limit of Detection: A Closer Look at the IUPAC Definition", *Analytical Chemistry*, 55(7), 712A-724A, doi:10.1021/ac00258a724. Paginação conferida no Crossref pela auditoria (2026-09-23); "713A" é variante de listas secundárias.
- Currie, L. A. (1968), "Limits for qualitative detection and quantitative determination. Application to radiochemistry", *Analytical Chemistry*, 40(3), 586-593, doi:10.1021/ac60259a007 — origem do trio L_C/L_D/L_Q e do fator 10 para o limite de quantificação. Acrescentada pela auditoria (2026-09-23).
- Actlabs, "Pressed Pellet XRF" — pastilha prensada como rotina de traços por XRF, LOD típico de 1 a 5 ppm. Acrescentada pela auditoria (2026-09-23).
- Jenkins, R. (1999), *X-Ray Fluorescence Spectrometry*, 2ª ed., Chemical Analysis vol. 152, Wiley-Interscience — estatística de contagens em XRF. VERIFICADO por busca na redação (2026-09-23): autor, edição, editora, ano e número do volume na série confirmados.

<!--
nivel: avancado
palavras_corpo: 1704
recontagem_didatica: "Recontado por script na revisao didatica de 2026-09-23, depois da ultima edicao, a ~84 palavras/min (achado DID-M28-DURACOES-DECLARADAS-006). Valor declarado antes: PREENCHER."
palavras_corpo_metodo: "tokens separados por espaco entre '## Conteudo' e '## Fontes', incluindo tabelas, contados por script."
duracao_estimada_min: 20

divisao_de_aula: "Parte 2 da antiga Aula 05 unica (arquivo NOVO criado pela revisao didatica de 2026-09-23, achado DID-M28-A05-SOBRECARGA-SEIS-BLOCOS-001; ID m28-a06 novo). Herdou com texto integral as secoes de estatistica de contagens, propagacao de erros e LOD/LOQ, o exemplo do Nb e os bullets 4-5 do recap. Os claims A05-004, A05-005 e A05-006 vivem neste arquivo com o prefixo A05 mantido por estabilidade (numeracao da auditoria de 2026-09-23). Acrescimos da revisao: callout de Parte 2, passo 'Quanto e grande demais' do exemplo (so aritmetica sobre os valores hipoteticos ja dados, ver claim 006), bullets de propagacao e de LOD/LOQ no recap, remissao da pastilha a Aula 05."

mapa_objetivo_secao:
  geologia-avancado-m28-oa04: "Estatística de contagens" + "Propagação de erros" + "Limite de detecção e limite de quantificação" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: ANINST-M28-A05-ESTATISTICA-POISSON-004
    claim: "Contagens de fotons de raios X seguem, com boa aproximacao, distribuicao de Poisson, cujo desvio-padrao de uma contagem N e a raiz quadrada de N; o erro relativo de uma contagem melhora com a raiz quadrada do tempo de contagem, de modo que reduzir o erro relativo a metade exige quadruplicar (nao dobrar) o tempo de contagem."
    risk: fato
    source: "Propriedade estatistica fundamental e bem estabelecida de processos de contagem de eventos discretos independentes (distribuicao de Poisson), aplicada de forma padrao em espectrometria de raios X e em contagem de particulas/fotons em geral; conhecimento consolidado de estatistica aplicada, nao dependente de uma fonte bibliografica especifica de geoquimica."
  - claim_id: ANINST-M28-A05-LOD-LOQ-FORMULAS-005
    claim: "A convencao mais usada em laboratorio define limite de deteccao (LOD) como tres vezes o desvio-padrao do branco dividido pela sensibilidade (LOD = 3*sigma_branco/m; convencao IUPAC 1976/78 discutida por Long & Winefordner 1983) e limite de quantificacao (LOQ) como dez vezes essa razao (LOQ = 10*sigma_branco/m; fator de Currie 1968). A recomendacao IUPAC de 1995 (Currie, Pure Appl. Chem. 67(10), 1699-1723) distingue L_C, L_D (~3,29 sigma0 com alfa=beta=0,05) e L_Q (10 sigma_Q). [Atribuicoes corrigidas pela auditoria 2026-09-23, achado 12: a redacao dizia que Currie 1995 definia branco/LOD/LOQ e que Long & Winefordner eram a 'formulacao original' depois formalizada por Currie.]"
    risk: fato
    source: "VERIFICADO por busca nesta redacao (2026-09-23): multiplas fontes (documento IUPAC Cha18sec437.pdf, ChemLibreTexts, MetricGate) confirmam as convencoes 3-sigma e 10-sigma para LOD e LOQ respectivamente, e a atribuicao a Currie (1995) e a discussao anterior de Long & Winefordner (1983). Observado que a formulacao original de Currie usa por vezes o fator 3,29 (approximadamente 3) para LD e ~10 (ou 16,7 em versoes revisadas com RSD assintotico) para LQ - a redacao usa os fatores simplificados 3 e 10, convencao mais didatica e mais citada na pratica de laboratorio, com a variante mais precisa sinalizada aqui como nota tecnica."
  - claim_id: ANINST-M28-A05-EXEMPLO-NB-BASALTO-006
    claim: "Exemplo pedagogico hipotetico de um teor de Nb de 4 ppm em basalto por WDXRF sobre perola, com LOD de 3 ppm e LOQ de 10 ppm, usado para discutir a diferenca entre 'detectado' e 'quantificavel com confianca' no contexto de uma razao Nb/Y; inclui a estimativa aritmetica sigma_branco/m = 1 ppm, erro relativo ~25% a 4 ppm e propagacao em quadratura para Nb/Y com um erro de Y de 3% suposto so para o calculo."
    risk: hipotetico
    source: "Exemplo pedagogico construido especificamente para a aula, com valores plausiveis para Nb em basalto e para LOD/LOQ de XRF sobre perola fundida, nao correspondentes a uma analise publicada especifica. [Auditoria 2026-09-23, achado 13: 'elementos-traco leves' retirado; pastilha prensada acrescentada como alternativa ao ICP-MS.] [Revisao didatica 2026-09-23: passo 'Quanto e grande demais' acrescentado - so aritmetica sobre os valores do proprio exemplo e as regras de propagacao da aula; a hipotese 'incerteza perto do branco ~ sigma do branco' e declarada no texto como admissao; o 3% de Y e declarado como suposicao de calculo. Nenhum fato externo novo.]"

auditoria:
  data: 2026-09-23
  modo: audit-and-fix
  relatorio: 28-analise-instrumental-i-auditoria.md
  nota_divisao: "Auditada como parte da antiga Aula 05 (arquivo 28-analise-instrumental-i-aula-05-fluorescencia-de-raios-x-estatistica-erros.md)."
  achados_nesta_aula:
    - "12 (laranja) ANINST-M28-A05-LOD-LOQ-FORMULAS-005 - L_C/L_D/L_Q de Currie; 3sigma = IUPAC 1976/78; Currie 1968 - corrigido"
    - "13 (laranja) ANINST-M28-A05-EXEMPLO-NB-BASALTO-006 - Nb nao e 'leve'; pastilha prensada como alternativa - corrigido"
  incertezas_resolvidas: "Paginacao de Long & Winefordner (712A) conferida no Crossref; marca retirada."
  verificados_sem_achado: "004 (Poisson, exemplo 10000 -> 40000 contagens)"

revisao_didatica:
  data: 2026-09-23
  modo: review-and-fix
  relatorio: 28-analise-instrumental-i-revisao-didatica.md
  achados_nesta_aula:
    - "DID-M28-A05-SOBRECARGA-SEIS-BLOCOS-001 (laranja) - antiga Aula 05 dividida; esta e a Parte 2"
    - "DID-M28-OA04-CALCULO-NAO-PRATICADO-004 (laranja) - passo numerico de LOD/LOQ e propagacao no exemplo do Nb"
-->
