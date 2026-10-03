# Aula 10: Determinação do teor de anortita em plagioclásios e leitura do zonamento composicional

**ID:** geologia-avancado-m40-a10
**Módulo:** [[40-mineralogia-dos-tectossilicatos-modulo|Módulo 40 — Mineralogia dos tectossilicatos]]
**Duração estimada:** ~30 min
**Nível:** avançado (graduação plena / pós-graduação em geologia)
**Objetivo:** executar os três métodos ópticos clássicos de determinação de An, saber quando cada um se aplica, resolver a ambiguidade de leitura do diagrama, e converter variações de ângulo de extinção em história de cristalização.

## Antes de começar, você precisa saber

- Da [[40-mineralogia-dos-tectossilicatos-aula-08-leis-de-geminacao-dos-feldspatos|aula 08]]: a lei da Albita (polissintética, plano (010) ‖ clivagem {010}), a do Periclínio (plano (001) ‖ clivagem {001}), a de Carlsbad e a manobra dos 45°.
- Da [[40-mineralogia-dos-tectossilicatos-aula-09-feldspatos-ao-microscopio-e-intercrescimentos|aula 09]]: que os índices crescem monotonicamente com An, e que An = 20 é a fronteira de sinal do relevo.
- Elipsoide óptico biaxial: os eixos principais α (maior velocidade, V_g), β e γ (menor velocidade, V_p); e o que é a **projeção** α' de α num plano de corte.
- Uso da **placa de gipso** (compensador de 1ª ordem) para identificar a direção de maior velocidade num grão.

## Conteúdo

### O princípio único por trás dos três métodos

Nas séries dos plagioclásios, o ângulo **α′/(010)** — ângulo entre o eixo de maior velocidade da luz do elipsoide biaxial e o plano (010) — **varia mais ou menos regularmente com a composição**, expressa pelo teor de anortita An = An/(An + Ab).

Essa monotonia é tudo. Se o ângulo varia regularmente com An, então **medir o ângulo é medir a composição**, desde que se tenha a curva de calibração — que é o diagrama de Michel-Lévy (Figura 12 do guia, reproduzido em Tröger e DHZ).

Precisão esperada:

| Instrumento | Desvio |
|---|---|
| Microscópio petrográfico comum | **< 5 %** de An |
| Platina universal acoplada | **até 1 %** de An |

A platina universal ganha porque permite **rotacionar o grão** e selecionar ativamente os cortes mais apropriados, em vez de depender de encontrá-los por acaso na lâmina.

### Método 1 — Michel-Lévy (extinções simétricas na zona ⊥ (010))

**A geometria.** A geminação polissintética da Albita relaciona cada indivíduo com o vizinho por uma rotação de 180° em torno de um eixo normal a (010). Portanto, as direções **α′** — a projeção de α no plano do corte, para qualquer plano da zona [010] — de dois indivíduos **imediatamente adjacentes** são **simétricas em relação ao traço do plano de geminação (010)**. No terceiro indivíduo, nova rotação torna α′ paralelo ao do primeiro. Resultado: os indivíduos **ímpares** (1, 3, 5…) têm todos a mesma orientação óptica, **simétrica** à dos **pares** (2, 4, 6…).

Consequência mensurável: **qualquer seção perpendicular a (010)** apresentará ângulos de extinção α′/(010) **numericamente iguais mas opostos** para dois indivíduos adjacentes. Se o α′ de um conjunto é achado girando a platina no sentido horário, o do conjunto vizinho é achado girando no anti-horário, do mesmo valor angular.

**O procedimento.**

**A. Selecione o grão.** Ele deve estar geminado pela Lei da Albita, com os planos (010) — que coincidem tanto com a clivagem pinacoidal lateral quanto com o plano de composição — orientados o **mais perpendicularmente possível à platina**. Dois testes confirmam que o grão serve, com os traços de geminação/clivagem {010} alinhados ao fio N–S do retículo:

- **(a)** os traços são **finos e bem definidos** e **não se movem lateralmente** quando o plano focal é levemente alterado (objetiva suavemente aproximada ou afastada);
- **(b)** as cores de interferência (atraso) dos indivíduos 1, 3, 5… são **equivalentes** às dos indivíduos 2, 4, 6…

