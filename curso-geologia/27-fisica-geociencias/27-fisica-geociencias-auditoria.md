# Auditoria científica — Módulo 27: Física para geociências

**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Data:** 2026-08-19
**Escopo:** as 6 aulas do módulo, auditadas em conjunto (aulas 01–06), incluindo
consistência interna entre elas (mesmo valor de densidade crustal usado nas aulas 03 e 05; mesma convenção de incerteza entre as aulas 01, 03 e 05; e verificação de que as aulas 03 e 06 realmente entregam o conteúdo prometido pelos objetivos `geologia-m17-oa01` e `geologia-m19-oa01`, que motivaram a criação deste módulo). **Veredito: Aprovado.** 0 achados 🔴, 0 achados 🟠, 0 achados 🟡, 0 achados 🔵, 0 achados ⚪.

## Metodologia

Leitura das 6 aulas em conjunto, listagem de todas as alegações verificáveis (definições, leis físicas, fórmulas, valores numéricos e exemplos calculados), verificação por `web_search` dos pontos de maior risco — gradiente geotérmico continental, papel da tensão diferencial na orientação da deformação estrutural, e o problema da não unicidade em inversão gravimétrica/magnética — e recálculo independente de todos os exemplos trabalhados (aritmética de física básica), além de checagem cruzada de consistência interna entre as aulas do módulo.

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `GEO-M27-A01-GRANDEZA-UNIDADE-001` | Grandeza física medida por comparação com unidade padrão; dimensões diferentes não se somam | Física geral básica; SI (BIPM) | Confirmado |
| `GEO-M27-A01-INCERTEZA-002` | Toda medida carrega incerteza ligada à resolução do instrumento, convenção valor ± incerteza | Física geral básica; metrologia | Confirmado |
| `GEO-M27-A01-PRECISAO-EXATIDAO-003` | Precisão e exatidão são conceitos independentes | Física geral básica; metrologia | Confirmado |
| `GEO-M27-A01-SIGFIG-004` | Algarismos significativos devem refletir a resolução do instrumento | Física geral básica; convenções de notação científica | Confirmado |
| `GEO-M27-A01-GEOCRON-INCERTEZA-005` | Idades radiométricas publicadas como valor ± incerteza | Prática consolidada de geocronologia (consistente com o Módulo 03 do curso) | Confirmado |
| `GEO-M27-A02-LEIS-NEWTON-001` | As três leis de Newton (inércia, F=ma, ação-reação) | Mecânica clássica, consolidada em qualquer texto de física geral | Confirmado |
| `GEO-M27-A02-MASSA-PESO-002` | Massa é propriedade intrínseca (kg); peso é força gravitacional sobre a massa (N), varia com gravidade local | Física geral básica | Confirmado |
| `GEO-M27-A02-DECOMPOSICAO-TALUDE-003` | Peso decomposto em componente perpendicular (∝cos θ) e paralela (∝sen θ) a um plano inclinado | Mecânica clássica — análise padrão de plano inclinado | Confirmado — recalculado de forma independente |
| `GEO-M27-A02-ATRITO-EQUILIBRIO-004` | Bloco em talude permanece em repouso enquanto atrito disponível cancela a componente do peso paralela à encosta | Mecânica clássica aplicada de forma introdutória; consistente com princípios gerais de estabilidade de taludes | Confirmado |
| `GEO-M27-A03-PRESSAO-DEFINICAO-001` | Pressão = força/área (Pa), isotrópica | Física geral básica; mecânica dos fluidos | Confirmado |
| `GEO-M27-A03-PRESSAO-LITOSTATICA-002` | Pressão litostática ≈ ρ·g·h, isotrópica em equilíbrio | Twiss & Moores, *Structural Geology*; Fossen, *Structural Geology* | Confirmado |
| `GEO-M27-A03-TENSAO-VS-PRESSAO-003` | Tensão é o conceito geral (pode variar com direção); pressão é o caso isotrópico particular | Twiss & Moores; Davis, Reynolds & Kluth, *Structural Geology of Rocks and Regions* | Confirmado |
| `GEO-M27-A03-NORMAL-CISALHANTE-004` | Tensão decomposta em componente normal e cisalhante em qualquer plano | Twiss & Moores; mecânica dos meios contínuos básica | Confirmado |
| `GEO-M27-A03-TENSAO-DIFERENCIAL-005` | Tensão diferencial (não a pressão litostática isotrópica) controla a orientação da deformação (dobras, falhas) | Twiss & Moores; Fossen — confirmado por busca web (opengeology.org, *An Introduction to Geology*: "deformation results from application of a differential stress"; strike/dip de fraturas consequência da orientação da tensão) | Confirmado |
| `GEO-M27-A04-TRABALHO-001` | Trabalho = F·d (J), mesma unidade de energia | Física geral básica | Confirmado |
| `GEO-M27-A04-ENERGIA-POTENCIAL-CINETICA-002` | Ep=m·g·h; Ec=½·m·v², cresce com o quadrado da velocidade | Física geral básica | Confirmado |
| `GEO-M27-A04-CONSERVACAO-003` | Conservação de energia em sistema isolado; dissipação por atrito | Física geral básica (primeira lei da termodinâmica, forma mecânica) | Confirmado |
| `GEO-M27-A04-TERREMOTO-ENERGIA-004` | Energia elástica acumulada e liberada na ruptura, parte convertida em ondas sísmicas, parte dissipada como calor por atrito | Stein & Wysession, *An Introduction to Seismology, Earthquakes, and Earth Structure* (modelo de rebote elástico de Reid) | Confirmado |
| `GEO-M27-A04-POTENCIA-005` | Potência = energia/tempo (W) | Física geral básica | Confirmado |
| `GEO-M27-A05-CALOR-TEMPERATURA-001` | Calor é energia térmica em trânsito; temperatura mede agitação média das partículas | Física geral básica (termodinâmica) | Confirmado |
| `GEO-M27-A05-TRES-MECANISMOS-002` | Condução, convecção e radiação como os três mecanismos de transporte de calor | Física geral básica; Turcotte & Schubert, *Geodynamics* | Confirmado |
| `GEO-M27-A05-CONDUCAO-CROSTA-003` | Condução domina o transporte de calor na crosta rígida | Turcotte & Schubert; Fowler, *The Solid Earth* | Confirmado |
| `GEO-M27-A05-CONVECCAO-MANTO-004` | Convecção domina no manto dúctil; motor proposto da tectônica de placas | Turcotte & Schubert — hipótese amplamente aceita, com balanço de forças ainda em debate (nota de escopo já registrada como pendência ⚪ transversal M02-F04/F06 em `_contexto.md`, não repetida como novo achado aqui pois a aula não afirma consenso fechado sobre o balanço quantitativo) | Confirmado |
| `GEO-M27-A05-GRADIENTE-GEOTERMICO-005` | Gradiente geotérmico continental próximo à superfície da ordem de 25–30 °C/km, variando regionalmente | Confirmado por busca web: valor comumente citado ~25 °C/km, faixa continental 20–40 °C/km, mais baixo em crátons estáveis (~10 °C/km), mais alto em regiões vulcânicas (>100 °C/km) — [Geothermal gradient, Wikipedia](https://en.wikipedia.org/wiki/Geothermal_gradient); [AAPG Wiki — Geothermal gradient](https://wiki.aapg.org/Geothermal_gradient) | Confirmado — valor de ordem de grandeza (LC-05), consistente com a faixa documentada |
| `GEO-M27-A06-CAMPO-DEFINICAO-001` | Campo físico atribui valor a cada ponto do espaço, prevê força sem contato | Física geral básica (conceito de campo em física clássica) | Confirmado |
| `GEO-M27-A06-CAMPO-GRAVITACIONAL-002` | Toda massa produz campo gravitacional; g varia com densidade do subsolo, latitude e altitude | Telford, Geldart & Sheriff, *Applied Geophysics*; Lowrie, *Fundamentals of Geophysics* | Confirmado |
| `GEO-M27-A06-CAMPO-MAGNETICO-003` | Campo magnético terrestre gerado no núcleo externo; minerais magnéticos contribuem com campo local adicional | Fowler, *The Solid Earth*; Lowrie, *Fundamentals of Geophysics* | Confirmado |
| `GEO-M27-A06-ANOMALIA-DEFINICAO-004` | Anomalia = medido − esperado por modelo de referência; positiva/negativa indicam excesso/déficit de massa ou magnetização | Telford, Geldart & Sheriff, *Applied Geophysics* | Confirmado |
| `GEO-M27-A06-NAO-UNICIDADE-005` | Diferentes distribuições de massa/magnetização podem produzir anomalias indistinguíveis na superfície | Confirmado por busca web: "the non-uniqueness of gravity or magnetic data inversion is well known... multiple inverse solutions can explain the measurements equally well" — [On the Non-uniqueness of Gravitational and Magnetic Field Data Inversion, Springer](https://link.springer.com/chapter/10.1007/978-3-319-57181-2_15) | Confirmado |

## Consistência interna verificada

- A densidade crustal usada no exemplo trabalhado da aula 03 (2.700 kg/m³) é a mesma ordem de grandeza padrão de densidade crustal usada implicitamente em outros módulos do curso (crosta continental, Módulos 01/02) — sem divergência.
- A convenção "valor ± incerteza" apresentada na aula 01 é usada de forma consistente (sem contradição) quando a aula 03 e a aula 05 tratam valores como "ordem de grandeza" (25–30 °C/km) em vez de precisão de laboratório — ambas seguem a mesma lógica de honestidade sobre a resolução/variabilidade do dado, sob a regra LC-05 do curso.
- Todos os exemplos trabalhados (aulas 01 a 06) foram recalculados de forma independente; nenhuma discrepância aritmética encontrada.
- As aulas 03 e 06 foram conferidas especificamente contra os objetivos `geologia-m17-oa01` e `geologia-m19-oa01` do `course-state.yaml`: a aula 03 entrega pressão, pressão litostática, pressão hidrostática, tensão, tensão normal e tensão cisalhante; a aula 06 entrega campo físico, campo gravitacional, campo magnético e anomalia — ambas cobrem integralmente o que os dois objetivos prometem.
- Nenhuma aula deste módulo redefine vocabulário de física já usado implicitamente em aulas-ponte anteriores do curso (onda, Módulo 02 aula 01; energia/calor qualitativo, Módulo 09 aula 01) de forma divergente — checado por leitura cruzada.

## Nota (fora do escopo da auditoria, apenas registro)

A aula 05 registra explicitamente, em "O que não concluir", que o gradiente geotérmico não é linear até o centro da Terra e que o valor de 25–30 °C/km só vale para os primeiros quilômetros da crosta — a aula já antecipa a limitação que a busca web confirmou (o valor de referência muda com o contexto tectônico e com a profundidade). Isso não é um achado, é a aula prevenindo corretamente a generalização indevida.

## Correções aplicadas

Nenhuma. Nenhum achado 🔴/🟠/🟡/🔵/⚪ — nada a corrigir nesta rodada.

**Pendências:** nenhuma. O módulo está liberado para gerar o questionário final.
