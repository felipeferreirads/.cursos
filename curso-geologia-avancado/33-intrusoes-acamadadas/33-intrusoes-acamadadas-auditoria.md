# Auditoria científica — Módulo 33: Petrologia de intrusões acamadadas e processos ígneos de mineralização

**Curso:** geologia-avancado
**Módulo:** 33 — `33-intrusoes-acamadadas` (8 aulas; as antigas Aulas 04 e 05 do plano foram divididas em Parte 1 e Parte 2 já na redação)
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Auditado em:** 2026-09-29 · **Passagens:** 1
**Backup do estado antes da auditoria:** `course-state.yaml.bak-20260929-pre-m33-audit` (idêntico byte a byte ao estado no início desta passagem).
**Escopo:** as 8 aulas, o hub do módulo e os 51 `claim_id` declarados na redação (o registro de encaminhamento falava em 49; a contagem em disco por script deu 51: a01 6, a02 6, a03 6, a04 6, a05 5, a06 8, a07 7, a08 7). Não existem questionário, baralho nem glossário do módulo.
**Veredito:** **Aprovado após correções.** Foram levantados 8 vermelhos, 19 laranjas, 2 amarelos, 3 azuis e 1 branco. Todos foram tratados nas aulas, e nada ficou em aberto.

---

## Resumo por severidade

| Severidade | Levantados | Corrigidos / tratados | Em aberto |
|---|---|---|---|
| 🔴 Erro | 8 | 8 | **0** |
| 🟠 Impreciso | 19 | 19 | **0** |
| 🟡 Desatualizado | 2 | 2 (nome antigo mantido como referência) | **0** |
| 🔵 Sem fonte | 3 | 3 (dois confirmados com fonte e reescritos; um reescrito sem a afirmação não confirmada) | 0 |
| ⚪ Controverso | 1 | 1 (reescrito como debate) | 0 |
| **Total** | **33** | **33** | **0** |

Gate de qualidade: **liberado** para o questionário e os flashcards (0 vermelhos e 0 laranjas em aberto), com as restrições do fim deste relatório.

### Inversões de sentido (as perigosas)

- **🔴 5 (Aula 04) — Stokes ao contrário.** A aula dizia que a Lei de Stokes prevê sedimentação "da ordem de metros por ano ou menos" para cristais milimétricos, lenta demais para formar as pilhas cumuláticas. É o contrário: para olivina milimétrica em basalto, Stokes dá velocidades de metros por dia (experimentos de Schmidt et al., 2012, dão 0,1–10 m/dia para ortocumulatos de olivina). A objeção física real ao modelo de sedimentação é outra. A convecção da câmara é muito mais rápida que a sedimentação e pode manter os cristais em suspensão. O magma pode ter comportamento não newtoniano, com limite de escoamento. O plagioclásio flutua em líquidos ricos em Fe. E há camadas nas paredes.
- **🔴 6 (Aula 04) — cristal pequeno "ajuda" a sedimentar.** O texto dizia que a cromita sedimenta com mais facilidade por ser densa **e** ocorrer em cristais pequenos. A velocidade de Stokes cresce com o **quadrado do raio**, então o cristal pequeno sedimenta **mais devagar**. Uma cromita de 0,15 mm, mesmo três vezes mais contrastante em densidade, cai cerca de 15 vezes mais devagar que uma olivina de 1 mm. Além disso, a sedimentação da cromita não é "a explicação mais amplamente aceita": o crescimento *in situ* de cromititos (Latypov et al., 2017) é uma posição ativa.
- **🔴 7 (Aula 05) — direção da troca Fe-Mg invertida.** No exemplo, a borda da olivina fica mais rica em Fe no contato com o ortopiroxênio, e o texto concluía que "o Fe saiu da olivina para o ortopiroxênio (ou o Mg foi na direção oposta)". As duas leituras deixariam a olivina **mais magnesiana**. O certo é o contrário: o Fe entrou na olivina e o Mg saiu dela para o ortopiroxênio. O exemplo também chamava de "diagnóstica" de reequilíbrio subsólido uma feição que a reação com o líquido intercumulus (o que cristalizou o próprio ortopiroxênio intersticial) explica igualmente bem.
- **🔴 1 (Aula 01) — a origem do termo "cumulato" invertida.** A aula dizia que Wager & Deer (1939) criaram o termo "deliberadamente neutro" e que Wager, Brown & Wadsworth (1960) só o "retomaram". Mas o termo foi **proposto** em 1960 (é a primeira frase do resumo do artigo). E nasceu associado à ideia de acumulação de cristais precipitados, sobretudo por decantação. A definição sem compromisso com o mecanismo é a de Irvine (1982), e o próprio "paradigma do cumulato" foi contestado por McBirney & Hunter (1995).
- **🔴 3 (Aulas 02, 06, 07) — B2 e B3 viraram boniníticos.** A aula dizia que B1, B2 (e, na Aula 06, também B3) do Bushveld são magmas boniníticos/SHMB. Só o **B1** é de alto Mg e afinidade boninítica (andesito basáltico de alto Mg). **B2 e B3 são toleíticos** (Sharpe, 1981; Barnes, Maier & Curl, 2010). O B2 é o progenitor proposto da Zona Crítica Superior, a do Merensky; o B3, da Zona Principal.

### Padrão dominante

É o mesmo dos Módulos 27–32. Os erros graves estavam em frases de ligação e de síntese que soavam seguras e **não** estavam na lista de risco da redação: o Horizonte Sanduíche no "topo da Zona Média", o Platinova Reef na "Zona Superior", a física de Stokes e a direção da troca Fe-Mg. Os pontos que a redação marcou como incertos (idades, número de recurso omitido, debates) em geral conferiram. A exceção são as atribuições bibliográficas "de memória". Nelas estavam dois erros de autoria (cumulato, heteradcumulato) e uma referência com título e periódico inventados (Wotzlaw et al., 2012).

---

## Achados

### 🔴 1. Origem do termo "cumulato" atribuída a Wager & Deer (1939) e descrita como "deliberadamente neutra"

**claim_id:** `LAY-M33-A01-CUMULATO-HIST-001`
**Tipo:** erro factual (atribuição e sentido invertidos)
**Onde:** Aula 01 · "Um vocabulário criado para não presumir a origem"; Recap (1º item)
**Está escrito:** "Lawrence Wager e Wallace Deer [...] no fim dos anos 1930, propuseram um termo deliberadamente neutro: cumulato [...] (Wager & Deer, 1939 [...])"; "Wager retomou e sistematizou esse vocabulário duas décadas depois"; recap: "'Cumulato' (Wager & Deer, 1939) substituiu 'diferenciado' por ser um termo descritivo, não genético".
**Problema:** o termo foi **proposto** por Wager, Brown & Wadsworth (1960). O resumo do artigo diz que o termo é proposto como nome de grupo para rochas ígneas formadas por acumulação de cristais. No quadro de Wager, "cumulus" designava o precipitado cristalino acumulado, sobretudo por decantação, que é justamente o modelo que a Aula 04 critica. Quem redefiniu "cumulato" sem compromisso com o mecanismo foi Irvine (1982). McBirney & Hunter (1995, "The cumulate paradigm reconsidered") contestaram o paradigma. A narrativa de que o termo nasceu para substituir "differentiate" não tem fonte e foi retirada.
**Correção proposta:** reescrever o parágrafo e o recap: o termo nasceu em 1960 (Wager, Brown & Wadsworth), a partir do trabalho em Skaergaard iniciado em Wager & Deer (1939); nasceu ligado à acumulação de cristais (decantação); foi redefinido descritivamente por Irvine (1982); o paradigma foi criticado em 1995.
**Fonte:** Wager, Brown & Wadsworth 1960, *J. Petrol.* 1:73-85 (resumo, OUP, consultado 2026-09-29); Irvine 1982, *J. Petrol.* 23:127-162; McBirney & Hunter 1995, *J. Geol.* 103:114-122  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 04 (o texto já diz que a sedimentação motivou em parte o termo, o que está coerente com a correção e fica).

### 🔴 2. Exemplo classifica 9 % de material intercumulus como "próximo de adcumulato"; adcumulato de olivina com "mais de 90 %"

