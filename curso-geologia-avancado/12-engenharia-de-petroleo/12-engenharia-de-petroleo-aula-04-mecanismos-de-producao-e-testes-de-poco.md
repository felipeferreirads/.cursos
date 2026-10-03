# Aula 04: Mecanismos de produção, recuperação primária e secundária e testes de poço

**ID:** geologia-avancado-m12-a04
**Módulo:** [[12-engenharia-de-petroleo-modulo|Módulo 12 — Engenharia de petróleo]]
**Duração estimada:** ~30 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** relacionar os mecanismos naturais de produção (drives) de um reservatório ao fator de recuperação típico de cada um, distinguir recuperação primária de secundária, e interpretar um teste de poço simples (índice de produtividade e curva de IPR).
**Ao final você vai conseguir:** identificar qual mecanismo de produção domina um reservatório a partir do comportamento de sua pressão; explicar por que a injeção de água (recuperação secundária) aumenta o fator de recuperação; e calcular a vazão esperada de um poço a partir de seu índice de produtividade.
**Pré-requisito:** Aula 03 deste módulo — OOIP, Bo e Rs, e o comportamento de Bo/Rs em torno da pressão de ponto de bolha.

## Conteúdo

### Por que um reservatório produz sozinho, no início

Um reservatório recém-descoberto está em equilíbrio de pressão, geralmente bem acima da pressão atmosférica em que o óleo será finalmente medido. Ao perfurar um poço e abri-lo à produção, essa diferença de pressão entre o reservatório e a superfície é o que empurra o fluido para cima — a **recuperação primária**, na qual nenhuma energia externa é adicionada ao sistema, apenas a energia natural já armazenada no reservatório é usada. Essa energia natural tem origem em um pequeno número de mecanismos físicos bem caracterizados, chamados **mecanismos de produção** ou **drives** (do inglês *drive mechanisms*), e o mecanismo dominante em um reservatório específico determina, mais do que qualquer outra variável isolada, o fator de recuperação primária esperado.

### Os quatro mecanismos de produção primária

**Depleção por gás em solução** (*solution gas drive*, também chamado *dissolved gas drive*): ocorre em reservatórios de óleo sem capa de gás inicial e sem influxo de água significativo. Enquanto a pressão do reservatório fica acima do ponto de bolha (Aula 03), o óleo produz por simples expansão — pouco eficiente. Assim que a pressão cai abaixo do ponto de bolha, gás começa a se liberar do óleo dentro do próprio reservatório; esse gás liberado, mais compressível que o óleo, expande-se e ajuda a empurrar o óleo remanescente para o poço — mas de forma progressivamente menos eficiente, porque o gás liberado tende a migrar mais rápido que o óleo através dos poros (por ter viscosidade muito menor) e a produzir preferencialmente pelo poço em vez de continuar empurrando óleo. O resultado é uma queda de pressão rápida e continuada ao longo da vida do campo, e um fator de recuperação primária tipicamente baixo — da ordem de 5% a 30% do OOIP, um dos mais baixos entre os mecanismos primários, o que torna este o mecanismo mais frequentemente complementado por recuperação secundária.

**Expansão de capa de gás** (*gas cap drive*): ocorre quando o reservatório tem, desde a descoberta, uma zona de gás livre sobrejacente ao óleo (a capa de gás, formada porque parte do gás original excede a capacidade de solubilidade do óleo naquela pressão e temperatura). À medida que o óleo é produzido e a pressão cai, a capa de gás se expande e ocupa o espaço, mantendo a pressão do reservatório de forma mais eficiente que a depleção por gás em solução isolada — se a capa for grande em relação ao volume de óleo, o suporte de pressão pode ser substancial. O fator de recuperação primária típico é intermediário, da ordem de 20% a 40%, e melhora quanto maior a razão entre volume de capa de gás e volume de óleo.

**Influxo de água** (*water drive*): ocorre quando o reservatório de óleo está em contato hidráulico com um aquífero extenso, cuja própria compressibilidade e eventual conexão com áreas de recarga fazem a água avançar para dentro do reservatório à medida que a pressão cai, substituindo o volume de óleo produzido e mantendo a pressão relativamente estável ao longo de grande parte da vida produtiva — o mecanismo mais eficiente entre os quatro, com fator de recuperação primária tipicamente de 35% a 75% (o valor mais alto do intervalo em aquíferos muito ativos e reservatórios homogêneos). A contrapartida é que, à medida que a água avança, ela eventualmente alcança e é produzida junto com o óleo em poços cada vez mais próximos do contato óleo-água original, aumentando o corte de água (*water cut*) ao longo do tempo — um padrão de produção característico que distingue este mecanismo dos demais mesmo sem medir pressão diretamente.

