# Aula 02: Tipos e organização de dados geológicos — litologia, geoquímica, geocronologia, sedimentos de corrente, ocorrências, aerogeofísica e isótopos

**ID:** geologia-avancado-m25-a02
**Módulo:** [[25-aquisicao-digital-ia-geociencias-modulo|Módulo 25 — Aquisição de dados digitais e inteligência artificial em geociências]]
**Duração estimada:** ~27 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** reconhecer as famílias de dados que um projeto geológico reúne, entender o que cada uma realmente mede (o suporte, a unidade e a incerteza) e organizá-las numa base consistente, resolvendo os três problemas que mais corrompem uma integração: coordenadas em datums diferentes, unidades misturadas e valores abaixo do limite de detecção.
**Ao final você vai conseguir:** descrever, para cada tipo de dado, a unidade de observação e a armadilha típica; normalizar unidades e sinalizar valores censurados numa tabela; juntar tabelas por identificador de amostra sem perder informação; e explicar por que a substituição de valores censurados por um número altera as estatísticas.
**Pré-requisito:** [[25-aquisicao-digital-ia-geociencias-aula-01-aquisicao-digital-campo-ferramentas-imagens-croquis|Aula 01 — Aquisição digital de dados em campo]] (o registro único com identificador, coordenada e metadados) e a familiaridade com `pandas` vista no [[24-machine-learning-geociencias-modulo|Módulo 24]].

## Conteúdo

### Sete famílias de dados, sete maneiras de errar

Um projeto de mapeamento ou de exploração mineral raramente trabalha com um só tipo de dado. Ele junta observações feitas por instrumentos, laboratórios, satélites e pessoas, em épocas diferentes, e cada família traz uma **unidade de observação** própria: aquilo a que uma linha da tabela, ou um pixel do grid, se refere de fato. Confundir essa unidade é a origem dos erros mais caros de integração. A tabela resume; o texto abaixo comenta o que a tabela não cabe.

| Família | Unidade de observação | Números típicos | Armadilha principal |
|---|---|---|---|
| Litologia (descrição) | ponto de afloramento ou trecho de furo | código de legenda, texto | vocabulário livre, mesma rocha com nomes diferentes |
| Geoquímica (rocha, solo) | uma amostra em laboratório | ppm, ppb, % em peso | unidades misturadas; valores abaixo do limite de detecção |
| Sedimento de corrente | ponto na drenagem que representa uma **bacia a montante** | ppm, ppb | ler o valor como se fosse do ponto, e não da bacia |
| Geocronologia | um mineral datado ou uma população de grãos | idade em Ma, incerteza (2σ) | esquecer a incerteza e o que a idade significa |
| Ocorrências minerais | ponto cadastrado | substância, tipo, situação | ocorrência não é depósito; qualidade heterogênea |
| Aerogeofísica | **grid** (célula) derivado de linhas de voo | nT, % K, ppm eTh, ppm eU | tratar como ponto de precisão que não tem |
| Isótopos | uma análise de amostra | razões, εNd, δ¹⁸O | notação e padrão de referência |

### Litologia: o dado que parece texto e é classificação

A descrição de campo é um dado **categórico**: nesta rocha, a lista permitida de valores importa mais do que a riqueza da frase. Se a coluna litológica aceita texto livre, o banco terá "granito", "Granito", "granitóide", "gr." e "granito porfirítico" como cinco categorias, e nenhum algoritmo (nem uma consulta) as reconhece como a mesma. O remédio é a **lista de domínio** definida na preparação do formulário (Aula 01) e uma tabela de legenda com código, nome e cor, mantida à parte e referenciada por chave. Uma boa prática: separar a **observação** ("rocha equigranular, cinza, com biotita e feldspato") da **interpretação** ("Granito X, da suíte Y"), em colunas distintas. A observação envelhece bem; a interpretação muda quando o mapa é revisado, e o banco precisa saber qual das duas está lendo.

### Geoquímica: valores, unidades e limites de detecção

Uma análise química reporta um valor **por elemento e por método**, em unidades que variam com o elemento e o laboratório: elementos maiores em % em peso de óxido, traços em ppm (mg/kg), ouro em ppb (µg/kg) ou ppm. O primeiro trabalho é converter tudo a **uma unidade por elemento**. O segundo é lidar com o **limite de detecção (LD)**: quando o teor é menor que o mínimo que o método distingue do ruído, o laboratório reporta "<5" e não um número. O valor é **censurado**: sabe-se que está em algum lugar entre 0 e 5, e mais nada.

