# Baralho de Flashcards — Módulo 09: Geometalurgia

**Módulo:** 09 — Geometalurgia
**Total de cards:** 72 (54 Basic + 18 Cloze)
**Data de geração:** 2026-08-30
**Baseado em:** Aulas 01–06 auditadas e aprovadas (open_findings: [])

## Notas de uso

- Os cards Basic cobrem conceitos, definições, classificações, relações causa-efeito e vocabulário de processo.
- Os cards Cloze fixam valores numéricos, fórmulas, exemplos trabalhados e cálculos de dimensionamento.
- Os valores numéricos refletem as aulas auditadas (exemplo: Wi de 15 kWh/t para cobre sulfetado, critério de concentração de Taggart, equação de Bond).
- Importar como dois decks no Anki: `09-geometalurgia-flashcards-basic.csv` (tipo Basic) e `09-geometalurgia-flashcards-cloze.csv` (tipo Cloze).

---

## Cards Basic (54 cards)

**Identificação:** geologia-avancado-m09-fb001 a fb054

### Objetivo 01: Conceito e programa geometalúrgico (aulas 01)

- **fb001** — O que é geometalurgia?
  - R: A disciplina que liga a caracterização geológica e mineralógica de um depósito ao desempenho do processamento mineral, medindo e modelando a variabilidade metalúrgica no corpo de minério para reduzir o risco de não alcançar a produção prevista.

- **fb002** — Qual é a diferença entre teor e recuperação?
  - R: Teor é a concentração do metal numa corrente. Recuperação é a fração do metal que entra na planta e sai no concentrado — depende de como o metal está distribuído entre os minerais e de como esses minerais estão arranjados na rocha, não da quantidade de metal.

- **fb003** — Por que a textura é mais importante que o teor para governar a moagem necessária?
  - R: O tamanho de grão dos minerais é uma propriedade textural. A textura fixa o teto de recuperação atingível a uma dada finura de moagem, porque um concentrador só separa bem o que está liberado.

- **fb004** — Qual é a diferença entre variável primária e variável proxy?
  - R: A variável primária (recuperação, energia, capacidade) é cara e existe em poucos pontos; a proxy (teor, dureza, mineralogia) é barata e medida em toda parte.

- **fb005** — Qual é a sequência de operações unitárias do minério até o produto?
  - R: Cominuição (britagem a seco, moagem a úmido) → Concentração (separação física) ou Lixiviação (dissolução química), produzindo concentrado e rejeito.

- **fb006** — O que distingue uma partícula liberada de uma travada?
  - R: Uma partícula liberada tem ≥ 90 % ou ≥ 95 % de um único mineral; abaixo do limiar, é mista ou travada — o mineral-alvo permanece fisicamente preso.

- **fb007** — O que é moabilidade?
  - R: A facilidade com que uma rocha é reduzida de tamanho. Quanto mais dura e tenaz, mais energia por tonelada e menos toneladas por hora numa planta de potência fixa.

- **fb008** — Qual é a regra geral para liberar um mineral?
  - R: Para liberar um mineral, é preciso moer a rocha até um tamanho de partícula igual ou menor que o tamanho de grão desse mineral na rocha.

### Objetivo 02: Mineralogia de processo e análise modal (aula 02)

- **fb009** — O que é partição do metal (deportment)?
  - R: A fração do metal que está em cada mineral portador — em um cobre, quanto está em calcopirita, calcosita, crisocola, óxidos de ferro. Cada mineral tem rota e recuperação própria.

- **fb010** — O que são minerais de ganga problemáticos?
  - R: Aqueles que não são neutros no beneficiamento: carbonatos consomem ácido, pirita consome cal e coletor, talco gera lama, minerais penalizantes (As, F) reduzem o preço.

- **fb011** — O que é a análise modal automatizada por MEV?
  - R: Uma técnica que segmenta uma seção polida pelo brilho de elétrons retroespalhados (BSE) e identifica cada fase por espectrometria de raios X (EDS), classificando-a contra uma biblioteca de minerais.

