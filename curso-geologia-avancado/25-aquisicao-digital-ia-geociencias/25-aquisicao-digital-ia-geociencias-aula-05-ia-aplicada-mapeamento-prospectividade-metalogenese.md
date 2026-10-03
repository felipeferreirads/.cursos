# Aula 05: Inteligência artificial aplicada — mapeamento geológico automatizado, prospectividade mineral e modelos metalogenéticos em províncias geotectônicas

**ID:** geologia-avancado-m25-a05
**Módulo:** [[25-aquisicao-digital-ia-geociencias-modulo|Módulo 25 — Aquisição de dados digitais e inteligência artificial em geociências]]
**Duração estimada:** ~26 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** avaliar criticamente as aplicações de inteligência artificial ao mapeamento geológico e à prospectividade mineral, entendendo por que a qualidade do rótulo, a escassez de exemplos positivos, o viés de amostragem e a validação espacial condicionam o resultado, e como o modelo metalogenético entra para tornar o modelo estatístico geologicamente defensável.
**Ao final você vai conseguir:** distinguir mapeamento litológico preditivo de prospectividade mineral e o tipo de rótulo de cada um; calcular os pesos de evidência de uma camada binária e interpretá-los; demonstrar, com um experimento, como a validação aleatória infla o desempenho de um modelo espacial; e listar as perguntas de auditoria que um mapa de prospectividade precisa responder antes de orientar uma campanha.
**Pré-requisito:** [[24-machine-learning-geociencias-modulo|Módulo 24]] (fluxo de trabalho, floresta aleatória, matriz de confusão, validação cruzada e o risco de vazamento espacial), [[20-geoestatistica-modulo|Módulo 20]] (a noção de **continuidade espacial**: amostras próximas se parecem, e o quanto se parecem tem alcance mensurável — é ela que torna a validação por blocos necessária, e não uma preciosidade) e as Aulas 01 a 04 deste módulo (dado digital de qualidade, base organizada, camadas de aerogeofísica e MDT).

## Conteúdo

### Duas tarefas que parecem uma só

Aplicar aprendizado de máquina a dados espaciais de geologia inclui duas tarefas com lógicas muito diferentes.

**Mapeamento geológico preditivo (ou automatizado).** A pergunta é: *que unidade litológica ocorre em cada ponto da área?* Os **preditores** são camadas contínuas cobrindo toda a área: canais de gamaespectrometria e magnetometria, bandas de sensoriamento remoto, derivadas do MDT. O **rótulo** é a unidade litológica conhecida, vinda de pontos de campo ou de um mapa existente. É um problema de **classificação multiclasse**, com muitos rótulos disponíveis (cada unidade mapeada fornece milhares de pixels). Cracknell & Reading (2014) compararam cinco algoritmos de aprendizado de máquina no mapeamento litológico com dados de sensoriamento remoto e estudaram como a distribuição espacial das amostras de treino afeta a resposta dos modelos. Duas conclusões deles interessam aqui: a **floresta aleatória é uma boa primeira escolha** para classificar litologia, e a distribuição espacial do treino tem influência considerável sobre as previsões — ou seja, **nenhum algoritmo resolve a falta de treino representativo**. O produto não substitui o mapa: é um **mapa preditivo**, que aponta onde o campo deve ir conferir e onde a cobertura de dados é insuficiente.

**Prospectividade mineral.** A pergunta é: *onde é mais provável haver um depósito de determinado tipo?* Os preditores são as camadas de evidência (estruturas, litologia favorável, anomalias geoquímicas, geofísica). O **rótulo** são as **poucas** ocorrências ou depósitos conhecidos, muitas vezes dezenas, contra uma área de milhares ou milhões de células. É um problema de **classificação binária extremamente desbalanceada**, como na Aula 06 do Módulo 24, e é onde a maioria das armadilhas mora.

### Guiado por conhecimento, guiado por dados, híbrido