Duas armadilhas concentram os erros. A primeira: uma coluna numérica que contém a string "<5" vira coluna de texto e trava qualquer cálculo; a solução é separar em duas colunas, o **valor** (o limite, quando censurado) e um **indicador** de censura. A segunda: substituir os valores censurados por um número (zero, o LD, ou a metade do LD, prática muito comum) e seguir como se fossem medidas. O exemplo trabalhado 2 mostra o tamanho do efeito. Existem métodos estatísticos próprios para dados censurados (Helsel, 2012, é a referência clássica), e a Aula 05 volta ao ponto quando a censura contamina o treino de um modelo.

Outro fato que muda a estatística: análises de composição (teores que somam 100%, como os óxidos de uma rocha) **não são variáveis independentes**, porque o aumento de um componente obriga a queda de outros — se a sílica sobe, algo tem de descer, e as duas colunas vão aparecer correlacionadas negativamente mesmo que nada geológico as ligue. A tradição de Aitchison (1986) trata esses dados por razões logarítmicas (*log-ratios*) antes de qualquer correlação ou modelo.

Este ponto entra aqui como **alerta, não como técnica**: o tratamento por razões logarítmicas está fora do escopo deste curso, e nenhuma aula adiante o desenvolve. O que você deve levar é a desconfiança operacional — ao ver uma matriz de correlação de **elementos maiores** em % de óxido, parte do que ela mostra é artefato do fechamento em 100%, e a conclusão precisa dizer isso. Nas matrizes de correlação do [[24-machine-learning-geociencias-modulo|Módulo 24]], que usaram teores de elementos-traço em ppm, o efeito é pequeno, porque esses teores somam uma fração ínfima do total; é nos maiores que ele morde.

### Sedimento de corrente: o ponto que representa uma bacia

Uma amostra de sedimento de corrente é coletada num ponto, mas o material que ela contém veio de **toda a bacia de captação a montante**. Um valor alto de cobre no ponto não diz que há cobre no ponto; diz que **em algum lugar da bacia** há uma fonte, cuja assinatura chega diluída. A diluição depende da área da bacia e do tamanho da fonte (Hawkes, 1976, trata da diluição a jusante de anomalias). Consequência para o banco: junto com cada amostra convém guardar, ou poder calcular, a **bacia de captação** (polígono ou área), e comparar amostras de bacias de tamanho parecido. Ler a anomalia como do ponto é o erro mais comum na interpretação desses dados.

### Geocronologia: idade com incerteza e com significado

Uma idade U-Pb em zircão vem sempre com **incerteza** (geralmente 2σ) e com um **significado geológico**: idade de cristalização de um magmatismo, idade de um evento metamórfico que recristalizou o grão, idade de um grão detrítico herdado da fonte. Uma tabela que guarde apenas "2712" perde o que a interpretação exige. O mínimo é: idade, incerteza, método, mineral, e um campo de **interpretação**. As bases e as convenções de cálculo ficam para o [[26-geologia-isotopica-aplicada-modulo|Módulo 26]]; aqui basta que o banco tenha onde guardá-las.

### Ocorrências minerais

Um cadastro de ocorrências (no Brasil, o acervo do Serviço Geológico do Brasil, o SGB-CPRM, disponibilizado no portal GeoSGB) registra pontos onde alguém reconheceu uma substância mineral, com o tipo e, às vezes, o porte do depósito. Serve de base de posições conhecidas de mineralização, e é justamente daí que a Aula 05 vai extrair os "rótulos positivos" dos modelos de prospectividade. Duas ressalvas: **ocorrência não é depósito** (a maioria dos pontos são indícios sem valor econômico comprovado) e a **qualidade é heterogênea** (pontos cadastrados por autores, escalas e épocas diferentes, alguns com coordenada de centro de folha). Um rótulo feito de um cadastro assim carrega esses defeitos para o modelo.

### Aerogeofísica: um grid não é um ponto

