# Aula 04: Bancos de dados e Big Data em geociências — modelagem, dados abertos, princípios FAIR e reprodutibilidade

**ID:** geologia-avancado-m25-a04
**Módulo:** [[25-aquisicao-digital-ia-geociencias-modulo|Módulo 25 — Aquisição de dados digitais e inteligência artificial em geociências]]
**Duração estimada:** ~25 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** projetar um banco de dados geológico relacional simples e íntegro, situar o que "Big Data" significa (e não significa) em geociências, e aplicar os princípios FAIR e as práticas de reprodutibilidade a um conjunto de dados, de modo que ele possa ser reencontrado, entendido e reutilizado, inclusive como base de treino de modelos de inteligência artificial.
**Ao final você vai conseguir:** desenhar tabelas ligadas por chaves com restrições de integridade e consultá-las com SQL; explicar o que cada letra de FAIR exige na prática; diagnosticar as falhas FAIR de um conjunto de dados real; e listar os elementos mínimos de um estudo computacional reprodutível.
**Pré-requisito:** [[25-aquisicao-digital-ia-geociencias-aula-02-tipos-organizacao-dados-geologicos|Aula 02]] (identificador de amostra, formato longo, censura e datum) e a Aula 03 (interpretações também são dados, com confiança e fonte).

## Conteúdo

### A planilha que ninguém acha

Um cenário comum: a planilha `dados_final_v3_OK.xlsx` de um projeto encerrado há dois anos. Ninguém sabe quais amostras foram descartadas, em que unidade estão as colunas, o que significa a coluna `X2`, nem se a versão `v3` é a mais recente. O dado existe e não pode ser usado. Esta aula trata do que separa um arquivo de um **acervo**: a modelagem, a documentação e a publicação. Ela cobre, ao mesmo tempo, a parte final do objetivo `oa02` (base consistente) e a base do `oa04` (qualquer avaliação de IA depende de dados que possam ser reencontrados e auditados).

### Big Data em geociências: o que a expressão quer dizer

"Big Data" é definido classicamente por características que começam com V: **volume** (muito dado), **velocidade** (chegada contínua) e **variedade** (formatos, escalas e fontes heterogêneas); acrescenta-se, muitas vezes, a **veracidade** (qualidade e incerteza). Nas geociências o volume é real em alguns domínios (imagens de satélite de arquivos como Sentinel e Landsat, sísmica de reflexão, levantamentos aerogeofísicos nacionais, sensores contínuos), mas o que dói no dia a dia do geólogo é quase sempre a **variedade e a veracidade**: bases de fontes e décadas diferentes, com sistemas de coordenadas, vocabulários e qualidade diferentes, e rótulos incompletos. Bergen et al. (2019) e Reichstein et al. (2019) discutem, para as geociências da Terra sólida e para o sistema Terra, como o aprendizado de máquina se beneficia desses dados e por que precisa de dados **bem descritos** e de compreensão dos processos, não só de volume. Não é preciso ter "big" para sofrer dos mesmos problemas: uma base de 5.000 amostras mal documentada tem os problemas de veracidade de uma de 5 milhões.

### Modelagem relacional: entidades, chaves e integridade

Um **banco de dados relacional** organiza os dados em **tabelas** (entidades), com linhas (registros) e colunas (atributos), ligadas por **chaves**: uma **chave primária** identifica de forma única cada linha de uma tabela (o `id_amostra`), e uma **chave estrangeira** numa outra tabela aponta para ela, indicando a que amostra pertence uma análise. O projeto do banco tem três etapas: o modelo **conceitual** (quais entidades e relações existem: uma amostra tem muitas análises e no máximo uma idade por método), o **lógico** (tabelas, chaves, tipos) e o **físico** (o gerenciador que implementa). As regras de **normalização** mandam não repetir o mesmo fato em vários lugares: a coordenada da amostra fica na tabela de amostras, e não copiada em cada análise. Se ela mudar (correção de datum), muda-se um lugar.