**B. Meça.** Obtenha α′/(010) para os ímpares (ângulo X₁) e para os pares (X₂). **Se o grão for adequado, a diferença entre X₁ e X₂ não deve exceder 5–6°.** Calcule o ângulo médio X_m = (X₁ + X₂)/2. Em estudos petrográficos de rotina, faça **pelo menos meia dúzia** de medidas desse tipo em grãos distintos de composição equivalente da mesma amostra, anotando cada X_m.

**C. Leia.** Leve o **maior X_m** encontrado ao diagrama de Michel-Lévy, curva **X/010**, e leia o teor de An diretamente na abscissa.

> [!warning] A ambiguidade que arruína a medida — e como resolvê-la
> Para ângulos de extinção médios **inferiores a ~15°**, a curva X/010 fornece **duas soluções**. Por exemplo, X_m = 10° admite **An₁₀ ou An₃₀**.
> **Desempate padrão:** pelo **relevo relativo ao Bálsamo do Canadá**, via linha de Becke — plagioclásio com **An < 20 tem índices menores** que o bálsamo; **An > 20, maiores**.
> **Caso-limite útil:** o oligoclásio **An₂₀** tem **extinção reta**, α′/(010) = 0°, em quaisquer cortes da zona [010]. Ele é o zero da curva.

**Três cuidados obrigatórios.**

1. **O meio de montagem.** Lâminas montadas com Araldite podem ter índice significativamente diferente de 1,54, o que desloca o desempate. Contorno: plagioclásios com **An próximo de 17 ou menor têm índices sempre inferiores aos do quartzo** — então **compare o relevo com um grão de quartzo adjacente**, que é padrão interno confiável. A intensidade e o tipo de alteração também auxiliam, já que albita de alta pureza se apresenta em geral muito límpida.
2. **Confirme que a direção medida é mesmo α′.** Use a **placa de gipso**, lembrando que α′ corresponde sempre à direção privilegiada de **maior velocidade (V_g)**.
3. **Confirme que a geminação polissintética é a da Albita, {010}, e não a do Periclínio, {001}.** Todo o método pressupõe a lei da Albita; medir sobre lamelas do Periclínio produz um número sem significado composicional.

### Método 2 — extinções simétricas em cortes (100)

**Por que existe.** O ângulo α′/(010) é **variável** nas infinitas seções perpendiculares a (010), e atinge um **valor máximo no pinacoide frontal {100}**. Esse valor máximo é, de fato, o mais diagnóstico — e é exatamente por isso que no método 1 se fazem várias medidas e se toma a maior.

**A vantagem.** Quando você **encontra** um corte (100) na zona ⊥ (010), basta **uma única medida**. Como reconhecê-lo: além das condições (a) e (b) do método 1, num corte (100) os traços da **clivagem basal {001}** e dos planos de geminação do **Periclínio** (quando presente) também aparecem **finos e nítidos** — porque este é o corte em que os planos das clivagens {010} e {001} e das geminações da Albita e do Periclínio estão todos perpendiculares à platina. É, como já dito na aula 08, o corte mais informativo do grupo.

O valor X_m obtido é projetado no diagrama, agora na curva **"extinção ‖ a"**, obtendo-se An na abscissa.

**O bônus, e ele é grande.** Em cortes (100), o **ângulo agudo entre os traços das clivagens {010} e {001} é próximo a 87°**, e plagioclásios com An < 20 têm **orientação óptica distinta** daqueles com An > 20. Em cortes (100) de um conjunto de indivíduos geminados, os traços da clivagem basal desenham um padrão em **zig-zag**, porque os traços de dois indivíduos contíguos são sempre simétricos em relação ao traço de (010). E então:

> [!important] O teste do ângulo agudo — o único sem margem para dúvida
> Observe, **num único indivíduo**, os dois ângulos formados pelos traços das clivagens {010} e {001} — um agudo (~87°) e um obtuso. Localize a direção de extinção **α′**:
> **α′ no ângulo AGUDO ⇒ plagioclásio com An > 20**, seguramente.
> **α′ no ângulo OBTUSO ⇒ An < 20.**
> Nos casos em que não se consegue comparar adequadamente os índices do plagioclásio e do meio, em que não se tem certeza do índice real do meio, ou em que não há cristais de quartzo adjacentes, **esta é a única técnica que não deixa margem para dúvidas**.

