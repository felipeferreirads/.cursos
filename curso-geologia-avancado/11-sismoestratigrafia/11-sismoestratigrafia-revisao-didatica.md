# Revisão didática — Módulo 11: Sismoestratigrafia

**Revisado em:** 2026-08-30 · **Modo:** `review-and-fix`
**Material:** `11-sismoestratigrafia/` — 6 aulas (a01 a a06)
**Rodada depois da** auditoria científica (`11-sismoestratigrafia-auditoria.md`), como manda a ordem.
**Veredito:** **Bem ensinado com ressalvas.**

## Resumo

🔴 0 bloqueiam · 🟠 4 prejudicam · 🟡 1 atrito · 🔵 1 sugestão

**Nenhum salto de pré-requisito** — o defeito mais grave e mais comum, ausente aqui. A cadeia
a01 → a02 → a03 → a04 → a05 → a06 é linear, declarada no cabeçalho e no bloco "Antes de
começar" de cada aula, e as três dependências externas (Módulo 10, Aulas 01, 02, 04 e 05) são
nomeadas com a aula de origem, não apenas com o número do módulo.

### Carga por aula (recontagem após auditoria e revisão)

| aula | palavras (corpo) | conceitos novos | exemplo trabalhado | figura |
|---|---|---|---|---|
| a01 | 1894 | ~8 (impedância, RC, CMP, deconvolução, NMO/empilhamento, migração, resolução vertical com dois limiares, zona de Fresnel) | sim, numérico | sim |
| a02 | 1701 | ~6 (sônico, densidade, wavelet, sismograma sintético, *well tie*/T-Z, checkshot/VSP) | sim, diagnóstico | sim |
| a03 | 1868 | ~6 (superfície cronoestratigráfica, onlap, downlap, toplap, truncamento, clinoforma) | sim, interpretativo | sim |
| a04 | 1648 | ~7 (sismofácies, cinco configurações internas, duas assinaturas carbonáticas) | sim, interpretativo | sim |
| a05 | 2045 | ~9 (acomodação, nível relativo, sequência deposicional, LST, TST, HST, FSST, SMST, Wheeler) | sim, interpretativo | sim |
| a06 | 1933 | ~5 (trato ↔ elemento de sistema petrolífero, critério sinsedimentar/pós-deposicional, coluna da margem brasileira) | sim, avaliação de risco | sim |

**Sobre a queixa de contagem levantada pelo próprio geo-redator:** procede como observação, mas
o diagnóstico correto não é "o número está baixo" — é **onde** ele estava baixo. Ver
`DID-M11-PALAVRAS-005` e `DID-M11-A02-RESOLUCAO-002`.

---

## Achados

### 🟠 1. "Clinoforma" — termo central do módulo, usado dezenas de vezes, nunca definido

