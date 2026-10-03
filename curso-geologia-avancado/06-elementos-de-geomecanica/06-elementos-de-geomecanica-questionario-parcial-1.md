# Questionário parcial 1 — Módulo 06: Elementos de geomecânica

**Módulo:** [[06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]]
**Cobertura:** Aulas 01 a 03 — classificação de solos, índices físicos e compactação, tensões totais, efetivas e neutras.
**Objetivos avaliados:** geologia-avancado-m06-oa01, geologia-avancado-m06-oa02 (parcial)

---

### 1. Múltipla escolha
Um solo tem 60% da massa passando na peneira nº 200, limite de liquidez LL = 55% e índice de plasticidade IP = 28%. Sabendo que a linha A é dada por IP = 0,73(LL−20), a classificação SUCS desse solo é:

a) SC — areia argilosa
b) CL — argila de baixa compressibilidade
c) CH — argila de alta compressibilidade
d) MH — silte de alta compressibilidade

<details>
<summary>Ver resposta</summary>

**Resposta: c**

Três decisões em sequência. Primeiro, mais de 50% passa na peneira nº 200 → solo de **granulação fina** (elimina a alternativa "a", que é solo grosso). Segundo, LL = 55% > 50% → **alta compressibilidade**, sufixo H (elimina "b", que é sufixo L). Terceiro, a posição na carta de plasticidade: a linha A em LL = 55 vale IP = 0,73×(55−20) = 0,73×35 = 25,6. Como o IP do solo (28) é **maior** que 25,6, o ponto está **acima** da linha A → argila (C), não silte (M). Logo, **CH** (Aula 01).
</details>

---

### 2. Verdadeiro ou Falso
"O teor de umidade de um solo é a razão entre a massa de água e a massa total da amostra, e por isso nunca pode ultrapassar 100%."

<details>
<summary>Ver resposta</summary>

**Falso.** As duas partes da afirmação estão erradas, e a segunda é consequência da primeira.

O teor de umidade usa a massa de **sólidos secos** como base: w = Mw/Ms, não Mw/Mtotal. Justamente por isso ele **pode** ultrapassar 100% — basta que a amostra contenha mais massa de água que de sólidos, situação comum em argilas moles e turfas (Aula 02).
</details>

---

### 3. Aplicação (cálculo)
Um corpo de prova tem volume total 120 cm³, massa total 228 g e massa seca 195 g. A densidade relativa dos grãos é Gs = 2,70. Calcule o teor de umidade, o índice de vazios e o grau de saturação.

<details>
<summary>Ver resolução</summary>

Massa de água: Mw = 228 − 195 = 33 g.

**Teor de umidade:** w = 33/195 = 0,1692 → **16,9%**

Volume de sólidos: Vs = Ms/(Gs·ρw) = 195/(2,70×1) = 72,22 cm³.

Volume de vazios: Vv = 120 − 72,22 = 47,78 cm³.

**Índice de vazios:** e = Vv/Vs = 47,78/72,22 = **0,662**

Volume de água: Vw = 33/1 = 33 cm³.

**Grau de saturação:** Sr = Vw/Vv = 33/47,78 = 0,6907 → **69,1%**

*Conferência pela identidade Sr·e = w·Gs:* 0,6907 × 0,662 = 0,457; 0,1692 × 2,70 = 0,457. Confere (Aula 02).
</details>

---

### 4. Múltipla escolha
Um mesmo solo é ensaiado por Proctor normal e por Proctor modificado. Em relação ao ensaio normal, o resultado do modificado apresenta:

a) Umidade ótima maior e densidade seca máxima maior
b) Umidade ótima menor e densidade seca máxima maior
c) Umidade ótima menor e densidade seca máxima menor
d) A mesma curva, pois a curva de compactação é propriedade do solo

<details>
<summary>Ver resposta</summary>

**Resposta: b**

O Proctor modificado (ASTM D1557) aplica **maior energia de compactação** por unidade de volume que o normal (ASTM D698). Energia maior desloca a curva para cima e para a esquerda: atinge-se uma densidade seca máxima **maior**, com uma umidade ótima **menor**. A alternativa "d" registra o erro conceitual que o callout da aula adverte — a curva de compactação não é propriedade do solo isoladamente, mas do par solo + energia aplicada, e por isso as duas curvas não são comparáveis sem qualificar a energia (Aula 02).
</details>