### Método 3 — geminados combinados Albita–Carlsbad

**Quando usar.** É simples e traz resultados excelentes. Aplica-se quando os grãos apresentam **simultaneamente** as geminações da Albita e de Carlsbad — situação **muito comum em rochas básicas e intermediárias** com plagioclásio abundante.

**Reconhecimento.** Sob polarizadores cruzados, posicione os traços dos planos de geminação a **45°** dos fios N–S/E–W do retículo — a posição de aclaramento máximo (a manobra da aula 08). Nessa posição:

- se estiver presente **somente** a geminação da Albita, todos os indivíduos geminados apresentam a **mesma cor de interferência** e ficam indistintos uns dos outros;
- se a geminação de **Carlsbad** também estiver presente, os dois indivíduos por ela relacionados ficam **perfeitamente visíveis**, porque mostram **cores de interferência distintas** — o eixo binário de Carlsbad se orienta segundo **[001]**, e não é anulado por essa posição.

**Procedimento.** Meça os ângulos de extinção como no método 1, mas obtenha **dois** ângulos médios, um por domínio de Carlsbad:

- **X_m**, dos geminados da Albita de **um** dos domínios Carlsbad (ângulos X₁, X₂);
- **Y_m**, dos geminados da Albita do **outro** domínio Carlsbad (ângulos Y₁, Y₂).

**Leitura.** Lance os dois valores no diagrama de dupla entrada: **o menor no eixo das ordenadas**, o **maior nas curvas denominadas "extinção maior"**. O **ponto de interseção** define diretamente na abscissa o teor de An. A distinção An < 20 / An > 20 se faz como nos métodos anteriores.

Embora não seja estritamente necessário, é muito mais fácil — e os melhores resultados são obtidos — quando os planos de geminação da Albita, e portanto os de Carlsbad, estão **perpendiculares à platina**. Basta **uma única medida**, mas não custa efetuar medidas adicionais para confirmação.

### Comparação dos três métodos

| | Método 1 (Michel-Lévy) | Método 2 (corte 100) | Método 3 (Albita–Carlsbad) |
|---|---|---|---|
| Exige | geminação da Albita | corte (100) + Albita | Albita **e** Carlsbad |
| N.º de medidas | ~6 grãos, toma-se o **maior** X_m | **1** | **1** (dois ângulos no mesmo grão) |
| Curva usada | X/010 | extinção ‖ a | dupla entrada, "extinção maior" |
| Vantagem | sempre aplicável | dá o valor máximo diretamente; permite o **teste do ângulo agudo** | dispensa procurar corte especial; excelente em rochas básicas |
| Fraqueza | depende de sorte estatística no corte | achar o corte (100) | exige as duas leis no mesmo grão |

### Zonamento: quando o ângulo muda dentro do grão

Variações composicionais em minerais são decorrência natural da existência de soluções sólidas: cátions diferentes podem ocupar o mesmo sítio, e a ordem de ocupação é determinada pelos **potenciais químicos** dos elementos e pelas características do ambiente de cristalização (o mecanismo é o tema da aula 14).

**Regra de ocorrência:** algum tipo de zonamento químico estará presente na **maioria dos feldspatos das rochas magmáticas**; feldspatos composicionalmente **homogêneos** devem ser esperados principalmente em **rochas metamórficas de médio a alto grau**, onde houve tempo e temperatura para reequilíbrio.

**Como se detecta.** Nos plagioclásios as variações relevantes envolvem a substituição Ca²⁺Al³⁺[Na⁺Si⁴⁺]₋₁, expressa pelo teor de An — do qual depende o ângulo α′/(010). Logo, **variações composicionais significativas se detectam como variações do ângulo de extinção**, e devem, sempre que possível, **ser medidas**. Na prática, as posições de extinção de cristais zonados de forma mais ou menos concêntrica **variam do núcleo para a borda** à medida que se gira a platina — o grão "se apaga por anéis".

**Os três padrões:**