Os dados aerogeofísicos são medidos ao longo de **linhas de voo** e interpolados para um **grid** regular. O que se tem é um raster: cada célula tem tamanho (por exemplo, algumas centenas de metros, função do espaçamento entre linhas e da altura de voo) e valores de magnetometria (campo magnético total, em nT) e de gamaespectrometria (potássio em %, equivalente de tório e de urânio em ppm). O erro típico de integração é **extrair o valor da célula sob um ponto de amostragem e tratá-lo como uma medida no ponto**: o valor do grid representa uma área e foi suavizado por interpolação. Guardam-se, nos metadados do grid, espaçamento entre linhas, altura de voo, direção, ano e nivelamento; sem eles, não se sabe que feições o dado pode resolver. As técnicas de interpretação estão no [[16-aerogeofisica-modulo|Módulo 16]] e no [[19-geofisica-exploracao-mineral-modulo|Módulo 19]].

### Isótopos: números que só fazem sentido com a notação

Razões isotópicas (⁸⁷Sr/⁸⁶Sr, ¹⁴³Nd/¹⁴⁴Nd) e desvios em notação delta (δ¹⁸O) só se interpretam com o **padrão de referência** e, no caso de εNd, com o **parâmetro de referência** (o reservatório condrítico) e o tempo a que se refere o valor. O banco deve guardar, junto ao número, a notação, o padrão e o tempo de referência; senão duas colunas "εNd" de origens diferentes, uma calculada hoje e outra na época de cristalização, viram uma coluna só sem que se perceba.

### Organizando: a chave, as tabelas e as coordenadas

O princípio que amarra tudo é o do **identificador único de amostra**, a chave que liga tabelas: uma tabela de amostras (uma linha por amostra, com coordenada, tipo, coletor, data), uma de análises químicas (uma linha por **amostra × elemento × método**, no formato "longo") e uma de idades, de isótopos e assim por diante. Por que não pôr tudo numa planilha larga, com uma coluna para cada elemento? Porque as análises são muitas, esparsas (cada amostra tem um subconjunto de elementos, métodos diferentes) e cada uma leva metadados próprios (método, laboratório, limite de detecção). O formato longo aguenta isso; a planilha larga, derivada dele para modelagem, é uma **visão**, não o dado. A Aula 04 leva esta ideia a um banco relacional.

Por fim, as **coordenadas**. No Brasil o sistema geodésico oficial é o **SIRGAS 2000**, adotado pela Resolução PR nº 1/2005 do IBGE, de **25 de fevereiro de 2005**, com um período de transição de dez anos em que o SAD69 e o Córrego Alegre ainda podiam ser usados em paralelo; desde **25 de fevereiro de 2015** o SIRGAS 2000 é o único sistema de referência oficialmente adotado no país. As coordenadas UTM em SIRGAS 2000 têm códigos EPSG próprios (por exemplo, o fuso 23 sul é o EPSG:31983, e o sistema geográfico é o EPSG:4674). Misturar um ponto em SAD69 com pontos em SIRGAS 2000 sem converter produz um deslocamento da ordem de algumas dezenas de metros, dependendo da região (consulte o IBGE para o valor da sua área), o suficiente para um ponto "cair" do outro lado de um contato ou de uma drenagem. Regra: **toda tabela com coordenada guarda o sistema (EPSG) em coluna própria**, e a conversão ao sistema do projeto se faz uma vez, no início.

## Exemplo trabalhado 1: normalizar, sinalizar a censura e juntar

**Situação.** Você recebe quatro amostras, uma tabela de análises (ouro em ppb e em ppm, valores como "<5", cobre em ppm) e uma idade U-Pb. O objetivo: uma tabela única, uma linha por amostra, com o ouro numa só unidade e a censura sinalizada.

