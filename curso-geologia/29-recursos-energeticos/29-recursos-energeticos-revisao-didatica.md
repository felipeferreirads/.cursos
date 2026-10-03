# Revisão didática: Módulo 29 — Recursos energéticos

**Revisado em:** 2026-08-29 · **Modo:** review-and-fix
**Material:** as 4 aulas do M29 (o módulo ainda não tem questionário nem baralho)
**Veredito da primeira passagem:** Requer revisão
**Veredito final:** Bem ensinado com ressalvas

## Resumo

**Primeira passagem:** 🔴 0 bloqueiam · 🟠 4 prejudicam · 🟡 6 atrito · 🔵 1 sugestão
**Após as correções:** 🔴 0 · 🟠 1 em aberto (não corrigível nesta skill) · 🟡 0 · 🔵 1 sugestão

**Carga estimada:** 29 termos únicos nos blocos de vocabulário (7 · 7 · 8 · 7); 1 exemplo trabalhado por aula, os três primeiros reescritos nesta revisão para terem passos encadeados; 4 aulas declaradas de 28–29 min. Corpo real por aula, recontado sobre "Conteúdo" até "Próxima aula" **depois** das correções: 1.588 · 1.600 · 1.579 · 1.584 (total 6.351) — as quatro dentro do teto de 1.600 palavras do LC-02. Antes desta revisão a aula 04 estava em 1.620, acima do teto.

A auditoria científica de 2026-08-29 aprovou o módulo e encaminhou explicitamente dois itens para esta revisão: a lacuna de alinhamento de `oa01` (achado 🟠 2 abaixo) e um erro de digitação (achado 🟡 9). Ambos foram tratados aqui.

## Achados

### 🟠 1. As quatro aulas não tinham "Erros comuns" nem "O que não concluir" — LC-07 violado no módulo inteiro

**Tipo:** bloco obrigatório do contrato de nível ausente
**Onde:** aulas 01, 02, 03 e 04 · entre o exemplo trabalhado e o recap
**Problema:** o LC-07 torna "Erros comuns", "O que não concluir" e "Recap relâmpago" obrigatórios, e a razão declarada no contrato é precisa: são eles que impedem que simplificar vire mentir. O M29 tinha só o recap. O custo disso é concreto e específico deste módulo, que é inteiro construído sobre distinções que o senso comum apaga: capacidade instalada versus energia gerada, matriz elétrica versus matriz energética total, R/P versus previsão de esgotamento, CCS versus geração limpa, armazenamento versus fonte. Cada uma dessas distinções aparecia uma única vez, no meio de um parágrafo expositivo, sem nenhum lugar no material onde o erro correspondente fosse nomeado como erro. Um aluno que lesse rápido sairia com exatamente a confusão que a aula tentava desfazer.
**Correção aplicada:** os dois blocos foram acrescentados às quatro aulas, com 4 itens em "Erros comuns" e 2 em "O que não concluir" cada. Todo o conteúdo dos blocos é negação direta de afirmação que a própria aula já fazia — nenhuma alegação factual nova foi introduzida, e nenhum número, limite ou classificação validado pela auditoria foi tocado.
**Escopo:** correção local nas quatro aulas, concluída.

### 🟠 2. `oa01` promete converter unidades e comparar matrizes; nenhuma aula mostra um fator de conversão nem uma matriz preenchida — EM ABERTO