| Padrão | Definição |
|---|---|
| **Normal** | bordas mais **sódicas** — o teor de An **diminui** do núcleo para a borda |
| **Inverso** | bordas mais **cálcicas** |
| **Oscilatório** (recorrente) | o teor de An **oscila** do núcleo para a borda |

Os padrões podem ser extremamente complexos, conforme a história evolutiva do plagioclásio. **Descrições adequadas devem incluir, sempre que possível, estimativas para o intervalo composicional medido** — por exemplo: *"núcleos labradoríticos que passam de modo gradual (ou brusco, normal ou oscilatoriamente) para bordas oligoclásicas"*; *"núcleos de andesina que passam para bordas de albita"*. Variações nos conteúdos de **K, Sr e Ba** também são comuns em plagioclásios de algumas rochas, mas **não são detectadas ao microscópio petrográfico** — exigem microssonda.

> [!warning] A borda albítica que NÃO é zonamento
> Em muitas rochas feldspáticas aparecem **bordas albíticas muito límpidas e puras** sobrecrescidas em plagioclásio, normalmente **acompanhando os intercrescimentos mirmequíticos**, nos contatos entre plagioclásio e feldspato potássico ou entre cristais de feldspato potássico.
> Essas bordas estão em geral associadas a fenômenos **tardi- a pós-magmáticos** — "metassomatismo" sódico e migração de albita **exsolvida** a partir de feldspatos alcalinos e reprecipitada sobre o plagioclásio. **Elas não têm, em geral, relação direta com variações composicionais decorrentes da cristalização primária.** Descrevê-las como "zonamento normal extremo" é um erro de interpretação, não de medida.

**E nos feldspatos alcalinos?** O reconhecimento de zonamento **não é simples** ao microscópio. Variações menores no padrão de extinção podem ser sugestivas de modificações composicionais, estruturais, ou ainda de deformações superimpostas — três causas que a óptica não separa. O único indício razoavelmente confiável é indireto: **variações na morfologia ou na abundância das lamelas de albita em pertitas** (ou de feldspato potássico nas antipertitas) são **indicação qualitativa positiva de algum zonamento químico primário** — porque a quantidade de fase exsolvida depende da composição inicial local (regra 2 da aula 07).

## Exemplo trabalhado

**Situação:** num basalto, seis grãos de plagioclásio geminados pela Albita dão X_m = 27°, 30°, 24°, 32°, 29° e 26°. Um sétimo grão, num corte (100) reconhecido pelos traços nítidos das duas clivagens, dá X_m = 33°, e a direção α′ cai no **ângulo agudo** entre {010} e {001}. Determine An e comente.

**Raciocínio.**

**Passo 1 — tome o maior.** Entre os seis do método 1, o maior é 32°. O sétimo, medido num corte (100) genuíno, dá 33° — coerente, e é o **valor máximo verdadeiro** por construção, já que {100} é onde α′/(010) é máximo. A concordância entre 32° e 33° é o melhor controle de qualidade possível: significa que o grão de maior X_m do método 1 já estava praticamente no corte ótimo.

**Passo 2 — resolva a ambiguidade.** X_m = 33° está **muito acima de 15°**, então a curva X/010 dá solução única — não há dualidade a desempatar. E o teste independente confirma o campo: α′ no **ângulo agudo** ⇒ **An > 20**, consistente.

**Passo 3 — leia.** Um ângulo de extinção simétrico máximo da ordem de 33° corresponde, na curva de Michel-Lévy, a um plagioclásio na faixa de **An ≈ 55–60** — **labradorita**.

**Passo 4 — interprete.** Labradorita é exatamente o plagioclásio esperado num basalto. Duas verificações fecham o raciocínio: (i) o relevo deve ser **positivo** frente ao bálsamo e maior que o do quartzo, se houver — coerente com An > 20; (ii) vale procurar zonamento, porque em rocha vulcânica ele é a regra: espere núcleos mais cálcicos passando a bordas mais sódicas (zonamento normal), com possíveis oscilações se houve recarga de câmara. A descrição correta seria algo como *"labradorita An₅₅₋₆₀, com zonamento normal e oscilatório subordinado"*, e não apenas "plagioclásio cálcico".

