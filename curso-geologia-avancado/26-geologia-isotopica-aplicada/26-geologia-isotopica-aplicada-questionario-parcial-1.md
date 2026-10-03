# Questionário parcial 1 — Módulo 26: Geologia isotópica aplicada

**Módulo:** [[26-geologia-isotopica-aplicada-modulo|Módulo 26 — Geologia isotópica aplicada]]
**Cobertura:** Aulas 01 a 03 — a lei do decaimento radioativo e a equação geral da idade; a espectrometria de massa; o decaimento ramificado do ⁴⁰K e os métodos K-Ar e ⁴⁰Ar/³⁹Ar; a técnica da isócrona no sistema Rb-Sr e a razão inicial de estrôncio como traçador de fonte.
**Recorte:** dos fundamentos ao primeiro sistema completo. A parcial 1 testa se você sabe deduzir e aplicar a equação geral da idade, reconhecer as quatro premissas que a sustentam, calcular uma idade K-Ar e ler um espectro ⁴⁰Ar/³⁹Ar, e entender por que o Rb-Sr precisa da técnica da isócrona onde o K-Ar não precisa.
**Objetivos avaliados:** `geologia-avancado-m26-oa01` (integral — a01), `geologia-avancado-m26-oa02` (parcial — sistemas K-Ar/Ar-Ar e Rb-Sr), `geologia-avancado-m26-oa03` (parcial — razão inicial de Sr)
**Pontuação total:** 100 pontos · o gabarito fica oculto; responda antes de abrir.

---

### 1. Múltipla escolha — `geologia-avancado-m26-q01` · oa01 · 8 pts

Sobre a relação entre a constante de decaimento (λ) e a meia-vida (t₁/₂) de um radionuclídeo, assinale a afirmação correta.

- a) λ e t₁/₂ são duas propriedades físicas independentes, cada uma medida separadamente em laboratório
- b) λ e t₁/₂ carregam exatamente a mesma informação — t₁/₂ = ln(2)/λ —, e a literatura de geocronologia cita as duas de forma intercambiável
- c) t₁/₂ é constante para um radionuclídeo, mas λ varia com a temperatura e a pressão do ambiente geológico
- d) Quanto maior a meia-vida, maior a constante de decaimento, porque um sistema "mais lento" decai com taxa mais alta

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A Aula 01 é explícita: meia-vida e constante de decaimento "carregam exatamente a mesma informação — são só duas formas de expressar a mesma taxa". "a" erra ao tratá-las como duas medidas independentes. "c" inverte uma premissa central do módulo (premissa 3 da Aula 01): a constante de decaimento não é sensível a temperatura, pressão ou ligação química nas condições da crosta e do manto. "d" inverte a relação matemática: t₁/₂ = ln(2)/λ é uma relação **inversa** — quanto maior λ (decaimento mais rápido), menor a meia-vida, não maior.
</details>

---

### 2. Aplicação / cálculo — `geologia-avancado-m26-q02` · oa01 · 12 pts

Um mineral hipotético de um sistema radioativo fictício "Y" tem constante de decaimento λ = 3,00 × 10⁻¹⁰ ano⁻¹ e não incorporou nenhum isótopo-filho inicial. Uma análise moderna mede uma razão filho radiogênico/pai remanescente D*/P = 0,150.

(a) Calcule a idade do mineral. (b) Calcule a meia-vida do sistema. (c) Faça a verificação de sanidade: a fração de decaimento observada é coerente com uma idade bem menor que a meia-vida?

<details>
<summary>Ver resposta</summary>

**(a)** Aplicando a equação geral da idade da Aula 01:

t = (1/λ)·ln(1 + D*/P) = ln(1,150)/3,00×10⁻¹⁰

ln(1,150) ≈ 0,139762. Logo t ≈ 0,139762/3,00×10⁻¹⁰ ≈ 4,659×10⁸ anos ≈ **465,9 milhões de anos**.

**(b)** t₁/₂ = ln(2)/λ = 0,693147/3,00×10⁻¹⁰ ≈ 2,310×10⁹ anos ≈ **2,31 bilhões de anos (2,31 Ga)**.

**(c)** Sim: 465,9 Ma é cerca de 20% da meia-vida de 2,31 Ga — coerente com D*/P = 0,150, que corresponde a uma fração ainda pequena do pai original convertida em filho (para cada átomo-pai remanescente há 0,15 átomo-filho acumulado, uma conversão parcial). É exatamente o hábito de checagem cruzada que a Aula 01 recomenda carregar para os cálculos das aulas seguintes.
</details>

