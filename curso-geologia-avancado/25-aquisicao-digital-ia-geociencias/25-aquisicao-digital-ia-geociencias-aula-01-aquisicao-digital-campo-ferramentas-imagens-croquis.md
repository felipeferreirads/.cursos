# Aula 01: Aquisição digital de dados em campo — ferramentas, sensores do celular, imagens e croquis

**ID:** geologia-avancado-m25-a01
**Módulo:** [[25-aquisicao-digital-ia-geociencias-modulo|Módulo 25 — Aquisição de dados digitais e inteligência artificial em geociências]]
**Duração estimada:** ~27 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** entender como um aplicativo de mapeamento em celular ou tablet mede e registra dados geológicos de campo, operar o fluxo escritório–campo–banco e avaliar, ponto a ponto, o que a caderneta digital ganha e o que ela perde frente à caderneta de papel.
**Ao final você vai conseguir:** explicar como o celular obtém direção e mergulho de um plano (acelerômetro, magnetômetro e declinação magnética); corrigir uma leitura magnética para o norte verdadeiro; medir a qualidade de um conjunto de leituras repetidas de uma mesma foliação; e listar as vantagens e as limitações da aquisição digital, incluindo o risco de o erro do observador ganhar aparência de precisão.
**Pré-requisito:** [[24-machine-learning-geociencias-modulo|Módulo 24]] (a noção de que a qualidade do dado limita o que qualquer modelo aprende) e [[14-sensoriamento-remoto-modulo|Módulo 14]] (imagens georreferenciadas e sistemas de coordenadas). Assume-se que você já mediu direção e mergulho com bússola de geólogo e conhece a notação de direção de mergulho (dip direction) e mergulho (dip).

## Conteúdo

### A pergunta que motiva: quantas vezes o mesmo dado é digitado?

Numa campanha de mapeamento tradicional, uma medida de foliação passa por quatro mãos: você lê a bússola, escreve na caderneta, à noite transcreve para uma planilha e, semanas depois, alguém plota o símbolo no mapa. Cada etapa é uma chance de troca de dígitos, de esquecer a declinação, de perder a coordenada. A aquisição digital nasceu para encurtar essa cadeia: o dado é registrado **uma vez**, no momento da observação, já com coordenada, hora, autor e campos padronizados, e chega ao banco por sincronização, sem retranscrição. Esta aula ensina o que há por trás desse fluxo, e onde ele engana.

### O fluxo escritório, campo, banco

Uma campanha digital tem três fases, e a parte mais importante acontece **antes** de ir a campo:

1. **Preparação no escritório.** Num GIS desktop de projeto (ArcGIS Pro, ou o QGIS, que é de código aberto) você monta o projeto: mapa-base, imagens, geologia prévia e, sobretudo, o **formulário de coleta**. O formulário define quais campos existem, quais são obrigatórios e quais respostas são permitidas (listas de domínio: litologia só pode ser um código da legenda, e não texto livre).
2. **Coleta em campo, em geral offline.** O aplicativo funciona sem sinal de rede: usa o mapa-base baixado, lê o GNSS (posicionamento por satélite, como o GPS) e os sensores do aparelho, e grava tudo em arquivo local.
3. **Sincronização e consolidação.** No fim do dia, os registros vão para o projeto central (arquivo, servidor ou nuvem) e são conferidos no GIS.

As ferramentas mais citadas hoje cobrem partes diferentes desse fluxo. Entre as de uso geológico: o **FieldMove**, aplicativo de mapeamento estrutural e geológico, e o **FieldMove Clino**, sua versão simples de clinômetro/bússola para medir e registrar orientações. Entre as de uso geral de GIS: o **QField**, aplicativo de campo do QGIS, e o **ArcGIS Field Maps**, do ecossistema Esri. A escolha depende menos de "qual é o melhor" do que de **qual se encaixa no seu banco de dados**: um aplicativo que exporta para um formato aberto e bem definido (como o GeoPackage, padrão do Open Geospatial Consortium baseado em SQLite) poupa retrabalho na Aula 04.

> [!info] Nota de nomenclatura
> O plano deste curso lista as ferramentas como "FieldClino" e "GIS-Pro". O nome comercial correto da primeira é **FieldMove Clino**, hoje publicada pela Petroleum Experts, que em 2017 incorporou a Midland Valley Exploration, desenvolvedora original do FieldMove e do FieldMove Clino. "GIS-Pro" não é nome de produto: está tratado aqui como GIS desktop de projeto, genericamente.