**id:** `DID-M11-CLINOFORMA-001` · **Tipo:** termo técnico usado antes de definido
**Onde:** a03 · "Downlap" (primeira ocorrência), e depois a03 (figura, exemplo, recap),
a04 (configuração progradacional, sistemas deltaicos, carbonatos, exemplo, recap),
a05 (TST, HST, FSST, exemplo) e a06.
**Problema:** "clinoforma" é a palavra geométrica que carrega metade do módulo — é o objeto que
faz downlap, que define a configuração progradacional, que distingue sigmoide de oblíqua, que
desce em degraus no FSST. Ela aparecia pela primeira vez a03 já em uso corrente ("depositando
sedimento em clinoformas que se estendem cada vez mais para a bacia"), como se o leitor já
soubesse, e nunca era definida em nenhuma das seis aulas nem em nenhum módulo anterior do
curso (verificado por varredura: as únicas ocorrências no curso inteiro estão neste módulo).
O leitor consegue inferir "algo inclinado" do contexto e seguir — por isso 🟠 e não 🔴 —, mas
inferir "algo inclinado" não basta quando a a04 pedir para distinguir sigmoide de oblíqua pela
forma, nem quando a a05 disser que o FSST não preserva *topset*. Um vocabulário de três termos
(topset, foreset, bottomset) fica inacessível porque o termo-mãe nunca foi ancorado.
**Correção aplicada:** aposto de definição na primeira ocorrência (a03), ancorando clinoforma
como a superfície deposicional inclinada que liga topset a bottomset pelo foreset, e dizendo
explicitamente que o empilhamento dessas superfícies é o que produz o padrão de refletores
oblíquos. Três termos entregues de uma vez, no lugar certo, sem seção nova.
**Escopo:** correção local. Aplicada.

### 🟠 2. A a02 promete "resolução" no título e entrega uma repetição da a01

**id:** `DID-M11-A02-RESOLUCAO-002` · **Tipo:** objetivo declarado servido de forma insuficiente
**Onde:** a02 · título, objetivo declarado e seção "Resolução revisitada"
**Problema:** este é o achado que o alerta de contagem de palavras do geo-redator estava
apontando sem nomear. A a02 era a aula mais curta do módulo (1390 palavras declaradas), e o
déficit não estava distribuído: estava concentrado na metade que o título anuncia como sua
segunda contribuição. O objetivo da aula promete "**aprofundar** a discussão de resolução
iniciada na Aula 01", e a seção correspondente entregava (i) o contraste de escala poço ×
sísmica, que a a01 já havia estabelecido no seu último parágrafo, e (ii) a complementaridade
dos dois métodos, que decorre imediatamente de (i). Nenhum dos dois é *aprofundamento*; é
recapitulação com outras palavras. Do ponto de vista de quem lê pela primeira vez, a seção
responde "os dois se completam" a uma pergunta que a a01 já tinha respondido, e a promessa do
título fica sem lastro.
O conteúdo que faltava não é externo à aula: é **a consequência direta do que a própria a02
ensina três seções antes**. A convolução com a wavelet, que a aula apresenta apenas como o
passo mecânico de construção do sintético, é exatamente o mecanismo que reconcilia as duas
resoluções — a wavelet tem banda limitada, e convolucioná-la com a série de RC do poço filtra
o poço até a resolução da sísmica. Sem isso explicitado, o leitor não percebe que o sintético
é "o poço visto com os olhos da sísmica", e a amarração fica parecendo um truque de
alinhamento em vez de uma tradução entre escalas.
**Correção aplicada:** um parágrafo na seção "Resolução revisitada" tornando explícita a
função de filtro passa-banda da convolução e sua consequência (a amarração informa o que há
dentro de um refletor composto sem tornar isso visível na seção), mais um item de recap.
Nenhum fato novo foi introduzido — o parágrafo só explicita o que a própria aula já continha
implícito. A a02 passou de 1390 para 1701 palavras, saindo do fundo da faixa.
**Escopo:** correção local. Aplicada.

### 🟠 3. A a05 é a aula mais densa do módulo, e ficou mais densa após a auditoria

**id:** `DID-M11-A05-CARGA-003` · **Tipo:** excesso de conceitos novos
**Onde:** a05 · toda
**Problema:** a a05 carrega ~9 conceitos independentes em 2045 palavras — espaço de acomodação
reancorado, nível relativo do mar vs. eustasia, sequência deposicional, quatro tratos de
sistemas, um quinto termo (SMST) que existe só para não ser confundido com o quarto, e o
diagrama de Wheeler, que é uma mudança de representação e não um conceito a mais na mesma
lista. É a aula de maior densidade e a que está no teto de palavras do curso. A auditoria
científica **agravou** o quadro por necessidade: o achado `SISMO-M11-A05-FSST-006` obrigou a
acrescentar o trato de estágio de queda, que estava ausente e cuja omissão era um erro de
conteúdo — não havia como resolver o achado sem aumentar a carga.
**Correção não aplicada, deliberadamente.** A correção certa para sobrecarga é dividir, não
explicar mais — encher a a05 de esclarecimento pioraria exatamente o que se quer resolver. E
dividir aqui tem um custo maior que nos módulos anteriores: levaria o módulo de 6 para 7
aulas, renumeraria a a06, invalidaria dois `content_hash`, obrigaria a reescrever links, hub e
travessias de pré-requisito, e — o ponto decisivo — **mudaria a decisão de questionário**,
desequilibrando o corte a03/a04 que hoje deixa os quatro objetivos inteiros (ver a seção de
recomendação de parciais). Mesmo precedente dos Módulos 08, 09 e 10: ressalva justificada em
vez de quebra.
**Mitigação já presente no texto:** o diagrama de Wheeler tem seção própria, o FSST entrou com
figura atualizada, e o SMST foi deslocado para parágrafo separado com a advertência explícita
"não confundir com o FSST" — a fonte de confusão mais provável ficou sinalizada em vez de
diluída na lista.
**Candidata a quebra futura, se houver fadiga relatada:** corte entre "Sequência deposicional
e os tratos de sistemas" e "O diagrama de Wheeler". A Parte 2 teria autonomia conceitual (o
Wheeler é uma mudança de representação, com exemplo trabalhado próprio possível) e a Parte 1
ficaria com a carga dos quatro tratos sozinha.
**Escopo:** exige dividir a aula — encaminhado ao `gerador-de-curso-modular`, não improvisado.

