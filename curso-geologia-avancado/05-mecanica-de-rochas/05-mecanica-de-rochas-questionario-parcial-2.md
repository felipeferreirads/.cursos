# Questionário parcial 2 — Módulo 05: Mecânica de rochas

**Módulo:** [[05-mecanica-de-rochas-modulo|Módulo 05 — Mecânica de rochas]]
**Cobertura:** Aulas 05 a 07 — tensões in situ, classificações geomecânicas, estabilidade de taludes e escavações.
**Objetivos avaliados:** geologia-avancado-m05-oa02 (parcial), geologia-avancado-m05-oa03 (parcial), geologia-avancado-m05-oa04

---

### 1. Múltipla escolha
Um ensaio de fraturamento hidráulico registra uma pressão de fechamento (shut-in) de 12 MPa. Essa pressão é interpretada como uma estimativa direta de:

a) A tensão vertical no ponto
b) A tensão principal menor no plano perpendicular ao furo (σ3)
c) A resistência à compressão uniaxial da rocha
d) O coeficiente de Poisson da rocha

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A pressão de fechamento é interpretada como a tensão principal menor no plano perpendicular ao furo, porque a fratura induzida se fecha quando a pressão do fluido cai abaixo dessa tensão (Aula 05).
</details>

---

### 2. Verdadeiro ou Falso
"O overcoring fornece o tensor de tensão 3D completo a partir de uma única medição bem-sucedida, enquanto um único ensaio de fraturamento hidráulico fornece apenas as tensões no plano perpendicular ao furo."

<details>
<summary>Ver resposta</summary>

**Verdadeiro.**

Overcoring mede a deformação elástica de alívio em múltiplas direções e inverte para o tensor 3D completo; fraturamento hidráulico dá as duas tensões principais no plano perpendicular ao furo (tipicamente as horizontais, para um furo vertical), não o tensor 3D completo (Aula 05).
</details>

---

### 3. Aplicação (cálculo)
Num ponto a 800 m de profundidade, a densidade média da rocha sobrejacente é 2.700 kg/m³. Um ensaio de fraturamento hidráulico mede pressão de fechamento de 14 MPa. Calcule a tensão vertical (σv) e a razão K = σh/σv.

<details>
<summary>Ver resolução</summary>

σv = ρ·g·z = 2.700×9,81×800 ≈ 2,119×10⁷ Pa ≈ 21,2 MPa.

K = σh/σv ≈ 14/21,2 ≈ 0,66.

(Aula 05 — mesmo método do exemplo trabalhado da aula.)
</details>

---

### 4. Dissertativa curta
Explique, em até quatro linhas, por que a tensão in situ não pode ser calculada com precisão apenas a partir da profundidade e da densidade da rocha sobrejacente.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** a componente vertical (σv=ρgz) é previsível, mas a componente horizontal depende de fatores locais difíceis de prever a priori — tensões tectônicas residuais de eventos passados e efeitos de descompressão por erosão — que frequentemente produzem razões K muito diferentes da previsão elástica simples (K0=ν/(1−ν)), incluindo K>1 (Aula 05).

**Comentário:** é exatamente por isso que projetos de grande porte medem a tensão diretamente por overcoring, fraturamento hidráulico ou macacos planos, em vez de assumir um valor teórico.
</details>

---

### 5. Múltipla escolha
No sistema RMR de Bieniawski, qual dos cinco parâmetros principais tem o maior peso na nota final (até 30 pontos)?

a) Resistência à compressão uniaxial da rocha intacta
b) RQD
c) Condição das descontinuidades
d) Condição de água subterrânea

<details>
<summary>Ver resposta</summary>

**Resposta: c**

A condição das descontinuidades (persistência, abertura, rugosidade, preenchimento, intemperismo) tem peso de até 30 pontos, o maior entre os cinco parâmetros — e também o mais qualitativo, exigindo mais julgamento de campo experiente (Aula 06).
</details>

---

### 6. Aplicação (cálculo)
Um maciço tem RQD = 80, Jn = 6 (três famílias de descontinuidades), Jr = 3, Ja = 1, Jw = 1 e SRF = 2,5. Calcule o índice Q.

<details>
<summary>Ver resolução</summary>

Q = (RQD/Jn) × (Jr/Ja) × (Jw/SRF) = (80/6) × (3/1) × (1/2,5) = 13,33 × 3 × 0,4 = 16,0.

(Aula 06 — mesma fórmula do sistema Q de Barton, Lien e Lunde.)
</details>

---

### 7. Verdadeiro ou Falso
"O GSI é calculado somando pontuações numéricas de parâmetros medidos separadamente, da mesma forma que o RMR."

<details>
<summary>Ver resposta</summary>

**Falso.**

O GSI é deliberadamente qualitativo e visual — estimado por um ábaco que cruza estrutura do maciço e condição das superfícies de descontinuidade, sem somar pontuações numéricas de parâmetros separados. Essa escolha evita a dupla contagem de fatores já correlacionados entre si (Aula 06).
</details>

---

### 8. Dissertativa curta (aplicação)
Um talude tem uma descontinuidade planar que aflora na face, mergulhando a 40°. A análise cinemática por projeção estereográfica confirma que a orientação torna a ruptura planar geometricamente possível. Antes de calcular o fator de segurança, que outra informação sobre essa descontinuidade ainda é indispensável, e por quê?

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** é indispensável conhecer a resistência ao cisalhamento da descontinuidade (parâmetros c e φ, idealmente obtidos do critério de Barton-Bandis para a tensão normal real do bloco) e o peso do bloco potencialmente instável (geometria e densidade), porque o fator de segurança é a razão entre a força resistente (que depende de c, φ e da tensão normal) e a força motriz (que depende do peso e do ângulo de mergulho) — a viabilidade cinemática apenas confirma que o deslizamento é geometricamente possível, não diz nada sobre se ele de fato ocorrerá sob as forças reais envolvidas (Aula 07).
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | b |
| 2 | Verdadeiro |
| 3 | σv ≈ 21,2 MPa; K ≈ 0,66 |
| 4 | ver comentário |
| 5 | c |
| 6 | Q = 16,0 |
| 7 | Falso |
| 8 | ver comentário |