### Como o celular mede uma orientação

O geólogo lê a bússola de Brunton apoiando a borda sobre o plano; o celular apoia-se **de face ou de dorso** sobre a superfície, e mede com dois sensores:

- o **acelerômetro** sente a aceleração da gravidade; a partir dela o aparelho sabe qual é a vertical, e portanto o **mergulho** do plano em que está apoiado;
- o **magnetômetro** mede o campo magnético local; a partir dele o aparelho encontra o **norte magnético** e portanto a **direção** do mergulho.

Esses dois vetores, combinados por algoritmos de fusão de sensores, dão a orientação do aparelho no espaço, e o aplicativo a converte em direção de mergulho e mergulho do plano. Duas consequências práticas, e nenhuma é detalhe:

- **O magnetômetro lê o norte magnético, não o verdadeiro.** A diferença é a **declinação magnética**, que varia com o lugar e com o tempo (o campo magnético da Terra muda de ano a ano). O aplicativo pode corrigi-la automaticamente com um modelo global do campo geomagnético (o *World Magnetic Model*, publicado pela NOAA e pelo British Geological Survey em ciclos de cinco anos; a época vigente é o **WMM2025**, com taxa de variação estimada para 2025,0–2030,0 e validade até o fim de 2029); mas você precisa **saber se a correção está ligada** e em qual convenção o dado é gravado, senão o arquivo mistura medidas magnéticas e verdadeiras sem que se perceba.
- **O magnetômetro é sensível a qualquer perturbação magnética.** Rochas ricas em magnetita (formações ferríferas bandadas, gabros, serpentinitos), objetos de aço (martelo, capa magnética do celular, carro por perto) e a calibração ruim deslocam a direção lida. Isto vale igualmente para a bússola de Brunton, mas na bússola você **vê** a agulha oscilar; no celular o número aparece limpo, sem sinal visível da perturbação. Em terrenos como o de formações ferríferas, o procedimento prudente é conferir a direção com um alinhamento visado no terreno.

Os dois estudos de comparação mais citados, ambos no *Journal of Structural Geology*, **não chegam à mesma conclusão**, e a divergência é o dado mais útil aqui. Allmendinger, Siron & Scott (2017), testando dispositivos iOS, concluem que a acurácia é suficiente para as tarefas de coleta estrutural, e apontam o ganho real do digital: a rapidez da medida viabiliza **leituras redundantes** e, com elas, uma estimativa quantitativa de incerteza que a bússola de mão, mais lenta, raramente permite. Novakova & Pavlis (2017), testando dois aparelhos Android (um celular e um tablet), chegam ao oposto: em campo, contra uma bússola Freiberg, observaram discrepâncias de **até 80°**, concentradas no **azimute** (a direção de mergulho saiu menos acurada que o mergulho), e atribuíram o problema à **instabilidade do magnetômetro** — ao sensor, e não ao procedimento. Os próprios autores ressalvam que o resultado pode depender do aparelho e da plataforma, e recomendam **aferir o conjunto aparelho-aplicativo contra uma bússola analógica antes da campanha**, monitorando as leituras ao longo do dia. A lição que as duas fontes sustentam é esta: a acurácia de um celular como bússola geológica é propriedade **do aparelho e do aplicativo**, não da tecnologia — afere-se, não se presume.

### Posição, imagens e croquis

**Posição.** O GNSS de um celular comum dá tipicamente erros de alguns metros em céu aberto, e mais em vale encaixado, mata densa ou junto a paredões. Para um mapa em escala 1:50.000, alguns metros são desprezíveis; para amarrar um furo de sondagem ou uma trincheira, não. Bons aplicativos gravam a **acurácia estimada** de cada posição num campo próprio — guarde-o, porque ele é o único jeito de saber depois quais pontos merecem confiança. Receptores GNSS externos, ligados ao celular por Bluetooth, reduzem o erro para centímetros a decímetros quando há correção diferencial.