**A lição:** o método 1 é estatístico por construção — ele **procura** o corte (100) na sorte de seis grãos. Quando você acha um corte (100) de fato, o método 2 entrega o mesmo número com uma medida e ainda oferece um teste independente de campo composicional.

## Erros comuns

- **Tomar a média dos X_m em vez do maior.** O valor diagnóstico é o **máximo**, atingido em {100}; médias entre cortes aleatórios subestimam An sistematicamente.
- **Confundir X_m (a média de X₁ e X₂ **dentro** de um grão) com o maior X_m (**entre** grãos).** São dois níveis de agregação diferentes, e a etapa B produz um por grão.
- **Medir sobre geminação do Periclínio achando que é da Albita.** Confirme o plano: Albita ‖ {010}, Periclínio ‖ {001}.
- **Esquecer de verificar α′ com a placa de gipso.** Medir sobre γ′ em vez de α′ produz o ângulo complementar e um An errado.
- **Aplicar o desempate por relevo sem checar o meio.** Em lâmina de Araldite, o "zero" não é 1,54. Compare com quartzo, ou use o teste do ângulo agudo.
- **Aceitar grãos com |X₁ − X₂| > 6°.** Isso indica corte inadequado — o plano (010) não está suficientemente perpendicular à platina — e a medida deve ser descartada.

## O que não concluir

- **Que o ângulo de extinção mede An em qualquer corte.** Ele mede An **no corte máximo**; em cortes arbitrários, subestima.
- **Que zonamento normal prova cristalização fracionada simples.** Prova apenas resfriamento fora do equilíbrio total; a causa pode ser cinética local, mistura de magmas, ou variação de pressão de fluidos (aula 14).
- **Que a ausência de zonamento visível significa homogeneidade química.** Variações de K, Sr e Ba não aparecem opticamente, e zonamentos de baixa amplitude em An passam despercebidos dentro do desvio de ±5 %.
- **Que borda albítica límpida é o extremo sódico do zonamento primário.** Em geral é sobrecrescimento tardi- a pós-magmático, e a companhia da mirmequita é o indício.
- **Que a platina universal é dispensável em trabalho quantitativo.** O ganho de ±5 % para ±1 % é a diferença entre "labradorita" e "An₅₆" — e termobarometria com plagioclásio exige a segunda.

## Recap relâmpago

- **Princípio:** o ângulo **α′/(010)** varia regularmente com An ⇒ medir ângulo = medir composição. Precisão **< 5 %** no microscópio comum, **até 1 %** com platina universal.
- **Método 1 (Michel-Lévy):** grão com geminação da Albita, (010) ⊥ platina; testes (a) traços finos que não migram com o foco e (b) cores iguais nos ímpares e pares; **|X₁ − X₂| ≤ 5–6°**; X_m = (X₁+X₂)/2; **~6 grãos** e usa-se **o maior X_m** na curva **X/010**.
- **Ambiguidade abaixo de ~15°:** X_m = 10° ⇒ An₁₀ **ou** An₃₀. Desempate por **relevo** (An < 20 ⇒ índices menores que o bálsamo). **An₂₀ tem extinção reta.**
- **Método 2 (corte 100):** α′/(010) é **máximo em {100}**; uma medida basta; curva **extinção ‖ a**. Corte reconhecido pelos traços nítidos de {010} **e** {001} (ângulo agudo ~**87°**, zig-zag). **Teste do ângulo agudo: α′ no agudo ⇒ An > 20; no obtuso ⇒ An < 20** — o único sem margem de dúvida.
- **Método 3 (Albita–Carlsbad):** com traços a **45°**, só Carlsbad contrasta. Medir **X_m** e **Y_m**, um por domínio Carlsbad; **menor na ordenada, maior nas curvas "extinção maior"**; interseção dá An. Comum em rochas básicas e intermediárias.
- **Sempre:** confirmar α′ com **placa de gipso**; confirmar que a lei é a da **Albita**; cuidado com **Araldite** — compare com quartzo (An ≲ 17 tem índice menor que o quartzo).
- **Zonamento:** regra nas magmáticas; homogeneidade esperada em metamórficas de grau médio a alto. **Normal** (bordas sódicas) · **inverso** · **oscilatório**. Reporte o **intervalo** (ex.: núcleo labradorítico → borda oligoclásica). K, Sr, Ba **não** aparecem opticamente.
- **Borda albítica límpida com mirmequita ⇒ tardi/pós-magmática**, não zonamento primário. Em feldspato alcalino, zonamento só se infere qualitativamente por **variação das lamelas pertíticas**.