A grande vantagem prática é a **integridade referencial** e as **restrições**: o próprio banco recusa um registro que viola uma regra, sem depender da disciplina de quem digita. É a versão institucional das listas de domínio da Aula 01. Para uso individual ou de pequena equipe, o SQLite (e o GeoPackage, que é um SQLite com componente espacial padronizado) basta; para vários usuários simultâneos e análises espaciais pesadas, é usual um servidor como o PostgreSQL com a extensão espacial PostGIS. A escolha é operacional; a modelagem é a mesma.

### Padrões de interoperabilidade

Modelar bem dentro do projeto não resolve a troca entre projetos e instituições. Para isso existem **padrões de intercâmbio** e **vocabulários controlados**, e a ideia central deles é uma só: que "granito" tenha uma **definição publicada e um identificador estável**, e não apenas uma etiqueta que cada projeto escreve à sua maneira. Os dois padrões da área são o **GeoSciML**, para modelagem e troca de dados de mapas geológicos, e o **EarthResourceML**, para recursos minerais.

Os dois saíram da mesma comissão da comunidade de serviços geológicos — a *Commission for the Management and Application of Geoscience Information* (CGI), da IUGS — mas têm **estatutos diferentes**, e a diferença importa na hora de citar um deles. O GeoSciML foi **adotado como padrão do Open Geospatial Consortium** na versão 4.1, em 2017 (documento OGC 16-008r1); o EarthResourceML segue sendo um **padrão da própria CGI** (versão 2.0, de 2013; a variante simplificada ERML-Lite chegou à 2.0 em 2018), assentado sobre padrões OGC e ISO — serviço de feições (WFS) e linguagem GML — sem ser ele mesmo um padrão OGC. Ambos são usados em iniciativas como a OneGeology, e a diretiva europeia INSPIRE **baseou neles** o modelo de dados das suas especificações de Geologia e de Recursos Minerais — e aqui vale a mesma cautela: o que é vinculante na União Europeia são as **especificações do INSPIRE**, não os padrões da CGI em si, e parte dos esquemas derivados, como a extensão de recursos minerais, fica declaradamente fora das regras de implementação. A lição de método, mais durável que qualquer número de versão: **antes de citar um padrão, confira de quem ele é e o que obriga.** (As versões vigentes mudam; consulte os sites do OGC e da CGI.)

### Dados abertos: onde buscar e como citar

Há hoje grande quantidade de dados geológicos abertos, e o geólogo moderno começa por eles. Alguns exemplos: no Brasil, o **GeoSGB** (Serviço Geológico do Brasil), com mapas, ocorrências, geoquímica e aerogeofísica; internacionalmente, o USGS, o Geoscience Australia, o repositório de geoquímica EarthChem (que reúne PetDB e outras bases) e o GEOROC (rochas e minerais ígneos e metamórficos, curado desde 2021 pelo projeto DIGIS na Universidade de Göttingen), o Macrostrat (unidades estratigráficas) e o Paleobiology Database. Para depositar os **seus** dados, existem repositórios de propósito geral, como o Zenodo, que dão a cada depósito um **DOI** (identificador persistente que permite citar). Regras de uso: leia a **licença** (a licença Creative Commons CC BY 4.0, por exemplo, exige atribuição; uma sem licença é, por padrão, de uso restrito) e **cite** a fonte com versão e data de acesso.

### Os princípios FAIR

Wilkinson et al. (2016) propuseram **quatro princípios**, desdobrados em quinze diretrizes, para que os dados possam ser usados **por pessoas e por máquinas**:

- **Findable (encontrável).** Os dados e seus metadados têm um **identificador único e persistente** (como um DOI), são descritos com **metadados ricos** que citam esse identificador, e estão **registrados num recurso pesquisável**.
- **Accessible (acessível).** Recuperáveis pelo identificador, por um protocolo padronizado, aberto e universal; o protocolo permite autenticação e autorização **quando necessário**; e os **metadados permanecem acessíveis mesmo que os dados deixem de estar**.
- **Interoperable (interoperável).** Os dados usam uma linguagem formal, compartilhada e amplamente aplicável, vocabulários que também sigam os princípios FAIR e referências qualificadas a outros dados (é aqui que entram GeoSciML, códigos EPSG e vocabulários de litologia).
- **Reusable (reutilizável).** Os dados têm descrição rica e relevante, **licença de uso clara**, **proveniência detalhada** (de onde vieram, como foram processados) e seguem os padrões da comunidade.

