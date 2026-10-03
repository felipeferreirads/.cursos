# Auditoria científica — Módulo 16: Introdução à aerogeofísica

**Data:** 2026-09-09
**Modo:** `audit-and-fix` (correções aplicadas cirurgicamente no texto)
**Escopo:** as 5 aulas do módulo, em conjunto, mais o hub do módulo
**Veredito:** **aprovado** — 0 achados vermelhos, 0 achados laranjas em aberto. Gate liberado para questionário e flashcards.

## Contagem por severidade

| Severidade | Contagem |
|---|---|
| 🔴 Vermelho (erro que inverte o sentido ou induz decisão errada) | **0** |
| 🟠 Laranja (erro factual/procedimental que precisa de correção antes de material derivado) | **6** |
| 🟡 Amarelo (impreciso, mal atribuído, faixa larga demais, citação defeituosa) | **16** |
| 🔵 Azul (verificado e correto — registro de que foi checado) | **5** |
| ⚪ Branco (questão em aberto na literatura, mantida com ressalva) | **1** |

**Alegações rastreadas:** as 29 `alegacoes_auditaveis` declaradas pelas aulas (6 na a01, 7 na a02, 5 na a03, 5 na a04, 6 na a05) foram reverificadas uma a uma; a auditoria levantou mais 13 fora da lista do autor, chegando a 42 alegações rastreadas. **Cinco dos seis achados laranjas estão nesse segundo grupo** — ou seja, o autor não havia sinalizado como arriscado aquilo que de fato estava errado.

**Aritmética:** todos os quatro exemplos trabalhados numéricos foram recalculados do zero e **todos fecham exatamente**. TMI residual da a02: 45.410 − 38 − 45.210 = +162 nT ✔. Conversão de gradiente da a03: 18 Eo × 0,1 mGal/km = 1,8 mGal/km × 0,4 km = 0,72 mGal ✔. Razões Th/U da a04: 16,5/4,2 = 3,93 e 14,8/1,1 = 13,45 ✔. Skin depth da a05: 503 × √0,05 = 112,5 m e 503 × √33,33 = 2.904 m ✔. **O único defeito num exemplo trabalhado não foi de conta, foi de grandeza física** (achado A03-F1).

**Unidades (verificação independente por derivação, não por citação):**
- mGal = 10⁻⁵ m/s² ✔ (Gal = 1 cm/s² = 10⁻² m/s²)
- Eötvös = 10⁻⁹ s⁻² ✔
- **1 Eo = 0,1 mGal/km ✔ confirmado por conversão direta**: 0,1 mGal/km = 10⁻⁶ m/s² ÷ 10³ m = 10⁻⁹ s⁻². A conversão que a tarefa pediu para confirmar está correta na aula.
- δ ≈ 503 √(ρ/f) ✔ confirmado por derivação: δ = √(2ρ/ωμ₀) = √(ρ/f) · √(1/(2π²×10⁻⁷)) = 503,3 √(ρ/f), com ρ em Ω·m e f em Hz.

## Padrão dominante

**ORDEM E DIREÇÃO — a sequência ou a direção de uma operação trocada, com a física por trás dela correta.** Quatro dos seis laranjas têm a mesma forma: a aula descreve corretamente **o que** cada etapa faz e erra **em que ordem** ela entra ou **em que direção** ela se aplica.

1. O stripping posto **depois** da correção de altura, quando a sequência padrão IAEA/Minty o põe **antes** (a04).
2. Um gradiente **vertical** multiplicado por uma distância **horizontal** (a03).
3. O espaçamento de linha dimensionado pela **profundidade** em vez da **distância sensor-fonte** — na alegação de metadados, contradizendo o próprio corpo da aula (a01).
4. A invariância do sinal analítico afirmada em **3D** quando ela vale em **2D** (a02).

O padrão é caro **neste** módulo em particular porque a aerogeofísica é, do começo ao fim, uma disciplina de cadeia de processamento: a promessa declarada do Módulo 16 é ensinar como o dado bruto vira mapa interpretável, e trocar a ordem de duas etapas é errar exatamente aquilo que o módulo existe para ensinar. É também o tipo de erro que vira flashcard invertido e questão de gabarito errado, porque "ordem das correções" é o formato natural de questão desse conteúdo.