```python
import pandas as pd, numpy as np, io

amostras = pd.read_csv(io.StringIO("""id_amostra,tipo,leste_m,norte_m,datum,litologia
GA-001,rocha,652310,7801520,SIRGAS2000,granito
GA-002,rocha,652980,7801875,SIRGAS2000,xisto
GA-003,sedimento_corrente,653400,7802300,SAD69,sedimento
GA-004,sedimento_corrente,654010,7802950,SIRGAS2000,sedimento
"""))
quimica = pd.read_csv(io.StringIO("""id_amostra,elemento,valor,unidade,limite_deteccao
GA-001,Au,<5,ppb,5
GA-002,Au,12,ppb,5
GA-003,Au,0.030,ppm,0.005
GA-004,Au,<0.005,ppm,0.005
GA-001,Cu,48,ppm,1
GA-002,Cu,95,ppm,1
"""))
idade = pd.DataFrame({"id_amostra": ["GA-001"], "metodo": ["U-Pb zircao"],
                      "idade_Ma": [2712], "incerteza_2s_Ma": [8]})

q = quimica.copy()
q["censurado"] = q["valor"].astype(str).str.startswith("<")
q["valor_num"] = q["valor"].astype(str).str.lstrip("<").astype(float)
fator = {"ppb": 1.0, "ppm": 1000.0}            # só para o Au: ppm -> ppb
au = q["elemento"] == "Au"
q.loc[au, "valor_num"] *= q.loc[au, "unidade"].map(fator)
q.loc[au, "limite_deteccao"] *= q.loc[au, "unidade"].map(fator)
q.loc[au, "unidade"] = "ppb"

larga = q.pivot(index="id_amostra", columns="elemento", values="valor_num")
larga["Au_censurado"] = q[au].set_index("id_amostra")["censurado"]
base = (amostras.set_index("id_amostra")
        .join(larga).join(idade.set_index("id_amostra")))
print(base[["tipo", "datum", "Au", "Au_censurado", "Cu", "idade_Ma"]])
print("Datum misto:", base["datum"].value_counts().to_dict())
```

**Saída obtida:** as quatro amostras ficam com Au de **5, 12, 30 e 5 ppb**; GA-001 e GA-004 marcadas como **censuradas**; o Cu existe só em GA-001 e GA-002 (as demais ficam `NaN`, não zero: ausência de análise não é teor nulo); a idade de 2712 Ma existe só em GA-001; e a contagem de datum revela **`{'SIRGAS2000': 3, 'SAD69': 1}`**, isto é, uma amostra fora do sistema do projeto (GA-003), a ser convertida antes de qualquer uso espacial.

**O que o exemplo ensina.** Três coisas em uma tabela de quatro linhas. (i) A conversão de ppm para ppb do ouro (0,030 ppm = 30 ppb) só funciona porque cada linha carrega a sua unidade; sem essa coluna a soma seria silenciosamente errada por um fator mil. (ii) O valor "5" de GA-001 e GA-004 **não é uma medida**: é o LD, e o indicador `Au_censurado` impede que ele seja lido como tal. (iii) O `join` à esquerda preservou as quatro amostras; um `join` interno teria descartado três delas por não terem idade.

## Exemplo trabalhado 2: quanto vale a convenção para os censurados?

**Situação.** Com o ouro do exemplo anterior, [5 (censurado), 12, 30, 5 (censurado)], compare a média segundo três convenções de substituição dos censurados.

**Resolução.**

- Substituir pelo próprio LD (5): (5 + 12 + 30 + 5) / 4 = **13,00 ppb**.
- Substituir por LD/2 (2,5): (2,5 + 12 + 30 + 2,5) / 4 = **11,75 ppb**.
- Substituir por zero: (0 + 12 + 30 + 0) / 4 = **10,50 ppb**.

A média varia de 10,5 a 13,0 ppb, ou cerca de **24% em relação ao menor valor**, apenas pela convenção, sobre exatamente as mesmas análises. Com metade das amostras censuradas, a "média" não é uma propriedade do terreno: é uma propriedade da convenção. Com poucas amostras censuradas em milhares, o efeito some; com **muitas** (típico do ouro e de elementos de fundo baixo), é decisivo. A prática defensável é **não substituir no banco**: guardar o valor e o indicador, e escolher o tratamento no momento do uso, declarando-o.

## Recap relâmpago

- Cada família de dado tem uma **unidade de observação** diferente: amostra, ponto que representa uma **bacia** (sedimento de corrente), **grid** de células (aerogeofísica), ponto cadastrado (ocorrência).
- Litologia é dado categórico: use **listas de domínio** e separe observação de interpretação.
- Valores abaixo do limite de detecção são **censurados**: guarde o valor e um **indicador**; substituir por zero, LD ou LD/2 muda as estatísticas, mais ainda quando há muitos censurados.
- Guarde **unidade por linha**, **método**, **incerteza** (idades) e **notação de referência** (isótopos): sem esses metadados o número não é interpretável.
- Organize com um **identificador único de amostra** e tabelas ligadas por chave; o formato longo é o dado, a planilha larga é uma visão.
- **Datum** é coluna obrigatória: misturar SAD69 com SIRGAS 2000 desloca pontos em dezenas de metros. Ausência de análise é `NaN`, nunca zero.