Há três famílias de abordagens de prospectividade. **Guiadas por conhecimento** (lógica fuzzy, sobreposição ponderada por especialistas) atribuem pesos às camadas a partir de um modelo conceitual do depósito, e funcionam onde há **poucos ou nenhum depósito conhecido** (fronteira exploratória). **Guiadas por dados** (pesos de evidência, regressão logística, floresta aleatória, redes neurais) estimam a relação a partir dos depósitos conhecidos, e exigem **exemplos suficientes** e representativos. **Híbridas** combinam ambos: o especialista escolhe e transforma as camadas com base no modelo genético; o algoritmo estima os pesos (Carranza, 2008, é a referência de GIS aplicado a prospectividade). A **floresta aleatória** mostrou-se útil mesmo com poucas ocorrências e dados com lacunas (Carranza & Laborte, 2015); o aprendizado profundo, como os autocodificadores para reconhecer anomalias geoquímicas (Xiong & Zuo, 2016), amplia o repertório; revisões (Zuo, 2017) trazem o panorama dos métodos.

### O papel do modelo metalogenético: escolher o que o algoritmo vê

Um algoritmo alimentado com 60 camadas e 30 depósitos vai encontrar padrões, inclusive espúrios. O modelo metalogenético é o que reduz o espaço de busca a um espaço **geologicamente defensável**. Guarde a frase que resume esta seção inteira: **o modelo decide as camadas; o algoritmo decide os pesos.**

A abordagem do **sistema mineralizador** organiza a pergunta em componentes — fonte dos fluidos e dos metais, transporte por condutos (as estruturas que conduzem), armadilhas (onde o metal se deposita) e preservação. A decomposição é de Wyborn, Heinrich & Jaques (1994), e foi refinada por Knox-Robinson & Wyborn (1997) e Hronsky & Groves (2008).

Só que ter o modelo genético não basta: é preciso traduzi-lo em camadas que existam num banco de dados. É essa a contribuição que interessa aqui. McCuaig, Beresford & Hronsky (2010) propõem um **processo de tradução** em quatro passos:

1. os **processos críticos** do sistema mineralizador (aqueles sem os quais não há depósito);
2. os **processos constituintes** em que cada um se decompõe;
3. os **elementos de alvo**, isto é, o que esses processos deixaram registrado na geologia;
4. os **critérios de alvo**, que detectam esses elementos diretamente ou por proxy.

É o quarto passo que torna um modelo genético operável em dados digitais, e é onde as aulas anteriores entram: o conduto por zonas de cisalhamento interpretadas no MDT e na aeromagnetometria (Aula 03), a armadilha por um contraste de reologia ou de composição da rocha, a fonte por uma assinatura geoquímica ou isotópica (Aula 02).

Numa **província geotectônica** específica, o modelo é escolhido pelo tipo de depósito dominante e pelo controle tectônico: em terrenos orogênicos, por exemplo, estruturas de segunda e terceira ordem próximas a zonas de cisalhamento crustais controlam depósitos de ouro; em ambientes de intrusões, contatos e indicadores de alteração medidos na magnetometria e na gamaespectrometria contam mais. O que se leva daqui não é a lista de cada província, e sim o **método** — e a sua consequência: um modelo treinado numa província **não é transferível** a outra cujo sistema mineralizador difere, mesmo que as camadas de dados sejam as mesmas.

### Cinco limitações que decidem se o mapa serve

1. **A qualidade do rótulo limita o modelo.** Um mapa geológico é uma **interpretação**, com a escala e a época de quem o fez, e não um dado observado. Se ele é usado como rótulo de treino, o algoritmo aprende a reproduzir o mapa, com seus contatos generalizados e seus erros, **em escala e com aparência de precisão**. Um mapa desatualizado usado como treino ensina o algoritmo a reproduzir o erro. O melhor rótulo é o de **pontos de campo verificados** (Aula 01, com o campo "tipo de medida" e "confiança").
2. **Os negativos não existem.** Em prospectividade, "não tem depósito conhecido aqui" **não significa** "não tem depósito": significa que ninguém achou ou procurou. Tratar toda célula sem depósito como negativa verdadeira ensina o modelo a penalizar áreas apenas por terem sido pouco exploradas. A literatura recorre a pseudoausências, a métodos de aprendizado com exemplos positivos e não rotulados, e à interpretação do resultado como **ordenação relativa** (o mapa mostra onde é *mais* provável, não a probabilidade absoluta de um depósito).
3. **Viés de amostragem.** Os depósitos conhecidos estão onde se explorou: perto de estradas, de afloramentos, de áreas de fácil acesso, de camadas com dados. O modelo aprende a "onde se procurou" com a mesma facilidade com que aprende "onde há minério".
4. **Autocorrelação espacial e validação.** Como no Módulo 24, uma validação com partição aleatória **vaza** informação entre treino e teste, porque células vizinhas são semelhantes; o resultado é uma métrica inflada. A defesa é validar **por blocos espaciais**. O exemplo trabalhado 2 mostra o tamanho do efeito.
5. **Coerência geológica.** Um mapa bom passa no teste do geólogo: as camadas mais importantes para o modelo são as que o modelo metalogenético diz que importam? Se a variável mais importante for a distância à estrada de acesso, o modelo aprendeu o viés de amostragem, não a geologia. Lembre-se, do Módulo 24, de que a importância por impureza e a por permutação têm vieses próprios; consulte as duas.