Um ponto que muita gente perde: **FAIR não é sinônimo de aberto.** Um dado sigiloso (uma sondagem de uma empresa em fase de exploração) pode e deve ser FAIR dentro da organização: bem descrito, identificável e reutilizável, com acesso controlado. O complemento ético mais citado são os princípios **CARE** (Carroll et al., 2020), sobre governança de dados de povos indígenas, relevantes quando a base contém dados de territórios ou de conhecimento tradicional.

### Reprodutibilidade: o dado, o código e o ambiente

Um resultado é **reprodutível** quando outra pessoa, com os seus dados e o seu código, obtém os mesmos números. Três camadas precisam estar registradas:

1. **Dados.** Uma versão **imutável** do conjunto usado (com uma soma de verificação, o *hash*, ou um DOI de versão) e a **linhagem**: o dado bruto **nunca é sobrescrito**; cada etapa de limpeza gera um arquivo novo, e o código que a fez fica guardado.
2. **Código.** Sob controle de versão (Git), com o histórico do que foi feito. Aleatoriedade fixada: a `random_state` que o [[24-machine-learning-geociencias-modulo|Módulo 24]] usou em todos os modelos serve exatamente a isso.
3. **Ambiente.** As versões das bibliotecas (o Módulo 24 declarou Python 3.13.2 e scikit-learn 1.9.1 exatamente por isso) num arquivo de dependências.

Um resultado que só o autor consegue reproduzir, na sua máquina, não é um resultado científico: é um relato. Em IA, a exigência é maior: o **conjunto de treino** e os **rótulos** também são artefatos versionados, porque trocar o mapa geológico usado como rótulo (a Aula 05) muda o modelo tanto quanto trocar o algoritmo.

## Exemplo trabalhado 1: um banco pequeno que recusa registros inválidos

**Situação.** Você projeta três tabelas (`amostra`, `analise`, `idade`), com chaves e restrições, e consulta o ouro de amostras não censuradas acima de 10 ppb, trazendo a idade quando existir.

```python
import sqlite3
con = sqlite3.connect(":memory:")
con.executescript("""
PRAGMA foreign_keys = ON;
CREATE TABLE amostra (
  id_amostra TEXT PRIMARY KEY,
  tipo TEXT NOT NULL CHECK (tipo IN ('rocha','sedimento_corrente','solo')),
  leste_m REAL NOT NULL, norte_m REAL NOT NULL,
  epsg INTEGER NOT NULL, coletor TEXT, data_coleta TEXT);
CREATE TABLE analise (
  id_analise INTEGER PRIMARY KEY,
  id_amostra TEXT NOT NULL REFERENCES amostra(id_amostra),
  elemento TEXT NOT NULL, valor REAL NOT NULL, unidade TEXT NOT NULL,
  censurado INTEGER NOT NULL DEFAULT 0, metodo TEXT, laboratorio TEXT);
CREATE TABLE idade (
  id_idade INTEGER PRIMARY KEY,
  id_amostra TEXT NOT NULL REFERENCES amostra(id_amostra),
  metodo TEXT NOT NULL, mineral TEXT, idade_ma REAL NOT NULL, incert_2s REAL NOT NULL);
""")
con.executemany("INSERT INTO amostra VALUES (?,?,?,?,?,?,?)", [
 ("GA-001","rocha",652310,7801520,31983,"FR","2026-03-02"),
 ("GA-002","rocha",652980,7801875,31983,"FR","2026-03-02"),
 ("GA-003","sedimento_corrente",653400,7802300,31983,"FR","2026-03-03")])
con.executemany("INSERT INTO analise(id_amostra,elemento,valor,unidade,censurado,metodo,laboratorio) VALUES (?,?,?,?,?,?,?)", [
 ("GA-001","Au",5,"ppb",1,"FA-AAS","Lab X"), ("GA-002","Au",12,"ppb",0,"FA-AAS","Lab X"),
 ("GA-003","Au",30,"ppb",0,"FA-AAS","Lab X"), ("GA-002","Cu",95,"ppm",0,"ICP-MS","Lab X")])
con.execute("INSERT INTO idade(id_amostra,metodo,mineral,idade_ma,incert_2s) VALUES ('GA-001','U-Pb','zircao',2712,8)")

q = """SELECT a.id_amostra, a.tipo, an.valor, an.censurado, i.idade_ma
FROM amostra a
JOIN analise an ON an.id_amostra = a.id_amostra AND an.elemento = 'Au'
LEFT JOIN idade i ON i.id_amostra = a.id_amostra
WHERE an.censurado = 0 AND an.valor >= 10
ORDER BY an.valor DESC"""
for r in con.execute(q): print(r)

for sql in ["INSERT INTO analise(id_amostra,elemento,valor,unidade) VALUES ('GA-999','Au',1,'ppb')",
            "INSERT INTO amostra VALUES ('GA-010','agua',1,1,31983,'FR','2026-03-04')"]:
    try: con.execute(sql)
    except sqlite3.IntegrityError as e: print("rejeitado:", e)
```

