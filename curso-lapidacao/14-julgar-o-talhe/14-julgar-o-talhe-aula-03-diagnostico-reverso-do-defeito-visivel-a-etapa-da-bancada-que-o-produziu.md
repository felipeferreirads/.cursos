# Aula 03: Diagnóstico reverso — do defeito visível à etapa da bancada que o produziu

**ID:** lapidacao-m14-a03
**Módulo:** [[14-julgar-o-talhe-modulo|Módulo 14]] — Julgar um talhe pronto
**Duração estimada:** ~30 min
**Objetivo:** inferir, a partir de um defeito observado, a etapa do processo que o produziu.
**Pré-requisito:** [[14-julgar-o-talhe-aula-02-o-catalogo-de-defeitos-o-que-se-ve-na-pedra-pronta|Aula 02]] deste módulo (o catálogo de defeitos); [[09-geometria-e-diagramas-aula-05-quando-o-meetpoint-nao-fecha-cheater-e-diagnostico|Módulo 09, aula 05]] deste curso (a árvore de diagnóstico do encontro de facetas); [[06-cabochao-aula-02-da-lasca-a-preforma-gabarito-serragem-contorno|Módulo 06, aula 02]] deste curso (a preformação como etapa que trava contorno e cinta); [[04-laps-abrasivos-e-dop-aula-03-contaminacao-de-grao|Módulo 04, aula 03]] deste curso (contaminação de grão e risco residual).

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **diagnóstico reverso** | o raciocínio que parte de um defeito visível na pedra pronta e conclui em qual etapa do processo ele nasceu, sem ter observado o processo. |
| **etapa de origem** | o estágio da cadeia — leitura do bruto, preformação, desbaste, facetamento, polimento — onde um defeito específico foi introduzido. |
| **causa de projeto** | uma causa que não é falha de execução nem propriedade do material, e sim consequência de uma **escolha** feita no desenho da pedra — o estilo de talhe, o contorno. |
| **defeito de material** | uma limitação que nasce de uma propriedade do próprio material (heterogeneidade, saturação de cor), não de uma etapa executada errado. |
| **assinatura** | o padrão específico de aparência que aponta, de forma confiável, para uma única etapa de origem. |

## Antes de começar, você precisa saber

- Da [[14-julgar-o-talhe-aula-02-o-catalogo-de-defeitos-o-que-se-ve-na-pedra-pronta|aula 02 deste módulo]]: os sete defeitos do catálogo e o critério que cada um viola.
- Do [[09-geometria-e-diagramas-aula-05-quando-o-meetpoint-nao-fecha-cheater-e-diagnostico|módulo 09, aula 05]]: um encontro de facetas que não fecha tem uma "assinatura" visível diferente conforme a coordenada errada — índice, altura ou ângulo — e essa árvore de diagnóstico é o modelo que esta aula generaliza para o processo inteiro.
- Do [[06-cabochao-aula-02-da-lasca-a-preforma-gabarito-serragem-contorno|módulo 06, aula 02]]: contorno e cinta são travados na preformação; a cúpula se ergue sobre eles e não os conserta.
- Do [[04-laps-abrasivos-e-dop-aula-03-contaminacao-de-grao|módulo 04, aula 03]]: um grão grosso contaminante numa etapa fina abre um risco fundo demais para a própria etapa apagar.

## Ao final você vai conseguir

- `lapidacao-m14-oa03` — Inferir, a partir de um defeito observado, a etapa do processo que o produziu.

## Conteúdo

### Por que o sintoma aponta a causa — de novo, agora em escala maior