### 🟠 4. O oa02 credita só a a03, mas SB e MFS são ensinadas na a05

**id:** `DID-M11-OA02-MAPEAMENTO-004` · **Tipo:** desalinhamento objetivo↔seção (metadado)
**Onde:** `mapa_objetivo_secao` da a05 e `covers_objectives` da a05 no `course-state.yaml`
**Problema:** o oa02 diz "Interpretar padrões de terminação de refletores **e identificar
superfícies com significado cronológico**". A primeira metade é da a03, que a cobre bem. A
segunda metade — as superfícies-chave nomeadas — é ensinada na **a05**: discordância de
sequência (SB), superfície de inundação máxima (MFS) e superfície transgressiva são definidas
ali, não na a03. Mas o mapa da a05 creditava tudo ao oa04, e o `covers_objectives` no estado
listava só `oa04`.
Consequência concreta e não burocrática, idêntica à do achado `DID-M10-OA03-MAPEAMENTO-002` do
módulo anterior: **o gerador de questionários lê esse mapa.** Todas as questões de oa02 sairiam
da a03 (onlap, downlap, toplap, truncamento) e **nenhuma** cobriria SB e MFS — as duas
superfícies que o objetivo nomeia em segundo lugar e que a a06 inteira usa como base para
prever elementos de sistema petrolífero. Agravante específico deste módulo: o corte de
parciais proposto abaixo coloca a a03 na parcial 1 e a a05 na parcial 2, de modo que, sem
esta correção, o oa02 apareceria como objetivo exclusivo da parcial 1 e a parcial 2 avaliaria
SB e MFS sob o rótulo errado.
**Correção aplicada:** metadado apenas, sem tocar no texto da aula. O `mapa_objetivo_secao` da
a05 foi desdobrado — `oa02` recebe "Sequência deposicional e os tratos de sistemas" (a parte
das superfícies-chave), "O diagrama de Wheeler" e o exemplo trabalhado; `oa04` mantém tudo. O
`covers_objectives` da a05 no `course-state.yaml` passou a incluir `oa02`, com nota explicativa
no próprio manifesto da aula.
**Escopo:** correção local (metadado). Aplicada.

### 🟡 5. As contagens de palavras declaradas estavam abaixo da faixa do curso — e a faixa era o sintoma, não a doença

