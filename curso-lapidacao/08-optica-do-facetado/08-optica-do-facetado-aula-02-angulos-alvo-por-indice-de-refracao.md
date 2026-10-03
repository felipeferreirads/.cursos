# Aula 02: Ângulos-alvo por faixa de índice de refração — a tabela e o que ela realmente diz

**ID:** lapidacao-m08-a02
**Módulo:** [[08-optica-do-facetado-modulo|Módulo 08]] — Óptica do talhe facetado
**Duração estimada:** ~28 min
**Objetivo:** ler uma tabela de ângulos-alvo por faixa de índice de refração, explicar sua base física e declarar seus limites.
**Pré-requisito:** [[08-optica-do-facetado-aula-01-angulo-critico-e-reflexao-interna-total-no-pavilhao|aula 01]] deste módulo (ângulo crítico e reflexão interna total aplicados ao pavilhão). Módulo 01 do curso de Gemologia (índice de refração), citado por nome.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **ângulo-alvo** | o valor de ângulo de pavilhão (ou de coroa) recomendado como ponto de partida de projeto. É publicado **por material**, não por faixa de índice; a faixa organiza a leitura da tabela, não determina o valor. |
| **ângulo de coroa** | a inclinação das facetas da coroa em relação ao plano da cinta. |
| **margem sobre o crítico** | a diferença, em graus, entre o ângulo-alvo recomendado e o ângulo crítico do material. |
| **faixa de índice de refração** | um intervalo de índice (não um valor único) usado para **organizar** a leitura da tabela, agrupando gemas de índice próximo. Não implica que elas recebam o mesmo ângulo-alvo: dentro de uma mesma faixa os valores publicados diferem. |
| **valor de referência** | um número de partida documentado pela literatura do ofício, não uma medida obrigatória de laboratório. |

## Antes de começar, você precisa saber

- Da [[08-optica-do-facetado-aula-01-angulo-critico-e-reflexao-interna-total-no-pavilhao|aula 01]] deste módulo: o ângulo de pavilhão precisa superar o ângulo crítico do material, com margem, para evitar o janelamento; e um pavilhão fundo demais produz extinção mesmo cumprindo a reflexão interna total. Esta aula tabela o meio-termo.
- Do curso de Gemologia, módulo 01 (por nome): **índice de refração** já foi definido. Aqui ele entra de duas maneiras — calcula o ângulo crítico de cada material e organiza as linhas da tabela —, mas não é ele que determina o ângulo-alvo: esse vem publicado material a material.
- Não é preciso saber ainda a diferença entre brilho, dispersão e cintilação (aula 03) — a tabela desta aula mira só no retorno bruto de luz branca.

## Ao final você vai conseguir

- `lapidacao-m08-oa02` — Ler uma tabela de ângulos-alvo por faixa de índice de refração, explicar sua base física e declarar seus limites.

## Conteúdo

### Por que a tabela existe

A aula 01 estabeleceu o princípio: o ângulo de pavilhão precisa ficar acima do ângulo crítico, com margem. Calcular o crítico é simples — $\theta_c = \arcsin(1/n)$ —, mas decidir **quanto acima** dele projetar o pavilhão não é uma conta fechada: depende do peso que se troca por desempenho óptico (aula 04) e de refinamentos que só o ray tracing (aula 06) resolve.

A literatura do ofício resolve isso publicando **valores de referência** de ângulo de pavilhão: pontos de partida documentados, não resultado de fórmula única nem resposta final de projeto. Sobra a pergunta que a seção seguinte responde — o que decide onde esses valores caem.

### A base física: um piso que desce e um teto que não desce

O ângulo crítico dá o **piso**: quanto maior o índice, menor o crítico ($\theta_c = \arcsin(1/n)$ decresce quando $n$ cresce). Há um detalhe elegante nesse piso: a refração na mesa confina os raios que descem ao pavilhão a um cone cujo meio-ângulo é **exatamente o ângulo crítico** do material — de modo que o cone interno também se estreita quando o índice sobe. Índice alto, piso baixo, cone estreito.