- **fb012** — O que o MLA, QEMSCAN e TIMA medem?
  - R: Composição modal, partição elementar (deportment), associação mineral, distribuição de tamanho de grão, grau de liberação por classe de tamanho e textura quantitativa.

- **fb013** — Qual é a limitação mais importante da análise modal automatizada?
  - R: O viés estereológico — uma seção 2D corta partículas fora do centro, o corte de uma mista pode atravessar só uma fase, indistinguível de uma genuinamente liberada. A seção 2D superestima a liberação 3D.

- **fb014** — Qual é a resolução espacial típica de análise modal automatizada?
  - R: Cerca de 1 µm; grãos e inclusões submícron ficam mal resolvidos e o travamento fino é subestimado.

### Objetivo 03: Textura, liberação e escolha de P80 (aulas 03–04)

- **fb015** — O que é o P80?
  - R: A abertura de malha pela qual passam 80 % da massa do produto de moagem; é o descritor padrão de finura.

- **fb016** — Qual é o custo-benefício de moer mais fino?
  - R: Mais fino → mais liberação e recuperação. Mas energia cresce (~1/√P80), custo sobe, capacidade cai e aumenta a fração de lamas ultrafinas problemáticas.

- **fb017** — O que é fratura não preferencial?
  - R: A trinca atravessa os grãos sem "enxergar" os contornos — comportamento de maioria dos minérios. A liberação só cresce com redução drástica, obrigando à sobremoagem.

- **fb018** — O que é descolamento ou liberação preferencial?
  - R: A fratura segue os contornos de grão ou fase frágil. Ocorre em parte dos minérios e reduz drasticamente o custo de energia da liberação.

- **fb019** — O que descreve a curva de liberação?
  - R: Mostra o grau de liberação do mineral-alvo em função do tamanho de partícula (P80). É monótona crescente com assíntota abaixo de 100 % — sempre restam travamento fino e inclusões.

- **fb020** — Como se lê corretamente a curva teor-recuperação?
  - R: Andar sobre a curva (reagente, tempo) apenas troca teor por recuperação sem ganho líquido; trocar de curva (moer mais fino) desloca a linha inteira e melhora as duas.

- **fb021** — Qual é o P80 de ótimo econômico?
  - R: Aquele em que o valor do metal marginal recuperado iguala o custo marginal de energia mais perdas por lama. Um minério limitado por liberação só melhora abaixo desse ponto.

- **fb022** — O que é a equação de Bond?
  - R: W = 10 × Wi × (1/√P80 − 1/√F80), com W em kWh/t, P80 e F80 em µm e Wi o Work Index. Vale para F80 de milímetros a P80 de ~50 µm; abaixo disso subestima a energia.

- **fb023** — O que é von Rittinger, Kick e Bond nas leis de cominuição?
  - R: Três "leis" de energia de cominuição: von Rittinger (energia ∝ área, moagem fina), Kick (energia ∝ razão redução, britagem grossa), Bond (intermediária, caso convencional para moinhos).

- **fb024** — O que é Work Index?
  - R: A energia, em kWh/t, para reduzir o material de tamanho teoricamente infinito a 80 % passante em 100 µm. Determinado pelo ensaio de moabilidade de Bond.

- **fb025** — Qual é a faixa de Work Index para minérios de cobre sulfetado?
  - R: Tipicamente 12–15 kWh/t, com maioria de minérios sulfetados nessa faixa conforme compilações de Bond.

- **fb026** — Qual é a diferença entre cominuição por britagem e por moagem?
  - R: Britagem trabalha a seco (razão redução ~3–6), moagem trabalha a úmido em moinhos tubulares (razão maior, eficiência mais alta).

- **fb027** — O que é circuito fechado com classificação por hidrociclone?
  - R: A descarga do moinho é classificada; o underflow (fração grossa) retorna ao moinho; o overflow (fração fina, P80 alvo) segue para concentração. Carga circulante 200–350 %.