---

### 3. Verdadeiro ou Falso (justifique) — `geologia-avancado-m26-q03` · oa01 · 10 pts

"A temperatura de bloqueio de um mineral é a temperatura na qual ele cristaliza a partir de um magma; abaixo dela, o mineral ainda não existe como fase sólida."

<details>
<summary>Ver resposta</summary>

**Falso.**

A temperatura de bloqueio não tem relação com a cristalização do mineral, e sim com a retenção do isótopo-filho depois que o mineral já existe: é a temperatura abaixo da qual a difusão do isótopo-filho para fora da rede cristalina fica lenta demais para importar em escala geológica. Acima da temperatura de bloqueio, o filho produzido pelo decaimento escapa por difusão à medida que é gerado, e o "relógio" isotópico não acumula nada; abaixo dela, o mineral retém o que produz e o relógio começa a contar. É por isso que uma idade isotópica data, a rigor, o **fechamento** do sistema (o resfriamento abaixo da temperatura de bloqueio), que pode ser um evento bem posterior à cristalização do mineral — o ponto de dificuldade central do módulo, que reaparece na perda de argônio (Aula 02), na perda de chumbo por dano radioativo em zircão (Aula 05) e na troca de estrôncio por fluido hidrotermal (Aula 03).
</details>

---

### 4. Dissertativa curta — `geologia-avancado-m26-q04` · oa01 · 10 pts

Enuncie as quatro premissas que precisam se sustentar para que uma idade isotópica seja geologicamente significativa, e para cada uma dê um exemplo, discutido no módulo, de como ela pode falhar.

<details>
<summary>Ver resposta</summary>

Uma boa resposta cobre as quatro premissas da Aula 01, cada uma com um exemplo de violação tratado no módulo:

1. **O sistema precisa estar fechado** — pode falhar por perda de argônio por difusão térmica (Aula 02), perda de chumbo por dano radioativo em zircão (Aula 05) ou troca de estrôncio por fluido hidrotermal (Aula 03).
2. **A quantidade inicial de filho precisa ser conhecida ou determinável** — desprezível por construção no K-Ar (o argônio escapa do magma antes da cristalização), mas não no Rb-Sr, onde o estrôncio inicial não é desprezível e exige a técnica da isócrona (Aula 03).
3. **A constante de decaimento precisa ser conhecida com precisão e ser de fato constante** — pode falhar não pela física (que é estável nas condições da crosta e do manto), mas por incerteza de calibração: o próprio módulo mostra valores concorrentes para λ do ⁴⁰K (Aula 02) e do ⁸⁷Rb (Aula 03).
4. **A razão isotópica precisa ser medida com exatidão e precisão suficientes** — tarefa da espectrometria de massa (TIMS, MC-ICP-MS), que pode falhar por erro analítico ou por combinar medidas independentes (a fragilidade estrutural do K-Ar convencional, que mede potássio e argônio em alíquotas separadas).
</details>

---

### 5. Múltipla escolha — `geologia-avancado-m26-q05` · oa02 · 8 pts

O ⁴⁰K decai por dois caminhos concorrentes. Qual afirmação descreve corretamente essa ramificação e por que apenas um dos ramos é geocronologicamente útil?

- a) ~89,5% decai por captura eletrônica para ⁴⁰Ar, gás nobre que escapa do magma antes da cristalização; o ramo para ⁴⁰Ca é inútil porque o cálcio radiogênico se perde na massa de cálcio comum já presente
- b) ~89,5% decai por emissão β⁻ para ⁴⁰Ca; o ramo para ⁴⁰Ar (~10,5%, por captura eletrônica) é o único útil, porque o argônio, gás nobre inerte, não entra na estrutura cristalina até ser produzido *in situ*
- c) Os dois ramos são igualmente úteis, e a idade K-Ar convencional soma as contribuições de ⁴⁰Ca e ⁴⁰Ar radiogênicos
- d) ~10,5% decai por emissão β⁻ para ⁴⁰Ar; o ramo majoritário (~89,5%) produz ⁴⁰Ca, que é o isótopo efetivamente medido em espectrometria de massa de gás nobre

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Os valores corretos (Steiger & Jäger, 1977) são ~89,5% por β⁻ para ⁴⁰Ca e ~10,5% por captura eletrônica para ⁴⁰Ar. O ramo do cálcio é geocronologicamente inútil porque o cálcio já é abundantíssimo na maioria dos minerais, e não há como separar analiticamente o ⁴⁰Ca "novo" do cálcio original. O ramo do argônio sustenta todo o método porque o argônio é quimicamente inerte e não entra na rede cristalina do mineral em formação — todo ⁴⁰Ar hoje aprisionado é presumivelmente radiogênico. "a" troca o modo de decaimento do ramo majoritário (é β⁻ para ⁴⁰Ca, não captura eletrônica para ⁴⁰Ar). "c" e "d" invertem frações e conceito.
</details>

