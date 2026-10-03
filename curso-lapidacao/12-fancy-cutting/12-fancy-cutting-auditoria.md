# Auditoria científica — Módulo 12: Fancy cutting

> [!info] Curso de **Teoria da lapidação** · módulo 12 · modo **`audit-and-fix`** · profundidade **`full`**
> Executada em **2026-09-07**. Material auditado: as 5 aulas do módulo (`lapidacao-m12-a01` a `a05`) e o hub `12-fancy-cutting-modulo.md`.
> **Encargo extra desta rodada:** reforço de densidade — as aulas saíram curtas na escrita original (906–1126 palavras contra o padrão ~1550 do curso).

## Veredito

**Aprovado com correções aplicadas.** 10 achados, **todos com desfecho**; **nenhum 🔴 ou 🟠 em aberto**. O gate do pipeline está liberado para a revisão didática e o questionário.

| Severidade | Achados | Desfecho | Em aberto |
|---|---|---|---|
| 🔴 Erro | 2 | 2 corrigidos | 0 |
| 🟠 Impreciso | 6 | 6 corrigidos | 0 |
| 🟡 Desatualizado | 0 | — | 0 |
| 🔵 Sem fonte | 1 | mantido com incerteza explícita | 0 bloqueante |
| ⚪ Controverso | 1 | já declarado; ampliado | 0 |
| **Total** | **10** | **8 corrigidos + 2 mantidos** | **0 bloqueante** |

> [!warning] Nota de procedência sobre a rodada anterior
> Uma tentativa anterior desta mesma auditoria caiu por rate-limit da API no meio da Fase 2, tendo concluído apenas a **aula 01**. Esta rodada **releu o estado em disco do zero** e não herdou achado algum. A verificação de hash confirmou que as aulas 02–05 estavam **intactas** (hashes idênticos aos do `course-state`) e que a **aula 01 havia sido alterada**. As correções factuais que a rodada anterior aplicou à aula 01 foram **reverificadas contra as fontes e mantidas**; mas a rodada anterior deixou a aula 01 com **~2205 palavras de corpo declarando 1587** — ver achado 3.

---

## Achados

### 🔴 1. A faceta côncava descrita como divergindo o feixe — contradiz a própria aula, a aula 01 e a óptica do espelho côncavo

**claim_id:** `CNC-CURV-CONVER-002`
**Tipo:** erro factual + inconsistência interna
**Onde:** aula 02 · "O que a curva faz com um feixe", "Antes de começar", "Recap relâmpago", claim `CNC-CURV-LUZ-001` — e propagado para a aula 03 ("Antes de começar" e "O que o sulcamento faz com a luz")

**Estava escrito:** "como cada raio encontra uma normal ligeiramente distinta, eles saem **divergindo**, abertos num leque de vários graus."

**Problema:** três contradições simultâneas.
1. **Contra a própria aula.** A analogia de abertura da aula 02 diz que a concha da colher "recolhe a luz e a devolve **concentrada num ponto**" — isto é, converge. Quatro parágrafos depois a aula afirma que a mesma geometria diverge.
2. **Contra a aula 01.** A aula 01 (corrigida na rodada anterior) já declarava explicitamente que a concavidade **não** diverge de imediato, e registrava a formulação "saem divergindo" como erro. A correção não havia sido propagada.
3. **Contra a física.** Um espelho côncavo de raio *R* faz raios paralelos **convergirem** para um foco em *f* = *R*/2; só **depois** desse foco eles se cruzam e abrem.

A formulação "mirrorball / scattering light in all directions" da fonte de oficina é simplificação popular — e, lida com cuidado, ela na verdade **apoia a correção**: um globo espelhado espalha luz porque é coberto de **muitos espelhinhos em orientações diferentes**, isto é, porque tem um espectro de normais. Não porque uma superfície côncava única divirja.