O [[09-geometria-e-diagramas-aula-05-quando-o-meetpoint-nao-fecha-cheater-e-diagnostico|módulo 09, aula 05]] já ensinou este raciocínio para um caso específico: um meetpoint que não fecha tem uma assinatura visível — girado, curto, longo, ou uma fileira inteira desviada — e cada assinatura aponta para uma única coordenada da facetadora. Esta aula generaliza o mesmo princípio para o processo inteiro, da leitura do bruto ao polimento final: **cada etapa da cadeia deixa uma assinatura diferente no defeito que produz**, porque cada etapa manipula uma variável distinta — contorno na preformação, forma no desbaste, ângulo e índice no facetamento, superfície no polimento. Ler a assinatura certa é o que transforma um defeito num diagnóstico, e não num mistério.

### Mapeando o catálogo às etapas

**Janela e extinção → o ângulo de pavilhão, e nem sempre só ele.** A janela nasce na etapa em que o ângulo do pavilhão é decidido contra o índice de refração do material ([[08-optica-do-facetado-modulo|módulo 08]]), e sua assinatura é limpa: pavilhão raso demais, sempre a mesma causa. A de extinção é ambígua por natureza: o [[05-leitura-do-bruto-aula-06-janelamento-e-extincao|módulo 05, aula 06]] listou **cinco** causas independentes, e só **uma** delas — pavilhão fundo demais — é de execução. Duas são do **material** (índice de refração baixo, saturação de cor alta) e duas são de **projeto** (estilo degrau, contorno alongado). Diagnosticar começa por perguntar se a extinção sumiria com o ângulo corrigido mentalmente: se sim, a causa é de execução. Se persistiria, o diagnóstico ainda não acabou — falta separar o que o material impõe do que a escolha de estilo e de contorno impôs, e é essa segunda separação que a aula 04 deste módulo retoma ao perguntar o que o recorte consegue e não consegue consertar.

**Quilha deslocada e cinta ondulada → facetamento, decisão de retenção de peso.** Diferente de janela e extinção, esses dois raramente são erro de execução: são a assinatura de uma decisão deliberada tomada durante o corte do pavilhão e da cinta, quando o lapidário escolhe reter massa em vez de simetria perfeita ([[10-familias-de-talhe-aula-05-onde-o-peso-se-esconde|módulo 10, aula 05]]). O diagnóstico aqui muda de natureza: não é "o que saiu errado", mas "que troca foi feita".

**Faceta extra → facetamento fino, correção de um encontro ou remoção de marca.** A assinatura é posicional: se a faceta extra está exatamente onde um vértice era esperado, a origem é uma correção de meetline que não fechava; se está numa posição sem relação óbvia com nenhum vértice do diagrama, é mais provável que tenha vindo da remoção de uma marca de superfície remanescente do bruto.

**Cinta socavada (undercut de cabochão) → desbaste, ângulo de apoio contra o esmeril.** Já estabelecido no [[06-cabochao-aula-04-cinta-e-base-onde-o-cabochao-mais-se-estraga|módulo 06, aula 04]]: peça inclinada contra o esmeril no sentido errado, ou apoio no ângulo errado. A assinatura é a base mais larga que o topo — geometricamente inconfundível com qualquer outro defeito do catálogo.

**Undercut de material heterogêneo (esfera, forma torneada) → não é etapa, é material.** O [[07-esfera-e-torneadas-aula-03-materiais-e-defeitos-undercut-e-bandeamento|módulo 07, aula 03]] já registrou que esse undercut nasce da resistência diferencial à abrasão de bandas ou zonas do próprio cristal — nenhuma etapa foi executada errado; o processo tratou o material de forma uniforme e o material respondeu de forma desigual. É o primeiro caso em que o diagnóstico correto é **não há etapa culpada**, só uma propriedade do material que o processo não controla.

**Arranhão de polimento → contaminação de grão, ou etapa da sequência pulada.** O [[04-laps-abrasivos-e-dop-aula-03-contaminacao-de-grao|módulo 04, aula 03]] e o [[02-fisica-do-desbaste-aula-03-a-sequencia-de-grao-e-a-mudanca-de-regime-da-superficie|módulo 02, aula 03]] já estabeleceram o mecanismo: um grão grosso sobrevivente de uma etapa anterior abre um risco fundo demais para a etapa fina seguinte apagar. A assinatura: um risco isolado, mais fundo que a textura ao redor, é típico de contaminação pontual; um padrão repetido de riscos rasos em toda a superfície sugere que uma etapa inteira da sequência de grão foi pulada ou abreviada demais.