## Próxima aula

[[40-mineralogia-dos-tectossilicatos-aula-11-feldspatoides|Aula 11 — Feldspatoides: nefelina, kalsilita, leucita, sodalita e a barreira da saturação em sílica]]

## Anterior

[[40-mineralogia-dos-tectossilicatos-aula-09-feldspatos-ao-microscopio-e-intercrescimentos|Aula 09 — Feldspatos ao microscópio e intercrescimentos]]

## Fontes

- Princípio do método óptico, precisões, os três métodos com procedimentos completos, ambiguidade abaixo de 15° e desempate por relevo, extinção reta do An₂₀, cuidados com placa de gipso e com a lei de geminação, ângulo de 87° entre as clivagens em cortes (100), teste do ângulo agudo, procedimento do método Albita–Carlsbad, e todo o item de zonamento (padrões normal, inverso e oscilatório; bordas albíticas tardias; zonamento em feldspatos alcalinos): Vlach, S. R. F., *A Classe dos Tectossilicatos: Guia Geral da Teoria e Exercício*, IGc-USP, Série Didática USP, itens III.6 e III.7, e Figura 12.
- Diagrama de Michel-Lévy e curvas de variação de índices, ângulo 2V e ângulos de extinção com a composição (Figura 12 do guia): quadro do Laboratório de Microscopia Petrográfica do IGc-USP; ver também Deer, W. A., Howie, R. A. & Zussman, J. (1992), *An Introduction to the Rock-Forming Minerals*, 2ª ed., Longman, e Tröger, W. E. (1979), *Optical Determination of Rock-Forming Minerals*, 4ª ed., Schweizerbart, para os esquemas morfológicos e determinativos correspondentes.

<!--
nivel: avancado
palavras_corpo: ~2380