**Padrão secundário: FAIXA APRESENTADA COMO VALOR DE REFERÊNCIA.** Três achados (Th/U 2-7 na a04, faixa FDEM na a05, "válido acima de 50 m" na a04) declaram uma faixa larga de tolerância e a usam como se fosse o valor esperado ou uma norma.

## Onde o módulo está limpo

Verificado e sem defeito: toda a lógica de plataformas e compromissos da a01 (o argumento área × resolução × custo, o decaimento r⁻³ do dipolo e r⁻² da massa pontual, a orientação perpendicular das linhas, a função das tie lines, o bloco inteiro de controle de qualidade, os azimutes N60°O = 300°/120° do exemplo); na a02, a distinção IGRF × diurna (que a tarefa pediu para checar — estão corretamente apresentadas como correções de natureza diferente, uma modelada e outra medida em tempo real), a faixa de campo total, o IGRF-14 e sua data, e toda a explicação da instabilidade da RTP em baixa latitude magnética; na a03, todas as unidades e conversões, o sentido do efeito Eötvös, a atribuição do Falcon à BHP e do Air-FTG à origem militar, e o argumento de cancelamento de ruído por diferença espacial; na a04, as três janelas de energia com seus radionuclídeos-filhos, a profundidade de 30-45 cm, o NaI(Tl), o background de alta altitude sobre água, a convenção de cores IAEA e a lógica inteira do exemplo Th/U; na a05, a fórmula e a constante de skin depth, a faixa VLF, o tipper como observável de campo natural, e a lista de falsos condutores. **A "ressalva pedagógica" da a05, alertando que skin depth não é profundidade máxima de detecção, já estava no texto original e é exatamente a ressalva certa** — nota positiva.

## Consistência com o Módulo 15 (pré-requisito)

Verificação transversal explícita, conforme pedido:

| Ponto do Módulo 15 | Como o Módulo 16 o trata | Situação |
|---|---|---|
| Magnetita e titanomagnetita como agentes ferrimagnéticos; **ilmenita é paramagnética** | a02 cita explicitamente "a magnetita (não a ilmenita, paramagnética)" e "magnetita e titanomagnetita" | ✅ consistente |
| Magnetização total = induzida + remanente | a02 mantém as duas parcelas separadas e usa a distinção corretamente (RTP pressupõe induzida; sinal analítico tolera remanente) | ✅ consistente e reforçado |
| Pirrotita **monoclínica** é a fase ferrimagnética | a05 dizia apenas "pirrotita" | 🟡 corrigido (A05-F4) |
| K-40 é **isótopo isolado**, U e Th são **séries** | a04 mantém "1,46 MeV, do próprio ⁴⁰K" contra os produtos-filhos ²¹⁴Bi e ²⁰⁸Tl | ✅ consistente |
| Convenção eU/eTh por medida de produto-filho | a04 repete e justifica | ✅ consistente |
| Régua Th/U 2-7 | a04 mantinha a faixa mas a chamava de "régua da IAEA" e a usava como valor de referência | 🟡 corrigido por **acréscimo** (A04-F4), sem remover a faixa, para não contradizer o M15 |
| Densidade como propriedade da gravimetria | a03 declara o pré-requisito e o usa | ✅ consistente |
| Lei de Archie / condutividade | a05 retoma explicitamente | ✅ consistente |

**Nenhuma contradição com o Módulo 15 foi encontrada.** O único ponto de atrito (Th/U) foi resolvido por acréscimo de precisão, não por substituição.

---

## Achados laranjas (todos corrigidos)

### 🟠 AUD-M16-A04-ORDEMCORRECOES-001 — Stripping e correção de altura em ordem invertida
**Aula 04, em quatro lugares: objetivo declarado, corpo, recap e alegação PROCESSAMENTO-003.**