**Tipo:** objetivo parcialmente não coberto
**Onde:** hub · aula 01 · bloco "Ao final você vai conseguir"
**Problema:** recebido da auditoria científica, que o identificou e o encaminhou nomeadamente para esta skill. O objetivo `oa01` tem três verbos — ler e comparar a matriz global e a brasileira; converter entre unidades; interpretar um balanço. O terceiro é bem ensinado. Os outros dois não são ensinados a ponto de o aluno conseguir executá-los. A aula nomeia tep, EJ, BTU e MWh e diz que "a conversão entre elas segue fatores fixos" — sem dar um único fator, o que deixa o aluno capaz de reconhecer as unidades e incapaz de converter entre elas. E descreve a matriz mundial e a brasileira qualitativamente ("majoritariamente fóssil", "bem acima da média mundial") sem nenhuma composição concreta, de modo que "comparar" nunca chega a ser praticado sobre um dado. É uma decisão de projeto defensável do ponto de vista de durabilidade — números de matriz energética envelhecem rápido —, mas o objetivo declarado não foi rebaixado junto com ela, e é o objetivo que a avaliação vai usar.
**Correção sugerida:** ou (a) acrescentar à aula 01 os fatores de conversão e uma composição de matriz mínima, sempre com ano e fonte no corpo do texto, no formato "(EPE/BEN 2025)" que a própria auditoria prescreveu; ou (b) reescrever `oa01` para declarar o que a aula de fato entrega. **Não aplicada aqui:** ambas exigem decisão fora do escopo desta skill — (a) introduz alegação factual nova, que precisa passar pelo `auditor-cientifico` antes de entrar; (b) altera um objetivo de aprendizagem, o que é decisão do `gerador-de-curso-modular`, não de uma revisão didática.
**Escopo:** exige conteúdo novo auditado ou revisão do objetivo. Encaminhado ao `gerador-de-aula` + `auditor-cientifico`. **Consequência imediata para a próxima etapa:** enquanto este achado estiver aberto, o `gerador-de-questionarios` **não deve** escrever questão que peça conversão numérica entre unidades de energia nem leitura de percentuais de uma matriz concreta — a aula não sustenta nenhuma das duas.

### 🟠 3. O exemplo trabalhado da aula 01 não fazia a conta que a aula existe para ensinar

**Tipo:** exemplo insuficiente
**Onde:** aula 01 · "Exemplo trabalhado"
**Problema:** o hub nomeia "não confundir capacidade instalada com energia gerada" como o principal ponto de dificuldade do módulo, e o exemplo trabalhado da aula 01 é onde essa dificuldade deveria ser vencida. Ele montava o cenário certo — 10 GW eólicos a ~35% de fator de capacidade contra 10 GW nucleares a ~90% — e então **não multiplicava nada**, encerrando com a afirmação qualitativa de que a nuclear "entrega uma fração muito maior". O aluno terminava o exemplo sabendo que os dois números diferem, sem nunca ter visto o quanto diferem, que é precisamente a informação que desfaz a confusão. Um exemplo trabalhado que não trabalha é um parágrafo expositivo com outro nome.
**Correção aplicada:** o exemplo foi reestruturado em três passos: o teto teórico (10 GW × 8.760 h ≈ 88 TWh), a aplicação do fator de capacidade de cada fonte (≈31 TWh contra ≈79 TWh) e a interpretação, que agora inclui o caminho inverso — quanta capacidade eólica seria necessária para igualar a nuclear. A aritmética opera exclusivamente sobre números que já estavam no texto e já haviam sido auditados; o único valor acrescentado é o número de horas do ano, derivado explicitamente (365 × 24).
**Escopo:** correção local, concluída.

### 🟠 4. "Entalpia" estrutura a segunda metade da aula 03 e nunca foi definido

**Tipo:** termo técnico usado antes de definido (LC-01)
**Onde:** aula 03 · vocabulário e seção "Energia geotérmica"
**Problema:** a aula divide todo o aproveitamento geotérmico em "alta entalpia" e "baixa entalpia", usa os dois rótulos oito vezes, e os define **um em função do outro** — sistema de alta entalpia é o que tem fluido quente o bastante para turbina, o de baixa é o que não tem. Em nenhum momento diz o que é entalpia. Para o público do contrato (ensino médio completo, sem geologia), "entalpia" é um termo de termodinâmica que não vem de graça; sem ele, o aluno decora dois rótulos opacos em vez de entender que a distinção é sobre quanto calor o fluido carrega. É o caso clássico de definição circular do LC-01.
**Correção aplicada:** entrada própria no vocabulário ("no uso corrente da geotermia, o conteúdo de calor que o fluido carrega por unidade de massa; alta e baixa entalpia são o modo do setor de dizer fluido muito quente e fluido pouco quente") e um aposto no corpo, na frase que introduz os dois tipos, ligando o rótulo à grandeza antes de usá-lo. O vocabulário da aula passa de 7 para 8 entradas, dentro do teto do LC-03.
**Escopo:** correção local, concluída.