mapa_objetivo_secao:
  geologia-avancado-m40-oa05: "O princípio único por trás dos três métodos" + "Método 1 — Michel-Lévy" + "Método 2 — extinções simétricas em cortes (100)" + "Método 3 — geminados combinados Albita–Carlsbad" + "Comparação dos três métodos" + "Zonamento: quando o ângulo muda dentro do grão" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: TECTO-M40-A10-PRINCIPIO-001
    claim: "Nas series dos plagioclasios o angulo alfa-linha/(010), entre o eixo de maior velocidade da luz do elipsoide biaxial e o plano (010), varia mais ou menos regularmente com o teor de anortita An/(An+Ab), permitindo estimar a composicao com desvio inferior a 5 % ao microscopio comum e ate 1 % com platina universal."
    risk: numero
    source: "Vlach, Guia dos Tectossilicatos, item III.6 e Figura 12"
  - claim_id: TECTO-M40-A10-SIMETRIA-002
    claim: "A geminacao polissintetica da Albita relaciona cada individuo ao vizinho por rotacao de 180 graus em torno de um eixo normal a (010), de modo que as direcoes alfa-linha de individuos adjacentes sao simetricas em relacao ao traco de (010) e qualquer secao perpendicular a (010) apresenta angulos de extincao numericamente iguais mas opostos para dois individuos adjacentes."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item III.6"
  - claim_id: TECTO-M40-A10-PROCEDIMENTO-003
    claim: "No metodo de Michel-Levy o grao adequado mostra tracos finos e bem definidos que nao se movem lateralmente com a variacao do plano focal e cores de interferencia equivalentes entre individuos impares e pares; a diferenca entre os angulos medidos nao deve ser superior a 5-6 graus; calcula-se Xm como a media de X1 e X2, fazem-se pelo menos meia duzia de medidas em graos distintos e considera-se o maior Xm no diagrama, curva X/010."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item III.6"
  - claim_id: TECTO-M40-A10-AMBIGUIDADE-004
    claim: "Para angulos de extincao medios inferiores a cerca de 15 graus a curva X/010 fornece duas solucoes distintas para o teor de An (por exemplo Xm = 10 graus admite An10 ou An30); a resolucao e feita pelo relevo relativo ao Balsamo do Canada, lembrando que plagioclasio com An < 20 tem indices menores que o balsamo e An > 20 tem indices maiores; o oligoclasio An20 tem extincao reta em quaisquer cortes da zona [010]."
    risk: numero
    source: "Vlach, Guia dos Tectossilicatos, item III.6 e Figura 12"
  - claim_id: TECTO-M40-A10-MAXIMO-005
    claim: "O angulo de extincao alfa-linha/(010) e variavel nas infinitas secoes perpendiculares a (010) e atinge valor maximo no pinacoide frontal {100}, sendo esse valor maximo o mais diagnostico para a determinacao do teor de An."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item III.6"
  - claim_id: TECTO-M40-A10-ANGULO-AGUDO-006
    claim: "Em cortes (100) o angulo agudo entre os tracos das clivagens {010} e {001} e proximo a 87 graus; quando a direcao de extincao alfa-linha se encontra no angulo agudo definido pelas clivagens observadas em um unico individuo trata-se seguramente de plagioclasio com An > 20, e quando esta no angulo obtuso o teor de An e inferior a 20; esta e a unica tecnica que nao deixa margem para duvidas quando nao se pode comparar indices de refracao."
    risk: numero
    source: "Vlach, Guia dos Tectossilicatos, item III.6"
  - claim_id: TECTO-M40-A10-CARLSBAD-METODO-007
    claim: "No metodo dos geminados combinados Albita-Carlsbad, com os tracos dos planos de geminacao a 45 graus dos fios do reticulo, os individuos relacionados apenas pela Albita mostram a mesma cor de interferencia e ficam indistintos, enquanto os dois individuos relacionados por Carlsbad mostram cores distintas; medem-se dois angulos medios Xm e Ym, um por dominio Carlsbad, lancando-se o menor no eixo das ordenadas e o maior nas curvas de extincao maior, e a intersecao define o teor de An na abscissa."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, itens III.5 e III.6 e Figura 12"
  - claim_id: TECTO-M40-A10-CUIDADOS-008
    claim: "Deve-se verificar com a placa de gipso que a direcao considerada e de fato alfa-linha, a direcao privilegiada de maior velocidade, e confirmar que a geminacao polissintetica observada e a da Lei da Albita {010} e nao a do Periclinio {001}; plagioclasios com teor de An proximo a 17 ou menor tem indices sempre inferiores aos do quartzo, o que permite usar graos de quartzo adjacentes como referencia."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item III.6"
  - claim_id: TECTO-M40-A10-ZONAMENTO-009
    claim: "Algum tipo de zonamento quimico esta presente na maioria dos feldspatos de rochas magmaticas, enquanto feldspatos composicionalmente homogeneos devem ser esperados principalmente em rochas metamorficas de medio a alto grau; zonamentos normais tem bordas mais sodicas, inversos o contrario, e oscilatorios ou recorrentes apresentam oscilacao do teor de An do nucleo para a borda; variacoes de K, Sr e Ba sao comuns mas nao detectadas ao microscopio petrografico."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item III.7"
  - claim_id: TECTO-M40-A10-BORDA-ALBITICA-010
    claim: "Bordas albiticas muito limpidas sobrecrescidas em plagioclasio, acompanhando intercrescimentos mirmequiticos nos contatos entre plagioclasio e feldspato potassico, estao associadas a fenomenos tardi- a pos-magmaticos de metassomatismo sodico e a migracao de albita exsolvida a partir de feldspatos alcalinos, e nao tem em geral relacao direta com variacoes composicionais da cristalizacao primaria."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item III.7"
  - claim_id: TECTO-M40-A10-ZONAMENTO-ALCALINO-011
    claim: "O reconhecimento de zonamentos composicionais em feldspatos alcalinos nao e simples ao microscopio; variacoes menores no padrao de extincao podem indicar modificacoes composicionais, estruturais ou deformacoes superimpostas, e variacoes na morfologia ou abundancia das lamelas de albita em pertitas ou de feldspato potassico em antipertitas sao indicacao qualitativa positiva de zonamento quimico primario."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item III.7"
-->