A aula ensinava a sequência "tempo morto → background → **altura → stripping**". A sequência padrão é **tempo morto → background → stripping → altura → conversão**. A inversão não é cosmética: as razões de stripping são elas próprias corrigidas para a altura de voo *antes* de aplicadas (a informação de altura entra no stripping, não o contrário), e os coeficientes de atenuação da correção de altura são definidos **por elemento**, o que só faz sentido sobre contagens já separadas por elemento pelo stripping. Aplicar altura antes de stripping reescalaria contagens ainda contaminadas entre janelas, usando um coeficiente que não corresponde ao elemento que de fato produziu aquela contagem.

*Fonte:* Minty (1997), AGSO Journal 17(2):39-50; IAEA-TECDOC-1363 (2003); BGS Earthwise OR/14/014, que declara literalmente que as taxas de contagem "corrigidas de background e *stripped*" é que são corrigidas para a altitude.

*Correção:* as duas seções trocadas de lugar; acrescentado parágrafo **"Repare na ordem"** explicando *por que* a ordem é obrigatória (é o tipo de justificativa que impede o erro de voltar); recap reescrito com a cadeia em setas; objetivo declarado corrigido; alegação reescrita com a ordem numerada e nota de correção. Acrescentado ainda um esquema de pipeline em linha única no início da seção (achado didático DID-3).

*Confiança:* alta.

### 🟠 AUD-M16-A03-GRADIENTEDIRECAO-002 — Gradiente vertical multiplicado por distância horizontal
**Aula 03, exemplo trabalhado.**

O enunciado declarava "um **gradiente vertical** de gravidade de 18 Eötvös entre dois pontos de uma mesma linha de voo, separados por 400 m de **distância horizontal**", e o Passo 2 multiplicava um pelo outro para obter Δg = 0,72 mGal. A aritmética fecha e as unidades fecham — e é justamente por isso que o erro é perigoso: ele é **dimensionalmente invisível**. Mas G_DD = ∂g_z/∂z descreve como g varia se a aeronave **subir ou descer**, não como ela varia ao longo de uma linha horizontal; essa última é governada pela componente horizontal do tensor (∂g_z/∂x). Um gradiente só pode ser multiplicado por uma distância se ambos apontarem na mesma direção.

*Correção:* o enunciado passou a declarar o **gradiente horizontal ao longo da linha de voo**, com a componente do tensor nomeada; o Passo 2 explicita a condição de mesma direção; foi acrescentado um parágrafo curto alertando para o erro (que é frequente e passa despercebido porque a conta fecha); o Passo 3 registra que o ±5,6 Eo do Falcon é especificado para G_DD e está sendo usado como régua de ordem de grandeza. A alegação UNIDADES-004 recebeu a condição de uso e a nota de correção.

*Confiança:* alta.

### 🟠 AUD-M16-A01-ALEGACAOESPACAMENTO-003 — Alegação auditável contradizendo o corpo da própria aula
**Aula 01, alegação ESPACAMENTO-004.**

O corpo da aula ensina, corretamente e com ênfase, que o espaçamento se dimensiona pela **distância sensor-fonte** (altura de voo + profundidade do topo), e chama de "erro de projeto mais comum" usar só a profundidade. A alegação auditável no bloco de metadados declarava exatamente o erro que o corpo denuncia: *"da ordem de 1 a 2 vezes a profundidade esperada do topo do alvo"*. Resíduo da tentativa de auditoria interrompida (o corpo já havia sido corrigido, o metadado não).

*Por que isso é laranja e não amarelo:* as `alegacoes_auditaveis` são a fonte de que os geradores de questionário e de flashcards puxam o conteúdo verificado. Uma alegação errada aqui produziria diretamente uma questão de gabarito errado, mesmo com o corpo da aula certo.

*Correção:* alegação reescrita com o critério de Reid completo (incluindo a forma funcional F = exp(−2π·h/Δx)), risco reclassificado de `aproximacao` para `fato`, e nota de correção registrada.

*Confiança:* alta. Critério de Reid verificado na fonte primária.

### 🟠 AUD-M16-A02-SINALANALITICO2D3D-004 — Independência do sinal analítico afirmada sem a ressalva 2D/3D
**Aula 02, corpo, recap e alegação SINALANALITICO-006.**

