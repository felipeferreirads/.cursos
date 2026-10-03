# Aula 03: Cartas derivadas e interpretativas: aptidão física ao assentamento urbano, suscetibilidade e risco

**ID:** geologia-avancado-m07-a03
**Módulo:** [[07-mapeamento-geotecnico-modulo|Módulo 07 — Metodologia de mapeamento geotécnico]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** distinguir rigorosamente carta geotécnica, carta de suscetibilidade, carta de perigo e carta de risco quanto a objetivo, conteúdo e conclusão que autorizam; e elaborar cartas derivadas a partir das cartas básicas pelos métodos heurístico, estatístico e determinístico, validando o resultado.

**Pré-requisito:** Aulas 01 e 02 deste módulo (escalas, atributos, cartas básicas); resistência ao cisalhamento e tensões efetivas do Módulo 06 (Aulas 03 e 06), usados diretamente no método determinístico.

## Antes de começar, você precisa saber

- Que as cartas básicas (Aula 02) registram um atributo cada, e que as derivadas as combinam segundo um modelo de comportamento.
- O critério de Mohr-Coulomb em tensões efetivas, τf = c' + σ'n·tan φ', e o efeito da poropressão sobre σ' (Módulo 06, Aulas 03 e 06).

## Conteúdo

### A cadeia conceitual: suscetibilidade, perigo, risco

Os três termos são usados como sinônimos na linguagem corrente e designam coisas rigorosamente diferentes na técnica. Confundi-los é o erro conceitual mais grave desta área, porque cada um autoriza uma conclusão distinta e envolve responsabilidades distintas.

- **Suscetibilidade:** a **predisposição** do terreno a um processo, dada por suas características físicas permanentes ou de lenta variação — declividade, material, estrutura, forma da vertente. Responde a *onde* o processo pode ocorrer. É **espacial e atemporal**: não diz quando, nem com que frequência.
- **Perigo (*hazard*):** a **probabilidade de ocorrência** de um processo de determinada magnitude, num determinado local, dentro de um período de referência. Acrescenta à suscetibilidade a dimensão **temporal** e a de **magnitude**. Responde a *onde, com que intensidade e com que frequência*.
- **Risco:** as **consequências esperadas** — perdas de vidas, danos materiais, interrupção de serviços — resultantes do perigo atuando sobre elementos expostos e vulneráveis. Introduz a dimensão **social e econômica**. Responde a *o que se perde*.

A formulação consagrada, seguindo Varnes (1984) e a terminologia consolidada pela UNDRR, é:

**Risco = Perigo × Exposição × Vulnerabilidade**

A consequência prática é decisiva: **uma encosta muito suscetível e desocupada tem risco nulo** — não há nada a perder ali. E uma encosta de suscetibilidade moderada densamente ocupada por edificações precárias pode ter risco altíssimo. Suscetibilidade é atributo do terreno; risco é atributo da relação entre terreno e ocupação. Uma carta de suscetibilidade **não** pode ser apresentada como carta de risco, e a inversa também não vale.

> [!important] Por que essa distinção não é preciosismo terminológico
> Uma carta de suscetibilidade classifica terreno e orienta planejamento — onde não expandir, onde exigir estudo. Uma carta de risco classifica **situações concretas com pessoas dentro** e fundamenta decisões de remoção, obra de contenção e alerta. Confundi-las produz dois erros simétricos e igualmente graves: tratar alta suscetibilidade em área vazia como emergência (desperdiçando recurso escasso) ou tratar suscetibilidade média em favela consolidada como situação tranquila (deixando de agir onde há vidas expostas).

### Carta de aptidão física ao assentamento urbano

É a carta derivada de uso mais direto no planejamento territorial. Ela responde: **este terreno serve para ser urbanizado, e sob que condições?** Combina as cartas básicas em classes tipicamente de três a cinco níveis:

- **Apta:** ocupação sem restrições geotécnicas relevantes; as obras convencionais bastam.
- **Apta com restrição** (frequentemente subdividida em graus): ocupação possível mediante exigências específicas — projeto de drenagem, contenção, limitação de corte e aterro, densidade máxima, investigação prévia obrigatória.
- **Inapta:** ocupação desaconselhada ou vedada, por restrição técnica (instabilidade, inundação recorrente, colapsividade severa, cavidade) ou legal (APP, faixas de proteção).

O ponto metodológico central é que **as restrições precisam ser nomeadas**, não apenas graduadas. "Apta com restrição" sem dizer qual restrição não orienta decisão nenhuma: o gestor não sabe se deve exigir contenção, drenagem, ou proibir corte. A legenda deve associar a cada classe o **fator limitante** e a **medida requerida**.

No Brasil, esse produto ganhou estatuto legal com a **Lei 12.608/2012**, que instituiu a Política Nacional de Proteção e Defesa Civil e, alterando o Estatuto da Cidade (Lei 10.257/2001), passou a exigir dos municípios inscritos no cadastro nacional de municípios com áreas suscetíveis a desastres o mapeamento das áreas suscetíveis e a elaboração de **carta geotécnica de aptidão à urbanização** como condição para ampliação do perímetro urbano.

> [!warning] Legislação muda; verifique o texto consolidado
> Os dispositivos citados foram alterados por leis posteriores (entre elas a Lei 14.285/2021), e a redação vigente pode diferir da original de 2012 em detalhes de aplicação. Trate as referências legais desta aula como o **enquadramento** do instrumento — que é estável —, e sempre confirme a redação atual antes de fundamentar um parecer técnico nela.

### Como se produz uma carta de suscetibilidade: três famílias de método

**1. Heurística (por conhecimento especialista).** O analista atribui pesos aos fatores condicionantes (declividade, material, forma de vertente, uso) e os combina por sobreposição ponderada em SIG. Transparente e aplicável mesmo com poucos dados de inventário, mas os pesos são subjetivos — daí o uso frequente de métodos de estruturação da decisão, como o AHP (*Analytic Hierarchy Process*), para tornar a atribuição de pesos explícita, comparável e auditável.

**2. Estatística (baseada em inventário).** Parte de um **inventário de ocorrências** (as cicatrizes mapeadas na Aula 02) e mede estatisticamente a associação entre a ocorrência do processo e cada classe de cada fator. Métodos usuais: razão de frequência, *weights of evidence*, regressão logística e, mais recentemente, algoritmos de aprendizado de máquina (florestas aleatórias, gradient boosting). É reprodutível e calibrado por dado real, mas **depende inteiramente da qualidade e da completude do inventário** — e herda seus vieses. Se as cicatrizes foram mapeadas apenas onde havia imagem de boa resolução ou acesso, o modelo aprende a geografia do mapeamento, não a do processo.

**3. Determinística (baseada em física).** Aplica um modelo mecânico célula a célula, calculando um fator de segurança. Para escorregamentos translacionais rasos — o processo dominante em encostas tropicais —, usa-se o **modelo de talude infinito**, em que a superfície de ruptura é plana e paralela à encosta, a uma profundidade z:

FS = [c' + (γ·z·cos²β − u)·tan φ'] / (γ·z·sen β·cos β)

onde β é a inclinação da encosta. Com fluxo paralelo à encosta e nível d'água na superfície, u = γw·z·cos²β. É o método que fornece a ligação mais direta com o Módulo 06: **cada termo da fórmula é um parâmetro daquele módulo**, espacializado. Sua limitação é justamente essa exigência: requer c', φ', γ, z e o regime de poropressão em toda a área, dados que raramente existem com essa densidade — motivo pelo qual o método é aplicado tipicamente com valores por unidade geotécnica e análise de sensibilidade, não com um valor por célula.

Quando o modelo determinístico é acoplado a um modelo hidrológico que simula a resposta da poropressão à chuva, ele deixa de produzir suscetibilidade e passa a produzir **perigo** — porque incorpora a probabilidade temporal associada ao regime de chuvas. É a transição formal de um conceito ao outro.

### Da suscetibilidade ao risco: o que falta acrescentar

Para converter suscetibilidade em risco, três camadas adicionais são necessárias, e nenhuma delas é geológica:

- **Exposição:** o que está lá — edificações, população, infraestrutura, serviços. Vem de cadastro, censo e imagem.
- **Vulnerabilidade:** quão suscetível ao dano é o que está exposto. Inclui a tipologia construtiva (alvenaria estrutural versus autoconstrução em talude cortado), a capacidade de resposta e a condição socioeconômica, que determina a possibilidade de evacuar e de se recuperar.
- **Magnitude esperada** do processo, que define a área de alcance e a intensidade do dano.

No Brasil, o instrumento operacional dessa camada é a **setorização de risco**, executada em grande detalhe (Aula 01) e apoiada na metodologia do Ministério das Cidades/IPT, que classifica setores em quatro graus — **R1 baixo, R2 médio, R3 alto e R4 muito alto** —, com base numa avaliação de campo que integra evidências de instabilidade, condicionantes geológico-geotécnicos e características da ocupação. É uma avaliação **por setor e por moradia**, não por polígono de terreno — a diferença de granularidade que separa risco de suscetibilidade.

### Validação: a etapa mais frequentemente omitida

Uma carta de suscetibilidade produz classes; nada garante que elas correspondam à realidade. A validação compara o mapa a um inventário de ocorrências **não usado** na sua construção:

- **Curva de sucesso** (*success rate*): usa o mesmo inventário do ajuste. Mede o quanto o modelo se ajustou aos dados — não o quanto ele prevê.
- **Curva de predição** (*prediction rate*): usa um inventário independente, tipicamente uma partição temporal (eventos posteriores) ou espacial. É a validação que de fato importa.
- A área sob a curva (**AUC**) resume o desempenho: 0,5 equivale a acaso, e valores acima de ~0,8 são usualmente considerados bons na literatura de suscetibilidade a escorregamentos.

Uma carta de suscetibilidade sem validação declarada não deve ser usada para fundamentar restrição de uso — é uma hipótese cartografada.

## Exemplo trabalhado

**Situação:** uma encosta tem 2 m de colúvio sobre solo residual, com contato basal paralelo à superfície. Do Módulo 06 obteve-se, para o colúvio: γsat = 19 kN/m³, c' = 5 kPa, φ' = 30°. A inclinação local é β = 25°. Calcule o fator de segurança pelo modelo de talude infinito (a) na condição seca, sem poropressão, e (b) na condição saturada, com fluxo paralelo à encosta e nível d'água na superfície. Use γw = 9,81 kN/m³.

**Resolução:**

Termos geométricos comuns (β = 25°): cos β = 0,9063, cos²β = 0,8214, sen β = 0,4226.

**Força motriz** (denominador, igual nos dois casos):
γ·z·sen β·cos β = 19 × 2 × 0,4226 × 0,9063 = 38 × 0,3830 = **14,55 kPa**

**Tensão normal total na superfície de ruptura:**
γ·z·cos²β = 38 × 0,8214 = **31,21 kPa**

**(a) Condição seca (u = 0):**
Resistência = c' + σ'n·tan φ' = 5 + (31,21 × 0,5774) = 5 + 18,02 = 23,02 kPa
**FS = 23,02 / 14,55 = 1,58**

**(b) Condição saturada, fluxo paralelo à encosta:**
u = γw·z·cos²β = 9,81 × 2 × 0,8214 = **16,12 kPa**
σ'n = 31,21 − 16,12 = **15,09 kPa**
Resistência = 5 + (15,09 × 0,5774) = 5 + 8,72 = 13,72 kPa
**FS = 13,72 / 14,55 = 0,94**

**Interpretação:** o mesmo talude, com a mesma geometria, os mesmos materiais e o mesmo peso, passa de estável com folga (FS = 1,58) a instável (FS = 0,94) apenas pela elevação do nível d'água. É a demonstração quantitativa do mecanismo apresentado no Módulo 06, Aula 03: a chuva não adicionou peso relevante — elevou u, reduziu σ'n de 31,2 para 15,1 kPa e derrubou a parcela friccional da resistência pela metade.

Três leituras cartográficas seguem daí. Primeira, **a suscetibilidade dessa encosta é alta**, porque existe uma condição hidrológica plausível que a leva à ruptura. Segunda, o resultado **não é ainda um perigo**: para isso seria preciso saber com que frequência a chuva satura o colúvio até a superfície — o que exige acoplar um modelo hidrológico e o regime pluviométrico local. Terceira, **não é ainda um risco**: se a encosta estiver desocupada e não houver nada a jusante no alcance de uma eventual corrida, o risco é nulo, por mais desfavorável que seja o FS. Se houver moradias no sopé, a mesma encosta entra em setorização de risco, provavelmente em grau alto.

Note também a sensibilidade ao parâmetro mais frágil: o c' de 5 kPa contribui com 5 dos 13,7 kPa de resistência no caso saturado — mais de um terço. Pelo alerta do Módulo 06, Aula 06, c' é um intercepto de extrapolação, especialmente incerto em tensões baixas como as desta análise (σ'n de apenas 15 kPa). Adotar c' = 0 por segurança levaria FS a 8,72/14,55 = 0,60, um resultado bem mais desfavorável — motivo pelo qual a análise de sensibilidade sobre c' é obrigatória em talude raso, e não um refinamento opcional.

## Erros comuns

- **Rotular uma carta de suscetibilidade como carta de risco**, o erro conceitual mais grave e mais frequente da área, com consequências diretas sobre decisões de remoção e alocação de recursos.
- **Concluir risco alto a partir de suscetibilidade alta em área desocupada** — sem exposição não há risco, por definição.
- **Aplicar método estatístico sobre inventário incompleto ou enviesado**, fazendo o modelo aprender a geografia do mapeamento em vez da geografia do processo.
- **Usar o modelo de talude infinito onde a hipótese não vale** — ele descreve rupturas planares rasas com superfície paralela à encosta, e não rupturas rotacionais profundas ou controladas por estrutura da rocha.
- **Aplicar o modelo determinístico célula a célula com parâmetros que só existem por unidade**, produzindo um mapa de FS com aparência de detalhe e sem base de dados correspondente.
- **Publicar carta de suscetibilidade sem validação**, ou apresentar a curva de sucesso (ajuste) como se fosse curva de predição.
- **Classificar "apta com restrição" sem nomear a restrição**, entregando ao gestor uma gradação que não orienta ação.

## O que não concluir

- **Que FS < 1 significa ruptura iminente.** O FS calculado corresponde a uma condição hipotética assumida (aqui, saturação completa). Ele indica que existe um cenário plausível de ruptura, não que ele esteja ocorrendo — e o resultado é tão bom quanto os parâmetros e as hipóteses que o alimentam.
- **Que uma carta de suscetibilidade autoriza remoção de moradias.** Ela orienta planejamento e indica onde investigar. Decisões sobre pessoas exigem avaliação de risco em grande detalhe, com vistoria por setor e por moradia.
- **Que AUC alta significa carta correta.** Um AUC alto obtido sobre o mesmo inventário do ajuste mede sobretudo o ajuste. Só validação com inventário independente sustenta a afirmação de capacidade preditiva.
- **Que "inapta" significa impossível de ocupar.** Significa que a ocupação convencional é desaconselhada nas condições avaliadas; obras de engenharia podem alterar o quadro, ao custo de investimento e manutenção permanentes — e essa é uma decisão de política pública, não uma conclusão geológica.

## Recap relâmpago

- **Suscetibilidade** (onde, atributo do terreno, atemporal) → **perigo** (onde, com que magnitude e frequência, acrescenta tempo) → **risco** (o que se perde, acrescenta exposição e vulnerabilidade). Risco = Perigo × Exposição × Vulnerabilidade — encosta suscetível e **desocupada tem risco nulo**.
- A **carta de aptidão à urbanização** classifica em apta, apta com restrição e inapta, e deve **nomear a restrição e a medida requerida**, não apenas graduar. No Brasil ganhou estatuto legal com a Lei 12.608/2012, que alterou o Estatuto da Cidade.
- Três famílias de método para suscetibilidade: **heurística** (pesos por especialista, frequentemente via AHP), **estatística** (inventário de cicatrizes, razão de frequência, regressão logística, aprendizado de máquina) e **determinística** (modelo físico com fator de segurança).
- O **modelo de talude infinito**, FS = [c' + (γ·z·cos²β − u)·tan φ']/(γ·z·sen β·cos β), é a ponte direta com o Módulo 06 — cada termo é um parâmetro daquele módulo, espacializado. Acoplado a modelo hidrológico, ele produz **perigo**, não mais suscetibilidade.
- Converter suscetibilidade em risco exige três camadas não geológicas: **exposição**, **vulnerabilidade** e magnitude esperada. No Brasil, o instrumento é a **setorização de risco** em graus R1 a R4, avaliada por setor e por moradia.
- **Validação** é obrigatória: curva de predição sobre inventário independente (não a curva de sucesso), resumida pelo AUC. Carta sem validação declarada é hipótese cartografada.

## Próxima aula

[[07-mapeamento-geotecnico-aula-04-sig-sensoriamento-remoto-analise-de-risco|Aula 04 — SIG, imagens de satélite e análise de risco aplicados ao planejamento urbano]]

## Anterior

[[07-mapeamento-geotecnico-aula-02-cartas-basicas-materiais-substrato-declividade|Aula 02 — Cartas básicas: materiais inconsolidados, substrato rochoso, declividade e feições do terreno]]

## Fontes

- Distinção entre suscetibilidade, perigo e risco e zoneamento de perigo a escorregamentos: Varnes, D. J. & IAEG Commission on Landslides (1984), *Landslide Hazard Zonation: A Review of Principles and Practice*, UNESCO, Paris; Fell, R. et al. (2008), "Guidelines for landslide susceptibility, hazard and risk zoning for land use planning", *Engineering Geology*, 102(3–4), p. 85–98.
- Terminologia de risco de desastres: UNDRR — United Nations Office for Disaster Risk Reduction, *Terminology on Disaster Risk Reduction* (ed. corrente).
- Cartas de aptidão e cartografia geotécnica aplicada ao planejamento: Zuquette, L. V. & Gandolfi, N. (2004), *Cartografia Geotécnica*, Oficina de Textos, São Paulo.
- Política Nacional de Proteção e Defesa Civil e exigência de carta geotécnica de aptidão à urbanização: Brasil, Lei nº 12.608, de 10 de abril de 2012, que alterou a Lei nº 10.257/2001 (Estatuto da Cidade) e a Lei nº 6.766/1979 — consultar texto consolidado vigente, considerando alterações posteriores.
- Setorização e graus de risco R1–R4: Ministério das Cidades / IPT (2007), *Mapeamento de Riscos em Encostas e Margem de Rios*, Brasília.
- Modelo de talude infinito: Skempton, A. W. & DeLory, F. A. (1957), "Stability of natural slopes in London Clay", *Proceedings of the 4th International Conference on Soil Mechanics and Foundation Engineering*, Londres, v. 2, p. 378–381; formulação em Duncan, J. M., Wright, S. G. & Brandon, T. L. (2014), *Soil Strength and Slope Stability*, 2ª ed., Wiley.
- Métodos estatísticos e validação de mapas de suscetibilidade: Chung, C.-J. F. & Fabbri, A. G. (2003), "Validation of spatial prediction models for landslide hazard mapping", *Natural Hazards*, 30(3), p. 451–472.

<!--
nivel: avancado
palavras_corpo: ~2350

mapa_objetivo_secao:
  geologia-avancado-m07-oa01: "A cadeia conceitual: suscetibilidade, perigo, risco" + "Carta de aptidão física ao assentamento urbano" + "Da suscetibilidade ao risco: o que falta acrescentar"
  geologia-avancado-m07-oa03: "Como se produz uma carta de suscetibilidade: três famílias de método" + "Validação: a etapa mais frequentemente omitida" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: CARTGEO-M07-A03-CADEIA-001
    claim: "Suscetibilidade é a predisposição espacial e atemporal do terreno a um processo; perigo acrescenta probabilidade temporal e magnitude; risco acrescenta exposição e vulnerabilidade, na forma Risco = Perigo × Exposição × Vulnerabilidade. Encosta suscetível e desocupada tem risco nulo."
    risk: fato
    source: "Varnes 1984; Fell et al. 2008; UNDRR terminology"
  - claim_id: CARTGEO-M07-A03-APTIDAO-002
    claim: "A carta de aptidão física ao assentamento urbano classifica o terreno em apta, apta com restrição e inapta, devendo nomear o fator limitante e a medida requerida de cada classe, não apenas graduá-las."
    risk: fato
    source: "Zuquette & Gandolfi 2004"
  - claim_id: CARTGEO-M07-A03-LEI12608-003
    claim: "A Lei 12.608/2012 instituiu a Política Nacional de Proteção e Defesa Civil e, alterando o Estatuto da Cidade (Lei 10.257/2001), passou a exigir dos municípios inscritos no cadastro nacional de municípios com áreas suscetíveis o mapeamento dessas áreas e a carta geotécnica de aptidão à urbanização como condição para ampliação do perímetro urbano."
    risk: fato
    source: "Brasil, Lei nº 12.608/2012 — verificar texto consolidado, alterado por leis posteriores (entre elas a Lei 14.285/2021)"
  - claim_id: CARTGEO-M07-A03-METODOS-004
    claim: "Cartas de suscetibilidade são produzidas por métodos heurísticos (pesos por especialista, frequentemente estruturados por AHP), estatísticos (inventário de ocorrências, razão de frequência, weights of evidence, regressão logística, aprendizado de máquina) e determinísticos (modelo físico com fator de segurança)."
    risk: fato
    source: "Fell et al. 2008; Zuquette & Gandolfi 2004"
  - claim_id: CARTGEO-M07-A03-TALUDEINF-005
    claim: "No modelo de talude infinito, FS = [c' + (γ·z·cos²β − u)·tan φ']/(γ·z·sen β·cos β), e com fluxo paralelo à encosta e nível d'água na superfície u = γw·z·cos²β. Ele descreve rupturas planares rasas paralelas à encosta, não rupturas rotacionais profundas."
    risk: fato
    source: "Skempton & DeLory 1957; Duncan, Wright & Brandon 2014"
  - claim_id: CARTGEO-M07-A03-PERIGO-006
    claim: "Acoplar o modelo determinístico a um modelo hidrológico que simule a resposta da poropressão à chuva converte o produto de suscetibilidade em perigo, por incorporar a probabilidade temporal."
    risk: fato
    source: "Fell et al. 2008"
  - claim_id: CARTGEO-M07-A03-SETORIZACAO-007
    claim: "No Brasil, a setorização de risco segue a metodologia do Ministério das Cidades/IPT, com quatro graus — R1 baixo, R2 médio, R3 alto e R4 muito alto — avaliados por setor e por moradia em campo."
    risk: fato
    source: "Ministério das Cidades / IPT 2007"
  - claim_id: CARTGEO-M07-A03-VALIDACAO-008
    claim: "A validação de carta de suscetibilidade distingue curva de sucesso (mesmo inventário do ajuste, mede ajuste) de curva de predição (inventário independente, mede capacidade preditiva), resumidas pelo AUC, em que 0,5 equivale ao acaso."
    risk: fato
    source: "Chung & Fabbri 2003"
-->