**Drenagem gravitacional** (*gravity drainage*): em reservatórios com inclinação estrutural significativa e boa permeabilidade vertical, a diferença de densidade entre óleo e gás (ou óleo e água) permite que o óleo migre para baixo, para os pontos mais baixos do reservatório onde poços de produção podem ser posicionados, enquanto gás ocupa progressivamente a parte alta. É lento — depende inteiramente da força da gravidade, muito mais fraca que um gradiente de pressão ativo — mas pode alcançar fatores de recuperação primária muito altos (até 60–80%) quando as condições estruturais e de permeabilidade são favoráveis, sendo por vezes o mecanismo dominante tardiamente na vida de um campo, depois que outros mecanismos já dissiparam a maior parte da energia de pressão original.

Uma ressalva de nomenclatura: parte da literatura de referência (Ahmed, cap. 4) conta ainda, **antes** destes quatro, a **expansão de rocha e fluido** (*rock and liquid expansion drive*) como mecanismo distinto — o regime que opera num óleo subsaturado enquanto a pressão ainda está acima do ponto de bolha, sustentado apenas pela compressibilidade da rocha e do líquido, e por isso de fator de recuperação muito baixo (tipicamente 3–5%). Aqui ele foi tratado como a fase inicial da depleção por gás em solução, mas vale saber que a contagem "quatro mecanismos" não é universal: algumas fontes falam em cinco ou seis.

Na prática, a maioria dos reservatórios reais produz sob combinação de mais de um mecanismo simultaneamente (um mecanismo **combinado**, ou *combination drive*), e parte do trabalho do engenheiro de reservatório é diagnosticar, a partir do comportamento observado de pressão, produção de gás e corte de água ao longo do tempo, qual mecanismo domina em cada fase da vida do campo — diagnóstico que o **balanço de materiais** (uma equação de conservação de volume entre o reservatório em duas datas distintas, considerando expansão de fluidos, influxo de água e volumes produzidos, e cuja formulação completa está fora do escopo quantitativo desta aula introdutória) formaliza numericamente.

```
Fator de recuperação primária típico por mecanismo (ordens de grandeza, não valores fixos)

solution gas drive   ▓▓▓░░░░░░░░░░░░░░░░░  ~5-30%
gas cap drive        ▓▓▓▓▓▓▓▓░░░░░░░░░░░░  ~20-40%
water drive          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░  ~35-75%
gravity drainage     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░  até ~60-80% (condições favoráveis)
```
A legenda a reter: a faixa é ampla em todos os mecanismos porque o fator de recuperação real depende fortemente da heterogeneidade específica de cada reservatório, não só do mecanismo dominante.

### Recuperação secundária: adicionando energia de fora

Quando a energia natural do reservatório se esgota — a pressão cai a um ponto em que a vazão de produção se torna anti-econômica — a **recuperação secundária** reintroduz energia externamente, tipicamente por **injeção de água** (*waterflooding*, disparadamente o método secundário mais usado na indústria mundial, por custo relativamente baixo e disponibilidade de água) em poços dedicados (poços injetores), distintos dos poços produtores, dispostos em padrões geométricos regulares (malhas de injeção, como o padrão de cinco pontos, *five-spot*) para varrer o óleo remanescente em direção aos produtores. A injeção de gás em poços dedicados é uma alternativa secundária menos comum, usada principalmente quando não há água disponível em volume suficiente ou quando as características do reservatório favorecem gás.

A injeção de água tipicamente adiciona 10 a 20 pontos percentuais de fator de recuperação acima do que a recuperação primária isolada alcançaria — por exemplo, um reservatório de depleção por gás em solução com 15% de recuperação primária pode alcançar 30-35% de recuperação total depois de um projeto de injeção de água bem-sucedido, embora o ganho real dependa fortemente da homogeneidade do reservatório (heterogeneidades permitem que a água "fure caminho" preferencial, ou *channeling*, através das zonas mais permeáveis, deixando óleo não varrido em zonas de baixa permeabilidade — um dos principais problemas práticos de projetos de injeção de água mal planejados).