---

### 5. Dissertativa curta
Explique, em até quatro linhas, por que uma chuva intensa pode deflagrar um escorregamento sem adicionar peso significativo ao talude.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** a infiltração eleva a poropressão u. Como σ' = σ − u, o aumento de u reduz a tensão efetiva sem que a tensão total mude de forma relevante. Como a resistência ao cisalhamento depende de σ' (é o contato grão a grão que gera atrito), a resistência disponível cai, podendo ficar abaixo da solicitação existente (Aula 03).

**Comentário:** o ponto central é que o gatilho é hidráulico, não gravitacional — a massa mobilizada é praticamente a mesma antes e depois da chuva. Esse mecanismo é a base da análise de estabilidade em condição não drenada e do papel da drenagem como medida de estabilização, retomados na Aula 06.
</details>

---

### 6. Aplicação (cálculo)
Um perfil tem 3 m de areia acima do nível d'água (γ = 18 kN/m³) e 5 m de argila saturada abaixo dele (γsat = 19 kN/m³). Calcule σv, u e σ'v a 8 m de profundidade. Use γw = 9,81 kN/m³.

<details>
<summary>Ver resolução</summary>

**Tensão total:** σv = (18 × 3) + (19 × 5) = 54 + 95 = **149 kPa**

**Poropressão** (coluna d'água de 8 − 3 = 5 m acima do ponto): u = 9,81 × 5 = **49,05 kPa**

**Tensão efetiva:** σ'v = 149 − 49,05 = **99,95 ≈ 100,0 kPa**

*Conferência pelo atalho do peso submerso* (válido: perfil hidrostático, sem fluxo):
γsub da argila = 19 − 9,81 = 9,19 kN/m³
σ'v = (18 × 3) + (9,19 × 5) = 54 + 45,95 = 99,95 kPa. Confere (Aula 03).
</details>

---

### 7. Verdadeiro ou Falso
"Para obter a tensão horizontal total num perfil geostático, basta multiplicar a tensão vertical total pelo coeficiente K0."

<details>
<summary>Ver resposta</summary>

**Falso.**

K0 relaciona tensões **efetivas**: K0 = σ'h/σ'v. O caminho correto tem dois passos: calcular σ'h = K0·σ'v e depois somar a poropressão de volta, σh = σ'h + u (a água pressiona igualmente em todas as direções). Aplicar K0 diretamente à tensão total subestima σh sempre que houver água no perfil — um dos erros de aplicação mais frequentes do tema (Aula 03).
</details>

---

### 8. Dissertativa curta
Um castelo de areia úmida se sustenta, mas desmorona tanto quando a areia seca quanto quando é submersa. Explique o mecanismo em termos de tensão efetiva, e diga por que o fenômeno é chamado de coesão "aparente".

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** na areia úmida não saturada, a água forma meniscos capilares sob tensão, e a poropressão é **negativa** (sucção). Aplicada a σ' = σ − u, uma poropressão negativa **aumenta** a tensão efetiva entre os grãos, elevando a resistência friccional disponível. Ao secar, a sucção desaparece; ao submergir, u passa a positivo — nos dois casos σ' cai e a estrutura colapsa. Chama-se coesão "aparente" porque nenhuma cimentação ou ligação verdadeira foi criada: trata-se de resistência friccional emprestada da sucção, que some junto com ela (Aula 03).

**Comentário:** o mesmo mecanismo explica a estabilidade temporária de taludes de corte e de paredes de escavação em solo úmido — estabilidade que se perde na primeira chuva forte, e que por isso nunca deve ser incorporada como resistência permanente de projeto.
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | c (CH) |
| 2 | Falso |
| 3 | w = 16,9%; e = 0,662; Sr = 69,1% |
| 4 | b |
| 5 | ver comentário |
| 6 | σv = 149 kPa; u = 49,05 kPa; σ'v ≈ 100,0 kPa |
| 7 | Falso |
| 8 | ver comentário |