### 🟡 5. Aula 04 acima do teto de palavras do LC-02

**Tipo:** violação de teto de carga
**Onde:** aula 04 · corpo inteiro
**Problema:** 1.620 palavras de corpo real contra o teto de 1.600 do LC-02 — estouro pequeno (1,25%), mas real, e agravado pelo fato de que a aula precisava ainda receber os dois blocos do achado 🟠 1. A aula concentrava a prolixidade em três lugares: um parágrafo único de 215 palavras sobre hidrelétrica que misturava geração, capacidade instalada e limitações geográficas; o parágrafo de fecho sobre transição energética, uma frase de quatro orações encadeadas; e o exemplo trabalhado, um bloco corrido sem estrutura de passos.
**Correção aplicada:** o parágrafo da hidrelétrica foi dividido em dois (o que é, e o que a limita) e podado; os parágrafos de CCS, armazenamento, eólica/solar, biocombustíveis e transição energética foram podados de prolixidade sem perda de conteúdo — nenhuma ideia, ressalva ou qualificador foi cortado, apenas redundância de fraseado; e o exemplo trabalhado ganhou estrutura de partes ("o que o CCS resolve" / "o que o armazenamento resolve" / conclusão), cada uma nomeando também o que a solução **não** faz. Corpo final: 1.584.
**Escopo:** correção local, concluída. Não foi caso de divisão de aula: a aula tem um único objetivo e o estouro era de prolixidade, não de excesso de conceitos.

### 🟡 6. O exemplo trabalhado da aula 02 anunciava um dado numérico que nunca usava

**Tipo:** exemplo que promete o que não entrega
**Onde:** aula 02 · "Exemplo trabalhado"
**Problema:** abria com "uma usina termelétrica a carvão betuminoso gerando 1.000 MWh de eletricidade por dia" e depois conduzia um raciocínio inteiramente qualitativo, sem usar os 1.000 MWh em conta nenhuma. O número não era errado — era decorativo, e decoração numérica num exemplo trabalhado ensina o aluno a esperar uma conta que não vem, ou pior, a supor que ele deveria conseguir fazê-la e não conseguiu.
**Correção aplicada:** o exemplo foi reescrito como comparação de três destinos possíveis para a usina (trocar por gás, trocar por renovável, manter o carvão), declarando **explicitamente e logo na abertura** que o raciocínio é qualitativo de propósito, porque quantificar exigiria os fatores de emissão específicos de cada usina, que esta aula não trata. O número decorativo saiu. A conclusão nomeia o que a aula permite decidir (a ordem de preferência) e o que exigiria dado adicional (o quanto cada troca economiza).
**Escopo:** correção local, concluída.

### 🟡 7. Três termos de geociências sem definição na primeira ocorrência

**Tipo:** termo técnico usado antes de definido (LC-01)
**Onde:** aula 02 ("florestas paludosas", "querogênio") e aula 03 ("áreas cratônicas")
**Problema:** os três chegam sem aposto. "Querogênio" é o mais grave dos três porque carrega o mecanismo da frase em que aparece — é ele que decide se a rocha geradora produz óleo ou gás — e o Módulo 22, onde foi ensinado, é pré-requisito declarado mas distante. O LC-01 é explícito em que termos de geociências continuam sempre definidos, mesmo já ensinados antes.
**Correção aplicada:** aposto curto em cada um, na primeira ocorrência: pântano permanentemente encharcado onde a falta de oxigênio impede o apodrecimento completo; matéria orgânica dispersa na rocha geradora que se converte em óleo ou gás conforme a origem biológica; núcleo continental antigo e tectonicamente quieto. Nenhum vira parágrafo — todos cabem numa oração intercalada, como o contrato pede.
**Escopo:** correção local, concluída.