### Testes de poço: medindo a capacidade de entrega antes de decidir

Além de conhecer o mecanismo de produção do reservatório como um todo, o engenheiro precisa saber quanto um poço específico é capaz de produzir — informação obtida por **testes de poço** (*well testing*), nos quais a vazão é controlada e variada de forma planejada enquanto a pressão de fundo de poço é registrada continuamente. Um teste de **drawdown** reduz a pressão de fundo (abrindo o poço à produção a partir de um estado estático) e observa como ela cai com o tempo; um teste de **buildup** faz o oposto — fecha um poço em produção e observa a pressão subir de volta em direção à pressão estática do reservatório. A análise da forma dessas curvas (em escalas apropriadas, tipicamente semilogarítmicas) permite estimar a permeabilidade efetiva ao redor do poço e o **fator de película** (*skin factor*, s) — um dano ou melhoria localizada de permeabilidade ao redor do poço, causado tipicamente por invasão de fluido de perfuração (dano positivo, reduz produtividade) ou por estimulação intencional como acidificação ou fraturamento hidráulico (dano negativo, melhora produtividade).

Uma medida prática e direta da capacidade produtiva de um poço é o **índice de produtividade** (IP ou J), definido, em regime de fluxo simplificado e para pressões acima do ponto de bolha, como a razão entre a vazão de óleo (q, em bbl/dia) e o rebaixamento de pressão que a produz (a diferença entre a pressão estática do reservatório, Pr, e a pressão de fundo de poço em fluxo, Pwf):

J = q / (Pr − Pwf)

Essa relação é aproximadamente linear apenas enquanto Pwf permanece acima do ponto de bolha (óleo monofásico fluindo); abaixo dele, gás liberado no próprio poço distorce a relação, e a curva de **IPR** (*inflow performance relationship* — a relação entre vazão e pressão de fundo de poço para todo o intervalo de Pwf, incluindo abaixo do ponto de bolha) deixa de ser uma reta e passa a ser descrita por correlações empíricas específicas (como a de Vogel, 1968, fora do escopo de cálculo desta aula introdutória, mas construída justamente para capturar essa não linearidade). A vazão máxima teórica de um poço, com Pwf reduzida a zero, é chamada **potencial absoluto de fluxo** (AOF, *absolute open flow*) — um limite teórico de referência, nunca operado na prática por razões de integridade de poço e de reservatório.

## Exemplo trabalhado

**Situação:** um teste de produção mostra que um poço, com a pressão estática do reservatório (Pr) em 3.200 psi, produz 450 bbl/dia de óleo quando a pressão de fundo de poço em fluxo (Pwf) é mantida em 2.750 psi — ambos os valores acima da pressão de ponto de bolha do óleo, portanto dentro do regime de fluxo monofásico onde o IP linear é válido. (a) Calcule o índice de produtividade do poço. (b) Estime a vazão esperada se a pressão de fundo for reduzida para 2.400 psi, ainda dentro do regime linear.

**Resolução:**

(a) J = q / (Pr − Pwf) = 450 / (3.200 − 2.750) = 450 / 450 = 1,0 bbl/dia/psi

O poço produz, nessa faixa de pressão, 1,0 barril adicional por dia para cada 1 psi adicional de rebaixamento de pressão — essa é a "constante de proporcionalidade" do poço enquanto o regime permanecer monofásico.

(b) Assumindo J constante (válido enquanto Pwf > pressão de ponto de bolha):
q = J × (Pr − Pwf) = 1,0 × (3.200 − 2.400) = 1,0 × 800 = 800 bbl/dia

Reduzir a pressão de fundo de poço de 2.750 para 2.400 psi (mais 350 psi de rebaixamento) elevaria a vazão esperada de 450 para 800 bbl/dia — um ganho substancial, mas que só se sustenta enquanto 2.400 psi ainda estiver acima da pressão de ponto de bolha daquele óleo específico. Se o ponto de bolha estivesse, por exemplo, em 2.600 psi, a pressão-alvo de 2.400 psi já estaria abaixo dele: gás começaria a se liberar no próprio poço e ao redor dele, a relação deixaria de ser linear, e a vazão real seria menor que os 800 bbl/dia previstos pelo IP constante — motivo pelo qual, na prática, verificar a posição da pressão de ponto de bolha (dado de PVT, Aula 03) é sempre o primeiro passo antes de extrapolar um IP medido para uma nova condição de operação.