Isso explicaria um alvo caindo depressa com o índice — e não é o que a literatura publica: os valores da tabela abaixo mal se movem enquanto o crítico despenca. A razão é um segundo limite, que a conta do ângulo crítico não expressa: um **teto**. Não basta que a luz sofra reflexão interna total no pavilhão; ela precisa, depois de refletir, **sair pela coroa** na direção do observador. Um pavilhão fundo demais cumpre a RIT e ainda assim entrega a luz na direção errada — é a extinção da aula 01. Esse teto é geometria de saída, e **não cai** com o índice.

O ângulo publicado fica espremido entre um piso que desce e um teto que não desce. A tabela abaixo mostra o resultado.

### A tabela — ângulo crítico calculado, pavilhão publicado por material

As duas colunas de números têm origens diferentes, e a diferença importa. O **ângulo crítico** é calculado aqui, por $\theta_c = \arcsin(1/n)$ sobre os extremos de cada faixa. O **ângulo de pavilhão principal** é publicado pelo International Gem Society **material a material** — não por faixa de índice, e por isso a tabela tem uma coluna de material.

| Faixa de índice de refração | Ângulo crítico (calculado) | Material | Pavilhão principal publicado |
|---|---|---|---|
| 1,43 – 1,46 | ≈ 43° – 44° | fluorita, opala | não tabelado |
| 1,50 – 1,55 | ≈ 40° – 42° | quartzo, calcedônia | quartzo **42°** |
| 1,56 – 1,65 | ≈ 37° – 40° | berilo, turmalina, topázio | berilo **43°**, turmalina **42°**, topázio **41°** |
| 1,66 – 1,75 | ≈ 35° – 37° | peridoto, espinélio, granada piropo | peridoto **42°**, espinélio **41°**, granada **39° – 41°** |
| 1,76 – 1,81 | ≈ 33,5° – 34,6° | coríndon (rubi, safira) | coríndon **42°** |
| 1,81 – 2,02 | ≈ 29,7° – 33,5° | zircão de gema | zircão **41°** |
| ≈ 2,42 | ≈ 24,4° | diamante | **40,75°** (Tolkowsky) |

Leia a coluna da direita de cima a baixo. Ela é quase **plana** — tudo entre 39° e 43° — enquanto a do ângulo crítico, ao lado, despenca de 44° para 24°. A tendência decrescente que se esperaria não está lá: o berilo (IR ≈ 1,57) recebe pavilhão **mais fundo** que o quartzo (IR ≈ 1,54), e o coríndon, de índice bem mais alto, fica nos mesmos 42°. É o teto aparecendo nos números.

E a faixa é índice de leitura, não compartimento — quem decide a linha de um material é o índice real dele. **Berilo não existe abaixo de 1,55**: seu índice é 1,562–1,602. E **zircão de gema não existe em 1,66–1,75**: o zircão vai de 1,810 a 2,024, e o *high*, que é o facetado, fica em 1,92–1,98 — só o *low*, metamíctico, desce a ~1,75, e é o que menos se faceta.