## Próxima aula

[[25-aquisicao-digital-ia-geociencias-aula-03-estereoscopia-digital-interpretacao-estrutural-integrada|Aula 03 — Estereoscopia digital por anaglifos e interpretação estrutural integrada]]: os dados desta aula são pontuais ou em grid; a próxima mostra como extrair estrutura geológica **de imagens e de modelos digitais de terreno**, em hierarquia de escala, e integrar com a aerogeofísica.

## Fontes

- Helsel, D. R. (2012), *Statistics for Censored Environmental Data Using Minitab and R*, 2ª ed., Wiley.
- Aitchison, J. (1986), *The Statistical Analysis of Compositional Data*, Chapman & Hall.
- Hawkes, H. E. (1976), "The downstream dilution of stream sediment anomalies", *Journal of Geochemical Exploration*, 6, 345-358.
- Serviço Geológico do Brasil (SGB-CPRM), portal GeoSGB, geosgb.sgb.gov.br (ocorrências minerais, litologia, geoquímica, aerogeofísica).
- IBGE, Sistema de Referência Geocêntrico para as Américas (SIRGAS 2000): informações de adoção, transição e transformação SAD69 para SIRGAS 2000 (ibge.gov.br).
- Registro de códigos EPSG (epsg.org) para os sistemas de coordenadas citados.

<!--
nivel: avancado
palavras_corpo: 2264
mapa_objetivo_secao:
  geologia-avancado-m25-oa02: "Sete famílias de dados" + cada subseção de tipo + "Organizando: a chave, as tabelas e as coordenadas" + "Exemplo trabalhado 1" + "Exemplo trabalhado 2"