A aula afirmava que a amplitude do sinal analítico "**não depende** da direção de magnetização do corpo", em termos absolutos, e a recomendava como a alternativa robusta à RTP perto do equador magnético e em presença de remanência. A invariância é **rigorosa apenas para fontes bidimensionais** (diques extensos, contatos retilíneos); para corpos **tridimensionais** compactos a amplitude volta a depender da direção de magnetização (Li, 2006, *Geophysics* 71(2):L13-L16). A recomendação prática permanece correta — o sinal analítico é de fato o que se usa em baixa latitude —, mas apresentar a independência como propriedade geral induz confiança indevida exatamente no caso em que ela falha: o alvo compacto e fortemente remanente, que é o alvo típico de exploração.

*Correção:* parágrafo de ressalva acrescentado ao corpo, distinguindo o caso 2D do 3D e dizendo o que fazer no caso 3D (modelagem direta, não leitura visual do mapa); recap ajustado; alegação reescrita com a ressalva marcada como essencial; Li (2006) acrescentado à lista de fontes.

*Confiança:* alta.

### 🟠 AUD-M16-A04-ALTERACAOPORFIRO-005 — Sericita atribuída à alteração potássica
**Aula 04, seção do mapa ternário.**

A aula descrevia "alteração hidrotermal **potássica** (…) onde fluidos hidrotermais introduzem **sericita** e feldspato potássico secundário". No modelo de zoneamento de pórfiro, essas são **duas zonas distintas**: a alteração **potássica** (núcleo, alta temperatura) é feldspato potássico + biotita; a **fílica/sericítica** (mais rasa e fria, envolvendo a anterior) é sericita + quartzo + pirita. Fundir as duas num só nome embaralha o modelo de Lowell & Guilbert (1970), e a distinção tem consequência exploratória: as duas zonas guardam relações diferentes com a mineralização de cobre.

*Correção:* a menção genérica foi trocada por "alteração hidrotermal enriquecida em potássio" e foi acrescentado um parágrafo explicando as duas zonas — com o ponto que de fato importa para a aula: **o mapa gamaespectrométrico não separa uma da outra**, ele registra "mais potássio aqui", não em que ponto do zoneamento se está. Recap ampliado; nova alegação ALTERACAOPORFIRO-006 criada; Lowell & Guilbert (1970) acrescentado às fontes.

*Confiança:* alta.

### 🟠 AUD-M16-A04-DESIGNACAOIAEA-006 — Documento IAEA com designação errada
**Aula 04, lista de fontes e quatro alegações.**

*Guidelines for Radioelement Mapping Using Gamma Ray Spectrometry Data* (IAEA, 2003) foi citado como **"Technical Reports Series 452"**. O documento é o **IAEA-TECDOC-1363** (Viena, julho de 2003, ISBN 92-0-108303-3; autores Erdi-Krausz, Matolin, Minty, Nicolet, Reford e Schetselaar). Não existe TRS 452 com esse título. Adicionalmente, *Airborne Gamma Ray Spectrometer Surveying* foi citado como "IAEA (1991/2003), TRS 323" — é **TRS No. 323, de 1991**, sem edição de 2003.

*Por que laranja e não amarelo:* este é o documento em que se apoiam a régua Th/U, a convenção de cores do mapa ternário, a sequência de correções e o limiar de 50 m — quatro das cinco alegações da aula. Uma designação errada torna toda essa cadeia não rastreável para quem for verificar.

*Correção:* designação corrigida na lista de fontes e nas quatro alegações; ano espúrio removido do TRS-323; acrescentadas às fontes o BGS Earthwise OR/14/014 (sequência de processamento), Rudnick & Gao (2003) (Th/U crustal) e Lowell & Guilbert (1970).

*Verificação:* a designação vaga do mesmo documento no Módulo 15 (*"Technical Reports Series"*, sem número) foi conferida — ela é **imprecisa, não errada**, e não propaga defeito para os flashcards e o questionário já gerados daquele módulo. Registrada abaixo como item de encaminhamento, não como achado deste módulo.

*Confiança:* alta. Designação confirmada na própria IAEA.

---

## Achados amarelos (todos corrigidos)