**id:** `DID-M11-PALAVRAS-005` · **Tipo:** métrica declarada desalinhada + densidade irregular
**Onde:** campo `palavras_corpo` das seis aulas
**Problema:** o geo-redator declarou 1390–1578 palavras e sinalizou, corretamente, que ficava
abaixo do padrão (~1900–2050 dos módulos anteriores). Duas observações sobre isso.
Primeiro, **estava tecnicamente dentro do precedente**: o Módulo 10 fechou com 1481–1955 sem
ressalva de volume. Se o julgamento parasse no número, o módulo passaria.
Segundo, e mais importante: o número era **irregular no lugar errado**. A dispersão declarada
(1390 a 1578, 13%) parecia saudável, mas escondia que a aula mais curta era justamente a que
tinha uma promessa de título por cumprir (a02, achado 2) — e não, por exemplo, uma aula
naturalmente enxuta. Contagem baixa não é defeito; contagem baixa **na metade da aula que o
título anuncia** é. Foi assim que o achado 2 foi encontrado: não pelo número, mas perguntando
o que cada aula prometeu e o que entregou.
**Correção aplicada:** os seis valores substituídos pela contagem medida após auditoria e
revisão — a01 1894, a02 1701, a03 1868, a04 1648, a05 2045, a06 1933 —, com o intervalo de
medição declarado dentro do próprio campo, para que a próxima revisão compare a mesma coisa.
O módulo saiu com dispersão de 24% (1648 a 2045), toda dentro da faixa histórica do curso, e
sem nenhuma aula estourando o teto. A a04 é agora a mais leve, e legitimamente: é a aula de
vocabulário descritivo, a de menor densidade conceitual real do módulo.
**Escopo:** correção local (metadado). Aplicada.

### 🔵 6. A a06 exercita oa03 sem crédito, e é o único lugar onde sismofácies é aplicada em decisão

**id:** `DID-M11-A06-OA03-006` · **Tipo:** oportunidade de alinhamento avaliação↔conteúdo
**Onde:** a06 · "Integrando sismoestratigrafia à interpretação estrutural" e Exemplo trabalhado
**Observação:** o exemplo trabalhado da a06 pede, entre outras coisas, que o leitor reconheça
uma camada "internamente transparente, de topo plano e base irregular" como corpo de sal — o
que é, literalmente, classificar sismofácies (oa03) e usar a classificação numa decisão
exploratória. A seção estrutural faz o mesmo com a configuração divergente. A a06 não
*ensina* sismofácies (quem ensina é a a04) e por isso **não** recebeu crédito de oa03 no mapa;
mas é o único ponto do módulo onde o oa03 aparece com consequência prática, e não como
taxonomia.
**Encaminhamento ao gerador de questionários, sem alteração de metadado:** reservar ao menos
uma questão de integração que cobre oa03 **a partir do cenário da a06**, e não da lista da
a04 — do tipo "que sismofácies você espera, e o que ela permite (e não permite) concluir sobre
a estrutura abaixo". É a diferença entre avaliar se o aluno decorou cinco configurações e
avaliar se ele sabe usá-las.
**Escopo:** nenhuma correção aplicada; encaminhamento.

---

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo trabalhado | Órfão? |
|---|---|---|---|
| `oa01` — aquisição, processamento e resolução | a01 (inteira) + a02 (inteira) | sim, nos dois | não |
| `oa02` — terminações e superfícies cronológicas | a03 (terminações) + **a05 (SB, MFS — crédito restaurado nesta revisão)** | sim, nos dois | não |
| `oa03` — sismofácies e sistemas deposicionais | a04 (inteira) | sim | não |
| `oa04` — sequências e sistema petrolífero | a05 (inteira) + a06 (inteira) | sim, nos dois | não |

**Nenhum objetivo sem seção que o ensine e nenhuma seção órfã.** Todas as seções substanciais
das seis aulas servem a um objetivo declarado. A seção "Integrando os quatro objetivos do
módulo numa única seção" (a06) é a única sem conteúdo novo próprio, e é deliberada: fecha o
módulo amarrando as seis aulas, papel equivalente ao "Encerramento do módulo" do Módulo 10.

---

## Recomendação de questionário: PARCIAIS (2 + 1 final cumulativo)

**Decisão: 2 questionários parciais mais 1 final cumulativo.** Corte entre a **a03** e a
**a04**.

Aplicação do critério fixado no Módulo 06 e reafirmado nos Módulos 09 e 10: **parciais quando o
módulo é grande E existe corte conceitual natural que nenhum objetivo atravessa.** Aqui as duas
condições se verificam, e a segunda se verifica de forma incomumente limpa.