**Saída obtida (Python 3, módulo `sqlite3`):** a consulta devolve `('GA-003', 'sedimento_corrente', 30.0, 0, None)` e `('GA-002', 'rocha', 12.0, 0, None)`: duas amostras, ordenadas por teor, com a idade `None` (`LEFT JOIN`, nenhuma das duas tem idade). GA-001 ficou de fora por ser censurada (o `5` é o limite de detecção, não uma medida). As duas inserções inválidas foram **rejeitadas pelo próprio banco**: a primeira por violar a chave estrangeira (`FOREIGN KEY constraint failed`: não existe a amostra GA-999) e a segunda por violar a lista de domínio (`CHECK constraint failed: tipo IN ('rocha','sedimento_corrente','solo')`: "agua" não é um tipo permitido).

**O que o exemplo ensina.** A regra de "só existe análise de amostra que existe" e a lista de valores permitidos ficam **no banco**, e não na memória de quem digita. Quando um modelo de IA (Aula 05) recebe uma tabela extraída daqui, herda essas garantias.

## Exemplo trabalhado 2: diagnóstico FAIR de um conjunto real de projeto

**Situação.** Um projeto de mapeamento entrega `dados_final_v3_OK.xlsx` numa pasta compartilhada da empresa, com uma aba por tipo de análise, colunas de nome curto (`Au`, `X2`), coordenadas sem indicação de datum e nenhum arquivo de descrição. Avalie contra FAIR.

**Diagnóstico.**

- **Findable: falha.** Não há identificador persistente (o caminho da pasta muda), não há metadados descritivos, o arquivo não está registrado em nenhum catálogo.
- **Accessible: parcial.** Está acessível a quem tem acesso à pasta, e a autenticação é aceitável para dado sigiloso; mas se o servidor sair do ar, tudo some, inclusive a descrição (que já não existia).
- **Interoperable: falha.** Litologia em texto livre, sem vocabulário; coordenadas sem EPSG; unidades sem coluna própria; formato de planilha em vez de um formato aberto e estruturado (CSV documentado ou GeoPackage).
- **Reusable: falha.** Sem licença ou condição de uso, sem proveniência (quem coletou, qual laboratório, que método, o que foi descartado), sem versão definida.

**Plano de reparo em ordem de custo-benefício.** (1) Escrever um **dicionário de dados** (cada coluna: significado, unidade, tipo, valores permitidos): é o item mais barato e o de maior efeito sobre a reutilização. (2) Acrescentar EPSG e unidade por linha (Aula 02). (3) Migrar para um formato aberto e estruturado, com tabelas ligadas por chave. (4) Registrar licença e condições de uso, mesmo que restritas à organização. (5) Se o dado puder ser aberto, depositar num repositório com DOI; se não, atribuir identificador interno persistente e catalogar. Note que a maior parte do ganho vem dos passos 1 a 2, que **não exigem infraestrutura nenhuma**, apenas disciplina; o resto é escala.

## Recap relâmpago