**Imagens.** A foto de afloramento é dado geológico, não decoração, e por isso precisa de três coisas: **escala** (martelo, caneta, escala impressa, sempre dizendo qual objeto e qual tamanho), **orientação** (anotar para onde a câmera aponta, ou fotografar com a face do afloramento perpendicular à visada e registrar o azimute) e **vínculo com o ponto** (o aplicativo associa a foto ao registro; o nome do arquivo e os metadados gravados no próprio arquivo de imagem, chamados EXIF, guardam hora e às vezes posição). Uma foto solta, sem ponto nem escala, vira ilustração e não dado.

**Croquis digitais.** Desenha-se sobre a foto, sobre o mapa ou em tela em branco, com o dedo ou uma caneta. A vantagem sobre o papel é que o croqui **herda coordenada e vínculo** com o ponto e pode ser vetorizado; a limitação é a velocidade e a precisão do traço a céu aberto, com reflexo de sol na tela. Regra prática: para relações geométricas complexas (dobra parasítica, relação de corte entre gerações de veio), o croqui rápido no papel, fotografado e anexado ao registro, ainda vence o traço no vidro. Não é retrocesso: é combinar suporte e tarefa.

### Vantagens e limitações, lado a lado

| Aspecto | Caderneta digital | Caderneta analógica |
|---|---|---|
| Retranscrição | Nenhuma: registro único, sincronizado | Transcrição noturna, chance de erro |
| Campos padronizados | Listas de domínio, campos obrigatórios | Livres; padrão depende da disciplina do autor |
| Coordenada e hora | Automáticas, com acurácia gravada | Manuais ou de um GPS separado |
| Orientação | Sensor sem visualização de perturbação magnética | Agulha visível oscila sob perturbação |
| Autonomia | Bateria, calor, tela ilegível ao sol | Sem dependência de energia |
| Criação de ideias no campo | Mais lenta para croquis livres e anotações interpretativas | Rápida e flexível |
| Rastreabilidade | Metadados (autor, hora, versão do formulário) | Depende da caligrafia e da letra do autor |

O ponto de dificuldade do módulo está nesta tabela, entre as linhas: a aquisição digital **não elimina o erro do observador; apenas o propaga mais rápido e com aparência de precisão**. Um mergulho de 42 graus lido no celular, com uma casa decimal, parece mais confiável que um "42" escrito à mão, e não é: a casa decimal vem do sensor, não da qualidade da medida. Um mergulho errado, uma declinação ligada ou desligada por engano, uma foliação medida sobre um bloco solto (rolado) entram no banco com a mesma cara de qualquer outro registro. A defesa tem três camadas: campos de qualidade no formulário (**tipo de medida**: afloramento *in situ* ou bloco; **confiança**: alta, média ou baixa), redundância (repetir a medida) e conferência no fim do dia com os dados plotados.

## Exemplo trabalhado 1: da leitura magnética ao norte verdadeiro

**Situação.** Numa campanha em Minas Gerais você lê, com o aplicativo em modo magnético, uma foliação com direção de mergulho de **128°** e mergulho de 35°. A declinação magnética do local, obtida de um modelo geomagnético para a data da campanha, é de **21° oeste** (valor hipotético e aproximado, apenas para o exemplo; use o valor do modelo vigente na sua data e local). Qual a direção de mergulho verdadeira?

**Resolução.** Adotamos a convenção em que a declinação leste é positiva e a oeste é negativa, e vale

$$\text{azimute verdadeiro} = \text{azimute magnético} + \text{declinação}$$

Como a declinação é oeste, é −21°:

$$128° + (-21°) = 107°$$

A direção de mergulho verdadeira é **107°** (mergulho de 35° inalterado: o mergulho depende só da vertical, e a declinação só afeta o azimute). Se o aplicativo já tivesse aplicado a correção e você a aplicasse de novo, teria 86°, um erro de 21° que nenhuma inspeção do número isolado revelaria — daí a regra de gravar, num campo do formulário, **qual convenção o registro usa**.

## Exemplo trabalhado 2: quão boa é a série de leituras?

**Situação.** Você mediu cinco vezes, em pontos vizinhos do mesmo afloramento, a mesma foliação. As leituras magnéticas (direção de mergulho, mergulho) foram: (112, 42), (118, 40), (109, 45), (115, 38), (121, 43). Com a mesma declinação de −21°, qual a orientação média e quanto as leituras se afastam dela?