### 🟡 8. `palavras_corpo` superestimado nas quatro aulas

**Tipo:** instrumento de verificação desalinhado
**Onde:** as 4 aulas · bloco de metadados
**Problema:** os valores declarados (~1550, ~1500, ~1600, ~1650) superestimavam a contagem real (1.411, 1.262, 1.356, 1.620) em até 244 palavras. É o mesmo defeito encontrado no módulo 19, na mesma direção. O risco é o de sempre: como o LC-02 usa esse campo para checar o teto, um valor inflado perto de 1.600 esconde por mais tempo o momento em que a aula de fato estoura — e neste módulo o campo da aula 04 já declarava ~1650, ou seja, **declarava um estouro do teto que ninguém tratou**.
**Correção aplicada:** os quatro valores foram recontados programaticamente sobre o corpo real, depois de todas as demais correções, e gravados sem o til de aproximação: 1588 · 1600 · 1579 · 1584.
**Escopo:** correção local, concluída.

### 🟡 9. "specíficos" — RECEBIDO DA AUDITORIA

**Tipo:** erro de digitação
**Onde:** aula 01 · "A matriz energética brasileira"
**Correção aplicada:** "específicos".
**Escopo:** correção local, concluída.

### 🟡 10. Texto de status obsoleto no fecho da aula 04 e no hub

**Tipo:** metadado desatualizado que desinforma o aluno
**Onde:** aula 04 · "Este é o último tópico do módulo" · e hub do módulo
**Problema:** o fecho da aula 04 dizia que "auditoria científica, questionário e flashcards deste módulo ficam para uma etapa de qualidade posterior", e o hub trazia dois avisos no mesmo sentido — todos escritos antes de 2026-08-29, quando a auditoria científica de fato rodou e aprovou o módulo. Um aluno que chega ao fim do módulo e lê que a auditoria não rodou tem motivo para desconfiar do material que acabou de estudar.
**Correção aplicada:** o fecho da aula 04 agora cita só questionário e flashcards como pendentes; o hub teve o callout de status e o aviso de pendência reescritos para refletir auditoria aprovada e revisão didática concluída.
**Escopo:** correção local, concluída.

### 🔵 11. Nenhuma das quatro aulas tem bloco de apoio visual

**Tipo:** oportunidade de apoio à compreensão
**Onde:** módulo inteiro
**Problema:** o módulo é fortemente comparativo — quatro fontes contra quatro atributos (disponibilidade, despachabilidade, emissão, limitação) — e esse tipo de estrutura é exatamente o que uma tabela-resumo consolida melhor que prosa. A aula 04, que fecha o módulo, seria o lugar natural: uma tabela de uma linha por fonte, com o que cada uma resolve e o que cada uma não resolve, reunindo o que hoje está espalhado por três aulas.
**Escopo:** sugestão, não defeito. Não aplicada porque acrescentaria carga a um módulo cujas quatro aulas já estão entre 1.579 e 1.600 palavras, sem folga sob o teto do LC-02. Registrada para uma eventual redistribuição futura do módulo.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em | Cards |
|---|---|---|---|---|
| `oa01` — matriz energética global e brasileira, unidades, balanço | aula 01, cinco seções | sim — 10 GW eólicos × 10 GW nucleares, com a conta feita | pendente | pendente |
| `oa02` — geologia dos fósseis × disponibilidade, produção e impacto | aula 02, cinco seções | sim — três destinos para uma termelétrica a carvão | pendente | pendente |
| `oa03` — base geológica do nuclear e do geotérmico | aula 03, cinco seções | sim — depósito tipo discordância e a invariância dos 0,7% | pendente | pendente |
| `oa04` — renováveis, armazenamento e CCS | aula 04, sete seções | sim — CCS e armazenamento lado a lado, com o limite de cada um | pendente | pendente |