| ID | Aula | Achado | Correção |
|---|---|---|---|
| A01-Y01 | a01 | Atribuição ao Serviço Geológico do Canadá ("2,5 vezes a altura de voo") não confirmada em fonte primária | atribuição institucional removida; mantida como "prática operacional corrente entre 2 e 2,5 vezes" |
| A01-Y02 | a01 | Citação de Saltus et al. (2026) sem autores nem identificador; "Geological Survey/USGS Open-File Report" com designação híbrida | referência completada (Saltus, Chulliat & Blakely, *Earth and Space Science* 13, e2025EA004336 — **existe e confere**); USGS OFR 00-0027 e 2004-1293 separados e nomeados |
| A01-Y03 | a01 | "critério de Reid, ainda hoje a prática padrão" — o próprio update de 2026 diz que fatores adicionais devem ser considerados | reformulado para "até hoje o ponto de partida", com a nuance do update registrada na fonte |
| A02-Y01 | a02 | Fluxgate descrito como tendo "resolução angular mais grosseira" (a limitação real é exatidão absoluta e deriva) e, na alegação, "usados sobretudo em gradiômetros" (o uso aeronáutico dominante é compensação magnética; gradiômetros aeromagnéticos usam sensores escalares de césio) | corpo e alegação reescritos |
| A02-Y02 | a02 | Passo 3 do exemplo dizia que o IGRF é "referenciado ao mesmo nível de base usado acima (08h00)" — o IGRF não é referenciado ao datum arbitrário da estação-base | frase removida; acrescentada ressalva explicando que a escolha do datum diurno injeta um deslocamento constante, absorvido depois pelo nivelamento, e que é por isso que a TMI residual se lê por contraste relativo |
| A03-Y01 | a03 | Palavra em inglês no corpo: "acelerações verticais **just** discutidas" | → "já discutidas" |
| A03-Y02 | a03 | Redução Bouguer aerotransportada equiparada à terrestre sem ressalva | acrescentada a diferença (entre sensor e terreno há **ar**, não rocha; o modelo digital de terreno passa a insumo obrigatório) |
| A04-Y01 | a04 | Faixa Th/U 2-7 apresentada como "a régua da IAEA" e usada como valor de referência | acrescentado o valor de referência crustal (**~3,5-4**: crosta superior 3,9 ± 0,9, crosta total 4,3 ± 1,2, Rudnick & Gao 2003) **sem remover** a faixa 2-7, para não contradizer o M15; acrescentado parágrafo "Faixa não é o mesmo que valor de referência"; interpretação do Quarteirão 1 fortalecida (3,9 **é** o valor crustal, não apenas "dentro da faixa") |
| A04-Y02 | a04 | "background subtraído antes de qualquer outra correção" contradizia o parágrafo anterior, que põe o tempo morto em primeiro | → "subtraído das contagens já corrigidas de tempo morto" |
| A04-Y03 | a04 | Exemplo trabalhado dependia implicitamente de a laterita ser **residual**, sem jamais declará-lo — e a aula abre alertando que cobertura **transportada** mascara a rocha | enunciado passou a dizer "laterítica **residual** (formado *in situ*)"; acrescentado fechamento "O que sustenta esse raciocínio inteiro — e quando ele cai"; recap ampliado; nova alegação COBERTURARESIDUAL-007 |
| A04-Y04 | a04 | "as correções da IAEA **só são válidas** acima de 50 m" soa como proibição normativa | reformulado para "as curvas foram **calibradas e validadas** para alturas acima de ~50 m" (limitação de calibração, não norma) |
| A05-Y01 | a05 | Energia dos relâmpagos descrita como "propagando-se **pela** ionosfera" | corrigido para propagação **no guia de onda entre a superfície e a base da ionosfera**, com reflexão entre as duas, e o termo *sferics* introduzido |
| A05-Y02 | a05 | Sincronização do TDEM descrita como "múltiplo ímpar de metade da frequência da rede" — formulação que não corresponde aos valores usados | substituído pelos valores reais: frequência de base de **25 Hz onde a rede é 50 Hz, 30 Hz onde é 60 Hz**, com o mecanismo (empilhamento com polaridade alternada) explicado |
| A05-Y03 | a05 | Faixa FDEM limitada a "algumas dezenas de kHz" | ampliada para "a mais de 100 kHz — sistemas helitransportados modernos na ordem de 400 Hz a 130 kHz" |
| A05-Y04 | a05 | "pirrotita" sem qualificar a fase, afrouxando distinção que o M15 faz com cuidado | → "**pirrotita monoclínica**, a fase ferrimagnética vista no Módulo 15", com a hexagonal (antiferromagnética) nomeada como contraste |