Cabe acrescentar o que a Aula 02 deixou pendente: **valores censurados** (abaixo do limite de detecção) e **dados ausentes** contaminam o treino se forem substituídos por constantes sem critério. Um modelo que treina com ouro "substituído por LD/2" aprende, em parte, a convenção de substituição do laboratório.

### Avaliar e comunicar

Uma métrica pontual não basta. Usa-se a **curva de sucesso** ou a **curva predição-área** (Yousefi & Carranza, 2015): qual fração dos depósitos conhecidos cai em qual fração da área classificada como mais prospectiva. O que interessa ao investidor é concentrar a maior parte dos depósitos numa pequena fração da área. Uma boa comunicação inclui: o mapa, a **incerteza** (onde o modelo é confiante e onde extrapola), as **camadas que o dirigem**, a **estratégia de validação** e as **limitações declaradas**, exatamente o roteiro de comunicação da Aula 07 do Módulo 24.

## Exemplo trabalhado 1: pesos de evidência de uma camada binária

**Situação.** A área tem 1.000 células (N). Há 20 depósitos conhecidos, cada um numa célula distinta (D = 20). A camada de evidência é um *buffer* de 500 m em torno de uma zona de cisalhamento; ela cobre 200 células (B = 200), e 12 dos 20 depósitos caem dentro dela (B∩D = 12). Calcule os pesos de evidência.

**Resolução.** O método de **pesos de evidência** (Bonham-Carter, Agterberg & Wright, 1989) compara a frequência do padrão entre as células com depósito e entre as sem depósito:

- P(B | D) = 12/20 = **0,600**
- P(B | não D) = (200 − 12) / (1.000 − 20) = 188/980 = **0,1918**
- W⁺ = ln[P(B | D) / P(B | não D)] = ln(3,128) = **+1,140**
- W⁻ = ln[P(não B | D) / P(não B | não D)] = ln(0,400/0,808) = **−0,703**
- Contraste C = W⁺ − W⁻ = **1,844**

**Interpretação.** O padrão ocupa 20% da área e contém 60% dos depósitos: é encontrado **3,1 vezes mais** entre as células com depósito do que entre as sem. W⁺ positivo diz que estar no *buffer* aumenta a chance; W⁻ negativo diz que estar fora a diminui. Convertendo para probabilidade a partir da chance *a priori* (20/980 = 0,0204): dentro do *buffer*, a chance passa a 0,0204 × 3,128 = 0,0638, ou **6,0%** por célula; fora, 0,0204 × 0,495 = 0,0101, ou **1,0%**. Confere com a contagem direta (12/200 = 6%, 8/800 = 1%), como deve ser numa camada só.

**Limitações que o exemplo esconde.** (i) Os pesos dependem do **tamanho da célula** escolhido; (ii) combinar várias camadas exige a hipótese de **independência condicional**, que camadas geológicas em geral violam (a zona de cisalhamento e a anomalia magnética que ela produz não são independentes); (iii) os 6% e 1% não são probabilidades de haver depósito no sentido comum: são frações relativas à definição de célula e aos depósitos **conhecidos**, com todo o viés de amostragem do item 3 acima. Use como **ordenação relativa**.

## Exemplo trabalhado 2: quanto a validação aleatória infla o desempenho?

**Situação.** Gere uma área sintética de 1.200 pontos em 100 × 100 km, com um rótulo (15% de "depósitos") que depende de duas coisas: um preditor geológico mensurável (`f1`, fraco) e um **campo espacial não medido**, agrupado em células de cerca de 8 km (peso maior). Treine uma floresta aleatória com `f1`, um segundo preditor `f2` e as coordenadas, e compare a validação aleatória com a validação por blocos de 25 km.

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, GroupKFold, cross_val_predict
from sklearn.metrics import roc_auc_score