Nenhuma seção órfã: as quatro aulas mapeiam um objetivo cada, sem repartimento entre aulas e sem sobra. A ressalva está toda em `oa01`, cujos verbos "converter" e "comparar" não são plenamente cobertos — ver o achado 🟠 2, que é a única pendência aberta do módulo.

## Verificação do contrato de nível

- **LC-01 — nenhum termo sem definição:** aprovado após os achados 🟠 4 e 🟡 7. Verificada a primeira ocorrência de cada termo técnico nas quatro aulas. Casos de fronteira restantes, todos aceitos: "embasamento cristalino" e "discordância" (aula 03) chegam contextualizados na própria frase que os usa, e "trapa" e "selo" (aula 04) são reativados com a função explicitada, não apenas nomeados.
- **LC-02 — teto de 1.600 palavras:** aprovado após o achado 🟡 5, nas quatro aulas (1.588 · 1.600 · 1.579 · 1.584). Nenhuma candidata a divisão: cada aula tem um único objetivo e o estouro que existia era de fraseado, não de conteúdo. Registre-se que o módulo agora opera **sem folga** sob o teto — qualquer acréscimo futuro a qualquer das quatro aulas exige poda equivalente.
- **LC-03 — abertura padronizada:** aprovado. Os quatro blocos de vocabulário ficam em 7 · 7 · 8 · 7 termos, dentro da faixa de 5 a 8, e os quatro blocos "Antes de começar" linkam pré-requisitos específicos por aula ou por módulo. Todos os wikilinks internos e externos das quatro aulas foram conferidos e resolvem.
- **LC-04 — analogia antes do termo:** parcialmente aprovado, com ressalva. O módulo usa pouca analogia de cotidiano — a estratégia dominante é a comparação entre fontes, não a metáfora. Onde há metáfora, ela vem na ordem certa: a "bateria gravitacional" (aula 04) aparece depois de o mecanismo do bombeamento ter sido descrito, e a contabilidade como imagem do balanço energético (aula 01) abre a seção antes do termo técnico. Não é achado — é um traço do assunto, que é econômico e sistêmico mais que fenomenológico.
- **LC-05 — ordem de grandeza:** aprovado, e é um ponto forte. "cerca de 0,7%", "poucos por cento", "da ordem de 25–30 °C/km", "cerca de −162 °C", "cerca de 14%" — nenhum valor de risco aparece como constante fechada. Os números novos introduzidos pela correção do achado 🟠 3 (≈88, ≈31, ≈79 TWh; 2,6 vezes) seguem a mesma disciplina, todos arredondados e todos com o "≈" explícito.
- **LC-06 — matemática reativada antes do uso:** aprovado. A única aritmética do módulo é a do exemplo da aula 01, e ela é multiplicação e porcentagem — nada que exija reativação formal. A conversão entre unidades de energia, que exigiria, é justamente a que não é ensinada (achado 🟠 2).
- **LC-07 — blocos obrigatórios:** aprovado após o achado 🟠 1. As quatro aulas passaram a ter "Erros comuns", "O que não concluir" e "Recap relâmpago", além de "Exemplo trabalhado".
- **LC-08 — controvérsia em uma frase:** aprovado. O módulo trata assunto com carga política real (nuclear, hidrelétrica, transição) e não arbitra nenhuma disputa: a escolha entre ciclo aberto e fechado é declarada como decisão de política energética e não técnica; os limites de "aceitação social" da nuclear e da hidrelétrica são nomeados sem serem debatidos; o gás como "ponte" aparece entre aspas na aula 02 e qualificado na aula 04. Nenhum caso de controvérsia expandida além de uma frase.

## Alinhamento entre as aulas

