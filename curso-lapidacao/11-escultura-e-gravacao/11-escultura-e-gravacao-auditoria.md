# Auditoria científica — Módulo 11: Escultura, gravação e contas

> [!info] Curso de **Teoria da lapidação** · módulo 11 de 14 · modo **audit-and-fix** · profundidade **full** · **2026-09-06**

**Veredito: aprovado com correções.** 8 achados — **2 🔴 · 6 🟠 · 0 🟡 · 0 🔵 · 0 ⚪** —, todos corrigidos, **nenhum em aberto**. O gate está liberado: o módulo pode seguir para a revisão didática e, depois dela, para o questionário.

**Material auditado:** as 6 aulas do módulo, 24 `claim_id` declarados nos rodapés (todos de 4 segmentos, todos casando com a regex do curso). Nenhum questionário e nenhum baralho existiam — a auditoria rodou antes deles, como o pipeline manda, e por isso não houve propagação para material derivado.

---

## Os dois achados vermelhos

### 🔴 1. Nefrita de Hotan atribuída ao Neolítico, e o início do jade chinês datado ~2.500 anos tarde demais

**claim_id:** `TRD-CHIN-MATERIAL-001` · **Tipo:** erro factual (erro de procedência) · **Onde:** aula 06, "A escola chinesa do jade — Material", tabela comparativa e recap

**Estava escrito:** "O jade chinês é, por milênios, a **nefrita** — sobretudo a de **Hotan (Khotan)**, no Xinjiang —, trabalhada desde o Neolítico (culturas Hongshan e Liangzhu, por volta de 3500 a.C.)." E no recap: "**nefrita** de Hotan desde ~3500 a.C., central por milênios".

**Problema:** dois erros encadeados.

1. **Procedência.** Hongshan e Liangzhu trabalhavam nefrita de fontes **locais** — Xiuyan, no nordeste, e depósitos do baixo Yangtzé —, não de Hotan. A nefrita de Hotan só se firma como fonte de referência muito depois, com as rotas ocidentais consolidadas na dinastia **Han**. Análises de proveniência de nefrita chegam a apontar Xiuyan ainda no Shang tardio.
2. **Cronologia.** Os jades trabalhados mais antigos da China são da cultura **Xinglongwa**, c. 6200–5400 a.C. Datar o início em ~3500 a.C. comprime o registro em cerca de 2.500 anos.

O agravante é o mesmo padrão do módulo 10: **a conclusão da seção dependia do fato errado.** O eixo "material" da comparação afirma que o jade chinês é "por milênios a nefrita" — afirmação que só se sustenta com a cronologia certa. Com ~3500 a.C. como marco inicial e Hotan como fonte de origem, a frase se apoiava em duas premissas falsas.

**Corrigido para:** cronologia refeita (Xinglongwa ~6000 a.C.; Hongshan c. 4500–3000 a.C.; Liangzhu c. 3300–2100 a.C.), com nefrita de fonte **local** nomeada, e Hotan situada explicitamente como fonte de referência posterior (rotas ocidentais / Han). Propagado para a tabela comparativa, para "Erros comuns", para "O que não concluir" e para o recap.

**Fonte:** Sotheby's, *Tracing the Origins of Chinese Archaic Jades*; Britannica, *Chinese jade* e *Jade carving*; literatura de proveniência de nefrita do Shang tardio (Yinxu); GIA, *The Evolution of Chinese Jade Carving Craftsmanship* (G&G primavera 2020). Consultadas em **2026-09-06**. · **Confiança:** confirmado.

---

### 🔴 2. O exemplo trabalhado classifica como meio relevo uma peça com partes destacadas do fundo

**claim_id:** `ESC-REL-SUBC-001` · **Tipo:** inconsistência interna + erro factual · **Onde:** aula 02, "Meio relevo e o contínuo entre os dois" e "Exemplo trabalhado (b)"

**Estava escrito:** "O **meio relevo** (*mezzo-rilievo*) fica no meio — projeção em torno de metade da espessura da figura, fundo levemente escavado, **subcorte pontual ou nenhum**." E no exemplo: "**(b)** Dragão numa peça de nefrita, corpo projetando cerca de metade da espessura, **patas dianteiras soltas do fundo por subcorte curto** [...] → **meio relevo**, tendendo a alto."