### O quadro do diagnóstico

| Defeito | Etapa de origem | Assinatura que confirma |
|---|---|---|
| Janela | facetamento (ângulo de pavilhão) | causa única, some com o ângulo corrigido mentalmente |
| Extinção | facetamento, **material** ou **projeto** (estilo, contorno) | some com o ângulo corrigido → execução; persiste → material ou projeto |
| Quilha deslocada / cinta ondulada | facetamento (decisão de peso) | assimetria sistemática, não isolada |
| Faceta extra | facetamento fino | posição no vértice → correção de encontro; fora dele → remoção de marca |
| Undercut de cabochão | desbaste (ângulo de esmeril) | base mais larga que o topo |
| Undercut de esfera/torneada | material (não é etapa) | segue o contorno de uma banda ou zona |
| Arranhão de polimento | sequência de grão / polimento | isolado e fundo → contaminação; disperso e raso → etapa pulada |

### O limite deste raciocínio

O diagnóstico reverso identifica a etapa **mais provável**, não a única possível — o [[09-geometria-e-diagramas-aula-05-quando-o-meetpoint-nao-fecha-cheater-e-diagnostico|módulo 09, aula 05]] já advertiu, no caso menor do meetpoint, que um talhe real com muitos encontros que não fecham pode ter mais de uma causa simultânea. O mesmo vale em escala maior: uma pedra pronta pode acumular defeitos de etapas diferentes ao mesmo tempo, e o diagnóstico correto trata cada defeito do catálogo isoladamente antes de somar o quadro completo.

## Exemplo trabalhado

**Uma esmeralda em talhe degrau chega para inspeção: o centro da mesa está com uma zona escura persistente, e a cinta mostra ondulação leve em dois pontos.**

**Passo 1 — a zona escura.** Aplicando o quadro: ela desapareceria com o ângulo de pavilhão corrigido mentalmente? Esta esmeralda tem saturação de cor forte e zonação — leituras do [[05-leitura-do-bruto-modulo|módulo 05]] —, e mesmo com o ângulo ideal o caminho óptico dentro da cor saturada continua absorvendo luz no mesmo trecho. Diagnóstico parcial: **não é execução**. Falta o segundo passo, e ele importa: a saturação é do material, mas o **talhe degrau** também é causa de extinção, e essa é de **projeto** — o mesmo escurecimento, num brilhante, apareceria picado entre pontos claros. Duas causas somadas, nenhuma delas de execução.

**Passo 2 — a ondulação de cinta.** Ela aparece em só dois pontos, não na cinta inteira, e é leve — assinatura de uma manobra de "pintar e escavar" pontual, não de um esmeril desregulado por toda a volta. Diagnóstico: **facetamento, decisão de retenção de peso**, provavelmente para preservar dois pontos onde o bruto tinha menos margem.

**Passo 3 — juntando os dois.** Nenhum dos dois defeitos compartilha a mesma etapa de origem, e nenhum se propaga para o outro — são independentes. Forçar uma causa comum onde há duas seria o erro — essa é a lição do exemplo.

## Erros comuns