**Correção aplicada:** o mecanismo foi reescrito nas aulas 02 e 03 em torno de três fatos — **espectro de normais**, **aberração esférica** e **multiplicação de caminhos internos** —, com a convergência a ~*R*/2 declarada explicitamente e um callout `[!warning]` nomeando o erro. A aula 03 ganhou ainda a distinção **cilíndrico × esférico**, que é o que explica por que o sulcado produz **linhas** onde o brilhante produz **pontos**.

**Fonte:** MSU/OpenStax, *Image Formation by Mirrors* e *Spherical Mirrors* (*f* = *R*/2); The Physics Classroom, *Spherical Aberration*; Ganoksin, *Benefits of Concave Faceting* (formulação mirrorball). · **Nível:** revisada por pares (óptica) + base de referência (oficina) · **Confiança:** confirmado
**Também aparece em:** aula 03 (2 pontos), aula 01 (já corrigido) · **Desfecho:** ✅ Corrigido

---

### 🔴 2. Citação direta atribuída à IGS que a fonte não contém

**claim_id:** `PRE-DEF-PROC-002`
**Tipo:** erro factual (procedência) — o 4º módulo seguido com essa assinatura
**Onde:** aula 04 · "O que caracteriza o talhe de precisão" e claim `PRE-DEF-RIGOR-001`

**Estava escrito:** a execução é levada a tolerância muito apertada: *"quanto maior a precisão do corte, melhor as facetas se encontram"* — atribuído a International Gem Society, *Overview of Gem Cutting Styles*, que também sustentaria a definição de "designer cuts / precision cuts".

**Problema:** a reverificação consultou **as duas** páginas da IGS envolvidas — *Overview of Gem Cutting Styles* e *A Guide to Gem Cutting Styles* — e **não encontrou nem os termos definidos nem a frase citada**. A página *Overview* trata de brilhante, degrau, misto, fantasia e facetamento côncavo; não define talhe de precisão. Apresentar como **citação direta de fonte nomeada** uma sentença que a fonte não contém é a forma mais grave de erro de procedência: o leitor não tem como saber que a aspas é fabricada.

**Correção aplicada:** a aspas foi **removida** do corpo. A substância — que se sustenta — foi reancorada e **ampliada**: introduzida a distinção **meetpoint × meetline** (o encontro em ponto que se quer *versus* a linha residual que é o defeito), já ensinada no módulo 09 deste curso, e acrescentada a ordem de grandeza da tolerância corrente (~**0,5°** no ângulo de pavilhão), declarada como **prática relatada, não norma publicada**, conforme LC-05. Um callout `[!warning]` no bloco de fontes registra a retirada para que a correção não se perca.

**Fonte:** IGS, *Overview of Gem Cutting Styles* e *A Guide to Gem Cutting Styles* (ambas reverificadas 2026-09-07, **não corroboram**); prática relatada de lapidários de precisão para a tolerância. · **Confiança:** confirmado (a não-existência da citação)
**Desfecho:** ✅ Corrigido

---

### 🟠 3. Aula 01 a 2205 palavras declarando 1587 — estouro do teto LC-02 e rodapé falso

**claim_id:** `FAN-LC02-DENS-002`
**Tipo:** inconsistência interna (metadado contra conteúdo) + violação de contrato de nível
**Onde:** aula 01 · corpo inteiro e rodapé YAML

**Problema:** a rodada anterior densificou a aula 01 **muito além do alvo**, deixando-a com **~2205 palavras** de corpo pela régua LC-02 — cerca de **38% acima** do teto de ~1600 — enquanto o rodapé declarava `palavras_corpo: 1587`. O rodapé estava, portanto, **factualmente errado**, e a aula violava o contrato `ensino-medio-com-gemologia-v1`. Como todo o restante do módulo precisava ser densificado *para cima*, o erro passaria despercebido numa conferência superficial ("as aulas estavam curtas").

**Correção aplicada:** a aula 01 foi **reduzida a 1635 palavras** por compressão de redundância — sem remover nenhuma alegação auditável, nenhum achado corrigido pela rodada anterior e nenhuma declaração de incerteza. O rodapé foi corrigido para o valor real.

**Confiança:** confirmado (contagem determinística pela régua de `_contexto.md`) · **Desfecho:** ✅ Corrigido