**Resolução.** Não se tira a média aritmética de direções e mergulhos separadamente: orientações vivem na esfera, e a forma correta é converter cada plano no **polo** (a normal ao plano, um vetor unitário), somar os vetores e reconverter a resultante em plano. O código abaixo faz isso.

```python
import numpy as np

def pole(dd, dip):
    """Polo (normal ascendente) em coordenadas (Leste, Norte, Cima)."""
    dd, dip = np.radians(dd), np.radians(dip)
    return np.array([-np.sin(dip)*np.sin(dd), -np.sin(dip)*np.cos(dd), np.cos(dip)])

def from_pole(n):
    n = n / np.linalg.norm(n)
    if n[2] < 0: n = -n
    return np.degrees(np.arctan2(-n[0], -n[1])) % 360, np.degrees(np.arccos(n[2]))

decl = -21.0
leituras = [(112, 42), (118, 40), (109, 45), (115, 38), (121, 43)]   # magnéticas
verd = [((dd + decl) % 360, dip) for dd, dip in leituras]
P = np.array([pole(dd, dip) for dd, dip in verd])
R = P.sum(axis=0)
dd_m, dip_m = from_pole(R)
n = R / np.linalg.norm(R)
ang = [np.degrees(np.arccos(np.clip(p @ n, -1, 1))) for p in P]
print("|R|/n:", round(np.linalg.norm(R)/len(P), 4))
print("media: dd=%.1f dip=%.1f" % (dd_m, dip_m))
print("desvios (graus):", np.round(ang, 1))
```

**Saída obtida (Python, NumPy):** `|R|/n = 0,9979`; orientação média de **direção de mergulho 93,9° e mergulho 41,5°**; desvios angulares de cada leitura em relação à média de **2,0°, 2,5°, 5,3°, 3,5° e 4,3°**, isto é, desvio máximo de 5,3° e médio de 3,5°.

**Interpretação.** O comprimento normalizado da resultante, `|R|/n`, vai de 0 (vetores em todas as direções) a 1 (vetores idênticos); 0,9979 indica uma série muito coesa. Um desvio máximo de cerca de 5° é o tipo de dispersão que se atribui ao procedimento (apoio do aparelho, rugosidade do plano), não a uma variação real de estrutura. **Cuidado com o que esse resultado não diz:** a coesão mede a **precisão** (repetibilidade), e não a **exatidão**. Se houvesse um erro sistemático (declinação errada, magnetita no afloramento), as cinco leituras estariam **todas** erradas do mesmo modo e a série continuaria perfeitamente coesa. Precisão alta com exatidão desconhecida é exatamente a "aparência de precisão" que a aquisição digital favorece.

## Recap relâmpago

- A caderneta digital registra o dado **uma vez**, no ponto, com coordenada, hora e autor, e o leva ao banco por sincronização; o valor do fluxo está na **preparação do formulário** no escritório, com listas de domínio e campos obrigatórios.
- O celular obtém o **mergulho** pelo acelerômetro (gravidade) e a **direção** pelo magnetômetro (campo magnético); a leitura é **magnética** e precisa de **declinação** para virar azimute verdadeiro (verdadeiro = magnético + declinação, com leste positivo).
- O magnetômetro é perturbado por magnetita e objetos de aço, e o celular **não mostra** a perturbação como a agulha da bússola mostra; em terreno magnético, confira com visada.
- A literatura **não** garante que celular equivale a bússola: há aparelhos com acurácia suficiente (iOS, Allmendinger et al. 2017) e aparelhos com discrepâncias de até 80° por magnetômetro instável (Android, Novakova & Pavlis 2017). **Afira o seu conjunto aparelho-aplicativo contra uma bússola analógica antes da campanha.**
- Posição de celular tem erro de alguns metros; grave a **acurácia**. Foto de afloramento só é dado com **escala, orientação e vínculo ao ponto**.
- Média de orientações se calcula pelos **polos** (vetores), não por médias de ângulos; coesão mede precisão, não exatidão.
- Digital não elimina o erro do observador: ele se propaga mais rápido e com aparência de precisão. Campos de **tipo de medida** e **confiança** são a defesa.

## Próxima aula

