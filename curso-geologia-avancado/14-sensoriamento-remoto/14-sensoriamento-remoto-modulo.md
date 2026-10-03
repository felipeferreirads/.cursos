# Módulo 14 — Sensoriamento remoto

> [!info] Área X. Métodos quantitativos e geoinformação · destino Obsidian · status: **concluído** (7/7 aulas escritas, auditadas e revisadas didaticamente · questionário completo (39 questões, 4 arquivos) · flashcards completos (96 cards))

## Objetivo do módulo
Interpretar imagens de sensores ópticos, ativos e termais e aplicar processamento digital e classificação para extrair informação geológica e ambiental.

## Pré-requisitos
[[13-geoprocessamento/13-geoprocessamento-modulo|Módulo 13]]

## Objetivos de aprendizagem
- `geologia-avancado-m14-oa01` — Explicar a interação da radiação eletromagnética com a atmosfera e com alvos naturais e relacionar o comportamento espectral à composição de água, solos, vegetação, minerais e rochas
- `geologia-avancado-m14-oa02` — Selecionar plataformas, sensores e resoluções adequados a um problema geológico e montar composições coloridas interpretáveis
- `geologia-avancado-m14-oa03` — Aplicar processamento digital de imagens (realces, razões de bandas, filtros e transformações multivariadas) e classificar imagens por métodos supervisionados e não supervisionados
- `geologia-avancado-m14-oa04` — Interpretar produtos de sensoriamento remoto ativo (Radar/SAR, InSAR, LiDAR), de fotogrametria digital e de imageamento termal

## Aulas (7)
1. [[14-sensoriamento-remoto-aula-01-conceitos-plataformas-sensores-composicoes-coloridas|Aula 01 — Conceitos, plataformas e sensores; resoluções espacial, espectral, temporal e radiométrica; composições coloridas]] — plataforma vs. sensor, passivo vs. ativo, órbita heliossíncrona, as quatro resoluções, Landsat/Sentinel-2/ASTER, composições coloridas
2. [[14-sensoriamento-remoto-aula-02-fundamentos-fisicos-radiacao-eletromagnetica-espectro-atmosfera|Aula 02 — Fundamentos físicos: radiação eletromagnética, espectro e interação com a atmosfera]] — comprimento de onda, frequência e energia, espectro eletromagnético, reflexão vs. emissão, janelas atmosféricas, espalhamento de Rayleigh e Mie
3. [[14-sensoriamento-remoto-aula-03-comportamento-espectral-agua-solos-minerais-rochas-vegetacao-geobotanica|Aula 03 — Comportamento espectral de água, solos, minerais, rochas e vegetação; geobotânica]] — curvas de reflectância, processos eletrônicos e vibracionais, feições diagnósticas de argilominerais no SWIR, curva espectral da vegetação, geobotânica como evidência indireta
4. [[14-sensoriamento-remoto-aula-04-pdi-i-realces-operacoes-aritmeticas-filtros|Aula 04 — Processamento digital de imagens I: realces, operações aritméticas e filtros de convolução]] — pré-processamento, alongamento de contraste, razões de banda, NDVI, NDWI, filtros passa-baixa/passa-alta, detecção de borda e lineamentos
5. [[14-sensoriamento-remoto-aula-05-pdi-ii-transformacoes-multivariadas-classificacao|Aula 05 — Processamento digital de imagens II: transformações multivariadas e classificação supervisionada e não supervisionada]] — Análise de Componentes Principais, ACP seletiva, K-means, Máxima Verossimilhança/SVM/Random Forest, matriz de confusão
6. [[14-sensoriamento-remoto-aula-06-sensoriamento-remoto-ativo-radar-sar-insar-lidar|Aula 06 — Sensoriamento remoto ativo: Radar/SAR, InSAR e LiDAR]] — princípio do SAR, bandas de radar, encurtamento/layover/sombra, interferometria e franjas de deslocamento, LiDAR e retornos múltiplos
7. [[14-sensoriamento-remoto-aula-07-fotogrametria-produtos-3d-sensoriamento-termal|Aula 07 — Fotogrametria digital, produtos 3D e sensoriamento remoto termal (TIR)]] — estereoscopia e paralaxe, fluxo de trabalho SfM, GCPs, ortomosaico, sensoriamento termal, leis de Planck e de Stefan-Boltzmann, janela dividida (e a ressalva da banda 11 do TIRS), feição de Christiansen e bandas de reststrahlen