**Problema:** o *mezzo-rilievo* é definido canonicamente como figuras arredondadas até cerca de metade das proporções naturais **mas sem partes destacadas**; a presença de parte solta do fundo é exatamente o que caracteriza o *alto-rilievo*. Pior: a mesma aula afirma em "Erros comuns" que "**é o subcorte que define o alto relevo**" — e quinze linhas adiante apresenta uma peça com patas soltas por subcorte e a classifica como meio relevo. A aula contradiz a regra que ela própria acabou de dar.

Este é o achado de maior custo prático do módulo, porque o exemplo trabalhado é justamente de onde um gerador de questionário extrai a questão de classificação. O erro iria direto para o gabarito.

**Corrigido para:** meio relevo redefinido pelo critério canônico — "nenhuma parte destacada do fundo; basta uma parte solta para passar a alto relevo" — no vocabulário, no corpo e no recap; e o exemplo **(b)** reclassificado como **alto relevo no limite inferior da faixa**, com a justificativa explícita de que são as patas soltas que decidem. O ponto pedagógico original (a tenacidade excepcional da nefrita é o que permite partes destacadas) foi preservado intacto.

**Fonte:** Britannica, *Relief (sculpture)*; *Catholic Encyclopedia*, *Bas-Relief*. Consultadas em **2026-09-06**. · **Confiança:** confirmado.

---

## Os seis achados laranja

### 🟠 3. A mó de arenito de Idar-Oberstein classificada como "caso de fronteira"

**claim_id:** `TRD-IDAR-ARENITO-001` · **Tipo:** confusão de escopo · **Onde:** aula 06, "Ferramenta e força motriz", tabela comparativa, "Erros comuns", recap

**Estava escrito:** "É um regime de **abrasivo fornecido pela ferramenta**, mas por desgaste dela, não por grão preso — **um caso de fronteira** entre os dois regimes da aula 04." E, em "Erros comuns": "**Tratar a roda de arenito como abrasivo fixo comum.** [...] um caso de fronteira."

**Problema:** a mó de arenito é o caso **natural** do abrasivo **ligado (fixo)** — os grãos de quartzo estão presos pelo cimento da rocha, que é a definição de rebolo ligado. O auto-desgaste que expõe grãos novos não é um estado intermediário: é a propriedade normal de uma roda ligada friável e auto-afiante, a mesma que o **próprio módulo 04 deste curso** atribui ao carbeto de silício sem por isso tirá-lo de nenhum regime.

Duas consequências. Primeira, a seção "Erros comuns" instruía o aluno a **não** classificá-la como abrasivo fixo — ou seja, ensinava o erro na seção destinada a evitá-lo. Segunda, e mais grave para a aula: o contraste central da comparação é *Idar = grão preso à ferramenta* × *China = lama de grão livre*. Chamar Idar de "fronteira" dissolvia exatamente o eixo que a tabela comparativa afirma estar comparando.

**Corrigido para:** abrasivo **fixo** em versão natural e auto-afiante, no corpo, na tabela, em "Erros comuns" e no recap — preservando a observação correta, e bem apurada, de que nenhum grão era adicionado às rodas.

**Fonte:** GIA, *Historical Reading List: The Lapidary Tradition of Idar-Oberstein*; *The Story of Idar-Oberstein* (Gemporia) — bom arenito local como matéria-prima das mós, 183 moinhos no Idarbach e no Nahe; terminologia corrente de rebolo ligado. Consultadas em **2026-09-06**. · **Confiança:** confirmado.

---

### 🟠 4. A dicotomia de dois regimes apaga o estado intermediário que o módulo 04 ensinou

**claim_id:** `FER-SLURRY-SOLTO-001` · **Tipo:** inconsistência interna (cross-módulo) · **Onde:** aula 04, "A pergunta única", "Pontas montadas", tabela, exemplo trabalhado, recap

**Estava escrito:** "**ponta de cobre ou feltro + pasta de diamante** (solto, para alcançar recesso e para acabar)".

**Problema:** o módulo 04 — pré-requisito que esta aula cita nominalmente em "Antes de começar" — define abrasivo solto como "grão jogado livre entre a pedra e o lap, **sem ficar cravado**", e ensina na sua aula 03 que "um lap de material mole abraça o grão e o retém **cravado** na superfície". Pasta de diamante sobre cobre ou feltro é precisamente esse terceiro estado, não grão livre. Como estava escrito, o aluno que viesse do módulo 04 encontraria a mesma configuração física com dois nomes conflitantes.