- **Tratar toda extinção como erro de ângulo, ou concluir "é material" assim que o ângulo é descartado.** São cinco causas: uma de execução, duas de material, duas de projeto. O teste do ângulo só separa a primeira das outras quatro.
- **Procurar uma etapa culpada para o undercut de material heterogêneo.** Às vezes não há: o processo tratou o material de forma uniforme, e é o material que respondeu de forma desigual.
- **Diagnosticar um defeito isolado e parar aí quando há vários no catálogo.** Cada defeito é diagnosticado por si; a pedra pode ter mais de uma etapa de origem simultânea.
- **Confundir manobra deliberada de peso com erro de execução.** Quilha deslocada e cinta ondulada raramente são acidente — o diagnóstico correto é "que troca foi feita", não "o que saiu errado".
- **Assumir certeza absoluta no diagnóstico reverso.** Ele aponta a etapa mais provável a partir da assinatura visível, não prova definitiva — o mesmo limite que já valia para o meetpoint no módulo 09.

## O que não concluir

- Não concluir como corrigir ou refazer a etapa diagnosticada na bancada — esta aula diagnostica, não prescreve execução; é competência de bancada, fora do nível teórico do curso.
- Não concluir se vale a pena agir sobre o defeito diagnosticado — essa é a decisão de recorte da aula 04 deste módulo.
- Não concluir que todo defeito tem uma única etapa de origem possível — alguns (extinção, arranhão de polimento) exigem descartar hipóteses antes de fechar o diagnóstico.
- Não tomar o quadro desta aula como exaustivo para toda família de talhe — ele cobre os sete itens do catálogo da aula 02; escultura e fancy cutting têm assinaturas próprias, fora do escopo deste módulo de síntese.

## Recap relâmpago

- O diagnóstico reverso generaliza, para o processo inteiro, o mesmo princípio já usado no módulo 09 para o meetpoint: cada etapa da cadeia deixa uma **assinatura** visível diferente no defeito que produz.
- **Janela** aponta para o facetamento (ângulo de pavilhão), com causa única; **extinção** tem cinco — uma de execução, duas de material, duas de projeto —, e o teste do ângulo corrigido só isola a primeira.
- **Quilha deslocada e cinta ondulada** apontam para uma decisão de retenção de peso no facetamento, raramente um acidente puro.
- **Faceta extra** aponta para o facetamento fino — no vértice, é correção de encontro; fora dele, é remoção de marca.
- **Undercut de cabochão** aponta para o desbaste (ângulo de esmeril); **undercut de material heterogêneo** não tem etapa culpada — é o material, não o processo.
- **Arranhão de polimento** aponta para contaminação de grão (isolado e fundo) ou etapa de sequência pulada (disperso e raso).
- O diagnóstico é sobre a etapa **mais provável**, não uma certeza absoluta, e uma pedra pode acumular defeitos de etapas diferentes ao mesmo tempo.

## Próxima aula

Na [[14-julgar-o-talhe-aula-04-recorte-quando-vale-o-que-se-perde-e-o-que-o-talhe-nao-conserta|Aula 04 — Recorte]], o curso fecha perguntando o que fazer com o diagnóstico: quando vale recortar uma pedra defeituosa, o que se perde ao tentar, e — a pergunta mais importante — o que o recorte simplesmente não consegue consertar.

## Fontes consultadas

- Wykoff, *Techniques of Master Faceting* — o diagnóstico de faceta fora de posição a partir do sintoma visível, generalizado nesta aula para o processo inteiro.
- Sinkankas, *Gem Cutting: A Lapidary's Manual* — undercut de cinta por ângulo de esmeril; contaminação de grão e risco residual.
- Vargas & Vargas, *Faceting for Amateurs* — pavilhão e índice de refração como origem de janela e extinção.
- [[09-geometria-e-diagramas-modulo|Módulo 09]], [[06-cabochao-modulo|módulo 06]], [[07-esfera-e-torneadas-modulo|módulo 07]] e [[04-laps-abrasivos-e-dop-modulo|módulo 04]] deste curso — as assinaturas de diagnóstico de cada etapa, reativadas e generalizadas nesta aula.

<!--
nivel: ensino-medio-com-gemologia-v1
palavras_corpo: 1600
cobertura:
  lapidacao-m14-oa03: [Conteúdo, "Exemplo trabalhado", "Erros comuns", "O que não concluir", "Recap relâmpago"]