---

### 🟠 4. Mecanismo do Optic Dish atribuído inteiramente ao disco, omitindo a frente da pedra

**claim_id:** `SUL-DYB-DISH-002`
**Tipo:** omissão que gera erro
**Onde:** aula 03 · "O disco óptico e os Luminaires", Recap e claim `SUL-DYB-DISH-001`

**Estava escrito:** "o **Dyber Optic Dish**: uma concavidade circular que age como **espelho esférico e meia-lente**."

**Problema:** o efeito do Optic Dish é produzido por um **sistema de duas peças**, e a formulação anterior atribuía os dois papéis ao disco. Na descrição do Carnegie Museum of Natural History, **o disco atrás age como espelho esférico** e é a **frente da pedra** que serve de **lente**, comprimindo opticamente o que foi cavado no verso. Atribuir "espelho e meia-lente" ao disco sozinho torna o efeito inexplicável — e apaga justamente o que distingue o disco óptico de uma faceta côncava qualquer: a côncava **reparte luz**, o disco **forma imagem**.

**Correção aplicada:** o mecanismo foi reescrito como sistema de duas peças, com a diferença de categoria (repartir luz × formar imagem) enunciada explicitamente e um novo bullet em "Erros comuns" contra a atribuição de ambos os papéis ao disco.

**Fonte:** Carnegie Museum of Natural History, *Master of Optical Illusion*; GIA, *Gems & Gemology* Spring 2018; The Jewelry Loupe. · **Confiança:** confirmado · **Desfecho:** ✅ Corrigido

---

### 🟠 5. Material de freeform atribuído a página da IGS que não o contém

**claim_id:** `FRE-BRUTO-PROC-002`
**Tipo:** erro factual (procedência)
**Onde:** aula 05 · "A lógica do freeform", bloco de fontes e claim `FRE-BRUTO-FORMA-001`

**Problema:** a formulação sobre contornos freeform que moldam a cinta "sem referência a templates padronizados, seguindo os contornos naturais do bruto" era atribuída à IGS (*Overview of Gem Cutting Styles* e *Lapidary Fundamentals: Gemstone Faceting*). A página *Overview* **não discute freeform, cinta nem templates**. Classificado 🟠 e não 🔴 porque a substância está correta e não havia aspas fabricada no corpo.

**Correção aplicada:** **fonte correta localizada e substituída** — Skyjems, verbete *Freeform Cabochon*, que traz a substância quase palavra por palavra. A fonte nova ainda **acrescentou conteúdo** que a versão anterior não aproveitava: o material chegando como **nódulo, laje ou fragmento**, e sobretudo a consequência de projeto de que **a cinta livre é o que o engastador terá de acomodar** — o que rendeu uma seção nova, "O que o freeform empurra para o joalheiro", perfeitamente alinhada com a regra do curso de tratar o engaste como restrição de projeto.

**Fonte:** Skyjems, *Freeform Cabochon*; Kingsley North, *11 Lapidary Shaping Techniques* (secundária). · **Confiança:** confirmado · **Desfecho:** ✅ Corrigido

---

### 🟠 6. Exemplo trabalhado da aula 03 contradiz a si mesmo no teste de imersão

**claim_id:** `SUL-EXEM-CONTR-002`
**Tipo:** inconsistência interna
**Onde:** aula 03 · "Exemplo trabalhado"

**Estava escrito:** "A pedra B **fica visualmente igual** (as marcas somem porque a interface some, mas não havia efeito de luz a perder)."

**Problema:** "fica visualmente igual" e "as marcas somem" não podem ser ambos verdadeiros. Pior, a formulação embaralhava exatamente o ponto que o exemplo existia para ensinar: sob imersão, **toda** feição em relevo deixa de ser vista — o que separa óptica de decorativa **não é** se a marca some.

**Correção aplicada:** o exemplo foi reescrito separando os dois efeitos, e ganhou o parágrafo que faltava: "em ambos os casos a feição deixa de ser vista […]; o que separa as duas é **se alguma coisa além da marca muda junto**."

