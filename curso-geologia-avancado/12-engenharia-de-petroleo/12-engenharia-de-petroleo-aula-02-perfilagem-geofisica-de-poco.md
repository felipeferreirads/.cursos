# Aula 02: Avaliação de formações: perfilagem geofísica de poço e testemunhagem

**ID:** geologia-avancado-m12-a02
**Módulo:** [[12-engenharia-de-petroleo-modulo|Módulo 12 — Engenharia de petróleo]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** interpretar perfis geofísicos de poço — raios gama, resistividade, nêutron e densidade combinados — para estimar volume de argila, litologia, porosidade e saturação de água, usando a equação de Archie como ponte quantitativa entre resistividade e saturação de hidrocarboneto.
**Ao final você vai conseguir:** identificar zonas reservatório e estimar seu volume de argila a partir do perfil de raios gama; calcular porosidade a partir da combinação nêutron-densidade; e aplicar a equação de Archie para estimar a saturação de água de uma zona a partir de resistividade.
**Pré-requisito:** Aula 01 deste módulo (construção do poço). Módulo 11, Aula 02 — este curso já introduziu o **perfil sônico** e o **perfil de densidade** como medidas de velocidade e densidade da rocha usadas para construir o sismograma sintético e amarrar poço à sísmica; esta aula não repete essa base, e assume que você sabe o que é um perfil de poço e como ele é registrado continuamente ao longo da trajetória.

## Conteúdo

### O que muda em relação ao que o Módulo 11 já ensinou

O Módulo 11 usou perfilagem de poço com um objetivo específico: transformar velocidade e densidade em impedância acústica para calibrar a sísmica. Aqui o objetivo é outro — usar perfis de poço para responder à pergunta central da **avaliação de formações** (*formation evaluation*): esta rocha é reservatório, e se for, quanto espaço poroso tem e que fração desse espaço está ocupada por hidrocarboneto em vez de água? Os perfis sônico e de densidade continuam relevantes (a densidade, em particular, reaparece adiante com um papel diferente do da Aula 02 do Módulo 11), mas o núcleo desta aula são três famílias de perfis ainda não tratadas neste curso: **raios gama**, **resistividade** e **nêutron** — que, combinadas com a densidade já conhecida, permitem estimar litologia, porosidade e saturação sem depender de amostra física.

### Raios gama: separando reservatório de folhelho

O perfil de **raios gama** (GR) mede a radioatividade natural da formação — predominantemente de potássio, tório e urânio presentes em minerais de argila e em alguns minerais acessórios. Folhelhos e argilas são sistematicamente mais radioativos que arenitos limpos e carbonatos, porque concentram esses elementos nas estruturas de argilominerais; por isso o GR é, na prática diária de um intérprete, o primeiro perfil consultado para separar zonas potencialmente reservatório (GR baixo) de zonas predominantemente argilosas (GR alto), antes mesmo de qualquer cálculo quantitativo.

Quantitativamente, normaliza-se a leitura de GR entre um valor mínimo de referência (GRmin, tipicamente lido numa zona limpa conhecida, arenito ou carbonato sem argila) e um valor máximo (GRmax, lido num folhelho espesso e homogêneo próximo) para obter o **índice de raios gama** (IGR):

IGR = (GR − GRmin) / (GRmax − GRmin)

O IGR varia de 0 (rocha limpa) a 1 (folhelho puro), e é convertido em **volume de argila** (Vsh) por uma relação não linear — a relação linear (Vsh = IGR) superestima sistematicamente o volume de argila em formações não consolidadas ou de idade geológica jovem, e por isso correções não lineares (como as propostas por Larionov, distintas para rochas terciárias e mais antigas) são preferidas na prática profissional. O Vsh entra depois como correção nos cálculos de porosidade e saturação, porque argila dispersa nos poros reduz a porosidade efetiva disponível para hidrocarboneto e distorce a resposta elétrica da formação.

### Resistividade: o perfil que enxerga o fluido, não a rocha

Diferente do GR, sônico e densidade — que respondem principalmente à matriz mineral e à porosidade —, o perfil de **resistividade** responde ao **fluido** que ocupa os poros. Água salgada (com íons dissolvidos) conduz corrente elétrica bem, logo tem resistividade baixa; óleo e gás são isolantes elétricos, logo uma rocha porosa saturada de hidrocarboneto tem resistividade muito mais alta que a mesma rocha saturada de água de formação. Essa é a base física de toda a avaliação quantitativa de saturação: **resistividade alta em uma zona porosa e com Vsh baixo é o indicador clássico de hidrocarboneto**.

Ferramentas modernas registram resistividade em múltiplas profundidades de investigação simultâneas (rasa, média, profunda), porque o filtrado da lama de perfuração invade a formação ao redor do poço (o mesmo fenômeno de invasão mencionado de passagem no Módulo 11 como fonte de distorção) e desloca parcialmente o fluido original perto da parede do poço. A leitura de resistividade **profunda** (*deep resistivity*, Rt), pouco afetada pela invasão, é a que se usa para representar a formação intacta nos cálculos de saturação; a comparação entre resistividades rasa e profunda, aliás, é ela mesma um indicador de permoporosidade e de presença de hidrocarboneto móvel.

### A equação de Archie: de resistividade a saturação de água

Archie (1942), em um trabalho hoje considerado fundacional da petrofísica quantitativa, propôs uma relação empírica entre a resistividade de uma rocha porosa saturada e a fração de seus poros ocupada por água — a **saturação de água** (Sw). A forma mais usada da equação, para uma formação limpa (Vsh desprezível):

Sw = [ (a / φᵐ) × (Rw / Rt) ] ^(1/n)

onde φ é a porosidade (fração), Rw é a resistividade da água de formação (que satura 100% dos poros numa zona de referência, ou obtida de análise de água produzida), Rt é a resistividade profunda lida no perfil, e a, m, n são constantes empíricas — o fator de tortuosidade (a, tipicamente próximo de 1), o expoente de cimentação (m, tipicamente entre 1,8 e 2,2 em arenitos consolidados, mais baixo em rochas menos cimentadas) e o expoente de saturação (n, tipicamente próximo de 2). Esses parâmetros não são universais: são calibrados por rocha e por bacia a partir de medidas de laboratório em testemunhos (a próxima seção), e seu uso sem calibração local é uma fonte conhecida de erro sistemático em avaliação de formações.

A saturação de hidrocarboneto é, por definição, o complemento: Sh = 1 − Sw. Uma Sw calculada baixa (por exemplo, 20%) numa zona porosa significa que 80% do espaço poroso está preenchido por hidrocarboneto — um indicador de reservatório produtivo, desde que a porosidade e a espessura também sejam suficientes, o que a Aula 03 devolve em forma de cálculo de volume.

### Nêutron e densidade combinados: porosidade e uma pista de litologia

O perfil de **nêutron** (NPHI) bombardeia a formação com nêutrons rápidos e mede o efeito de sua desaceleração, que depende quase inteiramente da concentração de átomos de hidrogênio ao redor do poço — presentes tanto na água quanto no óleo que preenche os poros. Em rocha limpa saturada de água ou óleo, o nêutron responde de forma aproximadamente direta à porosidade. O perfil de **densidade** (RHOB, já visto no Módulo 11 como insumo do sismograma sintético) mede a densidade eletrônica da formação, da qual se deriva a porosidade por densidade (φD) conhecendo a densidade da matriz mineral (ρmatriz, ex.: 2,65 g/cm³ para quartzo) e do fluido (ρfluido):

φD = (ρmatriz − ρformação) / (ρmatriz − ρfluido)

Isoladamente, cada perfil tem uma fraqueza: o nêutron superestima porosidade em zonas argilosas (a água ligada à argila também desacelera nêutrons, sem ser porosidade efetiva útil), e a densidade depende de se conhecer corretamente a matriz mineral, que pode não ser conhecida a priori. A combinação dos dois resolve ambos os problemas ao mesmo tempo: em rocha limpa, nêutron e densidade convergem para valores de porosidade próximos; em zonas de gás, o efeito de baixa densidade de hidrogênio no gás faz o nêutron subestimar fortemente a porosidade enquanto a densidade a superestima ligeiramente — um afastamento característico entre as duas curvas conhecido como **efeito de gás** (*gas crossover*), um dos indicadores diretos mais confiáveis de gás em um perfil combinado, sem precisar de nenhum cálculo de saturação. Já a separação nêutron-densidade em rocha limpa saturada de líquido também varia sistematicamente por litologia (calcário, dolomita e arenito respondem de forma distinta à mesma porosidade real), o que torna a combinação nêutron-densidade também uma ferramenta indireta de identificação litológica quando calibrada com testemunhos ou perfis adicionais.

```
Leitura combinada de perfis (esquemático, profundidade no eixo vertical)

  GR         Resistividade      Nêutron-Densidade
  │              │                  │  │
  baixo→limpo    alta→hidrocarb.   ΝΦ  ρ  (convergem = líquido; ΝΦ << ρ = gás)
  alto→argiloso  baixa→água        │  │
```
A leitura integrada — não perfil a perfil isoladamente — é o que sustenta uma interpretação de formação defensável.

### Testemunhagem: a verdade física contra a qual o perfil é calibrado

Nenhum perfil mede a rocha diretamente — todos inferem uma propriedade física a partir de uma resposta indireta (radioatividade, resistência elétrica, desaceleração de nêutrons, atenuação gama). A **testemunhagem** (*coring*) recupera uma amostra física contínua da formação, cortada por uma coroa especial na broca (testemunho de fundo, ou *conventional core*) ou lateralmente por uma ferramenta de cabo em pontos específicos (*sidewall core*), e enviada a laboratório para medida direta de porosidade, permeabilidade, litologia e, por vezes, saturação residual de fluidos.

O papel do testemunho na avaliação de formações não é substituir o perfil — testemunhar o poço inteiro seria proibitivamente caro e lento — mas **calibrar** os perfis: os parâmetros de Archie (a, m, n), a relação Vsh-IGR e a curva de porosidade por densidade são todos ajustados comparando a previsão do perfil com a medida direta de laboratório num intervalo testemunhado, e essa calibração é então extrapolada ao longo de todo o poço e, com cautela, a poços vizinhos da mesma formação. Um perfil sem nenhuma calibração por testemunho é uma estimativa não verificada; a prática profissional testemunha seletivamente as zonas de maior interesse ou de litologia atípica exatamente para ancorar essa calibração.

## Exemplo trabalhado

**Situação:** um intervalo de arenito registra GR = 25 API (contra GRmin = 20 API numa zona limpa de referência e GRmax = 120 API num folhelho espesso vizinho), densidade da formação ρformação = 2,32 g/cm³ (matriz de quartzo ρmatriz = 2,65 g/cm³, fluido ρfluido = 1,00 g/cm³, água salgada) e nêutron NPHI = 0,21 (21%). A resistividade profunda é Rt = 20 ohm·m e a resistividade da água de formação é Rw = 0,05 ohm·m (água salgada, valor típico de bacia sedimentar profunda). (a) A zona é limpa o suficiente para aplicar a forma de Archie para formação sem correção de argila? (b) Qual porosidade os dois perfis indicam, e há sinal de gás? (c) Usando a = 1, m = 2 e n = 2 (valores padrão de Archie para arenito consolidado, na ausência de calibração local mais específica) e a porosidade obtida em (b), calcule a saturação de água e a saturação de hidrocarboneto dessa zona.

**Resolução:**

(a) Índice de raios gama: IGR = (GR − GRmin) / (GRmax − GRmin) = (25 − 20) / (120 − 20) = 5/100 = 0,05. Um IGR de 0,05 é baixíssimo — mesmo sem aplicar a correção não linear de Larionov (que faria pouca diferença nesse extremo, onde a curva linear e a não linear quase coincidem), a zona é essencialmente limpa (Vsh próximo de zero). Isso justifica usar a forma de Archie para formação limpa, sem termo de correção de argila, no item (c).

(b) Porosidade por densidade: φD = (ρmatriz − ρformação) / (ρmatriz − ρfluido) = (2,65 − 2,32) / (2,65 − 1,00) = 0,33 / 1,65 = 0,20. O nêutron lê NPHI = 0,21, praticamente igual à porosidade por densidade — as duas curvas **convergem**, sem o afastamento característico de gás (*gas crossover*, que exigiria NPHI bem menor que φD). Reconciliando as duas leituras, adota-se φ = 0,20 (20%) para o cálculo de Archie.

(c) Com φ = 0,20:

Sw = [ (a / φᵐ) × (Rw / Rt) ]^(1/n)

Substituindo:
φᵐ = 0,20² = 0,04
a / φᵐ = 1 / 0,04 = 25
Rw / Rt = 0,05 / 20 = 0,0025
(a/φᵐ) × (Rw/Rt) = 25 × 0,0025 = 0,0625

Sw = 0,0625^(1/2) = √0,0625 = 0,25

Sw = 25% → a zona tem 25% de seus poros ocupados por água de formação.

Saturação de hidrocarboneto: Sh = 1 − Sw = 1 − 0,25 = 0,75, ou 75%.

Interpretação: três quartos do espaço poroso dessa zona estão ocupados por hidrocarboneto — um resultado consistente com uma zona de reservatório produtiva, supondo porosidade e espessura suficientes (Aula 03) e permeabilidade que permita o fluxo até o poço (Aula 04). Vale notar a sensibilidade do resultado ao expoente de cimentação m: se a calibração local por testemunho indicasse m = 1,8 em vez de 2 (rocha menos cimentada), φᵐ **subiria** de 0,04 para 0,20^1,8 ≈ 0,055 — porque φ é menor que 1, e reduzir o expoente aproxima a potência de 1. Com isso, a/φᵐ cai de 25 para ≈ 18,1, o produto vira 18,1 × 0,0025 ≈ 0,0453, e Sw cai de 25% para √0,0453 ≈ 0,213, ou ≈ 21%. Ou seja: um m menor **reduz** a saturação de água calculada, e a diferença de 4 pontos percentuais de Sw vinda de uma única constante empírica é um lembrete de que os parâmetros de Archie não são constantes universais, e usá-los sem calibração é uma das fontes mais comuns de erro em estimativas de saturação publicadas sem essa ressalva.

## Erros comuns

- **Usar a relação linear Vsh = IGR sem checar a idade/consolidação da rocha.** Em formações jovens ou não consolidadas, isso superestima sistematicamente o volume de argila — e um Vsh inflado distorce todos os cálculos posteriores de porosidade e saturação que dependem dele.
- **Ler resistividade alta como hidrocarboneto sem checar Vsh e porosidade primeiro.** Uma zona argilosa também pode ter resistividade elevada por outros efeitos; a leitura de resistividade só é indicador confiável de hidrocarboneto numa zona já identificada como limpa e porosa — a ordem de leitura dos perfis (GR → porosidade → resistividade) importa.
- **Aplicar os parâmetros "padrão" de Archie (a=1, m=2, n=2) como se fossem universais.** Como o próprio exemplo trabalhado mostra, uma mudança de m = 2 para m = 1,8 move a saturação de água calculada em vários pontos percentuais — usar valores de tabela sem calibração local por testemunho é a fonte de erro sistemático mais citada em avaliação de formações.
- **Confundir convergência nêutron-densidade com "ausência de hidrocarboneto".** As duas curvas convergem em qualquer rocha limpa saturada de líquido, seja água ou óleo — convergência indica ausência de **gás**, não ausência de hidrocarboneto líquido, que só a resistividade (via Archie) discrimina.

## O que não concluir

- **Que perfil substitui testemunho.** Perfil infere uma propriedade a partir de uma resposta física indireta; sem testemunho para calibrar (Vsh, porosidade, parâmetros de Archie), a estimativa fica sem verificação independente — o papel do testemunho é ancorar a calibração, não ser substituído por ela.
- **Que Sw baixa em qualquer zona implica reservatório produtivo.** Saturação de água baixa diz que o espaço poroso é majoritariamente hidrocarboneto, mas nada diz sobre se há porosidade e espessura suficientes ou permeabilidade que permita o fluxo até o poço — completude do julgamento fica só com a Aula 03 (volumes) e a Aula 04 (produtividade).
- **Que um único perfil (GR, ou nêutron, ou densidade isolado) basta para uma interpretação defensável.** A leitura integrada dos quatro perfis é o que sustenta a interpretação; cada um, isolado, tem uma fraqueza conhecida (o nêutron superestima porosidade em argila; a densidade depende de matriz mineral assumida corretamente).

## Recap relâmpago

- O perfil de raios gama (GR) separa reservatório de folhelho pela radioatividade natural de argilominerais; normalizado como índice de raios gama (IGR) e convertido (de preferência não linearmente) em volume de argila (Vsh), que corrige os demais cálculos.
- A resistividade responde ao fluido dos poros, não à matriz: água salgada conduz bem (resistividade baixa), hidrocarboneto é isolante (resistividade alta) — a leitura profunda (Rt), menos afetada pela invasão de filtrado de lama, representa a formação intacta.
- A equação de Archie (1942), Sw = [(a/φᵐ)(Rw/Rt)]^(1/n), converte porosidade e resistividade em saturação de água; seus parâmetros (a, m, n) são empíricos e precisam de calibração local por testemunho, não valores universais.
- Nêutron e densidade combinados estimam porosidade e, pelo padrão de convergência ou afastamento entre as duas curvas, indicam litologia e, no caso de forte afastamento (nêutron muito mais baixo que densidade), a presença de gás — o efeito de gás (gas crossover).
- A testemunhagem recupera amostra física da formação e serve para calibrar os parâmetros usados nos perfis (Archie, Vsh, porosidade por densidade) — os perfis inferem, o testemunho mede diretamente, e a prática profissional combina os dois.
- Esta aula parte da base de perfil sônico e de densidade já ensinada no Módulo 11 (amarração poço-sísmica) e acrescenta raios gama, resistividade e nêutron como o conjunto padrão de avaliação petrofísica de formações.

## Próxima aula

[[12-engenharia-de-petroleo-aula-03-propriedades-de-reservatorio-e-pvt|Aula 03 — Propriedades de rocha-reservatório e de fluidos (PVT) e cálculo de volumes in place]]

## Anterior

[[12-engenharia-de-petroleo-aula-01-perfuracao-de-pocos|Aula 01 — Perfuração de poços]]

## Fontes

- Archie, G. E. (1942), "The Electrical Resistivity Log as an Aid in Determining Some Reservoir Characteristics", *Transactions of the AIME*, 146(1), p. 54–62 (equação de Archie original).
- Schlumberger (2013), *Log Interpretation Charts*, e *Log Interpretation Principles/Applications*, cap. 3–8 (GR, resistividade, nêutron, densidade).
- Rider, M. & Kennedy, M. (2011), *The Geological Interpretation of Well Logs*, 3ª ed., Rider-French, cap. 4–8 (Vsh, porosidade nêutron-densidade, efeito de gás).
- Ellis, D. V. & Singer, J. M. (2007), *Well Logging for Earth Scientists*, 2ª ed., Springer, cap. 3, 10–12 (testemunhagem e calibração).

<!--
nivel: avancado
palavras_corpo: 2004 (Conteudo ate Exemplo trabalhado, recontagem apos revisao didatica 2026-09-02 - exemplo trabalhado ampliado para demonstrar tambem Vsh via IGR e porosidade via neutron-densidade, DID-M12-A02-EXEMPLO-001)
mapa_objetivo_secao:
  geologia-avancado-m12-oa02: "O que muda em relação ao que o Módulo 11 já ensinou" + "Raios gama: separando reservatório de folhelho" + "Resistividade: o perfil que enxerga o fluido, não a rocha" + "A equação de Archie: de resistividade a saturação de água" + "Nêutron e densidade combinados: porosidade e uma pista de litologia" + "Testemunhagem: a verdade física contra a qual o perfil é calibrado" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: PETRENG-M12-A02-GR-001
    claim: "O perfil de raios gama mede a radioatividade natural da formação (predominantemente potássio, tório e urânio associados a argilominerais), sendo sistematicamente mais alto em folhelhos/argilas que em arenitos limpos e carbonatos; normalizado entre GRmin e GRmax define o índice de raios gama (IGR), convertido em volume de argila (Vsh) preferencialmente por relações não lineares (ex. Larionov) em vez da relação linear direta, que superestima Vsh em rochas menos consolidadas ou mais jovens."
    risk: fato
    source: "Rider & Kennedy 2011, The Geological Interpretation of Well Logs, cap. 4; Schlumberger, Log Interpretation Principles/Applications, cap. 3"
  - claim_id: PETRENG-M12-A02-RESIST-002
    claim: "O perfil de resistividade responde principalmente ao fluido que satura os poros: água de formação salgada tem resistividade baixa (condutora, por conter íons dissolvidos) e óleo/gás têm resistividade alta (isolantes elétricos); a leitura de resistividade profunda (Rt) é a menos afetada pela invasão do filtrado de lama e é a usada para representar a formação intacta nos cálculos de saturação."
    risk: fato
    source: "Schlumberger, Log Interpretation Principles/Applications, cap. 4-5; Ellis & Singer 2007, cap. 5"
  - claim_id: PETRENG-M12-A02-ARCHIE-003
    claim: "A equação de Archie (1942), Sw = [(a/phi^m) x (Rw/Rt)]^(1/n), relaciona a saturação de água (Sw) à porosidade (phi), à resistividade da água de formação (Rw) e à resistividade profunda medida (Rt), por meio de constantes empíricas calibráveis a (fator de tortuosidade, tipicamente ~1), m (expoente de cimentação, tipicamente 1,8-2,2 em arenitos consolidados) e n (expoente de saturação, tipicamente ~2); esses parâmetros exigem calibração local por testemunho e não são universais."
    risk: fato
    source: "Archie 1942, Transactions of the AIME 146(1); Schlumberger, Log Interpretation Principles/Applications, cap. 8"
  - claim_id: PETRENG-M12-A02-NEUTRONDENS-004
    claim: "O perfil de nêutron responde à concentração de hidrogênio ao redor do poço (presente em água e óleo nos poros) e se aproxima da porosidade em rocha limpa saturada de líquido, mas superestima porosidade em zonas argilosas; o perfil de densidade deriva porosidade a partir da densidade eletrônica da formação e da densidade conhecida da matriz mineral e do fluido; forte afastamento entre as curvas de nêutron e densidade (nêutron muito mais baixo que densidade) é indicador direto de gás, conhecido como efeito de gás (gas crossover)."
    risk: fato
    source: "Rider & Kennedy 2011, cap. 6-7; Schlumberger, Log Interpretation Principles/Applications, cap. 6-7"
  - claim_id: PETRENG-M12-A02-TESTEMUNHO-005
    claim: "A testemunhagem (coring) recupera amostra física contínua ou pontual da formação para medida direta em laboratório de porosidade, permeabilidade e litologia, servindo para calibrar os parâmetros usados na interpretação de perfis (parâmetros de Archie, relação Vsh-IGR, porosidade por densidade), em vez de substituir a perfilagem de todo o poço."
    risk: fato
    source: "Ellis & Singer 2007, Well Logging for Earth Scientists, cap. 3, 10-12"
-->