## Erros comuns

- **Assumir que o mecanismo mais eficiente (influxo de água) é o mais comum.** Depleção por gás em solução — o menos eficiente dos quatro — é justamente o mais frequente na prática, e é por isso o mais comumente complementado por recuperação secundária.
- **Confundir corte de água crescente com sinal de reservatório em declínio.** Num mecanismo de influxo de água, o corte de água subir é o próprio mecanismo funcionando como esperado, não uma falha — é o sintoma característico que permite diagnosticar esse drive mesmo sem medir pressão diretamente.
- **Extrapolar o índice de produtividade J para qualquer pressão de fundo.** Como o próprio exemplo trabalhado mostra, J só é constante enquanto Pwf estiver acima do ponto de bolha; abaixo dele, a curva de IPR deixa de ser linear e um J medido em regime monofásico superestima a vazão real.
- **Achar que injeção de água sempre entrega o ganho médio de 10-20 pontos percentuais.** O ganho real depende da homogeneidade do reservatório — heterogeneidades permitem que a água "fure caminho" pelas zonas mais permeáveis (channeling), deixando óleo não varrido para trás.

## O que não concluir

- **Que "quatro mecanismos" é uma contagem universal e definitiva.** A própria aula registra a ressalva: parte da literatura conta a expansão de rocha e fluido como um quinto mecanismo distinto. A física é a mesma; o que muda é como os livros-texto agrupam as fases.
- **Que recuperação secundária é sempre injeção de água.** É disparadamente a mais comum, mas injeção de gás é usada quando não há água disponível ou quando as características do reservatório a favorecem — a escolha depende de disponibilidade e de rocha, não é automática.
- **Que o AOF (potencial absoluto de fluxo) é uma meta operacional.** É um limite teórico de referência para calibrar a curva de IPR, nunca uma vazão que se busca operar — fazê-lo comprometeria a integridade do poço e do reservatório.

## Recap relâmpago

- Recuperação primária usa apenas a energia natural do reservatório; os quatro mecanismos são depleção por gás em solução (FR ~5-30%, o mais baixo), expansão de capa de gás (~20-40%), influxo de água (~35-75%, o mais eficiente, com corte de água crescente) e drenagem gravitacional (até ~60-80%, lenta, depende de estrutura e permeabilidade vertical).
- Recuperação secundária reintroduz energia externamente, predominantemente por injeção de água (waterflooding) em poços injetores dedicados, tipicamente adicionando 10-20 pontos percentuais de fator de recuperação acima da primária isolada, sujeita a perda de eficiência por heterogeneidade (channeling).
- Testes de drawdown (queda de pressão ao abrir o poço) e buildup (subida de pressão ao fechá-lo) permitem estimar permeabilidade e o fator de película (skin), que indica dano ou estimulação ao redor do poço.
- O índice de produtividade J = q/(Pr−Pwf) é aproximadamente constante e a relação vazão-rebaixamento é linear apenas acima da pressão de ponto de bolha; abaixo dela, a curva de IPR deixa de ser linear (correlações como Vogel são usadas nesse regime).
- O potencial absoluto de fluxo (AOF) é a vazão teórica com Pwf = 0, um limite de referência nunca operado na prática.

## Próxima aula

[[12-engenharia-de-petroleo-aula-05-completacao-elevacao-artificial-e-eor|Aula 05 — Completação, elevação artificial e recuperação avançada (EOR); gestão de reservatórios]]

## Anterior

[[12-engenharia-de-petroleo-aula-03-propriedades-de-reservatorio-e-pvt|Aula 03 — Propriedades de rocha-reservatório e de fluidos (PVT)]]

## Fontes

- Ahmed, T. (2019), *Reservoir Engineering Handbook*, 5ª ed., Gulf Professional Publishing, cap. 4, 6, 10 (mecanismos de produção, testes de poço, IPR).
- Craft, B. C. & Hawkins, M. (revisado por Terry & Rogers, 2015), *Applied Petroleum Reservoir Engineering*, 3ª ed., cap. 5-6 (mecanismos de drive e recuperação primária).
- Dake, L. P. (1978), *Fundamentals of Reservoir Engineering*, Elsevier, cap. 3, 5 (balanço de materiais e mecanismos, introdução).
- Vogel, J. V. (1968), "Inflow Performance Relationships for Solution-Gas Drive Wells", *Journal of Petroleum Technology*, 20(1), p. 83–92 (correlação de IPR abaixo do ponto de bolha).
- Lee, J. (1982), *Well Testing*, SPE Textbook Series, cap. 1-3 (drawdown, buildup, skin factor).