- "Big Data" tem volume, velocidade e variedade; nas geociências o problema cotidiano é sobretudo **variedade e veracidade**, e não o volume.
- Banco relacional: tabelas, **chave primária e estrangeira**, **restrições** (`CHECK`, `NOT NULL`) e **normalização**: o banco impede o registro inválido, em vez de depender do digitador.
- **Padrões e vocabulários** (GeoSciML, EarthResourceML, EPSG) tornam "granito" e "SIRGAS 2000" identificáveis entre projetos.
- **FAIR** = Findable, Accessible, Interoperable, Reusable; **não é sinônimo de aberto**, e o metadado deve sobreviver ao dado; o dicionário de dados é o passo de maior retorno.
- **Reprodutibilidade** = dados versionados e imutáveis + código versionado com aleatoriedade fixada + ambiente declarado; o **dado bruto nunca se sobrescreve**.
- Em IA, o **conjunto de treino e os rótulos são artefatos versionados**: trocar o mapa usado como rótulo troca o modelo.

## Próxima aula

[[25-aquisicao-digital-ia-geociencias-aula-05-ia-aplicada-mapeamento-prospectividade-metalogenese|Aula 05 — Inteligência artificial aplicada]]: fecha o módulo aplicando o [[24-machine-learning-geociencias-modulo|Módulo 24]] aos dados aqui organizados: mapeamento geológico automatizado, prospectividade mineral e o papel dos modelos metalogenéticos, com atenção especial à qualidade dos rótulos e à validação espacial.

## Fontes

- Wilkinson, M. D. et al. (2016), "The FAIR Guiding Principles for scientific data management and stewardship", *Scientific Data*, 3, 160018, DOI 10.1038/sdata.2016.18.
- Carroll, S. R. et al. (2020), "The CARE Principles for Indigenous Data Governance", *Data Science Journal*, 19, 43, DOI 10.5334/dsj-2020-043.
- Bergen, K. J., Johnson, P. A., de Hoop, M. V. & Beroza, G. C. (2019), "Machine learning for data-driven discovery in solid Earth geoscience", *Science*, 363(6433), eaau0323, DOI 10.1126/science.aau0323.
- Reichstein, M. et al. (2019), "Deep learning and process understanding for data-driven Earth system science", *Nature*, 566, 195-204, DOI 10.1038/s41586-019-0912-1.
- OGC 16-008r1, *GeoSciML v4.1* (Implementation Standard, 2017), docs.ogc.org/is/16-008/16-008r1.html; CGI/IUGS, página do projeto *EarthResourceML* (cgi-iugs.org/project/earthresourceml), para o estatuto e a versão de cada padrão.
- Documentação oficial do SQLite (sqlite.org), do PostGIS (postgis.net) e do padrão GeoPackage (OGC); portais GeoSGB, EarthChem, GEOROC, Macrostrat, PBDB e Zenodo.

<!--
nivel: avancado
palavras_corpo: 2122
mapa_objetivo_secao:
  geologia-avancado-m25-oa02: "Modelagem relacional" + "Padrões de interoperabilidade" + "Exemplo trabalhado 1"
  geologia-avancado-m25-oa04: "Big Data em geociências" + "Os princípios FAIR" + "Reprodutibilidade" + "Exemplo trabalhado 2"