O diamante é o caso que mais ensina sobre o limite da tabela. Tem o ângulo crítico mais baixo de todos (≈ 24,4°) e mesmo assim o pavilhão de referência não é "pouco acima de 24°" — é 40,75°, o desenho de Tolkowsky (coroa 34°30', mesa ~53%). O que o levanta tão acima do piso é a exigência de saída pela coroa. E a dispersão entra pelo lado oposto do que se supõe: Tolkowsky registra que um ângulo **maior** daria reflexão ainda melhor, mas não compensaria a perda de fogo — a dispersão é o que **impede o valor de subir**, não o que o levanta.

Nem quem publica um conjunto completo o publica sem ressalva. Para IR 1,54, a United States Faceters Guild publica **pavilhão *mains* 43,00°, *breaks* 41,00°; coroa *mains* 32,00°, *breaks* 28,00°, *stars* 13,00°**. É o único conjunto que ela publica, e vem com uma advertência que vale para a aula inteira — *"There simply is no magic bullet or universal set of angles"*: não existe conjunto universal de ângulos.

### O que a tabela não substitui

A tabela é ponto de **partida** documentado, não prova de otimalidade. Assume um desenho de referência (o brilhante redondo padrão), um ângulo de coroa típico e facetas idealizadas; variação de contorno, de proporção mesa/cinta ou de estilo de talhe (módulo 10) desloca o ângulo ideal. Quem calcula o comportamento óptico de um desenho específico, faceta por faceta, é o ray tracing (aula 06) — a tabela é o que se usa antes dele, ou como checagem de sanidade depois.

## Exemplo trabalhado

**Comparar o pavilhão publicado do quartzo (IR ≈ 1,54) com o da safira (coríndon, IR ≈ 1,77), sabendo que os dois ângulos críticos diferem em mais de 6°.**

**Passo 1 — ângulos críticos.** Quartzo: $\theta_c = \arcsin(1/1{,}54) \approx 40{,}5°$. Safira: $\theta_c = \arcsin(1/1{,}77) \approx 34{,}4°$. Diferença entre os críticos: ≈ 6,1°.

**Passo 2 — ângulos de pavilhão publicados.** Quartzo: **42°**. Safira: **42°**. Diferença entre os dois: **zero**.

**Passo 3 — as margens sobre o crítico.** Quartzo: 42° − 40,5° = **1,5°**. Safira: 42° − 34,4° = **7,6°**. Em termos relativos ao próprio crítico, 3,7% contra 22,1%. A safira, de índice mais alto, tem margem muito **maior** — absoluta e proporcionalmente.

**Passo 4 — a lição do exemplo.** Dois materiais cujos pisos diferem em 6,1° recebem o mesmo ângulo de pavilhão. Nenhum alvo do tipo "crítico mais uma constante" produz isso — mas o piso-com-teto produz: como o teto de saída pela coroa não desce com o índice, o alvo mal se move e toda a queda do crítico vira margem.

## Erros comuns

- **Tratar o ângulo-alvo como igual ao ângulo crítico mais uma constante universal.** O exemplo trabalhado mostra dois materiais com o mesmo pavilhão publicado e pisos separados por 6,1°.
- **Supor que o ângulo-alvo cai com o índice de refração.** Quem cai é o piso. Os valores publicados são quase planos em 40°–43°, e o berilo recebe pavilhão mais fundo que o quartzo apesar do índice maior.
- **Aplicar o ângulo-alvo do brilhante redondo a qualquer contorno ou estilo de talhe.** A tabela assume o desenho de referência; outros contornos (módulo 10) e outras profundidades de mesa deslocam o valor ideal.
- **Achar que a dispersão empurra o ângulo do diamante para cima.** É o contrário: quem levanta o pavilhão muito acima do crítico é a exigência de saída pela coroa, e Tolkowsky registra a dispersão como o motivo de o valor **não** subir mais.
- **Tomar a tabela como suficiente e dispensar o ray tracing.** A tabela é ponto de partida; o ajuste fino de um desenho específico exige a modelagem da aula 06.

## O que não concluir

- Não concluir a fórmula completa do tangent ratio — fica para o módulo 09, aula 06.
- Não concluir os mecanismos de brilho, dispersão e cintilação separadamente — é a aula 03.
- Não tomar os valores publicados como medidas de precisão de laboratório. A exceção de LC-05 deste curso os trata como objeto de estudo, com valor e fonte declarados — mas continuam sendo pontos de partida, não medidas obrigatórias.
- Não concluir como um ângulo de pavilhão é ajustado ou verificado numa facetadora real — competência de bancada, fora do escopo teórico deste curso.

## Recap relâmpago

- A tabela converte o princípio da aula 01 (pavilhão acima do crítico, com margem) em valores de referência, mas o ângulo de pavilhão publicado vem **por material**, não por faixa de índice: a faixa organiza a leitura, não determina o valor.
- Índice mais alto significa ângulo crítico mais baixo ($\theta_c = \arcsin(1/n)$), e o cone interno de incidência tem meio-ângulo igual ao próprio crítico — mas isso governa só o **piso**. O **teto** é a exigência de a luz sair pela coroa depois de refletir, e ele não cai com o índice.
- Pavilhão principal publicado (IGS): quartzo 42°, berilo 43°, turmalina 42°, topázio 41°, peridoto 42°, espinélio 41°, coríndon 42°, zircão 41°, granada 39°–41°; diamante 40,75° (Tolkowsky). Conjunto completo da USFG para IR 1,54: pavilhão *mains* 43,00°, *breaks* 41,00°, coroa *mains* 32,00°, *breaks* 28,00°, *stars* 13,00°.
- Os valores publicados são quase **planos** em 40°–43° enquanto o ângulo crítico varia de ≈44° a ≈24° — e por isso a **margem sobre o crítico cresce com o índice**: quartzo 1,5°, safira 7,6°, com o mesmo pavilhão de 42°.
- A tabela é ponto de partida documentado, não substituto do ray tracing (aula 06) nem válida fora do desenho de referência que a originou.

## Próxima aula

Na aula 03 — Brilho, dispersão e cintilação: o que é, exatamente, o "fogo" que segundo Tolkowsky impede o pavilhão do diamante de subir mais, e como os três efeitos ópticos se distinguem por mecanismo, não por definição de dicionário.

## Fontes consultadas

- International Gem Society, *Faceting Made Easy, Part 1: Gemstone Properties* (gemsociety.org) — a tabela de propriedades para facetamento, de onde vêm os ângulos de pavilhão principal por material. Consultada em 2026-09-04.
- United States Faceters Guild, *Choosing the Best Angles for Your SRB* (usfacetersguild.org) — o conjunto completo para IR 1,54 e a advertência de que não existe conjunto universal de ângulos. Consultada em 2026-09-04.
- United States Faceters Guild, *Refractive Index and Critical Angle* — a convenção da fórmula θc = arcsin(1/n) e a tabela de índices de refração. *(Esta página não publica coluna de ângulo crítico nem de ângulo-alvo: para os ângulos recomendados ela remete a Sinkankas, sem reproduzi-los.)* Consultada em 2026-09-04.
- Marcel Tolkowsky, *Diamond Design* (1919), via transcrição da OctoNus — pavilhão 40°45', coroa 34°30', mesa ~53%, e a passagem em que a dispersão aparece como o limite superior do ângulo, não como sua causa. Consultada em 2026-09-04.
- Índices de refração de berilo e zircão — dados gemológicos padrão (berilo 1,562–1,602; zircão 1,810–2,024, com a distinção *high*/*low* metamíctico). Consultados em 2026-09-04.
- Cálculo direto de θc = arcsin(1/n) para os extremos de cada faixa citada — a coluna de ângulo crítico desta aula é derivada, não copiada de fonte.

<!--
nivel: ensino-medio-com-gemologia-v1
palavras_corpo: 1600
cobertura:
  lapidacao-m08-oa02: [Conteúdo, "Exemplo trabalhado", "Erros comuns", "O que não concluir", "Recap relâmpago"]
alegacoes_auditaveis:
  - claim_id: TAB-BASE-FISICA-001
    claim: "O ângulo de pavilhão está limitado por baixo e por cima por dois mecanismos distintos. O PISO é o ângulo crítico, que decresce quando o índice de refração cresce (θc = arcsin(1/n)); a refração na mesa confina os raios internos a um cone cujo meio-ângulo é exatamente igual ao ângulo crítico, de modo que o cone interno também se estreita com o índice. O TETO é a exigência de que a luz, depois de refletir no pavilhão, SAIA PELA COROA na direção do observador — uma restrição de geometria de saída que o ângulo crítico não expressa e que NÃO cai com o índice de refração. Como o alvo publicado fica espremido entre um piso que desce e um teto que não desce, ele é quase plano (40°-43°) para toda a gama de gema comum, e a margem sobre o ângulo crítico CRESCE com o índice em vez de encolher."
    risk: causa-efeito
    source: "Cálculo direto de θc = arcsin(1/n); Marcel Tolkowsky, Diamond Design (1919), via transcrição da OctoNus, para a restrição de saída pela coroa; International Gem Society, Faceting Made Easy, Part 1, para o caráter plano dos valores publicados. Consultadas em 2026-09-04. CORRIGIDO na auditoria de 2026-09-04 (achado vermelho 3): a versão anterior concluía que materiais de índice alto toleram margem proporcionalmente MENOR e que o alvo cai mais rápido que o crítico — o oposto do que o exemplo trabalhado da própria aula calcula, e do que os valores publicados mostram."
  - claim_id: TAB-ALVO-FAIXA-001
    claim: "Os ângulos de pavilhão principal publicados pelo International Gem Society, por material, são: quartzo 42°, berilo 43°, turmalina 42°, topázio 41°, peridoto 42°, espinélio 41°, coríndon (rubi e safira) 42°, zircão 41°, granada 39°-41°. Os valores são praticamente PLANOS na faixa de 39° a 43° para toda a gama de gema comum, apesar de o ângulo crítico dessa mesma gama variar de cerca de 44° a cerca de 24° — e o berilo (IR ~1,57) recebe pavilhão MAIS FUNDO que o quartzo (IR ~1,54), contrariando qualquer tendência decrescente com o índice. Para IR 1,54 a United States Faceters Guild publica um conjunto completo, declarado como o único que publica: pavilhão mains 43,00°, breaks 41,00°; coroa mains 32,00°, breaks 28,00°, stars 13,00° — acompanhado da advertência de que não existe conjunto universal de ângulos."
    risk: dado numerico
    source: "International Gem Society, Faceting Made Easy, Part 1: Gemstone Properties (tabela de propriedades para facetamento); United States Faceters Guild, Choosing the Best Angles for Your SRB ('There simply is no magic bullet or universal set of angles'). Consultadas em 2026-09-04. CORRIGIDO na auditoria de 2026-09-04 (achado vermelho 1): a versão anterior publicava uma tabela de seis faixas com alvos decrescentes de 45°-46° a 38°-40°, sem origem localizável em nenhuma fonte, e a atribuía à USFG — que não publica tal tabela e afirma textualmente o contrário. O erro individual mais grave era o coríndon, dado como 38°-40° contra os 42° publicados."
  - claim_id: TAB-ALVO-FAIXA-002
    claim: "Berilo não ocorre na faixa de índice de refração 1,50-1,55: o índice do berilo é 1,562-1,602 (esmeralda 1,577-1,583; água-marinha 1,567-1,590), de modo que ele pertence à faixa 1,56-1,65. Zircão de qualidade gema não ocorre na faixa 1,66-1,75: o zircão vai de 1,810 a 2,024, e o zircão high, que é o facetado como gema, fica em 1,92-1,98; apenas o zircão low, metamíctico (danificado por radiação), desce a cerca de 1,75, e é justamente o menos facetado."
    risk: dado numerico
    source: "Dados gemológicos padrão de índice de refração para berilo e zircão, com a distinção high/low do zircão. Consultados em 2026-09-04. Alegação CRIADA pela auditoria de 2026-09-04 (achado vermelho 2): a tabela anterior listava berilo como exemplo da faixa 1,50-1,55 — fisicamente impossível, e duplicando o material, que já aparecia corretamente na faixa 1,56-1,65 — e zircão como exemplo da faixa 1,66-1,75."
  - claim_id: TAB-ALVO-FAIXA-003
    claim: "A coluna de ângulo crítico desta aula é DERIVADA por cálculo, não copiada de fonte externa: θc = arcsin(1/n) aplicado aos extremos de cada faixa de índice. Os valores são: IR 1,43-1,46 → 43,2°-44,4°; 1,50-1,55 → 40,2°-41,8°; 1,56-1,65 → 37,3°-39,9°; 1,66-1,75 → 35,3°-37,0°; 1,76-1,81 → 33,5°-34,6°; 1,81-2,02 → 29,7°-33,5°; n = 2,417 (diamante) → 24,4°."
    risk: dado numerico
    source: "Cálculo direto de θc = arcsin(1/n), recalculado e verificado em 2026-09-04; convenção da fórmula conforme United States Faceters Guild, Refractive Index and Critical Angle. Alegação CRIADA pela auditoria de 2026-09-04 (achado laranja 8): três faixas estavam mal arredondadas na versão anterior (1,43-1,46 dada como valor único ~44°; 1,50-1,55 como ~40°-41° em vez de ~40°-42°; 1,56-1,65 como ~37°-39° em vez de ~37°-40°). LC-05 deste curso trata números tabelados como objeto de estudo, o que eleva o padrão exigido desta coluna."
  - claim_id: TAB-DIAM-EXCE-001
    claim: "O diamante tem o ângulo crítico mais baixo entre os materiais tabelados (≈24,4°, decorrente de índice de refração ≈2,417), mas o ângulo de pavilhão de referência do brilhante redondo clássico de Marcel Tolkowsky é de 40,75° (40°45'), com coroa 34°30' e mesa ~53% — muito acima do piso mínimo teórico. A razão de estar tão acima do piso é a exigência de que a luz, após refletir no pavilhão, saia pela coroa na direção do observador. A dispersão atua na direção OPOSTA: Tolkowsky registra que um ângulo maior daria reflexão ainda melhor, mas não compensaria a perda de fogo correspondente — isto é, a dispersão é o TETO que impede o valor de subir, não a causa de ele estar acima do crítico."
    risk: dado numerico
    source: "Marcel Tolkowsky, Diamond Design (1919), via transcrição da OctoNus — 'although a greater angle would give better reflection, this would not compensate for the loss due to the corresponding reduction in dispersion'; cálculo de θc para n=2,417. Consultadas em 2026-09-04. CORRIGIDO na auditoria de 2026-09-04 (achado laranja 6): os valores estavam corretos, mas a direção do argumento estava invertida — a aula ensinava que a dispersão empurra o ângulo para cima."
  - claim_id: TAB-LIMITE-RAY-001
    claim: "A tabela de ângulos-alvo assume um desenho de referência (o brilhante redondo padrão), um ângulo de coroa típico e uma geometria de facetas idealizada; variações de contorno, de proporção mesa/cinta ou de estilo de talhe deslocam o ângulo ideal para longe do valor tabelado, e o ajuste fino de um desenho específico exige a modelagem por ray tracing (ver aula 06 deste módulo), não apenas a consulta à tabela."
    risk: causa-efeito
    source: "United States Faceters Guild; Vargas & Vargas, Faceting for Amateurs — tabela como ponto de partida, não como resultado final de projeto"
  - claim_id: TAB-EX-MARGEM-001
    claim: "Quartzo (IR≈1,54) e coríndon (IR≈1,77) têm ângulos críticos de ≈40,5° e ≈34,4°, separados por ≈6,1°, e recebem EXATAMENTE O MESMO ângulo de pavilhão principal publicado: 42°. A margem sobre o próprio crítico é portanto de 1,5° para o quartzo e 7,6° para a safira — 3,7% contra 22,1% em termos relativos. A margem cresce com o índice de refração, absoluta e proporcionalmente, o que é incompatível com um alvo formado por 'ângulo crítico mais constante fixa' e é exatamente o que a estrutura piso-com-teto de TAB-BASE-FISICA-001 prevê."
    risk: dado numerico
    source: "Cálculo direto a partir dos valores publicados em TAB-ALVO-FAIXA-001 (IGS) e de θc=arcsin(1/n) para n=1,54 e n=1,77. ATUALIZADO na auditoria de 2026-09-04 por propagação do achado vermelho 1: a aritmética anterior estava correta, mas partia dos valores-alvo incorretos da tabela antiga (42,5° e 39°, dando margens de 2,0° e 4,6°); com os valores publicados a conclusão do exemplo se mantém e fica mais forte."
-->