<!--
nivel: avancado
palavras_corpo: 2040
mapa_objetivo_secao:
  geologia-avancado-m12-oa03: "Por que um reservatório produz sozinho, no início" + "Os quatro mecanismos de produção primária" + "Recuperação secundária: adicionando energia de fora" + "Testes de poço: medindo a capacidade de entrega antes de decidir" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: PETRENG-M12-A04-DRIVES-001
    claim: "Os quatro mecanismos clássicos de recuperação primária de óleo são depleção por gás em solução (solution gas drive, fator de recuperação tipicamente ~5-30% do OOIP, o mais baixo por gás liberado migrar mais rápido que o óleo), expansão de capa de gás (gas cap drive, ~20-40%), influxo de água (water drive, ~35-75%, o mais eficiente, com corte de água crescente ao longo da vida do campo) e drenagem gravitacional (gravity drainage, até ~60-80% em condições estruturais e de permeabilidade vertical favoráveis, porém lenta). Ressalva de nomenclatura: parte da literatura (Ahmed cap. 4) conta ainda a expansao de rocha e fluido (rock and liquid expansion drive, ~3-5%, regime do oleo subsaturado acima do ponto de bolha) como um quinto mecanismo distinto, de modo que a contagem 'quatro mecanismos' nao e universal."
    risk: fato
    source: "Craft & Hawkins (rev. Terry & Rogers) 2015, Applied Petroleum Reservoir Engineering, cap. 5-6; Ahmed 2019, Reservoir Engineering Handbook, cap. 4"
  - claim_id: PETRENG-M12-A04-WATERFLOOD-002
    claim: "A recuperação secundária mais comum na indústria é a injeção de água (waterflooding) em poços injetores dedicados dispostos em malhas regulares (ex. padrão five-spot), tipicamente adicionando 10 a 20 pontos percentuais de fator de recuperação acima do alcançado pela recuperação primária isolada, com eficiência reduzida por heterogeneidade do reservatório (canalização preferencial da água pelas zonas mais permeáveis)."
    risk: fato
    source: "Craft & Hawkins (rev. Terry & Rogers) 2013, cap. 5; Ahmed 2019, cap. 4"
  - claim_id: PETRENG-M12-A04-TESTES-003
    claim: "Testes de poço do tipo drawdown (queda de pressão de fundo ao abrir o poço à produção) e buildup (subida de pressão ao fechar um poço em produção), analisados em escalas semilogarítmicas apropriadas, permitem estimar a permeabilidade efetiva ao redor do poço e o fator de película (skin factor), que quantifica dano (positivo, ex. invasão de fluido de perfuração) ou estimulação (negativo, ex. acidificação, fraturamento hidráulico) localizados."
    risk: fato
    source: "Lee 1982, Well Testing, SPE Textbook Series, cap. 1-3"
  - claim_id: PETRENG-M12-A04-IP-004
    claim: "O índice de produtividade de um poço é definido como J = q / (Pr - Pwf), a razão entre a vazão de óleo e o rebaixamento de pressão (pressão estática do reservatório menos pressão de fundo de poço em fluxo), sendo aproximadamente constante (relação linear) apenas para Pwf acima da pressão de ponto de bolha do óleo; abaixo dela, a relação vazão-pressão (curva de IPR) deixa de ser linear devido à liberação de gás, sendo descrita por correlações empíricas como a de Vogel (1968)."
    risk: fato
    source: "Vogel 1968, Journal of Petroleum Technology 20(1); Ahmed 2019, Reservoir Engineering Handbook, cap. 6"
  - claim_id: PETRENG-M12-A04-AOF-005
    claim: "O potencial absoluto de fluxo (AOF, absolute open flow) é a vazão teórica máxima de um poço obtida com a pressão de fundo de poço reduzida a zero, um limite de referência da curva de IPR nunca efetivamente operado na prática por razões de integridade de poço e de reservatório."
    risk: fato
    source: "Ahmed 2019, Reservoir Engineering Handbook, cap. 6"
-->