---

### 6. Aplicação / cálculo — `geologia-avancado-m26-q06` · oa02 · 12 pts

Uma amostra de biotita mostra uma razão medida ⁴⁰Ar*/⁴⁰K = 0,00350. Usando os valores convencionais de Steiger & Jäger (1977) — λ = 5,543 × 10⁻¹⁰ ano⁻¹ e λε = 0,581 × 10⁻¹⁰ ano⁻¹ —, calcule a idade K-Ar convencional dessa biotita.

<details>
<summary>Ver resposta</summary>

Fator de correção pela ramificação:

λ/λε = 5,543×10⁻¹⁰ / 0,581×10⁻¹⁰ ≈ 9,540

Substituindo na equação da idade K-Ar:

t = (1/λ)·ln[(λ/λε)·(⁴⁰Ar*/⁴⁰K) + 1] = (1/5,543×10⁻¹⁰)·ln[9,540 × 0,00350 + 1]

9,540 × 0,00350 = 0,033390 → ln(1,033390) ≈ 0,032845

t ≈ 0,032845/5,543×10⁻¹⁰ ≈ 5,926×10⁷ anos ≈ **59,3 milhões de anos**

Como no Exemplo 1 da Aula 02, essa idade só é confiável se o sistema permaneceu fechado desde o evento que se quer datar e se a medida de potássio total (em alíquota separada) corresponde à mesma população mineral analisada para argônio — a fragilidade estrutural do método que o ⁴⁰Ar/³⁹Ar resolve.
</details>

---

### 7. Múltipla escolha — `geologia-avancado-m26-q07` · oa02 · 8 pts

Qual é a vantagem estrutural do método ⁴⁰Ar/³⁹Ar sobre o K-Ar convencional?

- a) Ele mede uma constante de decaimento diferente do ⁴⁰K, mais precisa e sem controvérsia de calibração
- b) Ele dispensa a medida química de potássio, substituindo-a por uma segunda medida de argônio (³⁹Ar, produzido por irradiação de nêutrons) feita na mesma alíquota e no mesmo instrumento que o ⁴⁰Ar, eliminando o erro sistemático de combinar duas medidas independentes
- c) Ele elimina qualquer incerteza de calibração, porque o fator J é uma constante universal que não depende do monitor de irradiação usado
- d) Ele converte todo o potássio da amostra em argônio antes da análise, tornando a medida de ⁴⁰K desnecessária mesmo indiretamente

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A fragilidade estrutural do K-Ar convencional é depender de duas medidas totalmente independentes (potássio químico e argônio por espectrometria de gás nobre), em geral feitas em alíquotas separadas — se o mineral perdeu argônio sem que isso deixe marca na medida de potássio, a idade subestima silenciosamente. O ⁴⁰Ar/³⁹Ar evita isso irradiando a amostra com nêutrons, convertendo uma fração conhecida de ³⁹K em ³⁹Ar: toda a informação sobre potássio passa a vir de uma razão entre dois isótopos de argônio medidos na mesma alíquota. "a" é falso — a constante de decaimento do ⁴⁰K é a mesma nos dois métodos, e tem, ela própria, calibrações concorrentes. "c" é falso — o fator J é calibrado empiricamente por um monitor de idade conhecida a cada irradiação, não é universal. "d" descreve mal o mecanismo: só uma fração pequena e conhecida do ³⁹K vira ³⁹Ar, não "todo o potássio".
</details>

---

### 8. Verdadeiro ou Falso (justifique) — `geologia-avancado-m26-q08` · oa02 · 10 pts