**(1) Tamanho.** Seis aulas — no limiar que aciona parciais, e alinhado com os Módulos 06, 08 e
09 (6 aulas, parciais + final), não com os Módulos 02, 03, 04, 07 e 10 (4–5 aulas, único).

**(2) Nenhum objetivo atravessa o corte a03/a04** — o argumento de peso, e o inverso exato do
que decidiu o Módulo 10:

- `oa01` → a01, a02 → **inteiro na parcial 1**
- `oa02` → a03 (terminações) + a05 (SB, MFS) → **atravessa** ⚠️ ver ressalva abaixo
- `oa03` → a04 → **inteiro na parcial 2**
- `oa04` → a05, a06 → **inteiro na parcial 2**

**Ressalva honesta sobre o oa02, porque ela nasceu desta própria revisão:** antes do achado
`DID-M11-OA02-MAPEAMENTO-004`, o oa02 caía inteiro na parcial 1 e o corte era perfeito. Ao
restaurar o crédito da a05, o oa02 passou a ter uma perna em cada lado. Isso **não** reverte a
decisão, por três razões: (i) as duas pernas são conceitualmente distintas e avaliáveis em
separado — *terminações de refletores* (a03) e *superfícies-chave de sequência* (a05) —, ao
contrário dos cortes rejeitados no Módulo 10, onde a mesma ideia ficava partida ao meio;
(ii) a a05 só pode ensinar SB e MFS **depois** que a a03 ensinou terminação, de modo que a
ordem parcial 1 → parcial 2 é a ordem pedagógica correta e a parcial 2 reencontra o oa02
como aprofundamento, não como repetição; (iii) o questionário final cumulativo existe
justamente para avaliar o oa02 inteiro, com as duas pernas juntas. Registrado para que a
decisão não seja lida como automática.

**(3) O corte é o que o próprio objetivo do módulo anuncia.** O objetivo declarado é
"Interpretar seções sísmicas do ponto de vista estratigráfico, **do refletor individual ao
trato de sistemas deposicionais**". O corte a03/a04 é exatamente essa fronteira:

- **Parcial 1 — a01 a a03: o dado e o refletor individual.** O que a sísmica mede, como o dado
  nasce e é processado, o que ele consegue resolver, como o poço o calibra, e o que um único
  refletor e sua terminação significam. Tudo em escala de refletor.
- **Parcial 2 — a04 a a06: o pacote e a bacia.** Sismofácies (o conteúdo interno de um pacote),
  tratos de sistemas (a organização dos pacotes numa sequência) e o sistema petrolífero (a
  consequência exploratória). Tudo em escala de pacote e de bacia.

A fronteira também é profissional e não só conceitual: a parcial 1 cobre o que um geofísico de
processamento e um petrofísico entregam; a parcial 2, o que um intérprete estratigráfico faz
com essa entrega.

**(4) Ponto de verificação antes da aula mais difícil.** A parcial 1 fecha imediatamente antes
da a04–a05, e a a05 é a aula de maior densidade do módulo (achado 3), que depende de terminação
(a03) e de sismofácies (a04) simultaneamente. Entrar na a05 sem ter verificado o domínio da a03
é o cenário de falha mais provável do módulo.

### Encaminhamentos ao gerador de questionários

1. **Consultar as nove advertências no fim da auditoria científica** (`11-sismoestratigrafia-auditoria.md`).
   Sete são pontos que mudaram e onde a versão antiga produziria gabarito errado — quatro delas
   são distratores de primeira qualidade porque a versão errada é a que o senso comum sugere
   (Widess = λ/4; RC = fração de energia; NMO antes da deconvolução; topo plano do sal por
   reologia). As duas últimas (posição da discordância de ruptura na margem brasileira;
   fronteira LST/FSST) são **divergências declaradas** e **não** devem virar múltipla escolha
   com resposta única — cabem como dissertativa que peça as duas leituras.