- **fb028** — Qual é a diferença entre moinho SAG e moinho de bolas?
  - R: SAG usa o próprio minério grosso como corpo moedor (+ 4–15 % bolas); de bolas usa só bolas de aço. SAG recebe só minério de britagem primária.

### Objetivo 04: Concentração, recuperação e variabilidade (aulas 05–06)

- **fb029** — O que é separação gravítica?
  - R: Explora a diferença de densidade no comportamento das partículas num fluido. A viabilidade se estima pelo critério de concentração CC = (ρ_pesado − ρ_fluido) / (ρ_leve − ρ_fluido).

- **fb030** — Qual é o critério de concentração de Taggart?
  - R: CC > 2,5 até ~75 µm (fácil), 1,75–2,50 até ~150 µm, 1,50–1,75 até ~1,7 mm, 1,25–1,50 até ~6,35 mm, CC < 1,25 inviável.

- **fb031** — O que é LIMS e WHIMS/HGMS?
  - R: LIMS (Low-Intensity Magnetic Separation): tambores ~0,1–0,4 T para magnetita e pirrotita. WHIMS/HGMS: campos 1–2 T para paramagnéticos (hematita, ilmenita).

- **fb032** — O que é hidrofobicidade na flotação?
  - R: Propriedade de uma superfície de repelir água e aderir a bolhas de ar. O coletor (molécula anfifílica) adsorve seletivamente e deixa a cauda apolar exposta.

- **fb033** — Qual é a função de um coletor e do espumante na flotação?
  - R: Coletor: adsorve e torna a superfície hidrofóbica. Espumante: estabiliza bolhas e espuma SEM alterar hidrofobicidade. São funções distintas.

- **fb034** — O que é contato trifásico na flotação?
  - R: Adesão sólido-líquido-gás que se forma quando o filme de água entre bolha e partícula se rompe. A firmeza cresce com ângulo de contato, que o coletor aumenta.

- **fb035** — O que são depressor e ativador na flotação?
  - R: Depressor: torna um mineral hidrofílico (cal deprime pirita). Ativador: prepara a superfície para coletor (sulfato de cobre ativa esfalerita).

- **fb036** — Como varia a recuperação em função do tempo de flotação?
  - R: R(t) = R_∞ (1 − e^(−kt)), com R_∞ recuperação máxima (limitada por liberação) e k constante de taxa (depende de reagente e granulometria).

- **fb037** — Qual é a faixa ideal de tamanho para flotação?
  - R: Entre ~10 µm e ~150–300 µm. Partículas grossas descolam por peso; ultrafinas colidem pouco com bolhas.

- **fb038** — O que é ouro refratário?
  - R: Ouro submicroscópico encapsulado em pirita ou arsenopirita, inacessível ao cianeto sem oxidação. É diagnóstico de mineralogia de processo com forte impacto no fluxograma.

- **fb039** — Qual é a diferença entre lixiviação em pilha e em tanque?
  - R: Em pilha: minério britado empilhado, solução por gotejamento, barata, baixo teor. Em tanque: minério moído, teores maiores, cinética rápida, cara.

- **fb040** — O que é lixiviação sob pressão (autoclave) e biolixiviação?
  - R: Autoclave: temperatura e pressão alta para oxidar sulfetos (níquel, ouro refratário). Biolixiviação: micro-organismos acidófilos para acelerar oxidação.

- **fb041** — O que é a fórmula de dois produtos?
  - R: R = [c × (f − t)] / [f × (c − t)] × 100 %, usada para fechar balanço metalúrgico medindo só os três teores (f alimentação, c concentrado, t rejeito) sem pesar vazões.

- **fb042** — Qual é a razão de enriquecimento e a razão de concentração?
  - R: Enriquecimento: c / f (quantas vezes concentrado é mais rico). Concentração: (c − t) / (f − t) ou F/C (toneladas minério por tonelada concentrado).

- **fb043** — O que é um domínio geometalúrgico?
  - R: Um volume do depósito que responde de forma homogênea no processo (recuperação, moabilidade, reagente), definido cruzando controles geológicos com resposta metalúrgica medida.