[[25-aquisicao-digital-ia-geociencias-aula-02-tipos-organizacao-dados-geologicos|Aula 02 — Tipos e organização de dados geológicos]]: o que fazer com o dado depois que ele está no banco — litologia, geoquímica, geocronologia, sedimentos de corrente, ocorrências, aerogeofísica e isótopos, cada um com suas unidades, incertezas e armadilhas, e como juntá-los numa base consistente.

## Fontes

- Novakova, L. & Pavlis, T. L. (2017), "Assessment of the precision of smart phones and tablets for measurement of planar orientations: A case study", *Journal of Structural Geology*, 97, 93-103. (Dois aparelhos Android; discrepâncias de até 80° contra bússola Freiberg, atribuídas à instabilidade do magnetômetro.)
- Allmendinger, R. W., Siron, C. R. & Scott, C. P. (2017), "Structural data collection with mobile devices: Accuracy, redundancy, and best practices", *Journal of Structural Geology*, 102, 98-112, DOI 10.1016/j.jsg.2017.07.011. (Dispositivos iOS; acurácia suficiente para coleta estrutural, com ênfase na redundância de medidas.)
- *World Magnetic Model 2025* (NOAA National Centers for Environmental Information e British Geological Survey), calculadora de declinação: ncei.noaa.gov/products/world-magnetic-model.
- Documentação oficial do QField (qfield.org), do FieldMove Clino (Petroleum Experts, que incorporou a Midland Valley Exploration em 2017) e do ArcGIS Field Maps (Esri); padrão GeoPackage: Open Geospatial Consortium (ogc.org/standards/geopackage).

<!--
nivel: avancado
palavras_corpo: 2288
mapa_objetivo_secao:
  geologia-avancado-m25-oa01: "O fluxo escritório, campo, banco" + "Como o celular mede uma orientação" + "Posição, imagens e croquis" + "Vantagens e limitações, lado a lado" + "Exemplo trabalhado 1" + "Exemplo trabalhado 2"