**Corrigido para:** o estado intermediário foi nomeado — **grão retido no portador** —, acrescentado ao vocabulário e à lista de regimes, e a ponta de cobre/feltro com pasta foi realocada para ele no corpo, na tabela de ferramentas, no exemplo trabalhado e no recap. A correção aproxima o módulo 11 do módulo 04; **o módulo 04 não foi alterado**.

**Fonte:** módulo 04 deste curso, aulas 03 e 04 (já auditadas); literatura de lapidação sobre lap carregado. · **Confiança:** confirmado.

---

### 🟠 5. "Fresa" dada como sinônimo de "testemunho"

**claim_id:** `FER-PONTA-FIXO-001` · **Tipo:** erro de nomenclatura · **Onde:** aula 04, tabela de vocabulário

**Estava escrito:** "| **fresa / testemunho** | o cilindro de material que sobra dentro de uma broca de tubo. |"

**Problema:** em português, **fresa** designa a ferramenta rotativa de corte — precisamente o objeto que a mesma aula chama de "ponta montada" duas seções adiante. O cilindro que sobra dentro da broca de tubo é o **testemunho** (ou núcleo). O verbete dava como sinônimos dois objetos opostos, a ferramenta e a sobra, dentro da única aula do curso em que ambos aparecem juntos.

**Corrigido para:** "testemunho (núcleo)"; "fresa" removida do vocabulário, e a alegação do rodapé registra explicitamente que o termo não se aplica.

---

### 🟠 6. "Muitos camafeus históricos são meio relevo, não alto"

**claim_id:** `ESC-REL-SUBC-002` *(novo, aberto nesta auditoria)* · **Tipo:** erro factual · **Onde:** aula 02, "Meio relevo e o contínuo entre os dois", recap

**Problema:** a caracterização corrente do camafeu de pedra dura na literatura de glíptica é a de um **baixo relevo em miniatura**; o meio relevo aparece só nas peças de maior projeção. A frase trocava a faixa típica e ficava em tensão com a aula 03 do próprio módulo, que diz corretamente "em geral baixo ou meio".

**Corrigido para:** "O camafeu de pedra dura é caracteristicamente **baixo relevo**, e chega ao meio relevo só nas peças de maior projeção." Propagado para o recap.

**Fonte:** The Met, *Cameo Appearances*; literatura de *hardstone carving*; Britannica, *Relief (sculpture)*. Consultadas em **2026-09-06**.

---

### 🟠 7. "Idar-Oberstein desenvolveu o tingimento de ágata"

**claim_id:** `GRV-INT-USO-001` · **Tipo:** omissão que gera erro · **Onde:** aula 03, "Por que o material manda no projeto do camafeu", "Erros comuns"

**Problema:** colorir calcedônia artificialmente já se fazia na Antiguidade. O que Idar-Oberstein fez no século XIX foi **reconstituir e industrializar** o processo — e é isso que o relato de 1819 documenta ("Account of the Method of Colouring Agates", J. MacCulloch, *Edinburgh Philosophical Journal*). "Desenvolveu", como afirmação de origem, é falso conforme escrito.

Vale notar que a aula usa esse ponto para desarmar a acusação de falsificação — argumento que fica **mais forte** com a precedência antiga no lugar, não mais fraco.

**Corrigido para:** "Colorir calcedônia artificialmente já se fazia na Antiguidade; o que Idar-Oberstein fez no século XIX foi **reconstituir e industrializar** o tingimento de ágata (o método aparece descrito em 1819)". Propagado para "Erros comuns" **e para a aula 06** — a seção "Cor" de Idar-Oberstein repetia a mesma afirmação de origem, e a classificação inicial deste achado como afetando apenas a aula 03 estava errada. Corrigido na mesma sessão.

**Confiança:** provável (a precedência antiga é bem atestada; a filiação direta Antiguidade → Idar não é, e não foi afirmada).

---

### 🟠 8. "gato-eco" — termo inexistente, dentro de "Erros comuns"

**claim_id:** `CNT-GEOM-FORMA-001` · **Tipo:** erro de nomenclatura · **Onde:** aula 05, "Erros comuns"

**Estava escrito:** "Ele decide se o **gato-eco**, a bicolor ou o padrão facetado aparecem com a conta enfiada."