alegacoes_auditaveis:
  - claim_id: DIGGEO-M25-A02-CENSURA-CONVENCOES-001
    claim: "Para o ouro [5 (censurado), 12, 30, 5 (censurado)] ppb, a media com censurados substituidos por LD (5) e 13.00, por LD/2 (2.5) e 11.75, por zero e 10.50; a variacao de 10.5 a 13.0 e cerca de 24% em relacao ao menor valor (13/10.5=1.238)."
    risk: calculo
    source: "Aritmetica direta, conferida na redacao."
  - claim_id: DIGGEO-M25-A02-TABELA-JUNCAO-002
    claim: "O codigo apresentado produz Au = 5, 12, 30, 5 ppb (0.030 ppm = 30 ppb), censurados GA-001 e GA-004, Cu apenas em GA-001 e GA-002, idade apenas em GA-001 e datum {'SIRGAS2000': 3, 'SAD69': 1}."
    risk: calculo
    source: "Execucao direta do codigo (Python, pandas), 2026-09-21."
  - claim_id: DIGGEO-M25-A02-CENSURA-TRATAMENTO-003
    claim: "Valores abaixo do limite de deteccao sao dados censurados; ha metodos estatisticos proprios para eles e a substituicao por constante (zero, LD, LD/2) enviesa as estatisticas, tanto mais quanto maior a proporcao de censurados."
    risk: fato
    source: "Helsel, D. R. (2012), Statistics for Censored Environmental Data Using Minitab and R, 2a ed., Wiley, ISBN 9780470479889, DOI 10.1002/9781118162729. REFERENCIA VERIFICADA na auditoria de 2026-09-21 (titulo, edicao, editora e ano conferem; Wiley Series in Statistics in Practice). O livro aplica metodos de analise de sobrevivencia, inclusive para dados censurados por intervalo, a contaminantes em baixa concentracao - o que sustenta a afirmacao da aula de que ha metodos proprios. Nenhum numero foi tirado do livro; a aula so o cita como referencia de metodo."
  - claim_id: DIGGEO-M25-A02-COMPOSICIONAL-004
    claim: "Dados composicionais (partes de um todo constante, como oxidos somando 100%) nao sao variaveis independentes e correlacoes entre teores brutos sao parcialmente artificiais; a tradicao de Aitchison propoe razoes logaritmicas."
    risk: fato
    source: "Aitchison, J. (1986), The Statistical Analysis of Compositional Data, Chapman & Hall (Monographs on Statistics and Applied Probability). REFERENCIA VERIFICADA na auditoria de 2026-09-21. A aula nao atribui numero nenhum ao livro, so a tese de que dados composicionais exigem transformacao por razoes logaritmicas antes de correlacao ou modelo - que e o conteudo central da obra. PASSAGEM 2 (2026-09-21), item azul B15: a citacao interna desta alegacao ao Modulo 24 foi CONFERIDA NO PROPRIO ARQUIVO da Aula 02 do M24 - as variaveis da matriz de correlacao sao Cu, Zn e As em ppm (mais Au em ppb e duas variaveis nao composicionais), de modo que a afirmacao de que o efeito de fechamento e menor ali que nos elementos maiores esta correta."
  - claim_id: DIGGEO-M25-A02-SEDIMENTO-CORRENTE-BACIA-005
    claim: "O sedimento de corrente representa a bacia de captacao a montante do ponto de coleta, e a assinatura de uma fonte e diluida a jusante em funcao da area da bacia e do tamanho da fonte."
    risk: fato
    source: "Hawkes, H. E. (1976), 'The downstream dilution of stream sediment anomalies', J. Geochem. Explor. 6, 345-358. REFERENCIA VERIFICADA na auditoria de 2026-09-21 (titulo, revista, volume e paginas conferem). O tema do artigo - diluicao a jusante pela mistura de sedimento de areas mineralizadas e nao mineralizadas durante o transporte - sustenta a afirmacao da aula. A aula nao reproduz a equacao de diluicao do artigo, so a ideia de que a diluicao depende da area da bacia e do tamanho da fonte."
  - claim_id: DIGGEO-M25-A02-SIRGAS-EPSG-006
    claim: "O sistema geodesico oficial brasileiro e o SIRGAS 2000, adotado pela Resolucao PR no 1/2005 do IBGE de 25/02/2005, com transicao de dez anos encerrada em 25/02/2015, desde quando e o unico sistema oficial; EPSG:4674 e o SIRGAS 2000 geografico e EPSG:31983 e SIRGAS 2000 / UTM fuso 23S; misturar SAD69 com SIRGAS 2000 desloca pontos na ordem de dezenas de metros conforme a regiao."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21. Datas: IBGE, Resolucao PR no 1/2005 de 25/02/2005 (geoftp.ibge.gov.br/.../normas/rpr_01_25fev2005.pdf), Nota Tecnica de termino do periodo de transicao e Resolucao PR no 1/2015 - transicao de dez anos, SAD69 e Corrego Alegre admitidos em paralelo entre 25/02/2005 e 25/02/2015. Codigos EPSG: registro oficial (epsg.org / epsg.io) - EPSG:4674 SIRGAS 2000 geografico (substitui SIRGAS 1995/EPSG:4179), EPSG:31983 SIRGAS 2000 / UTM zone 23S, Transverse Mercator, elipsoide GRS 1980, CRS base EPSG:4674, Brasil entre 48W e 42W. MAGNITUDE DO DESLOCAMENTO: mantida como 'dezenas de metros, dependendo da regiao', com o ponteiro ao IBGE preservado - o valor e genuinamente regional (o IBGE publica parametros de transformacao e grades de distorcao, nao um numero unico), e a ordem de grandeza esta correta. NAO e um numero a fixar na aula."
  - claim_id: DIGGEO-M25-A02-OCORRENCIAS-SGB-007
    claim: "O acervo de ocorrencias minerais do Servico Geologico do Brasil (SGB-CPRM) e disponibilizado no portal GeoSGB; ocorrencia mineral nao equivale a deposito e a qualidade dos registros e heterogenea."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21: o portal GeoSGB (geosgb.sgb.gov.br, tambem em geoportal.sgb.gov.br/geosgb) e o sistema de geociencias do Servico Geologico do Brasil (SGB-CPRM) e sucede o antigo Geobank (pagina 'sobre_geosgb'); serve unidades geologicas, tipos e idades de rochas, ocorrencias minerais, afloramentos, recursos minerais e geoquimica, com download aberto e gratuito. A ressalva da aula (ocorrencia nao e deposito; qualidade heterogenea) e julgamento metodologico padrao sobre cadastros de ocorrencia, nao afirmacao sobre o portal."
-->