## Achados azuis (verificados, sem alteração)

- **A01-B01** — Critério de Reid conferido na fonte primária: F = exp(−2π·h/Δx), com h = distância média sensor-fonte. Em Δx = 2h, F = e^(−π) ≈ 4,3% da potência aliasada — o "teto" que a aula cita está correto e agora aparece justificado. Decaimento r⁻³ do dipolo e r⁻² da massa pontual, corretos. Azimutes do exemplo (N30°E → linhas N60°O = 300°/120°), corretos. Aritmética 60-80 + 150 → 210-230 → 420-460 m, correta.
- **A02-B01** — IGRF-14 com coeficientes finalizados em novembro de 2024, época 2025.0, mantido pela IAGA com atualização quinquenal: confere. Faixa do campo total 25.000-65.000 nT: dentro do usual para material didático. **A distinção IGRF × variação diurna (que a tarefa pediu para checar) está correta e bem construída** — a aula as apresenta como correções de natureza diferente (uma modelada, outra medida em tempo real por estação-base) e não as confunde em nenhum ponto. Instabilidade da RTP em baixa latitude e a alternativa RTE: corretas.
- **A03-B01** — Todas as unidades e a conversão 1 Eo = 0,1 mGal/km reverificadas por derivação (ver acima). Sentido do efeito Eötvös (voo para leste soma-se à rotação e **reduz** a gravidade medida): correto. Falcon como acelerômetros rotativos originalmente da BHP e Air-FTG de origem militar adaptada: corretos.
- **A04-B01** — Janelas de energia e seus radionuclídeos: K 1,46 MeV do ⁴⁰K direto; U 1,76 MeV do ²¹⁴Bi; Th 2,61 MeV do ²⁰⁸Tl — corretos e consistentes com o M15. Profundidade de 30-45 cm: confere. NaI(Tl) de grande volume, background de alta altitude sobre água, convenção de cor K=vermelho/Th=verde/U=azul: corretos. **Profundidade de investigação (item que a tarefa pediu para checar): a aula está correta e é enfática no ponto certo** — o sinal vem só de solo/rocha exposta, não penetra cobertura espessa, vegetação nem água.
- **A05-B01** — Fórmula e constante de skin depth verificadas por derivação, não por citação. Faixa VLF 15-30 kHz: correta. Tipper como observável dos sistemas de campo natural: correto. Falsos condutores (grafita, água salina, argila saturada): corretos e é a lista canônica. **A "Ressalva pedagógica" alertando que skin depth é medida de atenuação e não profundidade máxima de detecção já estava no texto original** — é exatamente a ressalva certa e o texto merece o registro positivo.

## Achado branco (questão em aberto, mantido com ressalva)

- **A05-W01** — A a05 afirma que o TDEM "se tornou o sistema dominante em exploração mineral aérea" e que discrimina melhor condutores pequenos sob cobertura condutora do que o FDEM. É a leitura majoritária da literatura de exploração e está mantida, mas a superioridade FDEM × TDEM **depende do alvo**: o FDEM helitransportado de alta frequência segue preferido para mapeamento de condutividade rasa e para condutores de resposta muito rápida. A alegação FDEMTDEM-002 permanece marcada como `risk: aproximacao`, que é a classificação correta. **Não gerar questão de gabarito fechado que trate "TDEM é melhor que FDEM" como verdade absoluta.**

## Encaminhamentos (fora do escopo deste módulo)