- **fb044** — Qual é a diferença entre domínio geológico e domínio geometalúrgico?
  - R: O domínio geológico não é automaticamente geometalúrgico. Uma mesma litologia pode ter duas respostas; duas litologias podem ter a mesma resposta. A validação é pelos dados de processo.

- **fb045** — O que são variáveis aditivas e não aditivas?
  - R: Teor é aditivo — média ponderada funciona. Work Index e recuperação NÃO são aditivos — blendar não produz comportamento da média.

- **fb046** — Por que não se pode krigar recuperação ou Work Index diretamente?
  - R: Porque não são aditivos — a média ponderada não funciona. Modela-se a partir de proxies aditivas (composição elementar, mineralogia modal) ou usa-se simulação não linear.

- **fb047** — Qual é a estratégia da modelagem geometalúrgica?
  - R: Construir uma relação entre proxies densas (baratas, medidas em todos os furos) e variáveis primárias esparsas (caras, poucos pontos), e propagar essa relação a todos os blocos do modelo.

- **fb048** — Qual é a preferência ao escolher proxies para modelar?
  - R: Preferir proxies fisicamente ligadas à causa. A razão de solubilidade prevê recuperação porque mede a fração não sulfetada; a dureza prevê Wi porque é a mesma propriedade.

- **fb049** — O que é o modelo geometalúrgico de blocos?
  - R: Cada bloco recebe atributos metalúrgicos: recuperação, energia de moagem/Wi, capacidade, consumo de reagente. Daí saem receita, custo e ritmo.

- **fb050** — O que acontece quando se ignora a variabilidade metalúrgica?
  - R: O VPL fica enviesado para cima e o risco subestimado. A planta é dimensionada para minério médio, e o minério de pior recuperação costuma estar no início da lavra.

- **fb051** — O que é o programa geometalúrgico?
  - R: A campanha planejada de amostragem e ensaios que alimenta o modelo: muitos testes de bancada (baratos, rápidos, mapeiam) e poucos testes de piloto (caros, calibram).

- **fb052** — Qual é a cobertura espacial apropriada para o programa geometalúrgico?
  - R: Cobrir a variabilidade estratificadamente: todas as litologias, estágios de alteração, zona oxidada e sulfeto primário, baixo e alto teor, profundidades diferentes.

- **fb053** — Qual é o fator mais importante para intervenção (redução de variabilidade)?
  - R: O mapeamento geometalúrgico com estratificação por domínio, amostragem representativa de todos os domínios, não só do minério de melhor teor.

- **fb054** — O que é "minério médio" no contexto da geometalurgia?
  - R: Uma ficção — a planta processa o minério que a sequência de lavra entrega a cada trimestre, não a média da vida da mina. Por isso a variabilidade mata o projeto.

---

## Cards Cloze (18 cards)

**Identificação:** geologia-avancado-m09-fc001 a fc018

### Valores, fórmulas e exemplos numéricos (aulas 01–06)

- **fc001** — Em um minério de cobre com teor f = 1,00 % Cu, se o bloco A tem R_A = 91 % e o bloco B tem R_B = 63 %, a diferença em metal recuperável por 10 000 t é {{c1::28 toneladas de Cu}}.
  
- **fc002** — Num programa geometalúrgico, a relação de número entre testes de bancada e testes de piloto é {{c1::muitos para poucos}}, refletindo a lógica de mapear a variabilidade com testes baratos e calibrar com testes caros.

- **fc003** — Na curva teor-recuperação, andar sobre a curva mudando {{c1::reagente, tempo, estágios de limpeza}} apenas troca teor por recuperação sem ganho líquido.

- **fc004** — O P80 é a abertura de malha pela qual passam {{c1::80 %}} da massa do produto de moagem.

- **fc005** — Na equação de Bond, a energia é proporcional a {{c1::1/√P80}}, o que significa que reduzir P80 de 106 µm para 75 µm custa {{c1::~21 %}} mais energia.

- **fc006** — Um minério com {{c1::disseminação grossa}} libera com moagem moderada, enquanto {{c1::disseminação fina}} exige moagem {{c1::fina a ultrafina}}.