alegacoes_auditaveis:
  - claim_id: DIA-ASSIN-GERAL-001
    claim: "O princípio de diagnóstico do módulo 09 deste curso — um meetpoint que não fecha produz uma assinatura visível diferente conforme a coordenada errada (índice, altura, ângulo) — generaliza-se para o processo de lapidação inteiro: cada etapa da cadeia (leitura do bruto, preformação, desbaste, facetamento, polimento) manipula uma variável distinta e, por isso, deixa uma assinatura visível diferente no defeito que produz quando executada errado."
    risk: consistencia interna
    source: "curso de lapidacao, módulo 09 aula 05 (árvore de diagnóstico do meetpoint), generalizada nesta aula como síntese do módulo de encerramento"
  - claim_id: DIA-JAN-ETAPA-001
    claim: "Janela tem origem única e diagnosticável no facetamento: ângulo de pavilhão raso demais para o índice de refração do material, e o defeito desaparece se o ângulo for corrigido. Extinção tem CINCO causas independentes, conforme o módulo 05, aula 06: uma de EXECUÇÃO (pavilhão fundo demais, somada à head shadow), duas de MATERIAL (índice de refração baixo, saturação de cor alta) e duas de PROJETO (estilo de talhe degrau, contorno alongado). O teste do ângulo de pavilhão corrigido isola SÓ a causa de execução: se a zona escura sumiria com o ângulo certo, a origem é de execução; se persistiria, o diagnóstico ainda precisa separar material de projeto — persistir NÃO implica, por si só, causa de material."
    risk: causa-efeito
    source: "curso de lapidacao, módulo 05 aula 06 (janelamento e as cinco causas de extinção) e módulo 08 (ângulo de pavilhão por índice)"
  - claim_id: DIA-PESO-DECISAO-001
    claim: "Quilha deslocada e cinta ondulada, ao contrário da maioria dos defeitos do catálogo, raramente têm origem em erro de execução isolado: são tipicamente a assinatura de uma decisão deliberada de retenção de peso tomada durante o corte do pavilhão e da cinta, e o diagnóstico correto para esses dois itens pergunta que troca foi feita, não o que saiu errado."
    risk: interpretacao
    source: "curso de lapidacao, módulo 10 aula 05 (quilha deslocada e cinta ondulada como manobras de retenção de peso)"
  - claim_id: DIA-UNDERCUT-MAT-001
    claim: "O undercut por resistência diferencial à abrasão em esfera ou forma torneada de material heterogêneo (bandas ou zonas de dureza distinta) não tem uma etapa de processo culpada diagnosticável: o processo tratou o material de forma uniforme durante o desbaste, e é a heterogeneidade do próprio material que produziu a depressão desigual — distinto do undercut de cinta de cabochão, que tem origem diagnosticável no ângulo de apoio contra o esmeril durante o desbaste."
    risk: consistencia interna
    source: "curso de lapidacao, módulo 07 aula 03 (undercut por heterogeneidade de material) e módulo 06 aula 04 (undercut de cinta por ângulo de esmeril)"
  - claim_id: DIA-ARRANHAO-SEQ-001
    claim: "Um arranhão de polimento isolado, mais fundo que a textura ao redor, é assinatura típica de contaminação pontual por um grão grosso sobrevivente de etapa anterior (módulo 04, aula 03: o grão contaminante abre um risco mais fundo do que a etapa fina seguinte consegue remover); um padrão disperso de riscos rasos por toda a superfície é assinatura mais consistente com uma etapa inteira da sequência de grão pulada ou abreviada (módulo 02, aula 03: cada etapa existe para apagar o risco e o dano subsuperficial da etapa anterior)."
    risk: interpretacao
    source: "curso de lapidacao, módulo 04 aula 03 (contaminação de grão) e módulo 02 aula 03 (sequência de grão e mudança de regime da superfície)"
-->