"Um espectro de idade ⁴⁰Ar/³⁹Ar em forma de U, com idades mais **altas** nas etapas de temperatura **baixa** e mais **baixas** nas etapas de temperatura **alta**, é a assinatura de perda parcial de argônio por reaquecimento."

<details>
<summary>Ver resposta</summary>

**Falso.**

A afirmação inverte o padrão. Quando o mineral perdeu argônio de forma parcial e recente, o espectro típico mostra idades aparentes anomalamente **jovens** nas etapas de temperatura **mais baixa** (o gás retido em sítios cristalinos mais fracamente ligados, mais suscetíveis à perda por difusão), subindo progressivamente até se aproximar da idade original de cristalização nas etapas de temperatura **mais alta** (gás retido em sítios estruturais mais robustos, que resistiram à perda). Um espectro sem perda de argônio, ao contrário, mostra um **platô**: etapas contíguas (cobrindo tipicamente ≥50% do ³⁹Ar liberado) com idades concordantes em 2σ, sem tendência sistemática.
</details>

---

### 9. Dissertativa — `geologia-avancado-m26-q09` · oa02 · 10 pts

Explique por que o método K-Ar (Aula 02) pode, na prática, assumir que o filho inicial (⁴⁰Ar) é desprezível numa medida de mineral único, enquanto o método Rb-Sr (Aula 03) não pode fazer a mesma suposição para o ⁸⁷Sr — e por que essa diferença obriga o Rb-Sr a recorrer à técnica da isócrona.

<details>
<summary>Ver resposta</summary>

O argônio é um gás nobre quimicamente inerte: um magma que está subindo e resfriando perde o argônio que contém antes de qualquer mineral cristalizar, de modo que ⁴⁰Ar inicial em um mineral ígneo recém-formado é, na prática, próximo de zero — a premissa de filho inicial desprezível se sustenta numa propriedade química conveniente, específica do argônio. O estrôncio não tem essa sorte: é um elemento litófilo comum, que entra facilmente na estrutura cristalina de minerais (plagioclásio, apatita, biotita, K-feldspato) **desde a cristalização**, trazendo consigo sua própria mistura natural de isótopos, incluindo ⁸⁷Sr não radiogênico herdado da fonte do magma. Não há como, medindo um único mineral, separar quanto do ⁸⁷Sr presente é filho radiogênico acumulado e quanto já estava lá desde o início — a equação geral da idade, sozinha, não resolve esse sistema. A técnica da isócrona resolve o problema ajustando uma reta a um conjunto de amostras cogenéticas (mesma idade, mesma razão inicial, Rb/Sr diferente): a inclinação da reta dá a idade e o intercepto dá diretamente a razão inicial de estrôncio, sem que ela precise ser conhecida de antemão.
</details>

---

### 10. Aplicação / cálculo — `geologia-avancado-m26-q10` · oa03 · 12 pts

Uma isócrona Rb-Sr construída a partir de quatro frações minerais de um corpo ígneo (diferente do exemplo da aula) tem inclinação 0,003300 e intercepto (⁸⁷Sr/⁸⁶Sr)_inicial = 0,70430. Usando λ = 1,42 × 10⁻¹¹ ano⁻¹ (Steiger & Jäger, 1977):

(a) Calcule a idade de cristalização do corpo. (b) Interprete a razão inicial quanto à fonte do magma (mantélica pura ou com envolvimento crustal).

<details>
<summary>Ver resposta</summary>

**(a)** A inclinação da isócrona é e^(λt) − 1:

e^(λt) − 1 = 0,003300 ⟹ λt = ln(1,003300) ≈ 0,003295

t = 0,003295/1,42×10⁻¹¹ ≈ 2,320×10⁸ anos ≈ **232,0 milhões de anos**

**(b)** A razão inicial de 0,70430 está **dentro** da faixa tipicamente mantélica (≈0,702–0,706), o que sugere que o magma que originou este corpo derivou de uma fonte mantélica com pouca ou nenhuma contaminação crustal significativa — ao contrário do exemplo da aula (razão inicial 0,70759, já fora dessa faixa e indicando envolvimento de crosta). Lembrando que uma reta bem ajustada é condição necessária, mas não suficiente, para uma idade confiável: seria preciso descartar isócrona de mistura ou rehomogeneização metamórfica com evidência independente antes de aceitar essa interpretação como definitiva.
</details>

---

**Total: 100 pontos.**