rng = np.random.default_rng(7)
n = 1200
x, y = rng.uniform(0, 100, n), rng.uniform(0, 100, n)          # km
def campo(x, y, ph): return np.sin(x/9 + ph) + np.cos(y/11 - ph)
f1, f2 = campo(x, y, 0.0), campo(x, y, 2.0)
ruido = rng.normal(0, 1, (12, 12))                               # células de ~8,3 km
ruido = ruido[(x//8.34).astype(int), (y//8.34).astype(int)]
score = 0.5*f1 + 1.5*ruido + rng.normal(0, 0.3, n)
lab = (score > np.quantile(score, 0.85)).astype(int)
X = np.column_stack([f1, f2, x, y])

rf = RandomForestClassifier(n_estimators=200, random_state=0, n_jobs=1)
p_alea = cross_val_predict(rf, X, lab, cv=KFold(5, shuffle=True, random_state=0),
                           method="predict_proba")[:, 1]
bloco = (x // 25).astype(int) * 4 + (y // 25).astype(int)       # 16 blocos 25x25 km
p_bloc = cross_val_predict(rf, X, lab, cv=GroupKFold(4), groups=bloco,
                           method="predict_proba")[:, 1]
print("AUC aleatoria: %.3f | AUC por blocos: %.3f" % (
      roc_auc_score(lab, p_alea), roc_auc_score(lab, p_bloc)))
```

**Saída obtida (Python, scikit-learn 1.9.1, NumPy):** prevalência de 15% (180 positivos em 1.200); **AUC com validação aleatória de 0,920** e **AUC com validação por blocos de 0,686**.

**Interpretação.** O mesmo modelo, com os mesmos dados, parece excelente (0,92) ou modesto (0,69) conforme a validação. A diferença de 0,23 é a parte do "desempenho" que **era só memória espacial**: com a partição aleatória, cada ponto de teste tem vizinhos de treino na mesma célula do campo não medido, e as coordenadas (`x`, `y`) deixam o modelo interpolar o campo escondido; com blocos, ele precisa **extrapolar** para regiões inteiras onde não viu nada, e só o sinal geológico genuíno (o `f1` fraco) sobrevive. Esse é o comportamento que importa numa campanha, porque o alvo novo está **fora** do que se conhece. **Cuidado:** o experimento é sintético, os números 0,92 e 0,69 valem para esta construção, e o que se generaliza é o **sentido** da diferença, não a magnitude. Note ainda que colocar as coordenadas como preditoras — o que Cracknell & Reading (2014) chamam de **informação espacial explícita** — é o que torna a partição aleatória tão enganosa aqui. E há uma tensão real entre os dois usos, que vale enxergar: naquele trabalho, incluir as coordenadas **melhorou** o mapeamento litológico, porque ali o objetivo é interpolar dentro de uma área já amostrada; em prospectividade o objetivo é o inverso, **extrapolar** para onde ninguém procurou, e aí a mesma variável passa de ajuda a ilusão. A variável não mudou; mudou a pergunta.

## Recap relâmpago

- **Mapeamento preditivo** (classificação multiclasse, muitos rótulos, rótulo vindo de campo ou de mapa) e **prospectividade** (binário, poucos depósitos, negativos desconhecidos) são tarefas com lógicas e armadilhas diferentes.
- **Guiado por conhecimento** serve onde há poucos depósitos; **guiado por dados** exige exemplos representativos; o **híbrido** usa o modelo metalogenético para escolher as camadas e o algoritmo para estimar os pesos.
- O **sistema mineralizador** (fonte, conduto, armadilha, preservação) transforma o modelo genético em camadas mapeáveis; um modelo não se transfere entre províncias com sistemas diferentes.
- A **qualidade do rótulo** limita o modelo: mapa geológico é interpretação, e um mapa desatualizado como treino reproduz o erro em escala.
- "Sem depósito conhecido" **não é** "sem depósito": interprete o mapa como **ordenação relativa**, cuidando do **viés de amostragem**.
- **Valide por blocos espaciais**: no experimento, a AUC caiu de 0,920 (aleatória) para 0,686 (blocos). Pesos de evidência: 12 de 20 depósitos em 20% da área dão W⁺ = +1,140, W⁻ = −0,703, C = 1,844.

## Próxima aula

Este é o **fim do módulo**. Os módulos seguintes deixam a organização e a modelagem estatística e entram em geoquímica isotópica ([[26-geologia-isotopica-aplicada-modulo|Módulo 26]]), cujos dados (razões isotópicas e idades) você já sabe como registrar (Aula 02) e que alimentarão futuros modelos metalogenéticos.

## Fontes

- Cracknell, M. J. & Reading, A. M. (2014), "Geological mapping using remote sensing data: A comparison of five machine learning algorithms, their response to variations in the spatial distribution of training data and the use of explicit spatial information", *Computers & Geosciences*, 63, 22-33.
- Carranza, E. J. M. (2008), *Geochemical Anomaly and Mineral Prospectivity Mapping in GIS*, Handbook of Exploration and Environmental Geochemistry, vol. 11, Elsevier.
- Carranza, E. J. M. & Laborte, A. G. (2015), "Random forest predictive modeling of mineral prospectivity with small number of prospects and data with missing values in Abra (Philippines)", *Computers & Geosciences*, 74, 60-70.
- Xiong, Y. & Zuo, R. (2016), "Recognition of geochemical anomalies using a deep autoencoder network", *Computers & Geosciences*, 86, 75-82.
- Zuo, R. (2017), "Machine learning of mineralization-related geochemical anomalies: A review of potential methods", *Natural Resources Research*, 26, 457-464.
- McCuaig, T. C., Beresford, S. & Hronsky, J. (2010), "Translating the mineral systems approach into an effective exploration targeting system", *Ore Geology Reviews*, 38, 128-138, DOI 10.1016/j.oregeorev.2010.05.008.
- Wyborn, L. A. I., Heinrich, C. A. & Jaques, A. L. (1994), "Australian Proterozoic mineral systems: essential ingredients and mappable criteria", *AusIMM Annual Conference*, 109-115. (Origem da decomposição do sistema mineralizador em fonte, transporte, acumulação e preservação.)
- Knox-Robinson, C. M. & Wyborn, L. A. I. (1997), "Towards a holistic exploration strategy: using Geographic Information Systems as a tool to enhance exploration", *Australian Journal of Earth Sciences*, 44(4), 453-463, DOI 10.1080/08120099708728326.
- Hronsky, J. M. A. & Groves, D. I. (2008), "Science of targeting: definition, strategies, targeting and performance measurement", *Australian Journal of Earth Sciences*, 55(1), 3-12, DOI 10.1080/08120090701581356.
- Bonham-Carter, G. F., Agterberg, F. P. & Wright, D. F. (1989), "Weights of evidence modelling: a new approach to mapping mineral potential", in Agterberg & Bonham-Carter (eds.), *Statistical Applications in the Earth Sciences*, Geological Survey of Canada Paper 89-9, 171-183.
- Yousefi, M. & Carranza, E. J. M. (2015), "Prediction-area (P-A) plot and C-A fractal analysis to classify and evaluate evidential maps for mineral prospectivity modeling", *Computers & Geosciences*, 79, 69-81.
- Roberts, D. R. et al. (2017), "Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure", *Ecography*, 40(8), 913-929, DOI 10.1111/ecog.02881.

<!--
nivel: avancado
palavras_corpo: 2217
mapa_objetivo_secao:
  geologia-avancado-m25-oa04: "Duas tarefas" + "Guiado por conhecimento" + "O papel do modelo metalogenético" + "Cinco limitações" + "Avaliar e comunicar" + "Exemplo trabalhado 1" + "Exemplo trabalhado 2"

alegacoes_auditaveis:
  - claim_id: DIGGEO-M25-A05-PESOS-EVIDENCIA-001
    claim: "Para N=1000 celulas, D=20 depositos, camada B=200 celulas com 12 depositos: P(B|D)=0.600, P(B|~D)=188/980=0.1918, W+=ln(3.128)=+1.140, W-=ln(0.400/0.808)=-0.703, contraste C=1.844; convertendo a chance a priori 20/980=0.0204, a probabilidade por celula e 6.0% dentro do buffer e 1.0% fora, coincidindo com 12/200 e 8/800."
    risk: calculo
    source: "Aritmetica direta e verificacao numerica (Python), 2026-09-21. REEXECUTADO e reproduzido digito a digito na auditoria de 2026-09-21 (passagem 2), item azul B8: P(B|D)=0.600, P(B|~D)=0.1918, razao 3.128, W+=+1.140, W-=-0.703, C=1.844, chances 0.0638 e 0.0101, probabilidades 6.000% e 1.000%, coincidindo com 12/200 e 8/800. O uso de 'chance' para odds e a conversao para probabilidade estao corretos. FORMULAS DE W+ E W- VERIFICADAS: Bonham-Carter, G. F., Agterberg, F. P. & Wright, D. F. (1989), 'Weights of evidence modelling: a new approach to mapping mineral potential', in Agterberg & Bonham-Carter (eds.), Statistical Applications in the Earth Sciences, Geological Survey of Canada Paper 89-9 (referencia confirmada)."
  - claim_id: DIGGEO-M25-A05-VALIDACAO-ESPACIAL-002
    claim: "No experimento sintetico (1200 pontos, 15% positivos, semente 7, floresta aleatoria de 200 arvores com f1, f2, x, y), AUC com validacao aleatoria 5-fold = 0.920 e com GroupKFold(4) por blocos de 25 km = 0.686."
    risk: calculo
    source: "Execucao direta do codigo apresentado (Python, NumPy, scikit-learn 1.9.1), 2026-09-21. REEXECUTADO NA AUDITORIA de 2026-09-21 (passagem 2), item azul B9, em Python 3.13.2, NumPy 2.5.1, scikit-learn 1.9.1: prevalencia 180/1200 (15%), 16 blocos de 25 km, AUC aleatoria 0.920 e AUC por blocos 0.686 - reproduzido exatamente. Valores especificos da construcao sintetica; apenas o sentido da diferenca se generaliza."
  - claim_id: DIGGEO-M25-A05-VAZAMENTO-ESPACIAL-003
    claim: "Com dados espacialmente autocorrelacionados, o particionamento aleatorio de treino e teste infla o desempenho por vazamento entre pontos vizinhos, e a validacao por blocos espaciais e a correcao."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2), item azul B10: Roberts, D. R. et al. (2017), 'Cross-validation strategies for data with temporal, spatial, hierarchical, or phylogenetic structure', Ecography 40(8), 913-929, DOI 10.1111/ecog.02881 (referencia confere). A alegacao de que e 'a mesma fonte da Aula 01 do Modulo 24' foi CONFERIDA NO PROPRIO ARQUIVO: a Aula 01 do M24 cita essa referencia com volume, paginas e DOI identicos - a citacao interna esta correta."
  - claim_id: DIGGEO-M25-A05-CRACKNELL-READING-004
    claim: "Cracknell & Reading (2014) compararam cinco algoritmos de aprendizado de maquina em mapeamento litologico com dados de sensoriamento remoto e avaliaram sua resposta a variacoes na distribuicao espacial dos dados de treino e ao uso de informacao espacial explicita; metodos de conjunto como floresta aleatoria costumam ter bom desempenho."
    risk: fato
    source: "VERIFICADO EM FONTE PRIMARIA na auditoria de 2026-09-21 (passagem 2), item azul B1 - A INCERTEZA DECLARADA DO REDATOR ESTA RETIRADA. Cracknell, M. J. & Reading, A. M. (2014), 'Geological mapping using remote sensing data: A comparison of five machine learning algorithms, their response to variations in the spatial distribution of training data and the use of explicit spatial information', Computers & Geosciences 63, 22-33, DOI 10.1016/j.cageo.2013.10.008 (titulo, revista, volume e paginas conferem). Os cinco algoritmos sao Naive Bayes, k-NN, florestas aleatorias, SVM e redes neurais artificiais. A floresta aleatoria e apontada como escolha robusta pela acuracia espacial, e a sua vantagem relativa AUMENTA a medida que o treino fica espacialmente mais disperso. O termo 'informacao espacial explicita' e dos proprios autores (esta no titulo). Sobre o uso das coordenadas: 'the use of explicit spatial information generates accurate lithology predictions but should be used in conjunction with geophysical data in order to generate geologically plausible predictions' - o que SUSTENTA a afirmacao da aula de que incluir coordenadas melhorou o mapeamento litologico, com a nuance de que coordenadas sozinhas dao acuracia sem plausibilidade geologica."
  - claim_id: DIGGEO-M25-A05-SISTEMA-MINERALIZADOR-005
    claim: "A abordagem do sistema mineralizador (McCuaig, Beresford & Hronsky 2010) organiza o alvo de exploracao em componentes (fonte, transporte/condutos, armadilha, preservacao) que podem ser mapeados por proxies em dados digitais."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2), item azul B2. McCuaig, T. C., Beresford, S. & Hronsky, J. (2010), Ore Geology Reviews 38, 128-138, DOI 10.1016/j.oregeorev.2010.05.008 (confere). O PROCESSO DE QUATRO PASSOS do artigo e exatamente o que a aula descreve: (1) processos criticos do sistema mineralizador, (2) processos constituintes, (3) elementos de alvo refletidos na geologia, (4) criterios de alvo que detectam esses elementos; o artigo ilustra com Ni-Cu-EGP em komatiito e ouro orogenico, e trata as quatro fontes de incerteza da cadeia. PRECISAO DE ATRIBUICAO: a DECOMPOSICAO POR COMPONENTES (fonte, transporte, acumulacao, preservacao) e de Wyborn, Heinrich & Jaques (1994) - 'mobilising ore components from a source, transporting and accumulating them in more concentrated form and then preserving them throughout the subsequent geological history' -, e o PROCESSO DE TRADUCAO e de McCuaig et al. (2010). O corpo da aula separa corretamente as duas atribuicoes; este campo source, que as juntava, fica corrigido. Knox-Robinson & Wyborn (1997), Aust. J. Earth Sci. 44(4), 453-463, DOI 10.1080/08120099708728326, e Hronsky & Groves (2008), Aust. J. Earth Sci. 55(1), 3-12, DOI 10.1080/08120090701581356, tambem conferem - ver ACHADO LARANJA 10 (claim -FONTES-AUSENTES-008), porque as tres estavam creditadas no corpo e ausentes da lista de Fontes."
  - claim_id: DIGGEO-M25-A05-LITERATURA-PROSPECTIVIDADE-006
    claim: "Carranza & Laborte (2015) aplicam floresta aleatoria a prospectividade com poucos prospectos e dados ausentes (Abra, Filipinas); Xiong & Zuo (2016) usam autocodificador profundo para reconhecer anomalias geoquimicas; Zuo (2017) revisa metodos de aprendizado de maquina para anomalias geoquimicas; Yousefi & Carranza (2015) propoem o grafico predicao-area; Carranza (2008) e a referencia de GIS aplicado a prospectividade."
    risk: fato
    source: "VERIFICADO EM FONTE PRIMARIA na auditoria de 2026-09-21 (passagem 2), itens azuis B3 a B7 - A INCERTEZA DECLARADA DO REDATOR ESTA RETIRADA. Carranza & Laborte (2015), Computers & Geosciences 74, 60-70, DOI 10.1016/j.cageo.2014.10.004 (confere, inclusive o conteudo: floresta aleatoria com MENOS DE 20 locais de treino - 12 prospectos de porfiro de Cu em Abra, Filipinas - e ganho de acuracia por imputacao de valores ausentes). Xiong & Zuo (2016), Computers & Geosciences 86, 75-82 (confere; autocodificador profundo que distingue anomalias pelo erro de reconstrucao). Zuo (2017), Natural Resources Research 26, 457-464, DOI 10.1007/s11053-017-9345-4 (confere; revisao de metodos de aprendizado de maquina para anomalias geoquimicas). Yousefi & Carranza (2015), Computers & Geosciences 79, 69-81 (confere; grafico predicao-area, ADS 2015CG.....79...69Y). Carranza (2008), Handbook of Exploration and Environmental Geochemistry vol. 11, Elsevier, 368 pp., ISBN 978-0-444-51325-0 (confere, e a caracterizacao como referencia de GIS aplicado a prospectividade esta correta: a Parte III do livro e exatamente sobre modelagem conceitual e preditiva de prospectividade em GIS)."
  - claim_id: DIGGEO-M25-A05-NEGATIVOS-VIES-007
    claim: "Em prospectividade mineral nao existem negativos verdadeiros (ausencia de deposito conhecido nao e ausencia de mineralizacao), os depositos conhecidos refletem viés de amostragem (acesso, exploracao previa), e o resultado deve ser lido como ordenacao relativa."
    risk: fato
    source: "AVALIADO na auditoria de 2026-09-21 (passagem 2), item azul B13: MANTIDO COMO JULGAMENTO METODOLOGICO CONSOLIDADO e NAO promovido a fato. Verificar uma alegacao nao muda a natureza dela: isto e principio de metodo da literatura de prospectividade (Carranza 2008; Zuo 2017), nao medida nem classificacao formal, e promove-lo a fato seria certeza indevida. Mesmo critério ja aplicado nos Modulos 22 e 23. O campo risk segue como esta e o texto da aula nao foi alterado."
  - claim_id: DIGGEO-M25-A05-FONTES-AUSENTES-008
    claim: "As tres obras creditadas no corpo da aula para a linhagem do sistema mineralizador - Wyborn, Heinrich & Jaques (1994); Knox-Robinson & Wyborn (1997); Hronsky & Groves (2008) - constam da lista de Fontes com veiculo, volume, paginas e DOI onde existe."
    risk: fato
    source: "ACHADO LARANJA 10 DA AUDITORIA de 2026-09-21 (passagem 2): as tres obras eram creditadas com autor e ano no corpo e NAO apareciam na secao Fontes, que lista oito outras referencias - numa aula cujo modulo ensina proveniencia, licenca e identificador persistente (Aula 04), uma citacao que o aluno nao consegue seguir e defeito material. As tres atribuicoes, verificadas, estao CORRETAS; o que faltava era poder conferi-las. VERIFICADO: Wyborn, L. A. I., Heinrich, C. A. & Jaques, A. L. (1994), 'Australian Proterozoic mineral systems: essential ingredients and mappable criteria', AusIMM Annual Conference, 109-115 (acervo AusIMM; ata de conferencia, sem DOI - RESSALVA DE FONTE: a literatura cita o volume com dois locais de conferencia, Darwin no acervo da AusIMM e Melbourne em citacoes secundarias); Knox-Robinson, C. M. & Wyborn, L. A. I. (1997), Australian Journal of Earth Sciences 44(4), 453-463, DOI 10.1080/08120099708728326; Hronsky, J. M. A. & Groves, D. I. (2008), Australian Journal of Earth Sciences 55(1), 3-12, DOI 10.1080/08120090701581356. Corrigido: as tres acrescentadas a secao Fontes. NOTA: 'refinada por' e caracterizacao frouxa para Hronsky & Groves (2008), que trata do PROCESSO de targeting mais do que da decomposicao por componentes; fica dentro da latitude editorial e o texto nao foi alterado por isso."
  - claim_id: DIGGEO-M25-A05-CITACOES-INTERNAS-009
    claim: "As tres citacoes internas desta aula ao Modulo 24 apontam para conteudo que aquelas aulas de fato tem: a Aula 06 do M24 formaliza classes desbalanceadas, a Aula 07 do M24 traz o roteiro de comunicacao de resultado com limitacoes, e a ressalva sobre vieses da importancia por impureza e por permutacao corresponde a achados ja corrigidos na auditoria do M24."
    risk: fato
    source: "VERIFICADO na auditoria de 2026-09-21 (passagem 2), item azul B11, POR LEITURA DIRETA DOS ARQUIVOS DO MODULO 24 em disco: (i) a Aula 06 do M24 e a que formaliza desbalanceamento, com o exemplo das 200 encostas (8 instaveis, acuracia 0.96, revocacao 0); (ii) a Aula 07 do M24 tem a secao 'Comunicar resultados com suas limitacoes', com os quatro itens; (iii) os vieses das duas medidas de importancia correspondem aos achados MLGEO-M24-A03-MDI-VIES-CARDINALIDADE-009 e MLGEO-M24-A06-PERMUTACAO-CORRELACAO-008. O DOMINANT_PATTERN dos Modulos 22, 23 e 24 - a citacao interna ao proprio curso como ponto de falha mais provavel - NAO SE REPETIU nesta aula. Repetiu-se apenas na Aula 03 deste modulo (achado amarelo 7, passagem 1)."
-->