**claim_id:** `LAY-M33-A01-EXEMPLO-005` (cobre também a atribuição de `LAY-M33-A01-PATAMARES-004`)
**Tipo:** inconsistência interna
**Onde:** Aula 01 · classificação textural (item 3); Exemplo trabalhado (Passo 4)
**Está escrito:** "Um adcumulato de olivina [...] mais de 90% de olivina"; "Com apenas 9% de material intersticial, a rocha se aproxima de um adcumulato de olivina".
**Problema:** a própria aula fixa os limites de Irvine (1982): adcumulato 0–7 %, mesocumulato 7–25 %, ortocumulato acima de 25 %. Com 9 % de material intercumulus, a amostra é **mesocumulato**. E "mais de 90 % de olivina" admite até 10 % de intercumulus, o que também é mesocumulato. Um questionário tirado do exemplo teria gabarito errado. Os limites numéricos são de Irvine (1982), não de Wager, Brown & Wadsworth (1960). Alguns autores usam 5 % e 30 %.
**Correção proposta:** adcumulato "com cerca de 93 % ou mais de olivina"; segunda amostra = **mesocumulato de olivina, no limite inferior da faixa**, registrando que o crescimento adcumulus foi mais eficiente ali, mas sem chegar a adcumulato; recap e metadados atualizados; limites atribuídos a Irvine (1982).
**Fonte:** Irvine 1982, *J. Petrol.* 23:127-162 (limites 0–7/7–25/>25 %, conferidos em literatura secundária 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 01 (recap)

### 🔴 3. Magmas B2 e B3 do Bushveld apresentados como boniníticos/SHMB

**claim_id:** `LAY-M33-A06-MAGMAS-B1B2B3-005` (cobre `LAY-M33-A02-MAGMAS-PROGENITORES-004` quanto ao Bushveld)
**Tipo:** erro factual (classificação invertida)
**Onde:** Aula 02 · "Magmas progenitores" (SHMB "progenitor proposto para os pulsos B1 e B2"); Aula 06 · Bushveld ("magmas B1, B2 e B3, de afinidade boninítica/SHMB") e recap; Aula 07 · Stillwater ("comparável aos magmas B1/B2") e quadro-síntese ("Bushveld [...] magma boninítico/SHMB")
**Problema:** só o **B1** (andesito basáltico de alto Mg, afinidade boninítica) é o progenitor da Zona Inferior e da Zona Crítica Inferior. **B2 e B3 são toleíticos**: o B2 é o progenitor proposto da Zona Crítica Superior (Merensky, UG2), e o B3 da Zona Principal. Há ainda debate se o B1 é boninito verdadeiro ou komatiito contaminado (ex.: Barnes 1989, *Contrib. Mineral. Petrol.*).
**Correção proposta:** "B1 de alto Mg e afinidade boninítica/SHMB; B2 e B3 toleíticos"; reescrever as quatro ocorrências e o recap.
**Fonte:** Barnes, S.-J., Maier & Curl 2010, *Econ. Geol.* 105:1491-1511 (B1 = andesito de alto Mg; B2, B3 = toleíticos); Sharpe 1981; *South African Journal of Geology* 128(3):255 (2025, revisão dos magmas parentais)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 02, Aula 06, Aula 07

### 🔴 4. Horizonte Sanduíche colocado "no topo da Zona Média" de Skaergaard

**claim_id:** `LAY-M33-A03-SANDUICHE-007` (criado pela auditoria)
**Tipo:** erro factual
**Onde:** Aula 03 · "Zoneamento estratigráfico"
**Está escrito:** "com o Horizonte Sanduíche marcando o topo da Zona Média onde as frentes de cristalização convergem".
**Problema:** o Horizonte Sanduíche fica no **topo da Série Estratificada**, acima da UZc, onde ela encontra a Série de Borda Superior. É o último líquido da câmara. A Zona Média fica no meio da pilha. A própria aula e a Aula 06 descrevem o Sanduíche como o ponto de convergência das frentes, e isso só pode ser o topo da Série Estratificada.
**Correção proposta:** "com o Horizonte Sanduíche no topo da Série Estratificada (acima da UZc), onde ela encontra a Série de Borda Superior".
**Fonte:** Wager & Brown 1968; Nielsen 2004, *J. Petrol.* 45:507; skaergaard.org (Layered Series)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🔴 5. Lei de Stokes "prevê velocidades muito baixas" (INVERSÃO)

**claim_id:** `LAY-M33-A04P1-SEDIMENTACAO-001`
**Tipo:** erro factual (inversão)
**Onde:** Aula 04 · "O modelo clássico" (1º tópico das dificuldades); "Cristalização in situ" (2º parágrafo); Recap (1º item)
**Está escrito:** "a Lei de Stokes preveja velocidades de sedimentação muito baixas para cristais de tamanho normal — da ordem de metros por ano ou menos para cristais milimétricos, ordens de grandeza mais lentas do que seria necessário"; "dispensa a necessidade de velocidades de sedimentação fisicamente implausíveis"; recap "velocidades de sedimentação implausivelmente lentas".
**Problema:** a conta dá o contrário. Com Δρ ≈ 400 kg/m³, r = 0,5 mm e η ≈ 50 Pa·s, v = 2Δρgr²/9η ≈ 4×10⁻⁶ m/s, cerca de 0,4 m/dia. Experimentos com olivina em basalto dão tempos de formação de cumulato equivalentes a 0,1–10 m/dia (Schmidt et al., 2012). As objeções reais ao modelo são outras: (a) a convecção é muito mais rápida que a sedimentação e pode manter os cristais em suspensão (o efeito é debatido; Martin & Nokes, 1988, acham a sedimentação eficiente mesmo assim); (b) as propriedades não newtonianas do magma, com possível limite de escoamento (McBirney & Noyes, 1979); (c) o plagioclásio flutua em líquidos ricos em Fe; (d) há camadas nas paredes.
**Correção proposta:** reescrever o 1º tópico com as objeções corretas e ajustar o parágrafo da cristalização *in situ* e o recap.
**Fonte:** Schmidt et al. 2012, *Contrib. Mineral. Petrol.* 164:959; Martin & Nokes 1988, *Nature* 332:534; McBirney & Noyes 1979, *J. Petrol.* 20:487-554  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 04 (recap, parágrafo da cristalização *in situ*)

### 🔴 6. Cromita "sedimenta mais" por ter cristais pequenos; sedimentação dada como explicação "mais amplamente aceita" (INVERSÃO)

**claim_id:** `LAY-M33-A04P1-CROMITITO-DENSIDADE-005`
**Tipo:** erro factual (inversão) + certeza indevida
**Onde:** Aula 04 · "Um debate aberto"; Exemplo (Passos 1 e 5); Recap (último item)
**Está escrito:** "cromitito [...] por causa da alta densidade e do pequeno tamanho de cristal da cromita"; "ocorre tipicamente em cristais pequenos — condições em que a Lei de Stokes prevê velocidades de sedimentação mais plausíveis"; "a sedimentação gravitacional continua sendo a explicação mais amplamente aceita".
**Problema:** v ∝ r², então cristal pequeno sedimenta **mais devagar**. O tamanho pequeno da cromita joga **contra** a sedimentação; é a densidade alta que joga a favor. E a sedimentação da cromita não é consenso. Latypov et al. (2017) propõem que os cromititos maciços do Bushveld cresceram *in situ* no assoalho a partir de um líquido saturado só em cromita. Há também modelos de fluxos de papa de cromita e revisões recentes que tratam o tema como aberto.
**Correção proposta:** "a densidade alta da cromita torna a sedimentação fisicamente mais plausível (o tamanho pequeno joga contra: v ∝ r²); por isso o cromitito é o caso em que a sedimentação, inclusive como fluxos de papa de cromita, é mais defendida, mas modelos de crescimento *in situ* (Latypov et al., 2017) a contestam". Passos 1 e 5 e recap alinhados.
**Fonte:** Latypov et al. 2017, *J. Petrol.* 58:1899-1940; revisão "Massive chromitites of the Bushveld Complex: a critical review of existing hypotheses", *Earth-Sci. Rev.* (2024); física de Stokes (consolidada)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 04 (exemplo, recap)

### 🔴 7. Direção da troca Fe-Mg olivina–ortopiroxênio invertida; reequilíbrio dado como "diagnóstico" (INVERSÃO)

**claim_id:** `LAY-M33-A05P2-EXEMPLO-005`
**Tipo:** erro factual (inversão) + certeza indevida
**Onde:** Aula 05 · Exemplo (Passos 2 e 3)
**Está escrito:** "é a assinatura diagnóstica de troca por difusão em estado sólido"; "consistente com um reequilíbrio que empurrou Fe da olivina para o ortopiroxênio (ou Mg na direção oposta)".
**Problema:** a borda da olivina ficou **mais rica em Fe** (Fo₈₁ contra Fo₈₅ no núcleo). Então o Fe **entrou** na olivina e o Mg **saiu** dela para o ortopiroxênio. As duas alternativas do texto deixariam a olivina mais magnesiana. Além disso, o ortopiroxênio é **intersticial**, isto é, cristalizou do líquido intercumulus. Uma borda mais ferrosa só junto a ele também é a assinatura da reação com esse líquido (o deslocamento do líquido aprisionado da própria aula, Barnes, 1986). Não dá para chamar de "diagnóstica" de difusão subsólida sem perfil de difusão.
**Correção proposta:** Passo 2 apresenta as duas leituras (reação com o líquido intercumulus que cristalizou o ortopiroxênio × reequilíbrio subsólido) e diz como distingui-las (forma do perfil núcleo–borda e comparação com o ortopiroxênio adjacente); Passo 3 corrige a direção: o Fe entrou na olivina e o Mg passou para o ortopiroxênio.
**Fonte:** Barnes 1986, *Contrib. Mineral. Petrol.* 93:524-531; princípio de partição Fe-Mg (consolidado)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 05 (recap não repete a direção; sem alteração)

### 🔴 8. Platinova Reef colocado na Zona Superior de Skaergaard

**claim_id:** `LAY-M33-A06-PLATINOVA-003`
**Tipo:** erro factual
**Onde:** Aula 06 · parágrafo da estratigrafia de Skaergaard; Recap (2º item)
**Está escrito:** "Nas últimas décadas da Zona Superior, foi identificado o Platinova Reef".
**Problema:** o Platinova Reef (Pd-Au) está no **Triple Group**, nos ~100 m superiores da **Zona Média** da Série Estratificada, e não na Zona Superior. Foi descoberto pela Platinova Resources no fim dos anos 1980 (Bird et al., 1991; Andersen et al., 1998). O líquido já era muito rico em Fe nesse ponto, e a ligação com a evolução em Fe se mantém. O que está errado é a posição estratigráfica. Há também um erro de redação: "últimas décadas".
**Correção proposta:** "Na parte superior da Zona Média, no chamado Triple Group, foi identificado [...]", mantendo a ligação com a evolução avançada em Fe.
**Fonte:** Andersen et al. 1998, *Econ. Geol.* 93(4):488 ("The Triple Group and the Platinova gold and palladium reefs in the Skaergaard Intrusion"); Nielsen et al. (GEUS Bulletin, "The PGE-Au mineralisation of the Skaergaard intrusion")  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 06 (recap)

### 🟠 9. Heteradcumulato atribuído a Irvine (1982); cadacristais "de outra geração do mesmo mineral"

**claim_id:** `LAY-M33-A01-HETERADCUMULATO-003`
**Tipo:** erro factual (atribuição) + imprecisão de definição
**Onde:** Aula 01 · item 4; metadados; Aula 05 · Fontes (Irvine 1982 "formalização da textura heteradcumulática")
**Problema:** o termo vem de Wager, Brown & Wadsworth (1960), junto com ortocumulato e adcumulato; Irvine (1982) o manteve. No heteradcumulato, o oicocristal é de um mineral **diferente** da fase cumulus, que cresce a partir do líquido intercumulus. Oicocristal do mesmo mineral não é heteradcumulato.
**Correção proposta:** retirar "ou de outra geração do mesmo mineral"; atribuir o termo a Wager, Brown & Wadsworth (1960), mantido por Irvine (1982).
**Fonte:** Wager, Brown & Wadsworth 1960; literatura sobre oicocristais (*J. Petrol.* 57(6):1171 (2016), complexo de Ntaka)  ·  **Nível:** revisada por pares
**Confiança:** provável
**Também aparece em:** Aula 05 (Fontes)

### 🟠 10. Crescimento adcumulus descrito como o cristal "incorporando" o líquido aprisionado

**claim_id:** `LAY-M33-A05P2-ADCUMULUS-COMPACTACAO-001`
**Tipo:** omissão que gera erro
**Onde:** Aula 01 · item 3 (adcumulato); Aula 05 · "Crescimento adcumulus e compactação"
**Problema:** um bolsão fechado de líquido aprisionado não produz adcumulato. Se cristaliza isolado, dá fases intersticiais próprias, ou seja, um ortocumulato. O crescimento adcumulus exige que o líquido intersticial continue **em comunicação com o magma principal**, por difusão ou convecção através dos poros. Esse líquido traz os componentes do mineral cumulus e leva embora os que ele rejeita. O texto dá a entender que o cristal "engole" o próprio líquido aprisionado.
**Correção proposta:** acrescentar, nas duas aulas, que o crescimento adcumulus depende de troca com o magma sobrejacente; sem essa troca, o líquido preso cristaliza como material intercumulus.
**Fonte:** Wager, Brown & Wadsworth 1960; Wager 1963; Hunter 1996 (in Cawthorn, ed., *Layered Intrusions*)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 01, Aula 05

### 🟠 11. Skaergaard "demonstrou de forma inequívoca" e "resolveu" o debate Bowen–Fenner

**claim_id:** `LAY-M33-A02-FENNER-BOWEN-003` (cobre `LAY-M33-A06-BOWEN-FENNER-002`)
**Tipo:** certeza indevida
**Onde:** Aula 02 · sistema fechado; Aula 03 · variação críptica; Aula 06 · título de seção, 3º parágrafo e recap
**Problema:** Skaergaard é o caso-tipo da tendência de enriquecimento em Fe, e a maior parte dos trabalhos conclui por um trend de Fenner. Mas a trajetória do líquido de Skaergaard foi e é debatida: Hunter & Sparks (1987) defenderam enriquecimento em sílica depois da entrada dos óxidos, contra McBirney & Naslund (1990) e Brooks & Nielsen (1990). Thy, Lesher & Tegner (2009) revisitou a questão, e há imiscibilidade de líquidos ricos em Fe e em Si nos estágios tardios (Jakobsen et al., 2005). "Resolveu de forma inequívoca" é mais do que a literatura sustenta.
**Correção proposta:** "tornou-se o caso-tipo da tendência de Fenner; a maior parte dos trabalhos confirma o enriquecimento em Fe, mas a extensão desse enriquecimento no líquido e a trajetória final (com imiscibilidade de líquidos) seguiram debatidas". Título da seção da Aula 06 ajustado.
**Fonte:** Thy, Lesher & Tegner 2009, *Contrib. Mineral. Petrol.* 157:735-747 ("The Skaergaard liquid line of descent revisited"); Hunter & Sparks 1987; McBirney & Naslund 1990; Jakobsen et al. 2005, *Geology* 33:885  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aulas 02, 03, 06

### 🟠 12. Reversões críticas "só podem" ser explicadas por recarga

**claim_id:** `LAY-M33-A02-EXEMPLO-006`
**Tipo:** certeza indevida
**Onde:** Aula 02 · Exemplo (Passo 2); Aula 03 · variação críptica ("assinatura diagnóstica") e recap
**Problema:** a recarga é a interpretação mais comum de reversões para composições mais magnesianas, mas não a única. O deslocamento do líquido aprisionado (Aula 05; Barnes, 1986) produz variações de Fo e Mg# que acompanham a fração de líquido preso. Camadas pobres em líquido aprisionado (adcumulatos, cromititos) podem parecer "reversões". Mudanças de pressão ou de fO₂ também deslocam a composição. O próprio módulo ensina isso na Aula 05.
**Correção proposta:** "a interpretação mais comum é a injeção de magma novo, desde que se descartem efeitos pós-cumulus (Aula 05)".
**Fonte:** Barnes 1986; Irvine 1982  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aulas 02 e 03

### 🟠 13. Magma progenitor do Muskox chamado de komatiítico e "o mais magnesiano" dos quatro

**claim_id:** `LAY-M33-A07-MUSKOX-MAGMA-009` (criado pela auditoria; cobre `LAY-M33-A02-MAGMAS-PROGENITORES-004` quanto ao Muskox)
**Tipo:** impreciso
**Onde:** Aula 02 · 3º item dos magmas progenitores e recap; Aula 07 · Muskox, quadro-síntese e recap
**Problema:** o magma parental do Muskox é **picrítico**, com ~13–15 % de MgO, abaixo do limite komatiítico de 18 % que a própria Aula 02 cita. "O mais magnesiano entre os quatro" não tem sustentação: o B1 do Bushveld e o magma tipo U do Stillwater também são de alto Mg. O Muskox pode continuar como exemplo de LIP de afinidade picrítica.
**Correção proposta:** "picrítico (~13–15 % MgO)"; retirar "komatiítico" do Muskox e o superlativo; manter a menção a magmas komatiíticos como progenitores discutidos para outras intrusões, sem nomear o Muskox.
**Fonte:** *Lithos* (2024), "The Muskox intrusion: Overview of a major open-system layered intrusion and its role as a sub-volcanic magma reservoir in the Mackenzie large igneous province"; Irvine 1977, 1980  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aulas 02 e 07

### 🟠 14. Stillwater com um único progenitor boninítico/SHMB

**claim_id:** `LAY-M33-A07-STILLWATER-MAGMA-008` (criado pela auditoria)
**Tipo:** impreciso
**Onde:** Aula 07 · 2º parágrafo; quadro-síntese; Aula 02 · recap ("boninítico/SHMB (Bushveld, Stillwater)")
**Problema:** no Stillwater se reconhecem **dois** magmas parentais (Irvine, Keith & Todd, 1983). O tipo U (ultramáfico, de alto Mg e afinidade boninítica/SHMB) gerou a Série Ultramáfica e a base da Série Bandada. O tipo A (anortosítico, de afinidade toleítica) gerou o restante da Série Bandada. A transição fica na base da Zona Troctolito-Anortosito I, onde está o Reef J-M.
**Correção proposta:** descrever os dois magmas; paralelo com o Bushveld: B1 ≈ U, B2/B3 ≈ A.
**Fonte:** Irvine, Keith & Todd 1983, *Econ. Geol.* 78:1287-1318; *J. Petrol.* 65(4) egae014 (2024)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aulas 02 e 07

### 🟠 15. Bushveld "em funil" e Skaergaard "tabular"

**claim_id:** `LAY-M33-A03-FORMAS-001`
**Tipo:** impreciso
**Onde:** Aula 03 · 1º parágrafo e recap; Aula 07 · Muskox ("corpo em funil, menor em escala do que o Bushveld")
**Problema:** o Bushveld (Suíte Acamadada de Rustenburg) é descrito como uma intrusão **lopolítica**, isto é, lobos em forma de pires ou bacia com mais de 66 000 km², e não como funil. O exemplo clássico de corpo em funil (calha alimentada por dique) é o **Muskox**. Skaergaard também não é uma lâmina: Nielsen (2004) o modela como uma **caixa irregular** de ~11 × 8 × 3,4–4 km.
**Correção proposta:** "em funil ou calha (Muskox); lopolíticos, em pires (Bushveld); tabulares ou em caixa (Skaergaard, uma caixa irregular de ~11 × 8 × 4 km; Stillwater, hoje basculado)".
**Fonte:** Nielsen 2004, *J. Petrol.* 45:507-530; Cawthorn 2015 (in Charlier et al., eds., *Layered Intrusions*, Springer)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 03 (recap), Aula 07

### 🟠 16. Ordem "olivina → clinopiroxênio → plagioclásio" dada como padrão geral

**claim_id:** `LAY-M33-A03-ORDEM-CRISTALIZACAO-008` (criado pela auditoria)
**Tipo:** confusão de escopo
**Onde:** Aula 03 · "Zoneamento estratigráfico"
**Problema:** em magmas toleíticos a baixa pressão, o plagioclásio costuma entrar **antes** do clinopiroxênio (Skaergaard: olivina + plagioclásio, depois clinopiroxênio). No Bushveld e no Stillwater, a ordem é olivina/ortopiroxênio → plagioclásio → clinopiroxênio. A ordem depende do magma e da pressão, e a própria Aula 02 diz isso.
**Correção proposta:** "seguida pela entrada de plagioclásio e clinopiroxênio (em ordem que depende do magma: em magmas toleíticos a baixa pressão o plagioclásio costuma vir antes)".
**Fonte:** Wager & Brown 1968; Cawthorn 2015; Irvine et al. 1983  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 17. Deslocamento do líquido aprisionado descrito como mudança da rocha total

**claim_id:** `LAY-M33-A05P2-TRAPPED-LIQUID-SHIFT-002`
**Tipo:** impreciso (conceito)
**Onde:** Aula 05 · "O deslocamento do líquido aprisionado"; Recap (2º item)
**Problema:** no modelo de Barnes (1986), o sistema é **quimicamente fechado**: a rocha total não muda. O que se desloca é a **composição dos minerais cumulus**, que reagem com o líquido aprisionado enquanto ele cristaliza (a olivina fica menos magnesiana, por exemplo). O tamanho do desvio depende da porosidade inicial e da moda. O texto dizia que o desvio atinge "retroativamente a composição média que se atribuiria à rocha como um todo" e que se corrige "a partir de uma análise de rocha total". Também dizia que a correção é "essencial" para o fator R, uma ligação exagerada: o fator R depende do teor de metais no magma e no sulfeto.
**Correção proposta:** reescrever o parágrafo: o desvio afeta a composição do mineral cumulus, e é preciso corrigi-lo antes de usar essa composição para inferir o líquido; a relação com o fator R fica indireta (reconstrução do magma parental).
**Fonte:** Barnes 1986, *Contrib. Mineral. Petrol.* 93:524-531 (resumo: sistema quimicamente fechado; desvio da composição do mineral cumulus)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 05 (recap)

### 🟠 18. Exemplo da Aula 06 dá a mistura de magmas como "modelo mais aceito" de cromitito

**claim_id:** `LAY-M33-A06-EXEMPLO-008`
**Tipo:** inconsistência interna
**Onde:** Aula 06 · Exemplo (Passo 2)
**Problema:** a Aula 08 (e o encaminhamento do módulo) trata os modelos de cromitito como debate aberto (mistura de magmas, adição de sílica, pressão/fO₂, crescimento *in situ*). O exemplo contradiz isso.
**Correção proposta:** "os modelos concorrentes de cromitito (Aula 08) em geral invocam uma perturbação do sistema (magma novo, contaminação, mudança de pressão); a ausência de cromitito é consistente com um sistema fechado, mas não o prova".
**Fonte:** Irvine 1975, 1977; Latypov et al. 2017, 2018  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 19. Bushveld responde pela "maior parte da produção" de todos os EGP

**claim_id:** `LAY-M33-A06-BUSHVELD-PRODUCAO-009` (criado pela auditoria)
**Tipo:** impreciso
**Onde:** Aula 06 · 1º parágrafo do Bushveld
**Problema:** a África do Sul (Bushveld) é o maior produtor de EGP no conjunto e domina a platina e o ródio, mas a **Rússia é o maior produtor mineiro de paládio** (USGS MCS 2026). O Bushveld concentra ~75 % dos recursos mundiais de platina e ~50 % dos de paládio.
**Correção proposta:** "o maior produtor mundial de EGP no conjunto (e de longe o de platina e ródio; no paládio divide a liderança com Noril'sk, na Rússia), com a maior parte das reservas mundiais de platina".
**Fonte:** USGS, *Mineral Commodity Summaries 2026*, Platinum-Group Metals  ·  **Nível:** base de referência
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 20. Zona Inferior do Bushveld "(dunito e harzburgito)"

**claim_id:** `LAY-M33-A06-ZONA-INFERIOR-010` (criado pela auditoria)
**Tipo:** impreciso
**Onde:** Aula 06 · estratigrafia do Bushveld
**Problema:** a Zona Inferior é dominada por **ortopiroxenito**, com harzburgito e dunito subordinados, em unidades cíclicas de 800–1300 m de espessura.
**Correção proposta:** "Zona Inferior (sobretudo ortopiroxenito, com harzburgito e dunito)".
**Fonte:** Cawthorn 2015; literatura da Suíte Acamadada de Rustenburg  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 21. Referência de Wotzlaw et al. (2012) com título e periódico inventados

**claim_id:** `LAY-M33-A06-SKAERGAARD-IDADE-001`
**Tipo:** erro factual (bibliografia)
**Onde:** Aula 06 · Fontes
**Está escrito:** "Wotzlaw, J.-F. et al. (2012), 'Skaergaard intrusion — A geochronological time capsule', *Geology* ou periódico correlato".
**Problema:** a referência real é Wotzlaw, Bindeman, Schaltegger, Brooks & Naslund (2012), "High-resolution insights into episodes of crystallization, hydrothermal alteration and remelting in the Skaergaard intrusive complex", *Earth and Planetary Science Letters* 355–356:199–212. Ela dá 55,960 ± 0,018 Ma para a cristalização do zircão e ~56,02 Ma para o posicionamento. A idade de ~56 Ma do texto está certa.
**Correção proposta:** substituir a referência.
**Fonte:** Wotzlaw et al. 2012, EPSL, doi:10.1016/j.epsl.2012.08.043  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 22. Reef J-M "em piroxenito e norito"

**claim_id:** `LAY-M33-A07-JM-REEF-002`
**Tipo:** impreciso
**Onde:** Aula 07 · 3º parágrafo; metadados
**Problema:** o Reef J-M fica na **Zona com Olivina I** (OB-I; também chamada Zona Troctolito-Anortosito I) da Série Bandada Inferior. Ali predominam troctolito, olivina gabronorito e anortosito. O reef é uma zona de 0,5–3 % de sulfetos disseminados, com média de ~18 ppm de Pt + Pd (Pd/Pt ≈ 3), o maior teor médio entre os depósitos de EGP conhecidos. O teor foi conferido e está correto; a rocha hospedeira não.
**Correção proposta:** "na zona com olivina (OB-I) da Série Bandada Inferior, em troctolito, olivina gabronorito e anortosito, com ~18 ppm de Pt + Pd em média".
**Fonte:** Todd et al. 1982, *Econ. Geol.* 77:1454; Jenkins et al. 2021, *Precambrian Res.* (USGS); Zientek (USGS)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 23. Irvine "formalizou" a unidade cíclica e a noção de recarga; "doze unidades = doze recargas"

**claim_id:** `LAY-M33-A07-UNIDADE-CICLICA-005`
**Tipo:** impreciso (atribuição) + imprecisão no exemplo
**Onde:** Aula 07 · Muskox (3º parágrafo); Exemplo (Passo 2)
**Problema:** Brown (1956), em Rum, já descrevia unidades cíclicas (peridotito → allivalito) como resultado de pulsos sucessivos de magma. O Muskox, com ~42 unidades cíclicas (Irvine & Smith, 1967), tornou-se o exemplo norte-americano clássico e foi a base dos modelos de Irvine, mas não "formalizou" a noção pela primeira vez. No exemplo, doze unidades implicam o preenchimento inicial mais **onze** recargas, não "pelo menos doze recargas".
**Correção proposta:** citar Brown (1956) como precedente e o Muskox (~42 unidades) como caso clássico desenvolvido por Irvine; no exemplo, "doze pulsos: o preenchimento inicial e pelo menos onze recargas".
**Fonte:** Brown 1956, *Phil. Trans. R. Soc. Lond. B* 240:1-53; Irvine & Smith 1967; *Lithos* (2024), visão geral do Muskox  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 07 (recap)

### 🟠 24. Contaminação externa por S dada como gatilho "mais frequente" também dos reefs de EGP

**claim_id:** `LAY-M33-A08-SATURACAO-ENXOFRE-002`
**Tipo:** confusão de escopo
**Onde:** Aula 08 · 1º parágrafo
**Problema:** o parágrafo abre com "reefs de EGP, sulfetos maciços e disseminados de Ni-Cu" e diz que o gatilho "mais frequente nos modelos aceitos para os grandes depósitos" é a contaminação externa. Isso vale para os grandes depósitos de **Ni-Cu** em condutos e no contato basal (Noril'sk, Voisey's Bay, Duluth). Para os **reefs de EGP** das grandes intrusões acamadadas, os modelos são sobretudo internos: mistura de magmas, fracionamento, mudança de pressão e, para alguns autores, fluidos. É o que as próprias Aulas 06–08 descrevem.
**Correção proposta:** separar os dois grupos na frase.
**Fonte:** Naldrett 2004, *Magmatic Sulfide Deposits* (Springer); Barnes, S.-J. & Lightfoot 2005, *Econ. Geol.* 100th Anniversary Vol.  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 25. Modelo de adição de sílica atribuído só a trabalhos recentes

**claim_id:** `LAY-M33-A08-CROMITITO-MODELOS-003`
**Tipo:** impreciso (atribuição)
**Onde:** Aula 08 · 2º tópico dos modelos de cromitito; Fontes
**Problema:** a adição de sílica (contaminação por material rico em sílica) foi proposta por Irvine (1975), também a partir do Muskox, **antes** do modelo de mistura (Irvine, 1977). Kinnaird et al. (2002) retomaram a contaminação para o Bushveld. O modelo de mudança de pressão tem versões modernas explícitas (Latypov et al., 2018).
**Correção proposta:** "Adição de sílica (Irvine, 1975, depois aplicada ao Bushveld)"; Fontes com Irvine 1975 e Latypov et al. 2018.
**Fonte:** Irvine 1975, *Geochim. Cosmochim. Acta* 39:991-1020; Latypov et al. 2018, *Nat. Commun.* 9:462  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 26. Remissões quebradas para a "Aula 04 (Parte 2)"

**claim_id:** `LAY-M33-MOD-REMISSOES-001` (de módulo; registrado só no relatório, no manifesto e no estado)
**Tipo:** inconsistência interna
**Onde:** Aula 01 · "Material pós-cumulus" ("A Aula 04 (Parte 2) trata em profundidade dos processos pós-cumulus"); Aula 04 · "Próxima aula" ("A Aula 04 (Parte 2) trata [...]")
**Problema:** os processos pós-cumulus estão na **Aula 05** (Parte 2 da diferenciação). A renumeração pela divisão deixou as duas remissões apontando para uma aula que não existe.
**Correção proposta:** "Aula 05 (Parte 2)".
**Fonte:** hub do módulo e `course-state.yaml` (renumeração de 2026-09-29)  ·  **Nível:** —
**Confiança:** confirmado
**Também aparece em:** Aulas 01 e 04

### 🟠 27. Hub fecha o debate que a Aula 04 deixa aberto

**claim_id:** `LAY-M33-MOD-HUB-DEBATE-002` (de módulo)
**Tipo:** inconsistência interna
**Onde:** hub · "Pontos de dificuldade"
**Está escrito:** "A imagem clássica do cristal denso afundando numa câmara líquida foi substituída por modelos de crescimento in situ [...]"; "podem reequilibrar completamente a composição do mineral cumulus".
**Problema:** a Aula 04 apresenta os três mecanismos como não excludentes e em debate, e a Aula 05 fala em deslocamento "mensurável", não "completo".
**Correção proposta:** "foi fortemente contestada por modelos de crescimento *in situ* e de convecção duplo-difusiva, sem que nenhum tenha substituído os outros"; "podem modificar de forma mensurável (às vezes substancial)".
**Fonte:** Aulas 04 e 05 (corrigidas); Latypov et al. 2024, *Earth-Sci. Rev.* 249:104653  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟡 28. Muskox "nos Territórios do Noroeste"

**claim_id:** `LAY-M33-A07-MUSKOX-IDADE-CONTEXTO-004`
**Tipo:** desatualização
**Onde:** Aula 07 · Muskox (1º parágrafo) e recap
**Problema:** desde 1999, a área do Muskox fica em **Nunavut**. A idade de 1,27 Ga (1269 ± 1 Ma), a ligação com a LIP de Mackenzie e com os basaltos do Rio Coppermine e as ~42 unidades cíclicas foram conferidas.
**Correção proposta:** "em Nunavut (até 1999, parte dos Territórios do Noroeste)".
**Fonte:** LeCheminant & Heaman 1989, *EPSL* 96:38-48; *Precambrian Res.* (2009), "Age and Nd–Hf isotopic constraints on the origin of marginal rocks from the Muskox layered intrusion (Nunavut, Canada)"  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 07 (recap)

### 🟡 29. "Departamento Nacional de Produção Mineral" nas Fontes

**claim_id:** `LAY-M33-A08-FONTE-ANM-008` (criado pela auditoria)
**Tipo:** desatualização
**Onde:** Aula 08 · Fontes
**Problema:** o DNPM foi substituído pela **Agência Nacional de Mineração (ANM)** (Lei 13.575/2017, instalada em 2018).
**Correção proposta:** "Agência Nacional de Mineração (ANM; antigo DNPM)".
**Fonte:** Lei nº 13.575/2017  ·  **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** —

### 🔵 30. "Evidências isotópicas (razões de Sr)" atribuídas à escola da cristalização *in situ*

**claim_id:** `LAY-M33-A04P1-DEBATE-ABERTO-004`
**Tipo:** evidência insuficiente
**Onde:** Aula 04 · "Um debate aberto" e recap (4º item)
**Problema:** não confirmei que o argumento central de Latypov, Chistyakova e colaboradores seja isotópico (Sr). A evidência que eles apresentam é sobretudo **de campo e textural**. Reefs e cromititos cobrem paredes subverticais e até invertidas de depressões do assoalho. Há camadas que acompanham pisos inclinados. E a pilha cumulática do Bushveld estava quase toda sólida sob poucos metros de papa. A heterogeneidade de Sr no plagioclásio do Bushveld é usada na literatura em sentidos diversos.
**Correção proposta:** trocar "evidências de campo e isotópicas (razões de Sr, por exemplo)" por "evidências de campo e texturais (camadas e reefs que acompanham pisos inclinados, paredes subverticais e até invertidas de depressões do assoalho)"; recap alinhado.
**Fonte:** Latypov et al. 2024, *Earth-Sci. Rev.* 249:104653; Latypov et al. 2017  ·  **Nível:** revisada por pares
**Confiança:** não verificado (a parte isotópica) → retirada
**Também aparece em:** Aula 04 (recap)

### 🔵 31. Ipueira-Medrado "um dos" depósitos de cromita mais importantes, "com camadas de cromitito"

**claim_id:** `LAY-M33-A08-IPUEIRA-MEDRADO-006`
**Tipo:** evidência insuficiente (marcada pela própria redação como de confiança moderada)
**Onde:** Aula 08 · 3º item dos complexos brasileiros
**Problema:** a busca confirmou e deixou a afirmação mais precisa. O sill de Ipueira-Medrado (Vale do Jacurici, Bahia; ~7 km de extensão, ~300 m de espessura; dunito e harzburgito) hospeda **o maior depósito de cromita do Brasil**. A mineralização é uma camada **principal** contínua de cromitito maciço de 5 a 8 m, em lavra.
**Correção proposta:** reescrever com esses dados. Números de recurso e reserva **continuam omitidos**, porque não consultei relatório técnico atual (ANM ou empresa).
**Fonte:** Marques & Ferreira Filho 2003, *Econ. Geol.* 98:87-108; Mindat (Ipueira-Medrado sill)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🔵 32. Texturas poiquilíticas como "parte central da textura de minério" do Reef J-M

**claim_id:** `LAY-M33-A07-JM-TEXTURA-010` (criado pela auditoria; cobre `LAY-M33-A05P2-POIQUILITICA-003`)
**Tipo:** evidência insuficiente
**Onde:** Aula 01 · item 4 (heteradcumulato "central para entender" os EGP do Stillwater); Aula 05 · "Texturas poiquilíticas" (2º parágrafo) e recap; Aula 07 · 4º parágrafo
**Problema:** confirmei que há oicocristais de piroxênio nas rochas da Zona com Olivina I e heteradcumulatos na Série Bandada Inferior. **Não** confirmei que oicocristais englobando sulfetos sejam "parte central da textura de minério" nem que o J-M seja "o exemplo mais estudado" desse papel. O que a literatura descreve do minério é outra coisa: sulfetos intersticiais, feições de reação com fluidos e fusão parcial incongruente.
**Correção proposta:** "texturas poiquilíticas (oicocristais de piroxênio) ocorrem nas rochas hospedeiras do J-M, e distinguir o que é cumulus e o que é pós-cumulus é parte do estudo do minério", sem o superlativo nem "parte central".
**Fonte:** *Mineralium Deposita* (2024), "The role of hydrothermal processes and the formation of the J-M reef and associated rocks of olivine-bearing zone I"; *J. Petrol.* 27:791 (1986)  ·  **Nível:** revisada por pares
**Confiança:** não verificado (o papel central) → suavizado
**Também aparece em:** Aulas 01, 05, 07

### ⚪ 33. Mistura de magmas como modelo "dominante" do Merensky e do J-M

**claim_id:** `LAY-M33-A06-MERENSKY-MODELO-007` (cobre `LAY-M33-A07-JM-MODELO-003`)
**Tipo:** controvérsia (apresentada como consenso)
**Onde:** Aula 06 · Merensky e parágrafo do Platinova ("o modelo de mistura de magmas que domina a explicação dos reefs"); Aula 07 · 4º parágrafo e recap; Aula 08 · fator R ("o mesmo modelo de mistura [...] já apresentado")
**Problema:** a mistura de magmas de Campbell, Naldrett & Barnes (1983) é influente, mas não é consenso. Há outros modelos: mistura por convecção duplo-difusiva (Irvine, Keith & Todd, 1983); modelo hidromagmático, com fluidos que sobem da pilha cumulática (Boudreau & McCallum, 1992, e trabalhos de 2024 sobre o J-M); crescimento *in situ* com redução de pressão (Latypov et al., 2018); e infiltração e refusão de cumulatos (Jenkins et al., 2021, para o J-M).
**Correção proposta:** "um dos modelos mais influentes [...]; concorre com modelos hidromagmáticos, de redução de pressão/crescimento *in situ* e de infiltração-refusão; o debate segue aberto". Nos modelos magmáticos, o fator R continua sendo o princípio que explica o tenor alto; no hidromagmático, a concentração é atribuída sobretudo aos fluidos.
**Fonte:** Campbell, Naldrett & Barnes 1983, *J. Petrol.* 24:133-165; Irvine, Keith & Todd 1983; Boudreau & McCallum 1992, *Econ. Geol.* 87:1830; Latypov et al. 2018; Jenkins et al. 2021  ·  **Nível:** revisada por pares
**Confiança:** em disputa
**Também aparece em:** Aulas 06, 07, 08

---

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `LAY-M33-A01-WBW1960-002` | Wager, Brown & Wadsworth (1960), *J. Petrol.* 1:73-85, formalizam cumulus/intercumulus e ortocumulato/adcumulato | resumo OUP | confirmado |
| `LAY-M33-A01-PATAMARES-004` | Limites aproximados 0–7 / 7–25 / >25 % (valores corretos; atribuição corrigida para Irvine 1982 no achado 2) | Irvine 1982 | confirmado |
| `LAY-M33-A01-DEFINICAO-INTRUSAO-006` | Intrusão acamadada exige acamadamento macroscópico sistemático; arquétipos máfico-ultramáficos | Irvine 1982; Cawthorn 1996 | confirmado |
| `LAY-M33-A02-AMBIENTES-001` | LIPs, riftes, terrenos arqueanos de regime debatido | Cawthorn 1996; *Lithos* 2024 (Muskox–Mackenzie) | confirmado |
| `LAY-M33-A02-FECHADO-ABERTO-002` | Skaergaard fechado; Bushveld/Stillwater abertos | Wager & Brown 1968; Wotzlaw et al. 2012; Barnes et al. 2010 | confirmado |
| `LAY-M33-A02-MUSH-TRANSCRUSTAL-005` | Cashman, Sparks & Blundy 2017, *Science* 355:eaag3055 | Science | confirmado |
| `LAY-M33-A03-TRES-FRENTES-002` | MBS, LS, UBS convergindo no Horizonte Sanduíche | Wager & Brown 1968 | confirmado |
| `LAY-M33-A03-ZONEAMENTO-BUSHVELD-003` | Zonas Marginal, Inferior, Crítica (Merensky no topo), Principal, Superior | Cawthorn 2015 | confirmado |
| `LAY-M33-A03-QUATRO-TIPOS-004` | Acamadamento modal, de fase, textural (granulométrico) e críptico | Irvine 1982; Namur et al. 2015 | confirmado |
| `LAY-M33-A03-VARIACAO-CRIPTICA-005` | Queda de Fo/Mg# para o topo em Skaergaard até olivina fayalítica | Wager & Brown 1968; Thy, Lesher & Tegner 2009 | confirmado (ressalva do achado 11) |
| `LAY-M33-A03-EXEMPLO-006` | Exemplo hipotético; lógica de fase/críptica coerente | — | confirmado |
| `LAY-M33-A04P1-INSITU-002` | McBirney & Noyes 1979, *J. Petrol.* 20:487-554, cristalização *in situ* | resumo OUP | confirmado |
| `LAY-M33-A04P1-DUPLA-DIFUSAO-003` | Huppert & Sparks 1984, *Annu. Rev. Earth Planet. Sci.* 12:11-37 | — | confirmado |
| `LAY-M33-A04P1-EXEMPLO-006` | Lógica do exemplo (ajustada pelo achado 6) | — | confirmado |
| `LAY-M33-A05P2-REEQUILIBRIO-004` | Reequilíbrio subsólido Fe-Mg pode deslocar composições mensuravelmente | Hunter 1996 | confirmado |
| `LAY-M33-A06-BUSHVELD-IDADE-EXTENSAO-004` | ~2,06 Ga (2055,9 Ma); >66 000 km²; até ~9 km | Cawthorn 2015; Zeh et al. 2015 | confirmado |
| `LAY-M33-A06-ZONEAMENTO-HORIZONTES-006` | UG1/UG2 e Merensky na Zona Crítica; Main Magnetite Layer na Zona Superior | Cawthorn 2015 | confirmado |
| `LAY-M33-A07-STILLWATER-IDADE-001` | ~2,7 Ga (2705 ± 4 Ma), basculado depois da consolidação | Premo et al. 1990 | confirmado |
| `LAY-M33-A07-GEODINAMICA-ARQUEANA-006` | Ambiente geodinâmico sem análogo moderno fechado | — | em disputa (já tratado como debate) |
| `LAY-M33-A07-EXEMPLO-007` | Lógica das unidades cíclicas (ajustada pelo achado 23) | — | confirmado |
| `LAY-M33-A08-FATOR-R-001` | Campbell & Naldrett 1979, *Econ. Geol.* 74:1503-1506 | — | confirmado |
| `LAY-M33-A08-MAGNETITA-TIV-004` | Saturação tardia em óxido de Fe-Ti; fO₂/overturn como hipótese discutida | Cawthorn 2015 | confirmado |
| `LAY-M33-A08-NIQUELANDIA-BARRO-ALTO-005` | Niquelândia, Barro Alto e Cana Brava neoproterozoicos (~0,79 Ga); Ni-Co laterítico | Ferreira Filho et al. 2010, *Precambrian Res.* 183:617-634 | confirmado |
| `LAY-M33-A08-EXEMPLO-007` | Lógica do fator R no exemplo | Campbell & Naldrett 1979 | confirmado |

**Nota sobre Niquelândia.** Ferreira Filho et al. (2010) restringem Niquelândia, Barro Alto e Cana Brava a intrusões acamadadas de ~0,79 Ga. A antiga "Série Superior de Niquelândia" hoje é o Complexo Serra dos Borges, de ~1,25 Ga. O texto diz "neoproterozoica", e está certo. A informação fica registrada aqui, sem alteração na aula.

**Números de recurso e reserva dos complexos brasileiros:** **não preenchidos.** Não consultei relatório técnico atual (NI 43-101/JORC, ANM ou operadora), e a ressalva da redação continua valendo. Nenhum número foi inventado.

## Observações não factuais

- Erros de digitação encontrados de passagem ("ddessa", "hipóses", "bonintico", "uma dunito", "suas diferentes lobos", "uma piroxenito") ficam para a revisão didática.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-29

| # | claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|---|
| 1 | `LAY-M33-A01-CUMULATO-HIST-001` | 🔴 | Corrigido | aula-01 |
| 2 | `LAY-M33-A01-EXEMPLO-005` | 🔴 | Corrigido | aula-01 |
| 3 | `LAY-M33-A06-MAGMAS-B1B2B3-005` | 🔴 | Corrigido | aula-02, aula-06, aula-07 |
| 4 | `LAY-M33-A03-SANDUICHE-007` | 🔴 | Corrigido | aula-03 |
| 5 | `LAY-M33-A04P1-SEDIMENTACAO-001` | 🔴 | Corrigido | aula-04 |
| 6 | `LAY-M33-A04P1-CROMITITO-DENSIDADE-005` | 🔴 | Corrigido | aula-04 |
| 7 | `LAY-M33-A05P2-EXEMPLO-005` | 🔴 | Corrigido | aula-05 |
| 8 | `LAY-M33-A06-PLATINOVA-003` | 🔴 | Corrigido | aula-06 |
| 9 | `LAY-M33-A01-HETERADCUMULATO-003` | 🟠 | Corrigido | aula-01, aula-05 |
| 10 | `LAY-M33-A05P2-ADCUMULUS-COMPACTACAO-001` | 🟠 | Corrigido | aula-01, aula-05 |
| 11 | `LAY-M33-A02-FENNER-BOWEN-003` | 🟠 | Corrigido | aula-02, aula-03, aula-06 |
| 12 | `LAY-M33-A02-EXEMPLO-006` | 🟠 | Corrigido | aula-02, aula-03 |
| 13 | `LAY-M33-A07-MUSKOX-MAGMA-009` | 🟠 | Corrigido | aula-02, aula-07 |
| 14 | `LAY-M33-A07-STILLWATER-MAGMA-008` | 🟠 | Corrigido | aula-02, aula-07 |
| 15 | `LAY-M33-A03-FORMAS-001` | 🟠 | Corrigido | aula-03, aula-07 |
| 16 | `LAY-M33-A03-ORDEM-CRISTALIZACAO-008` | 🟠 | Corrigido | aula-03 |
| 17 | `LAY-M33-A05P2-TRAPPED-LIQUID-SHIFT-002` | 🟠 | Corrigido | aula-05 |
| 18 | `LAY-M33-A06-EXEMPLO-008` | 🟠 | Corrigido | aula-06 |
| 19 | `LAY-M33-A06-BUSHVELD-PRODUCAO-009` | 🟠 | Corrigido | aula-06 |
| 20 | `LAY-M33-A06-ZONA-INFERIOR-010` | 🟠 | Corrigido | aula-06 |
| 21 | `LAY-M33-A06-SKAERGAARD-IDADE-001` | 🟠 | Corrigido | aula-06 |
| 22 | `LAY-M33-A07-JM-REEF-002` | 🟠 | Corrigido | aula-07 |
| 23 | `LAY-M33-A07-UNIDADE-CICLICA-005` | 🟠 | Corrigido | aula-07 |
| 24 | `LAY-M33-A08-SATURACAO-ENXOFRE-002` | 🟠 | Corrigido | aula-08 |
| 25 | `LAY-M33-A08-CROMITITO-MODELOS-003` | 🟠 | Corrigido | aula-08 |
| 26 | `LAY-M33-MOD-REMISSOES-001` | 🟠 | Corrigido | aula-01, aula-04 |
| 27 | `LAY-M33-MOD-HUB-DEBATE-002` | 🟠 | Corrigido | modulo |
| 28 | `LAY-M33-A07-MUSKOX-IDADE-CONTEXTO-004` | 🟡 | Corrigido (nome antigo mantido como referência) | aula-07 |
| 29 | `LAY-M33-A08-FONTE-ANM-008` | 🟡 | Corrigido (nome antigo mantido como referência) | aula-08 |
| 30 | `LAY-M33-A04P1-DEBATE-ABERTO-004` | 🔵 | Corrigido com ressalva (afirmação não confirmada retirada) | aula-04 |
| 31 | `LAY-M33-A08-IPUEIRA-MEDRADO-006` | 🔵 | Corrigido (confirmado com fonte; números de recurso seguem omitidos) | aula-08 |
| 32 | `LAY-M33-A07-JM-TEXTURA-010` | 🔵 | Corrigido com ressalva (superlativo retirado) | aula-01, aula-05, aula-07 |
| 33 | `LAY-M33-A06-MERENSKY-MODELO-007` | ⚪ | Corrigido com ressalva (reescrito como debate) | aula-06, aula-07, aula-08 |

Também foram alterados o bloco `alegacoes_auditaveis` das oito aulas (claims criados pela auditoria e fontes atualizadas), um bloco `auditoria` no fim dos metadados de cada aula e o hub do módulo (registro e "Pontos de dificuldade").

**Propagação.** O módulo **não tem questionário, baralho nem glossário**: a auditoria correu antes deles, e nenhum card no Anki precisa de correção. Busquei no curso inteiro "Skaergaard", "Bushveld", "Merensky", "UG2", "Stillwater", "Muskox", "fator R", "Niquelândia", "Barro Alto", "Ipueira" e os termos cumuláticos. O único outro módulo que toca no assunto é o **Módulo 22** (Aula 04, questionário e baralho): cita Merensky, UG2 e J-M apenas como exemplos de geometria **estratiforme**, com espessura de centímetros a poucos metros. É compatível e não foi alterado. Nenhum outro módulo foi tocado.

**Claims.** 51 declarados na redação, 8 criados pela auditoria nas aulas (A03-SANDUICHE-007, A03-ORDEM-CRISTALIZACAO-008, A06-BUSHVELD-PRODUCAO-009, A06-ZONA-INFERIOR-010, A07-STILLWATER-MAGMA-008, A07-MUSKOX-MAGMA-009, A07-JM-TEXTURA-010, A08-FONTE-ANM-008) e 2 de módulo, que ficam só no relatório, no manifesto e no estado (MOD-REMISSOES-001, MOD-HUB-DEBATE-002). Em disco, depois da auditoria, contados por script: **59**, sem duplicata (a01 6, a02 6, a03 8, a04 6, a05 5, a06 10, a07 10, a08 8). Rastreados no total: 61. Nenhum claim ficou sem auditoria.

**Manifesto.** O `.json` foi gravado antes das edições (Fase 1) e regravado depois no formato de `schemas/audit.schema.json` (`schema_version`, `target`, `summary`, `findings` com `kind`, `location` e `source` como objeto, `verified_claims`). O conteúdo é o mesmo. Validado com jsonschema: **0 erros de estrutura**. O único desvio restante é o padrão do `claim_id` (33 ocorrências). A convenção do curso (`LAY-M33-A01-TEMA-NNN`, igual à dos Módulos 30–32) tem mais segmentos do que o padrão `^[A-Z]{2,4}-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}$` aceita. Esses IDs vêm da redação, e o próprio auditor proíbe renomeá-los.

**Pendências:** nenhuma.

---

## Restrições obrigatórias para quem gerar a avaliação (questionário e flashcards)

1. **"Cumulato" = Wager, Brown & Wadsworth (1960)**, não Wager & Deer (1939). O termo nasceu ligado à acumulação de cristais (decantação); a definição sem mecanismo é de Irvine (1982). Não cobrar "termo criado em 1939 para ser neutro".
2. **Limites de Irvine (1982):** adcumulato 0–7 %, mesocumulato 7–25 %, ortocumulato >25 % de material intercumulus (aproximados; há autores com 5/30 %). 9 % = mesocumulato.
3. **Heteradcumulato** = oicocristal de mineral **diferente** da fase cumulus, a partir do líquido intercumulus; termo de Wager et al. (1960).
4. **Crescimento adcumulus exige comunicação com o magma principal**; líquido aprisionado isolado cristaliza como material intercumulus.
5. **Bushveld: B1 = alto Mg, afinidade boninítica; B2 e B3 = toleíticos.** Nunca "B1, B2 e B3 boniníticos".
6. **Stillwater: dois magmas**, tipo U (ultramáfico, alto Mg) e tipo A (anortosítico, toleítico).
7. **Muskox: magma parental picrítico (~13–15 % MgO)**, não komatiítico; Nunavut; ~1,27 Ga; LIP de Mackenzie; ~42 unidades cíclicas.
8. **Horizonte Sanduíche = topo da Série Estratificada** (acima da UZc), encontro com a Série de Borda Superior; nunca "topo da Zona Média".
9. **Platinova Reef = Triple Group, parte superior da Zona Média**; nunca "Zona Superior".
10. **Stokes:** olivina milimétrica em basalto sedimenta a metros por dia; v ∝ r² (cristal pequeno sedimenta **mais devagar**). As objeções à decantação são convecção, reologia não newtoniana, flutuação do plagioclásio em líquido rico em Fe e camadas nas paredes. Nunca cobrar "Stokes prevê sedimentação lenta demais".
11. **Cromitito:** a densidade alta favorece a sedimentação e o tamanho pequeno a desfavorece; sedimentação × crescimento *in situ* em debate. Os modelos de formação (mistura, adição de sílica, pressão/fO₂, *in situ*) **não têm vencedor**.
12. **Exemplo da Aula 05:** borda de olivina mais ferrosa = Fe **entrou** na olivina, Mg saiu para o ortopiroxênio; a feição não é diagnóstica sozinha (reação com líquido intercumulus × difusão subsólida).
13. **Deslocamento do líquido aprisionado** (Barnes, 1986): muda a composição dos **minerais cumulus**, em sistema fechado; não muda a rocha total.
14. **Reversões críticas:** interpretação mais comum = recarga, depois de descartados efeitos pós-cumulus; não cobrar "só podem ser recarga".
15. **Bowen–Fenner:** Skaergaard é o caso-tipo do trend de Fenner, mas a trajetória do líquido foi debatida (Hunter & Sparks, 1987; imiscibilidade tardia); não cobrar "resolveu de forma inequívoca".
16. **Merensky e J-M:** mistura de magmas (Campbell, Naldrett & Barnes, 1983) é **um** dos modelos (concorrem hidromagmático, pressão/*in situ* e infiltração-refusão). Nos modelos magmáticos, o fator R explica o tenor; no hidromagmático, a concentração é atribuída aos fluidos.
17. **Reef J-M:** Zona com Olivina I da Série Bandada Inferior (troctolito, olivina gabronorito, anortosito); ~18 ppm Pt + Pd, maior teor médio conhecido.
18. **Contaminação externa por S** = gatilho típico dos grandes depósitos de **Ni-Cu** de conduto e contato basal; nos **reefs de EGP** predominam modelos internos.
19. **Adição de sílica = Irvine (1975)**; **mistura de magmas = Irvine (1977)**, ambos a partir do Muskox.
20. **Formas:** Muskox em funil ou calha; Bushveld lopolítico; Skaergaard em caixa irregular (Nielsen, 2004).
21. **Zona Inferior do Bushveld:** sobretudo ortopiroxenito. **Produção:** Bushveld domina platina e ródio; a Rússia é o maior produtor mineiro de paládio.
22. **Unidade cíclica:** Brown (1956, Rum) antecede Irvine; doze unidades = preenchimento inicial + onze recargas.
23. **Ipueira-Medrado** = maior depósito de cromita do Brasil, camada principal de 5–8 m. **Não cobrar números de recurso ou reserva** de nenhum complexo brasileiro. Niquelândia, Barro Alto e Cana Brava ~0,79 Ga; Ni-Co sobretudo laterítico.
24. Os números dos exemplos hipotéticos (68/32 %, 91/9 %, Fo₈₈→Fo₈₃, Fo₈₅/Fo₈₁, doze unidades) **não são constantes a memorizar**.