alegacoes_auditaveis:
  - claim_id: DIGGEO-M25-A04-SQL-INTEGRIDADE-001
    claim: "No codigo apresentado (SQLite), a consulta devolve (GA-003, sedimento_corrente, 30.0, 0, None) e (GA-002, rocha, 12.0, 0, None); a insercao de analise para GA-999 falha com 'FOREIGN KEY constraint failed' e a insercao de tipo 'agua' falha com \"CHECK constraint failed: tipo IN ('rocha','sedimento_corrente','solo')\"."
    risk: calculo
    source: "Execucao direta do codigo (Python 3, sqlite3), 2026-09-21."
  - claim_id: DIGGEO-M25-A04-FAIR-PRINCIPIOS-002
    claim: "Os principios FAIR (Findable, Accessible, Interoperable, Reusable), propostos por Wilkinson et al. (2016) em quatro principios desdobrados em quinze diretrizes, exigem identificador persistente, metadados ricos, protocolo aberto, vocabularios compartilhados, licenca clara e proveniencia; metadados devem permanecer acessiveis mesmo sem os dados; FAIR nao e sinonimo de aberto."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21: Wilkinson, M. D. et al. (2016), Sci. Data 3, 160018, DOI 10.1038/sdata.2016.18 (referencia confere). A CONTAGEM DE QUINZE ESTA CORRETA - conferida item a item contra a lista canonica (GO FAIR Foundation, gofair.foundation/fair-principles): F1, F2, F3, F4 (4) + A1, A1.1, A1.2, A2 (4) + I1, I2, I3 (3) + R1, R1.1, R1.2, R1.3 (4) = 15 subprincipios sob quatro principios. A frase da aula sobre metadados sobreviverem ao dado e literalmente A2: 'metadata are accessible, even when the data are no longer available'. A autenticacao 'quando necessario' e literalmente A1.2. A tese de que FAIR nao e sinonimo de aberto e sustentada pelo proprio A1.2 e e consenso na comunidade FAIR."
  - claim_id: DIGGEO-M25-A04-CARE-003
    claim: "Os principios CARE para governanca de dados indigenas (Carroll et al., 2020) complementam FAIR no que se refere a dados de povos indigenas."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21: Carroll, S. R. et al. (2020), 'The CARE Principles for Indigenous Data Governance', Data Science Journal 19: 43, DOI 10.5334/dsj-2020-043 (confere). CARE = Collective Benefit, Authority to Control, Responsibility, Ethics; desenvolvidos pelo International Indigenous Data Sovereignty Interest Group, e o proprio artigo se posiciona como orientado a pessoas e a proposito, COMPLEMENTAR a abordagem centrada no dado dos principios FAIR - exatamente o que a aula afirma."
  - claim_id: DIGGEO-M25-A04-BIGDATA-VS-004
    claim: "Big Data e caracterizado por volume, velocidade e variedade (e frequentemente veracidade); em geociencias o problema cotidiano e sobretudo variedade e veracidade."
    risk: fato
    source: "REFERENCIAS VERIFICADAS na auditoria de 2026-09-21: Bergen, K. J., Johnson, P. A., de Hoop, M. V. & Beroza, G. C. (2019), 'Machine learning for data-driven discovery in solid Earth geoscience', Science 363(6433), eaau0323, DOI 10.1126/science.aau0323 (confere); Reichstein, M., Camps-Valls, G., Stevens, B. et al. (2019), 'Deep learning and process understanding for data-driven Earth system science', Nature 566, 195-204, DOI 10.1038/s41586-019-0912-1 (confere). A tese que a aula extrai deles - que o aprendizado de maquina precisa de dados bem descritos e de compreensao dos processos, nao so de volume - e o argumento central de Reichstein et al. A definicao dos 'Vs' segue sem atribuicao de autoria primaria, o que e correto: ela e folclore da industria (usualmente remetida a um relatorio da Gartner de 2001, de Doug Laney) e nao tem fonte normativa; a aula nao atribui a ninguem. A segunda parte (variedade e veracidade como problema cotidiano em geociencias) permanece julgamento pedagogico do autor, declarado como tal, nao afirmacao dos artigos."
  - claim_id: DIGGEO-M25-A04-GEOSCIML-005
    claim: "GeoSciML e EarthResourceML saem ambos da CGI (Commission for the Management and Application of Geoscience Information) da IUGS, mas tem estatutos DIFERENTES: GeoSciML foi adotado como padrao OGC na versao 4.1, em 2017 (OGC 16-008r1), enquanto EarthResourceML permanece padrao da CGI (v2.0 de 2013; ERML-Lite v2.0 de 2018), assentado em padroes OGC/ISO (WFS/ISO 19142, GML/ISO 19136) sem ser padrao OGC. Os dois sao usados na OneGeology e foram adotados pela diretiva europeia INSPIRE."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21: OGC 16-008r1, 'GeoSciML v4.1', publicado como Implementation Standard (docs.ogc.org/is/16-008/16-008r1.html), e pagina de padrao do OGC (ogc.org/standards/geosciml); trajetoria v4 (2015) -> v4.1 OGC (2017) descrita pela CGI/IUGS (cgi-iugs.org) e pelo BGS ('GeoSciML data standard becomes official'). EarthResourceML: pagina oficial do projeto na CGI (cgi-iugs.org/project/earthresourceml) - mantido pelo EarthResourceML Working Group, declarado padrao CGI/IUGS e nao OGC, 'underpinned by established OGC and ISO standards, including WFS (ISO 19142), GML (ISO 19136) and SWE Common', v2.0 publicada em 2013 e ERML-Lite v2.0 em 2018, adotado pela INSPIRE como padrao oficial de troca de informacao de recursos minerais. ACHADO LARANJA 3 DA AUDITORIA de 2026-09-21: a redacao original punha o GeoSciML 'no ambito do OGC' e tratava os dois como 'alinhados ao OGC', achatando a distincao - o GeoSciML E padrao OGC, o EarthResourceML NAO."
  - claim_id: DIGGEO-M25-A04-REPOSITORIOS-006
    claim: "GeoSGB (Servico Geologico do Brasil), USGS, Geoscience Australia, EarthChem (com PetDB), GEOROC, Macrostrat, Paleobiology Database e Zenodo (DOI) sao fontes ou repositorios de dados geologicos abertos; a licenca CC BY 4.0 exige atribuicao."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2), item azul B16: portais dos provedores e registro re3data conferidos. O EarthChem de fato agrega o PetDB e outras bases, com busca combinada sobre seis bases geoquimicas. CC BY 4.0 exige atribuicao (Creative Commons). UMA CORRECAO DE ESCOPO no GEOROC - ver ACHADO AMARELO 13 (claim -GEOROC-ESCOPO-008)."
  - claim_id: DIGGEO-M25-A04-INSPIRE-OBRIGATORIO-007
    claim: "A diretiva europeia INSPIRE baseou em GeoSciML e EarthResourceML o modelo de dados das suas especificacoes de Geologia e de Recursos Minerais; o que e vinculante na Uniao Europeia sao as ESPECIFICACOES DO INSPIRE, nao os padroes da CGI em si, e parte dos esquemas derivados (como a MineralResourcesExtension) fica fora das regras de implementacao."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2): INSPIRE, D2.8.III.21 'Data Specification on Mineral Resources - Technical Guidelines' (inspire-mif.github.io/technical-guidelines/data/mr/dataspecification_mr.html) - 'The core data model for Mineral Resources is based on the GeoSciML and EarthResourceML developed by the international geosciences community', e a ressalva explicita de que esquemas adicionais 'are not included in the Implementing Rules'; especificacao de Geologia; BGS, pagina EU INSPIRE Directive. ACHADO LARANJA 9 DA AUDITORIA de 2026-09-21: a redacao original dizia que o INSPIRE 'os adotou como padroes obrigatorios de troca', achatando o estatuto - o MESMO erro do achado laranja 3, uma frase adiante. A PASSAGEM 1 verificou este ponto contra a PAGINA DO PROPRIO PADRAO NA CGI, isto e, contra a fonte interessada e nao a normativa. Corrigido."
  - claim_id: DIGGEO-M25-A04-GEOROC-ESCOPO-008
    claim: "O GEOROC reune analises de rochas e minerais IGNEOS E METAMORFICOS e, desde 2021, deixou o Max Planck de Mainz e passou a ser curado pelo projeto DIGIS na Universidade de Gottingen (georoc.eu, GEOROC 2.0), com pipeline de dados para o EarthChem."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2): georoc.eu; DIGIS / Geowissenschaftliches Zentrum e SUB, Universidade de Gottingen; re3data.org/repository/r3d100011206; documentacao da API GEOROC 2.0. ACHADO AMARELO 13 DA AUDITORIA de 2026-09-21: a aula rotulava o GEOROC como '(rochas igneas)', escopo incompleto, numa secao que ensina a citar fonte com versao e data de acesso. Corrigido com o escopo completo e a curadoria atual nomeada."
-->