## Pontos de dificuldade
Resolução espectral e resolução espacial são confundidas com frequência, e a escolha errada compromete o projeto inteiro antes do primeiro processamento. Em SAR, a geometria lateral do imageamento (encurtamento, inversão e sombra de relevo) inverte a leitura do relevo para quem vem de imagens ópticas — e qual das três ocorre depende de uma única comparação, entre a declividade da encosta e o ângulo de incidência. Três pares de conceitos de sinal oposto, apontados pela auditoria, são a armadilha fina do módulo: transferência de carga (ultravioleta, dá a cor) contra campo cristalino (0,87-0,92 µm, separa hematita de goethita) nos óxidos de ferro; feição de Christiansen (máximo de emissividade) contra bandas de reststrahlen (mínimos) no termal; e Stefan-Boltzmann (emissão total) contra a inversão de Planck (radiância de uma banda para temperatura).

## Registro do módulo
- Aulas: ✅ 7 / 7 escritas (18.566 palavras medidas; a06 e a07 pesam ~40 min, as demais ~30 min)
- Auditoria científica: ✅ **aprovada** — [[14-sensoriamento-remoto-auditoria|relatório]] · 11 achados (2 🔴 · 5 🟠 · 2 🟡 · 2 ⚪), todos corrigidos ou registrados, `open_findings: []`. Nenhum achado quantitativo: os sete exemplos numéricos foram recalculados e conferem. Nenhum achado bibliográfico: as 23 referências estão corretas.
- Revisão didática: ✅ **bem ensinado com ressalvas** — [[14-sensoriamento-remoto-revisao-didatica|relatório]] · 10 achados (4 🟠 · 3 🟡 · 3 🔵). Sem salto de pré-requisito, sem objetivo descoberto, sem seção órfã.
- Questionário: ✅ concluído — **3 parciais + 1 final cumulativo**: [[14-sensoriamento-remoto-questionario-parcial-1|parcial 1 (a01-a03, oa02+oa01, 10 questões)]] · [[14-sensoriamento-remoto-questionario-parcial-2|parcial 2 (a04-a05, oa03, 9 questões)]] · [[14-sensoriamento-remoto-questionario-parcial-3|parcial 3 (a06-a07, oa04, 10 questões)]] · [[14-sensoriamento-remoto-questionario-final|final cumulativo (todo o módulo, 10 questões)]] — 39 questões no total, 100 pontos cada questionário, cobertura: oa02 integral (a01, com peso reforçado por ser ensinado numa única aula) e oa01 integral (a02+a03) na parcial 1 + reforço no final, oa03 integral na parcial 2 + reforço no final, oa04 integral na parcial 3 + reforço no final. O final concentra a discriminação dos três pares de sinal oposto da auditoria e a cadeia integrada a01-a07 que nenhum exemplo trabalhado individual do módulo percorre (achado DID-M14-INTEGRACAO-009)
- Flashcards: ✅ **concluído** — 58 Basic (fb001–fb058) · 38 Cloze (fc001–fc038) · 96 cards no total · formato CSV compatível com Anki · validação zero-erro (10 avisos esperados sobre múltiplas lacunas em cards complexos) · cobertura: oa01 (a02-a03), oa02 (a01), oa03 (a04-a05), oa04 (a06-a07), com ênfase nos três pares de sinal oposto apontados pela auditoria

> [!warning] Encaminhado ao orquestrador, não executado
> A revisão didática registrou que a **Aula 07 são duas meias-aulas independentes** (fotogrametria | termal), com corte limpo disponível, e que a **Aula 06** também admite corte limpo (radar | LiDAR). Dividir a metade final do módulo em 9 aulas é decisão do gerador de curso, deliberadamente não tomada aqui. Enquanto isso, as duas aulas declaram a própria carga e o ponto de corte ao leitor.

## Navegação
Anterior: [[13-geoprocessamento/13-geoprocessamento-modulo|Módulo 13 — Geoprocessamento]] · Próximo: [[15-petrofisica/15-petrofisica-modulo|Módulo 15 — Introdução à petrofísica]] · Índice: [[_curso|Voltar ao curso]]
