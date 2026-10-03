# Questionário parcial 1 — Módulo 01: Hidrogeologia e recursos hídricos

**Módulo:** [[01-hidrogeologia-recursos-hidricos-modulo|Módulo 01 — Hidrogeologia e recursos hídricos]]
**Cobertura:** Aulas 01 a 04 — aquíferos e propriedades hidráulicas, lei de Darcy e zona não saturada, cartografia hidrogeológica, poços tubulares e de monitoramento.
**Objetivos avaliados:** geologia-avancado-m01-oa01, geologia-avancado-m01-oa02, geologia-avancado-m01-oa03 (parcial)

---

### 1. Múltipla escolha
Um material geológico tem porosidade total de 45 % mas condutividade hidráulica de 5 × 10⁻¹⁰ m/s. Esse material é mais provavelmente classificado como:

a) Aquífero livre de alta produtividade
b) Aquífero confinado
c) Aquitardo ou aquicludo, dependendo do grau de transmissão residual
d) Aquífugo, por não ter porosidade relevante

<details>
<summary>Ver resposta</summary>

**Resposta: c**

Porosidade alta com K extremamente baixa é a assinatura clássica de argila — porosidade total alta não implica condutividade hidráulica alta (Aula 01). Dependendo de a unidade ainda transmitir alguma água apreciável em escala regional/geológica (aquitardo) ou não transmitir quantidade significativa (aquicludo), a classificação exata varia, mas nunca seria "aquífero" nem "aquífugo" (que exigiria porosidade desprezível, não 45 %).
</details>

---

### 2. Verdadeiro ou Falso
"A superfície potenciométrica de um aquífero confinado é uma superfície física real, correspondente ao topo da água dentro da rocha."

<details>
<summary>Ver resposta</summary>

**Falso.**

A superfície potenciométrica de um confinado é um construto matemático — o lugar geométrico dos níveis de água que se estabeleceriam em poços que atravessam apenas aquele aquífero confinado. A água preenche todo o aquífero confinado (que está sempre saturado); a superfície potenciométrica pode estar bem acima do topo físico da rocha, inclusive acima do nível do solo (Aula 01).
</details>

---

### 3. Dissertativa curta
Explique, em até quatro linhas, por que a velocidade de Darcy (q) subestima sistematicamente a velocidade real de percolação da água (vx), e qual a fórmula que relaciona as duas.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** q é calculada como se a água atravessasse toda a área da seção transversal, inclusive a fração ocupada pelos grãos sólidos; a água real só se move através dos poros interconectados (porosidade efetiva, ne). A relação é vx = q / ne. Como ne < 1, vx é sempre maior que q (Aula 02).

**Comentário:** essa distinção é central para estimar tempo de trânsito de contaminantes (retomado no Módulo 03) — usar q em vez de vx nesse cálculo subestima a velocidade real por um fator de 1/ne, tipicamente de 2 a 10 vezes.
</details>

---

### 4. Aplicação (cálculo)
Dois piezômetros num aquífero livre, distantes 800 m, registram cargas hidráulicas de 150 m e 147,2 m. A condutividade hidráulica é K = 4 × 10⁻⁵ m/s e a porosidade efetiva é 0,25. Calcule a descarga específica (q) e a velocidade linear média (vx), em m/dia.

<details>
<summary>Ver resolução</summary>

Gradiente: dh/dl = (147,2 − 150)/800 = −0,0035.

q = −K·(dh/dl) = −(4×10⁻⁵)×(−0,0035) = 1,4×10⁻⁷ m/s = 1,4×10⁻⁷ × 86.400 ≈ 0,0121 m/dia.

vx = q/ne = 0,0121/0,25 ≈ 0,0484 m/dia (≈ 4,8 cm/dia).

(Aula 02 — mesma lógica do exemplo trabalhado da aula, com valores diferentes.)
</details>

---

### 5. Múltipla escolha
Num mapa potenciométrico, uma área onde a carga hidráulica diminui com a profundidade (medida em poços aninhados) é diagnóstico de:

a) Área de descarga, com fluxo ascendente
b) Área de recarga, com fluxo descendente
c) Rio desconectado do aquífero
d) Aquífero confinado sob pressão artesiana

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Carga decrescente com a profundidade indica que o fluxo vertical é descendente — água descendo de um nível mais raso e de carga maior para um nível mais profundo e de carga menor —, a assinatura de área de recarga (Aula 03). O padrão espelhado (carga crescente com a profundidade) indicaria descarga.
</details>

---

### 6. Verdadeiro ou Falso
"Um rio pode ser efluente em um trecho do seu curso e influente em outro trecho, ou mudar de regime ao longo do ano."

<details>
<summary>Ver resposta</summary>

**Verdadeiro.**

A relação rio-aquífero é local e depende da comparação entre a carga do aquífero adjacente e o nível do rio naquele ponto e momento específicos — pode variar espacialmente ao longo do curso e sazonalmente (efluente na estação chuvosa, influente na seca, por exemplo) (Aula 03).
</details>

---

### 7. Múltipla escolha
Em um aquífero arenoso mal selecionado (curva granulométrica larga), o dimensionamento correto do filtro de um poço tubular deveria:

a) Usar abertura igual ao D50 do aquífero diretamente, sem pré-filtro
b) Instalar pré-filtro artificial de granulometria selecionada e dimensionar a abertura do filtro para reter o pré-filtro
c) Usar o maior diâmetro de revestimento disponível, independentemente da granulometria
d) Escolher o método de perfuração por rotopercussão pneumática, que dispensa dimensionamento de filtro

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Aquíferos mal selecionados têm fração fina significativa que passaria por uma abertura dimensionada pelo D50; a solução de projeto é o pré-filtro artificial (D50 do pré-filtro entre 4 e 6 vezes o D50 do aquífero), com o filtro dimensionado para reter o pré-filtro, não a formação diretamente (Aula 04, incluindo o exemplo trabalhado dessa aula).
</details>

---

### 8. Dissertativa curta
Um poço de monitoramento tem filtro longo, atravessando dois aquíferos separados por uma camada de argila, sem selo isolando os dois intervalos. Explique o risco hidráulico introduzido por esse projeto.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** o poço cria uma via artificial de comunicação vertical entre os dois aquíferos que não existia na geologia original (a argila os isolava). Isso pode misturar águas de composição e idade diferentes na amostra coletada (invalidando a interpretação hidrogeoquímica) e, mais grave, pode transportar contaminante de um aquífero raso para um profundo através do próprio poço (Aula 04).

**Comentário:** esse é exatamente o tipo de falha que a norma técnica de poços de monitoramento (ABNT NBR 15495) busca evitar exigindo selo de bentonita/cimento isolando cada intervalo monitorado.
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | c |
| 2 | Falso |
| 3 | ver comentário |
| 4 | q ≈ 0,0121 m/dia; vx ≈ 0,0484 m/dia |
| 5 | b |
| 6 | Verdadeiro |
| 7 | b |
| 8 | ver comentário |