2. **Incluir ao menos duas questões de cálculo.** O módulo tem grandezas calculáveis e só a a01
   as calcula. Candidatas: λ = V/f e os dois limiares (λ/4 e λ/8) a partir de frequência e
   velocidade dadas; RC a partir de duas impedâncias, com a pergunta complementar sobre a
   fração de **energia** (RC²); espessura de sintonia em duas profundidades diferentes para
   mostrar a degradação da resolução com a profundidade.
3. **Cobrir o oa02 pelos dois lados** (`DID-M11-OA02-MAPEAMENTO-004`): terminações na parcial 1
   (a03) e superfícies-chave SB/MFS na parcial 2 (a05). Não deixar o objetivo inteiro sair da
   a03.
4. **Cobrir oa03 também por aplicação, não só por taxonomia** (`DID-M11-A06-OA03-006`):
   reservar uma questão de integração que use o cenário da a06.
5. **Não distribuir as questões da a04 uniformemente pelas cinco configurações internas.** A
   distinção que o resto do módulo consome é progradacional/clinoformas (usada em a05 e a06) e
   transparente (usada na a06 para o sal); paralela e divergente valem uma questão de
   reconhecimento cada. A distinção carbonática plataforma × *buildup* recifal merece questão
   própria, por ser onde a auditoria achou o erro.
6. **A a06 é a matéria natural de integração** para o questionário final — é a aula que já
   pensa em módulo, e sua seção de fechamento lista explicitamente as seis contribuições.

---

## O que está bem feito

- **A cadeia de pré-requisitos é a mais limpa que este curso produziu até agora.** Cada aula
  declara no cabeçalho o que consome da anterior e, no bloco "Antes de começar", reafirma em
  linguagem de conteúdo, não de numeração. As dependências do Módulo 10 vêm com a **aula** de
  origem (Aula 01, 02, 04, 05), não só com o módulo — o leitor sabe exatamente onde voltar.
- **A a03 cita o Módulo 10 literalmente, entre aspas, e depois formaliza.** A definição de
  onlap "dada de passagem no Módulo 10" é reproduzida e então promovida a definição formal.
  É o gesto pedagógico certo para vocabulário que atravessa módulos: o aluno reconhece o que
  já leu em vez de suspeitar que são duas coisas diferentes com o mesmo nome.
- **A seção "Conectando ao vocabulário de bacias do Módulo 10" (a03) é o melhor parágrafo do
  módulo.** Ela faz o que quase nenhum material autodidata faz: mostra que dois módulos
  descrevem **o mesmo objeto** a partir de fontes de evidência diferentes, e nomeia a fonte de
  cada um. O exemplo trabalhado da a03 então executa a correspondência inteira numa seção.
- **As seis figuras ensinam algo que o texto sozinho não ensinaria**, e em todos os casos a
  ideia é intrinsecamente geométrica (geometria CMP, cadeia do sintético, os quatro padrões de
  terminação, as cinco configurações internas, a curva de nível relativo com os tratos, a
  coluna da margem brasileira). Nenhuma é decorativa.
- **Os seis exemplos trabalhados variam de tipo em vez de repetir um molde** — numérico (a01),
  diagnóstico diferencial com discriminação de hipóteses (a02), reconstrução histórica (a03),
  interpretação de ciclo de vida (a04), tradução entre representações (a05) e avaliação de
  risco exploratório (a06). O da a02 é especialmente bom de projeto: pede para *discriminar
  entre hipóteses*, não para identificar, que é o gesto profissional real.
- **A a01 abre nomeando o erro conceitual mais comum do módulo inteiro** ("uma seção sísmica
  não é uma foto do subsolo") e o módulo volta a esse fio em quase todas as aulas. Uma tese
  organizadora explícita, sustentada até o fim.
- **Os seis recaps destilam em vez de repetir**; nenhum recicla frases do corpo.
- **Nível consistente entre as seis aulas** — mesmo registro, mesma densidade de termo técnico
  destacado, mesma disposição de nomear a literatura quando importa e de omiti-la quando não.