A progressão do módulo é bem construída e merece registro por ser o que o hub prometia: a unidade de análise migra de depósito (Módulos 21 e 22) para matriz, e cada aula reutiliza o instrumento da anterior em vez de reensiná-lo. A aula 01 estabelece capacidade instalada versus energia gerada; a aula 04 usa exatamente essa distinção para explicar por que a solar lidera um indicador e a hidrelétrica lidera o outro — e a auditoria científica registrou que essa passagem nasceu de uma correção, o que significa que o módulo hoje ensina, no ponto mais delicado, aquilo em que ele próprio havia tropeçado. A aula 02 estabelece a hierarquia carvão > petróleo > gás; a aula 04 a invoca por nome ao tratar do gás como ponte. A aula 04 recupera reservatório e selo do Módulo 22 aplicados ao CO₂, que é a melhor conexão entre módulos do material inteiro: o aluno reconhece a estrutura antes de o texto nomear a analogia.

Uma escolha de sequência merece nota por ser um acerto deliberado: a aula 03 junta nuclear e geotérmica, que não têm nada em comum do ponto de vista de recurso, e as junta pelo critério certo — são as duas fontes cujo calor não vem de combustão. O parágrafo de transição da aula 02 para a 03 explicita isso ("em vez do calor liberado pela quebra de ligações químicas do carbono fóssil"), o que transforma um agrupamento que poderia parecer arbitrário em uma categoria com conteúdo.

## O que está bem feito

A disciplina de separar o que uma fonte resolve do que ela não resolve atravessa as quatro aulas e é o traço mais forte do módulo. Ela já estava lá antes desta revisão — "R/P não é previsão de esgotamento", "geotermia não é ilimitada num ponto", "CCS não gera energia limpa", "substituir carvão por gás não elimina a dependência fóssil" — e foi essa consistência que tornou possível montar os blocos "Erros comuns" e "O que não concluir" do achado 🟠 1 inteiramente a partir de material já presente no texto, sem inventar um único fato. Um módulo que precisasse de conteúdo novo para preencher esses blocos teria um problema bem maior do que o de formatação.

A aula 03 tem o melhor movimento conceitual do módulo: estabelecer que os 0,7% de ²³⁵U são invariantes porque vêm da nucleossíntese estelar, e não de processo geológico local, e então usar essa invariância no exemplo trabalhado para mostrar que nem o depósito mais rico do mundo dispensa o enriquecimento. É a estrutura de raciocínio que separa teor de minério de proporção isotópica sem nunca precisar dizer "não confunda teor com proporção" — a distinção é construída, não avisada.

## Gate didático

**Liberado com uma restrição nomeada.** Nenhum achado 🔴. Os nove achados corrigíveis nesta skill (🟠 1, 🟠 3, 🟠 4 e 🟡 5–10) foram aplicados; nenhuma edição introduziu alegação factual nova e nenhuma tocou em número, limite, classificação ou fonte validados pela auditoria científica de 2026-08-29 — a única aritmética acrescentada (achado 🟠 3) opera sobre valores que aquela auditoria já havia conferido.

Permanece **um achado 🟠 em aberto**, o achado 2, que não é corrigível por esta skill: `oa01` promete converter unidades e comparar matrizes concretas, e a aula 01 não entrega nenhuma das duas coisas. A restrição que isso impõe à etapa seguinte é específica e verificável:

> O `gerador-de-questionarios` e o `gerador-de-flashcards` **não devem** produzir item que exija conversão numérica entre tep, EJ, BTU e MWh, nem leitura ou comparação de percentuais de uma matriz energética concreta. `oa01` deve ser avaliado pelo que a aula ensina: a necessidade de unidade comum, a estrutura do balanço, a distinção primária/final, a distinção matriz elétrica/matriz total e a distinção capacidade instalada/energia gerada — esta última com item de aplicação numérica, que o exemplo trabalhado corrigido agora sustenta.

Fora essa restrição, o módulo está liberado para questionário e flashcards. Uma sugestão fica registrada, não bloqueante: o achado 🔵 11 (tabela-resumo comparativa), que exige folga de palavras que o módulo hoje não tem.