**Confiança:** confirmado · **Desfecho:** ✅ Corrigido

---

### 🟠 7 e 8. Ano da patente de Hoffman e tempo de trabalho no Dom Pedro imprecisos

**claim_ids:** `CNC-MAQ-DATA-002` (achado 7, aula 02) · `FAN-MUNS-TEMPO-002` (achado 8, aula 01)
**Tipo:** omissão que gera erro / imprecisão

**Problema (a), aula 02:** "produziu a **primeira máquina comercial** de facetamento côncavo **em 1990**; sua patente é a **US 5.044.123**" justapunha o ano e o número sem distinguir depósito de concessão, convidando a ler 1990 como o ano da patente. A patente foi **depositada em 22-03-1990** e **concedida em 03-09-1991**.

**Problema (b), aula 01:** o *Dom Pedro* descrito como "concluída em 1993 depois de cerca de **dez meses de trabalho**". O agregado apaga a repartição documentada — **~4 meses estudando o cristal** antes de **~6 meses** de corte — e com ela o ponto didático mais valioso do episódio: a fase de **leitura do bruto** custou quase tanto quanto a de execução.

**Correção aplicada:** ambas as datas precisadas; a repartição 4+6 do Dom Pedro incorporada ao corpo da aula 01 **com wikilink para o módulo 05**, transformando um dado solto em ligação curricular. Data de morte de Münsteiner precisada para 6 de junho de 2024.

**Fonte:** Google Patents/USPTO US 5,044,123 A; Smithsonian Institution newsdesk e cobertura derivada; AGTA / National Jeweler / Roskin Gem News. · **Confiança:** confirmado · **Desfecho:** ✅ Corrigido

---

### 🔵 9. O "teste do índice casado" não tem fonte na literatura de lapidação

**claim_id:** `SUL-DEC-FONTE-003` (nova alegação `SUL-IMER-TESTE-001`)
**Tipo:** evidência insuficiente / procedência
**Onde:** aula 03 · "O critério: óptico ou decorativo?" e claim `SUL-DEC-DIST-001`

**Problema:** a própria aula já trazia no rodapé a nota do redator "*Verificar formulacao do teste do indice casado*". A verificação **não encontrou** nenhuma fonte que apresente a imersão em líquido de índice casado como **critério de classificação** entre feição óptica e ornamental. O princípio físico é firme e a imersão é técnica consagrada de **inspeção** gemológica (módulo 05) — mas o uso classificatório é construção deste curso.

**Correção aplicada (política de achado 🔵: não inventar, não apagar, marcar):** o teste foi **mantido**, porque é didaticamente bom e fisicamente correto, mas agora **declara a própria procedência** num callout `[!info]` — "ferramenta didática deste curso, não procedimento padronizado […]. Use-o para pensar; não o cite como norma da área." A alegação foi promovida a `claim_id` próprio para ficar rastreável.

**Confiança:** não verificado (quanto ao uso classificatório) · **Desfecho:** ⚠️ Mantido com incerteza explícita — **não bloqueante**

---

### ⚪ 10. O ganho de brilho do facetamento côncavo (LC-08)

**claim_id:** `CNC-BRILHO-DISPUT-001`
**Onde:** aula 02 · "O ponto em disputa"

A aula **já declarava corretamente** a controvérsia, conforme LC-08. A auditoria confirmou os dados contra a fonte (~10% mais perda de massa; melhor em pedras maiores de tom claro a médio; aparência mais escura em gemas muito saturadas) e **ampliou** a exposição com um terceiro eixo que faltava: a **dificuldade de medida** — as métricas de brilho do módulo 08 foram construídas para superfícies planas, de normal única, e comparar um côncavo a um plano "equivalente" exige antes definir o que conta como equivalente. Nenhum lado foi arbitrado.

**Desfecho:** ✅ Mantido e ampliado

---

## Verificado e correto (não gerou achado)