**Problema:** não existe o termo em gemologia de língua portuguesa. O fenômeno é o **olho-de-gato** (chatoyance) — nome que a própria aula usa corretamente no corpo ("conta de material chatoyante") e no recap ("efeito chatoyante"). Um nome inventado numa seção intitulada "Erros comuns" é o pior lugar possível para um termo errado.

**Corrigido para:** "olho-de-gato".

---

### 🟠 9. "Não há subcorte" no baixo relevo, em termos absolutos

**claim_id:** `ESC-REL-BAIXO-001` · **Tipo:** certeza indevida · **Onde:** aula 02, "Baixo relevo — o plano de fundo permanece intacto"

**Problema:** a definição canônica de *basso-rilievo* é "projeção leve, com **pouco ou nenhum** subcorte". A forma absoluta transformava uma tendência em critério binário e, somada à correção do achado 2, arriscava produzir uma questão de classificação com gabarito rígido demais.

**Corrigido para:** "Praticamente não há subcorte"; a alegação do rodapé registra a formulação canônica.

---

## Verificado e correto

Estas alegações foram conferidas contra fonte e **passaram** — a lista existe para que uma auditoria futura saiba o que já foi olhado.

| `claim_id` | O que foi conferido | Resultado |
|---|---|---|
| `FER-ULTRA-NEG-001` | usinagem ultrassônica a ~20 kHz **sem rotação**; lama de **carbeto de boro** ~50% água / 50% grão em volume; cavidade como negativo exato da ferramenta | ✅ os três conferem; a faixa citada na literatura para a concentração é 20–60% em volume, com 50/50 entre as figuras correntes, e a aula já declarava ambos os números como ordem de grandeza |
| `CNT-FURO-BILAT-001` | lascamento de saída; furação a partir das duas faces até o encontro no meio; **perfil em duplo cone** como assinatura da furação bilateral, com o exemplo das contas de cornalina do Vale do Indo | ✅ confirmado — perfil biconício visível em MEV é o diagnóstico corrente de furação bidirecional |
| `CNT-FURO-CRIT-001`, `CNT-FURO-DESAL-001` | furo como concentrador de tensão; escareado; desvio de broca puxada pela banda mais mole; furação alternada | ✅ |
| `TRD-IDAR-AGATA-001` | depleção das fontes locais em meados do séc. XIX e importação de ágata brasileira; ágata, calcedônia e jaspe desde o séc. XV (1497) | ✅ confirmado na fonte GIA |
| `TRD-CHIN-ABRASAO-001` | "o jade não é cortado, é desgastado"; disco *tuo* horizontal movido a **pedal**, com o jade levado à roda; *jieyu sha* de quartzo → granada/corindo → carborundo/diamante; máquinas rotativas de ferro até cerca de **1960**, quando entra o motor elétrico | ✅ |
| `GRV-CAM-CAMADA-001` | sardônica (camada clara sobre sard escuro), ônix preto-e-branco, concha (camada externa clara sobre interna escura); contraste vindo da **estratigrafia**, não de pigmento; exigência de camadas planas, paralelas e de contato limpo | ✅ |
| `GRV-INT-NEG-001`, `GRV-CAM-POS-001` | intaglio como imagem negativa e sinete, anterior ao camafeu; camafeu surgindo no mundo helenístico, sem função de selagem; intaglio clássico monocromático em cornalina, granada, ametista, heliotrópio | ✅ |
| `ESC-REL-FUNDO-001`, `ESC-REL-ALTO-001` | relevo como figura presa ao plano; alto relevo com projeção de mais de metade, partes destacadas, subcorte e fundo escavado | ✅ conferem com a classificação canônica |
| `ESC-FORM-*` (4 alegações da aula 01) | escultura sem critério externo de "pronto"; leitura por luz rasante; processo subtrativo e irreversível; *qiaose* e a orientação pelo bruto | ✅ |
| `FER-FIO-SERRA-001` | serra de fio para linha curva e contorno interno fechado; vazado; fio nu + lama (solto) × fio diamantado (fixo) | ✅ |
| — | contagem de facetas do brilhante redondo citada de passagem na aula 01 ("57 facetas") | ✅ confere com os módulos 01 e 10 — **sem contradição cross-módulo** |

---

## Regras duras do curso