alegacoes_auditaveis:
  - claim_id: DIGGEO-M25-A01-SENSORES-ORIENTACAO-001
    claim: "Um celular obtem a orientacao de um plano com acelerometro (direcao da gravidade, que fornece o mergulho) e magnetometro (campo magnetico local, que fornece a direcao em relacao ao norte magnetico); a leitura e magnetica e exige correcao de declinacao para virar azimute verdadeiro, e o magnetometro e perturbado por rochas magneticas (magnetita), objetos de aco e calibracao ruim."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2), item azul B12: Allmendinger, R. W., Siron, C. R. & Scott, C. P. (2017), 'Structural data collection with mobile devices: Accuracy, redundancy, and best practices', J. Struct. Geol. 102, 98-112, DOI 10.1016/j.jsg.2017.07.011 (ADS 2017JSG...102...98A) - resumo conferido: os celulares tem sensores que permitem coletar orientacao uma ordem de grandeza mais rapido que a bussola analogica, e e essa rapidez que viabiliza redundancia e estimativa quantitativa de incerteza; os autores registram explicitamente que 'recent work has called into question the reliability of sensors on Android devices', que e a divergencia que a aula ensina. Novakova & Pavlis (2017), J. Struct. Geol. 97, 93-103, ja verificada na passagem 1 (ver claim -PRECISAO-CELULAR-VS-BRUNTON-002). O mecanismo (acelerometro para o mergulho, magnetometro para a direcao, fusao de sensores, correcao de declinacao, perturbacao por magnetita e aco) esta sustentado pelas duas fontes. A RESSALVA 'auditoria deve conferir' DO REDATOR ESTA RETIRADA."
  - claim_id: DIGGEO-M25-A01-PRECISAO-CELULAR-VS-BRUNTON-002
    claim: "Os dois estudos de comparacao mais citados DIVERGEM: Allmendinger, Siron & Scott (2017), em dispositivos iOS, concluem que a acuracia e suficiente para coleta estrutural e destacam o ganho de redundancia de medidas; Novakova & Pavlis (2017), em dois aparelhos Android, observaram discrepancias de ate 80 graus contra bussola Freiberg, concentradas no azimute (direcao de mergulho menos acurada que mergulho), atribuidas a instabilidade do magnetometro e nao ao procedimento, e recomendam aferir aparelho+aplicativo contra bussola analogica antes da campanha. A acuracia e propriedade do aparelho e do aplicativo, nao da tecnologia."
    risk: fato
    source: "VERIFICADO EM FONTE PRIMARIA na auditoria de 2026-09-21. Novakova & Pavlis (2017), J. Struct. Geol. 97, 93-103: resumo e secao 5 (Conclusions) lidos na integra em PDF do artigo - 'the observed differences ... in some cases is higher than 80 deg', 'The dip direction measurements were found less accurate than dip measurements', 'the source of the problem was instability in the magnetic sensor', 'it is possible the conclusion might be device as well as platform dependent'. Allmendinger, Siron & Scott (2017), J. Struct. Geol. 102, 98-112, DOI 10.1016/j.jsg.2017.07.011: resumo - 'The accuracy of iOS devices is sufficient for structural geology data collection tasks' e enfase em redundancia e estimativa quantitativa de incerteza. ACHADO VERMELHO 1 DA AUDITORIA de 2026-09-21: a redacao original atribuia as DUAS fontes a conclusao de precisao 'comparavel a bussola' com incerteza dominada pelo procedimento 'mais do que pelo sensor' - exatamente o oposto do que Novakova & Pavlis concluem."
  - claim_id: DIGGEO-M25-A01-DECLINACAO-CALCULO-003
    claim: "Com declinacao leste positiva, azimute verdadeiro = azimute magnetico + declinacao; com declinacao de -21 graus (oeste, valor hipotetico), 128 graus magneticos correspondem a 107 graus verdadeiros, e aplicar a correcao duas vezes daria 86 graus; o mergulho nao muda com a declinacao."
    risk: calculo
    source: "Aritmetica direta (128-21=107; 128-42=86); convencao de sinal padrao de declinacao magnetica."
  - claim_id: DIGGEO-M25-A01-MEDIA-POLOS-004
    claim: "Para as cinco leituras (112,42),(118,40),(109,45),(115,38),(121,43) corrigidas por declinacao -21, a media vetorial dos polos resulta em direcao de mergulho 93.9 graus e mergulho 41.5 graus, com |R|/n = 0.9979 e desvios angulares 2.0, 2.5, 5.3, 3.5 e 4.3 graus."
    risk: calculo
    source: "Execucao direta do codigo apresentado (Python, NumPy), valores reproduzidos na redacao em 2026-09-21."
  - claim_id: DIGGEO-M25-A01-FERRAMENTAS-005
    claim: "FieldMove e FieldMove Clino sao aplicativos de mapeamento/clinometria de origem Midland Valley (hoje Petroleum Experts); QField e o aplicativo de campo do QGIS; ArcGIS Field Maps e da Esri; GeoPackage e padrao OGC baseado em SQLite. O termo 'FieldClino' do plano e tratado como FieldMove Clino e 'GIS-Pro' como GIS desktop generico (ArcGIS Pro ou QGIS)."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21: FieldMove Clino e publicado por Petroleum Experts Limited (petex.com, Move Suite; Google Play, com.mve.fieldmove.clino), e Petroleum Experts incorporou a Midland Valley Exploration em outubro de 2017 - a relacao de propriedade esta confirmada e o hedge foi removido da aula. 'FieldClino' e 'GIS-Pro' sao termos DO PLANO CURRICULAR, nao nomes comerciais: seguem tratados como FieldMove Clino e como GIS desktop generico, o que e decisao editorial declarada e nao alegacao factual."
  - claim_id: DIGGEO-M25-A01-WMM-006
    claim: "O World Magnetic Model, publicado por NOAA NCEI e British Geological Survey, e o modelo global usado para calcular declinacao, com atualizacao quinquenal; a epoca vigente e o WMM2025, valido de 2025.0 a 2030.0 (expira em 31/12/2029)."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21: NOAA NCEI, pagina oficial do World Magnetic Model (ncei.noaa.gov/products/world-magnetic-model) e nota de lancamento do WMM2025 - modelo harmonico esferico de grau 12 em 2025.0, taxa media de variacao para 2025.0-2030.0, expira em 31/12/2029; produzido conjuntamente por NCEI e BGS, em ciclos de cinco anos. Nota adicional: em 2025 foi lancada tambem uma versao de alta resolucao (WMMHR2025), nao mencionada na aula por nao ser necessaria ao ponto."
-->