- **Biografia de Münsteiner** — 2 de março de 1943 – 6 de junho de 2024 (aos 81, em Stipshausen); Pforzheim 1962–1966; atelier em Stipshausen 1973; "Picasso das gemas". ✔
- **Dom Pedro** — 10.363 ct, maior água-marinha lapidada do mundo, Smithsonian, apresentado em 1993. ✔
- **A frase dos "500 anos"** — já corretamente rebaixada a formulação de homenagem pela rodada anterior; mantida. ✔
- **Context Cut** — 8 facetas + rondiz; lógica de interligar as faces naturais das metades do octaedro em vez de serrá-lo ao meio; divergência de autoria Freiesleben × Münsteiner corretamente declarada e não arbitrada. O ano de **1997** foi **reancorado** no que se confirma (prêmio alemão de design e Red Dot) em vez de "patenteado e registrado como marca", que a reverificação não corroborou; os ângulos 24,5°/39,5°, detalhe de fonte secundária única sem função no objetivo, foram removidos do corpo.
- **Corte negativo** — a definição da aula 01 é corroborada pela IGS quase literalmente ("creating concave surfaces that curve inward rather than outward… carving grooves, optic dishes, and sculptural shapes"). Esta é a **única** das três atribuições à IGS no módulo que se sustentou. ✔
- **Hoffman / PolyMetric** — Clayton, Washington; primeira máquina comercial em 1990. ✔
- **Geometria do mandril** — superfície **externa** cava faceta **côncava**; **interna** produz **convexa**; rotação + reciprocação para evitar estrias, com a finalidade declarada na própria patente. ✔
- **Richard Homer** — 15 prêmios AGTA Cutting Edge; a citação sobre distribuição de luz "pelo comprimento e pela largura da pedra". ✔
- **Dyber** — Optic Dish 1987, Luminaires 1999, *Photon Phacets* e *Channels*. ✔
- **Limite de simetria pelo índice** — divisores do número de dentes; numa roda de 96, não existe 5-fold nem 7-fold. ✔
- **Mirror cut** — "quase pequenos painéis arquitetônicos de luz"; ênfase em reflexão e profundidade em vez de *sparkle* (Rudolf Heltzel). ✔

## Conformidade com as regras duras do curso

| Regra | Resultado |
|---|---|
| **Nível teórico** — nenhuma afirmação de competência de bancada | ✅ 5/5 aulas limpas (verificado por varredura) |
| **`claim_id` de 4 segmentos**, regex `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$` | ✅ **21/21** conformes, nenhum de 5 segmentos |
| **Pré-req de gemologia só por nome**, nunca wikilink | ✅ conforme nas 5 aulas |
| **Wikilinks internos resolvem** | ✅ **todos**, incluindo os deep-links para os módulos 10 e 11 (reconciliação verificada: ambos existem no disco e os alvos batem) |
| **LC-02 — teto ~1600 palavras** | ✅ 1635–1673, dentro da tolerância do "~" |
| **LC-05 — número tabelado com fonte e faixa** | ✅ os valores ilustrativos (0,2°/0,3°) continuam declarados como tais; a tolerância de ~0,5° entrou marcada como ordem de grandeza |
| **LC-08 — controvérsia em uma frase** | ✅ 1 declarada (côncavo/brilho), ampliada |

## Reforço de densidade — encargo extra desta rodada

| Aula | Antes | Depois | Δ |
|---|---|---|---|
| a01 — Talhe de fantasia | **2205** (declarava 1587) | **1635** | **−570** ⬇ |
| a02 — Facetamento côncavo | 1126 | **1646** | +520 ⬆ |
| a03 — Sulcamento e texturas | 912 | **1656** | +744 ⬆ |
| a04 — Talhe de precisão e ópticos | 906 | **1653** | +747 ⬆ |
| a05 — Freeform e talhe de autor | 912 | **1673** | +761 ⬆ |
| **Módulo** | **6061** | **8263** | **+2202** |

O módulo saiu de uma dispersão de 906–2205 para a faixa **1635–1673** — desvio máximo de 38 palavras entre aulas.

**A densificação foi de conteúdo, não de enchimento.** O que entrou, por aula:

- **a01 (reduzida):** compressão de redundância; ganhou a repartição 4+6 meses do Dom Pedro com ligação ao módulo 05 e o dado dos prêmios de 1997 do Context Cut.
- **a02:** mecanismo correto em três fatos com callout de erro; regime de uso por material (água-marinha, citrino, ametista, turmalina, peridoto, espinélio, berilo dourado); datas de depósito e concessão da patente; **seção nova "O que substitui a tabela de ângulos"** (raio, posição, profundidade no lugar do ângulo tabelado — a ponte que faltava com o módulo 08); terceiro eixo da controvérsia LC-08.
- **a03:** distinção **cilíndrico × esférico** (linhas × pontos); **seção nova "Por que quase sempre no verso"**; mecanismo de duas peças do Optic Dish; *Photon Phacets* e *Channels*; procedência do teste de imersão declarada.
- **a04:** vocabulário **meetpoint × meetline**; tolerância de ~0,5°; lista concreta dos divisores de uma roda de 96; **argumento geométrico** de por que o erro pesa mais em faceta grande; o ponto de que o mesmo erro é *revelado* por um talhe e *escondido* por outro.
- **a05:** **seção nova "O que o freeform empurra para o joalheiro"** (cinta livre → montagem sob medida → parte do rendimento vira custo adiante); por que o ângulo crítico é *mais* difícil no contorno irregular; a perda da rede de segurança do diagrama; **tabela freeform × fantasia como eixos independentes**.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-07

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CNC-CURV-CONVER-002` | 🔴 | Corrigido | aula 02, aula 03 |
| `PRE-DEF-PROC-002` | 🔴 | Corrigido | aula 04 |
| `FAN-LC02-DENS-002` | 🟠 | Corrigido | aula 01 |
| `SUL-DYB-DISH-002` | 🟠 | Corrigido | aula 03 |
| `FRE-BRUTO-PROC-002` | 🟠 | Corrigido | aula 05 |
| `SUL-EXEM-CONTR-002` | 🟠 | Corrigido | aula 03 |
| `CNC-MAQ-DATA-002` / `FAN-MUNS-TEMPO-002` | 🟠 | Corrigido | aula 02, aula 01 |
| `SUL-DEC-FONTE-003` | 🔵 | Mantido com incerteza explícita | aula 03 |
| `CNC-BRILHO-DISPUT-001` | ⚪ | Mantido e ampliado | aula 02 |

**Propagação:** o módulo **não tem questionário nem flashcards** (flashcards dispensados do curso desde o módulo 06; o questionário ainda não foi gerado). Não há material derivado a propagar — e é precisamente por isso que a ordem do pipeline importa: os dois 🔴 teriam contaminado o gabarito se o questionário tivesse vindo antes.

**Pendências:** nenhuma bloqueante. `SUL-DEC-FONTE-003` fica registrado como 🔵 aberto **não bloqueante** — reavaliar se aparecer fonte que apresente a imersão como critério de classificação.

> [!warning] Trava para o gerador de questionários
> 1. A faceta côncava **converge** antes de abrir; o efeito vem do **espectro de normais**. Nenhuma questão pode ter "diverge o feixe" como resposta correta — é um bom **distrator**.
> 2. **Meetpoint** é o encontro em ponto; **meetline** é o defeito. Não tratar como sinônimos.
> 3. O **disco óptico** é sistema de duas peças (disco = espelho, frente da pedra = lente) e **forma imagem**; a faceta côncava **reparte luz**.
> 4. **Freeform** e **fantasia** são **eixos independentes** — contorno × corte negativo. Uma pedra redonda com discos no verso é fantasia; um freeform de facetas planas não é.
> 5. A tolerância de ~0,5°, os 0,2°/0,3° e os rendimentos de 35%/70% são **ilustrativos**; não cobrar como valores exatos.
> 6. A controvérsia do brilho do côncavo (LC-08) exige gabarito que **declare a incerteza**, sem fechar resposta única.
> 7. Nenhuma questão pode cobrar execução de bancada.