1. **Módulo 15, aula 03 e lista de fontes:** o mesmo documento IAEA é citado como *"Technical Reports Series"* sem número. É impreciso, não errado, e não contamina o questionário nem os dois baralhos já gerados daquele módulo. Sugerido completar para **IAEA-TECDOC-1363** numa eventual passagem `cross-course`, com custo zero de repropagação.
2. **Título da aula 03 no `course-state.yaml`** dizia "Aerogravimetria e gradiometria gravimétrica **e magnética**", mas a aula (e o hub, e o nome do arquivo) tratam apenas de gradiometria **gravimétrica**. Gradiometria aeromagnética não é ensinada em lugar nenhum do módulo. Título do estado corrigido para casar com o conteúdo; **se a gradiometria magnética for desejada, é assunto de seção nova na a02 ou a03, não de remendo desta auditoria** — acrescentar conteúdo factual novo depois da auditoria é justamente o que esta skill não faz.

## Notas para quem for gerar questionário e flashcards

1. **A ordem das correções da a04 é o melhor material de questão do módulo** — e é justamente o que estava errado. Cadeia correta: tempo morto → background → **stripping** → **altura** → concentração. O distrator forte é inverter stripping e altura, que era o texto original. Excelente dissertativa curta: *por que o stripping tem de vir antes da correção de altura?*
2. **NÃO criar card ou gabarito que diga que a amplitude do sinal analítico independe da direção de magnetização, sem qualificar** — foi exatamente esse o erro corrigido. A resposta certa é "independe para fontes 2D; para corpos 3D volta a depender".
3. **NÃO criar questão que dimensione espaçamento de linha pela profundidade do alvo.** É a distância sensor-fonte (altura + profundidade do topo). O distrator perfeito é "150 m de profundidade → teto de 300 m", esquecendo a altura de voo; a resposta certa no exemplo da a01 é 210-230 m de distância sensor-fonte → teto de 420-460 m.
4. **Th/U: cobrar o limiar e o valor de referência, não o adjetivo.** Faixa 2-7 = rocha não alterada; valor crustal ≈ 3,5-4. Boa questão de discriminação: *3,9 e 6,5 estão ambos "dentro da faixa" — o que os distingue?*
5. **A distinção IGRF × diurna é o par conceitual mais limpo da a02**: uma é modelada (componente lenta e previsível), a outra é medida em tempo real por estação-base (componente temporal rápida). Distrator forte: "a diurna é removida pelo IGRF".
6. **Ordem obrigatória × ordem indiferente** (acréscimo desta passagem, a02): entre IGRF e diurna a ordem é indiferente (subtrações comutam); antes do nivelamento e dos realces, obrigatória. Ótima questão conceitual, e a regra geral ("a etapa é subtração ponto a ponto ou mistura pontos/canais?") é transferível para a a04.
7. **1 Eo = 0,1 mGal/km é par numérico limpo e verificado** — bom para questão de cálculo. Mas **não criar questão que multiplique um gradiente vertical por uma distância horizontal**: foi exatamente o erro corrigido na a03, e a questão boa cobra justamente a consistência de direção.
8. **Cobertura residual × transportada (a04)** é a melhor questão de aplicação do módulo depois da ordem das correções: os números do exemplo (eTh 16,5 vs. 14,8 ppm) já estão calculados e a questão pode cobrar *o que mudaria se a cobertura fosse transportada?* — a resposta é que o argumento inteiro cai.
9. **Duas zonas de alteração de pórfiro enriquecem em K** e o mapa gama não as separa. Distrator forte: "sericita é diagnóstica de alteração potássica". Novo no material após a correção.
10. **δ ≈ 503√(ρ/f)** com os dois números do exemplo (112 m para VLF a 20 kHz, 2.904 m para AFMAG a 30 Hz em 1.000 Ω·m) admite variação numérica infinita. Mas toda questão deve preservar a ressalva: skin depth é atenuação, **não** profundidade máxima de detecção.
11. **Não gerar questão de gabarito fechado afirmando superioridade absoluta do TDEM sobre o FDEM** (achado branco A05-W01).
12. **Estrutura de questionário recomendada:** ver a decisão registrada no `course-state.yaml`, campo `assessment_plan` — questionário **único**, 5 aulas, com corte interno entre campos potenciais e não-potenciais.

## Material derivado a propagar

**Nenhum.** O módulo não tem questionário nem baralho — a auditoria rodou antes deles, como manda a cadeia. Nada a reimportar no Anki.