| Regra | Situação |
|---|---|
| **Nível teórico, sem competência de bancada** | ✅ nenhuma aula, antes ou depois das correções, afirma ou avalia destreza manual. As seis mantêm o bloco "O que não concluir" remetendo o detalhe operacional para fora do nível do curso, e os verbos dos seis objetivos são explicar / distinguir / relacionar / descrever / comparar. |
| **`claim_id` de 4 segmentos** | ✅ 24 declarados antes da auditoria, todos casando com `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$`; **nenhum de 5 segmentos**. Um `claim_id` novo foi aberto (`ESC-REL-SUBC-002`), também de 4 segmentos. Total após a auditoria: **25**. |
| **Pré-requisito de Gemologia só por nome** | ✅ as citações (aulas 01, 02, 03, 06) são todas por nome; nenhum wikilink para fora do curso. |
| **LC-02 — teto de ~1.600 palavras** | ⚠️ **pendente, carregado para a revisão didática** — ver observações abaixo. |

---

## Observações (não são achados factuais)

**1. Os `palavras_corpo` declarados nos rodapés não vêm da régua.** Medindo a régua de `_contexto.md` ao pé da letra — `len(texto.split())` de `## Conteúdo` até o fim de `## Recap relâmpago` —, a aula 01 dá **1317** contra 1389 declarados (−72) e a aula 05 dá **1398** contra 1468 declarados (−70); mas a aula 04 dava **1569** contra 1512 declarados (**+57**) *antes de qualquer edição desta auditoria*. Ou seja: os números do rodapé são estimativas do redator, com desvio de −72 a +57, não uma medição. Os rodapés das cinco aulas editadas foram regravados com o valor medido; a aula 01, não editada, ficou com o valor declarado, para não alterar seu `content_hash` sem motivo factual. **Um re-baseline de `palavras_corpo` dos módulos 03–12 é trabalho separado.**

**2. Consequência:** pela régua real, as aulas **04 (1644)** e **06 (1619)** ficaram acima do teto de ~1600 depois das correções — e a aula 04 já estava em 1569 antes. As correções factuais **não** foram comprimidas para caber no teto; a compressão foi carregada para a revisão didática, que é a etapa dona de LC-02. **→ Resolvido na mesma sessão:** as seis aulas fecharam sob o teto (1320 · 1432 · 1450 · 1597 · 1401 · 1594), com os cortes vindos de redundância, não de conteúdo auditado. Ver `11-escultura-e-gravacao-revisao-didatica.md`.

**3. Para a revisão didática:** a aula 04 traz uma tabela-resumo das cinco ferramentas ("O quadro que a aula deixa montado") e, logo em seguida, um recap de oito *bullets* que cobre as mesmas cinco ferramentas com o mesmo conteúdo. É a maior redundância do módulo e o primeiro lugar onde cortar para recuperar LC-02. **→ Foi exatamente o corte feito.**

---

## Correções aplicadas

**Aplicadas em:** 2026-09-06

| `claim_id` | Severidade | Desfecho | Arquivo alterado |
|---|---|---|---|
| `TRD-CHIN-MATERIAL-001` | 🔴 | Corrigido | aula 06 |
| `ESC-REL-SUBC-001` | 🔴 | Corrigido | aula 02 |
| `TRD-IDAR-ARENITO-001` | 🟠 | Corrigido | aula 06 |
| `FER-SLURRY-SOLTO-001` | 🟠 | Corrigido | aula 04 |
| `FER-PONTA-FIXO-001` | 🟠 | Corrigido | aula 04 |
| `ESC-REL-SUBC-002` | 🟠 | Corrigido | aula 02 |
| `GRV-INT-USO-001` | 🟠 | Corrigido | aula 03 |
| `CNT-GEOM-FORMA-001` | 🟠 | Corrigido | aula 05 |
| `ESC-REL-BAIXO-001` | 🟠 | Corrigido | aula 02 |

**Aula 01:** auditada, **nenhum achado**, arquivo não tocado.

**Propagação:** não havia questionário nem baralho a corrigir (a auditoria é o que destrava a geração deles); flashcards estão dispensados deste curso desde o módulo 06. O hub `11-escultura-e-gravacao-modulo.md` não repete nenhum dos fatos corrigidos — só o bloco de estado precisa ser atualizado. Nenhum outro módulo repete os fatos corrigidos; o módulo 04 foi consultado e **não** alterado.

**Pendências:** nenhuma factual. A única pendência é LC-02 nas aulas 04 e 06, endereçada na revisão didática.