- **fc007** — A liberação preferencial ocorre quando a fratura segue {{c1::os contornos de grão}} ou uma {{c1::fase frágil ou clivável}}, reduzindo drasticamente o custo de energia.

- **fc008** — A curva de liberação é {{c1::monótona crescente}} com {{c1::assíntota abaixo de 100 %}}, porque sempre restam {{c1::travamento fino e inclusões}}.

- **fc009** — Um moinho de bolas opera em circuito fechado com {{c1::hidrociclone}}, com {{c1::carga circulante}} de {{c1::200–350 %}}.

- **fc010** — A resolução espacial típica de análise modal automatizada por MEV é de {{c1::~1 µm}}, o que significa que {{c1::grãos e inclusões submícron}} ficam mal resolvidos.

- **fc011** — No exemplo da Aula 02 sobre partição de cobre, o cobre total é {{c1::1,025 %}} distribuído como calcopirita {{c1::74,2 %}}, calcosita {{c1::14,0 %}}, crisocola {{c1::8,8 %}}, óxidos {{c1::2,9 %}}.

- **fc012** — A recuperação máxima teórica por flotação de sulfetos no mesmo exemplo é {{c1::~83,8 %}}}, porque o cobre em crisocola e óxidos fica {{c1::invisível}}.

- **fc013** — No exemplo da Aula 04 com F80 = 9 000 µm, P80 = 106 µm e Wi = 15,0 kWh/t, a energia específica de moagem é {{c1::~13,0 kWh/t}}.

- **fc014** — Se o P80 baixar de 106 µm para 75 µm no mesmo minério, a energia sobe para {{c1::~15,7 kWh/t}}}, um aumento de {{c1::~21 %}}.

- **fc015** — No exemplo da Aula 05, com f = 0,85 % Cu, c = 27,5 % Cu, t = 0,072 % Cu, a recuperação é {{c1::~91,8 %}} e a razão de concentração é {{c1::~35,3}} t de minério por tonelada de concentrado.

- **fc016** — Se o rejeito baixar de 0,072 % Cu para 0,050 % Cu, a recuperação sobe para {{c1::~94,3 %}}, um ganho de {{c1::~2,5 pontos}}.

- **fc017** — No exemplo da Aula 06, processando dois domínios (A: 60 Mt, 0,80 % Cu, 90 % R; B: 15 Mt, 0,70 % Cu, 62 % R), o cobre recuperável real é {{c1::0,4971 Mt}}, enquanto uma recuperação única de 88 % prevê {{c1::0,5148 Mt}}, uma superestimativa de {{c1::~US$ 150 milhões}}.

- **fc018** — No domínio B do exemplo, uma planta que processava 20 Mt/ano do minério A (Wi 15,5) processa {{c1::~16,3 Mt/ano}} do minério B (Wi 19,0), um atraso de {{c1::~dois meses}} para os 15 Mt totais, reduzindo o VPL.

---

## Cobertura de objetivos de aprendizagem

- **geologia-avancado-m09-oa01** (Definir geometalurgia): fb001–fb008, fc001–fc003
- **geologia-avancado-m09-oa02** (Análise modal): fb009–fb014, fc011–fc012
- **geologia-avancado-m09-oa03** (Liberação e P80): fb015–fb028, fc004–fc010, fc013–fc014
- **geologia-avancado-m09-oa04** (Variabilidade e VPL): fb029–fb054, fc015–fc018

---

## Validação e importação

- Todos os cards foram gerados com base nas aulas auditadas (sem achados vermelhos em aberto).
- IDs seguem a numeração sequencial: fb001–fb054 (Basic) e fc001–fc018 (Cloze).
- Formato CSV compatível com Anki (sem cabeçalho, separador `;`, notação Cloze `{{c1::}}`).
- Valores numéricos validados contra os exemplos trabalhados das aulas (recuperação Aula 01, partição Aula 02, liberação Aula 03, energia Bond Aula 04, balanço metalúrgico Aula 05, domínios Aula 06).
