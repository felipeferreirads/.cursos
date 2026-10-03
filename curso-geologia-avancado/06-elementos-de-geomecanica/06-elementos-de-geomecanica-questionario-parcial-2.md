# Questionário parcial 2 — Módulo 06: Elementos de geomecânica

**Módulo:** [[06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]]
**Cobertura:** Aulas 04 a 06 — percolação, compressibilidade e adensamento, resistência ao cisalhamento e prospecção geotécnica.
**Objetivos avaliados:** geologia-avancado-m06-oa02 (parcial), geologia-avancado-m06-oa03, geologia-avancado-m06-oa04

---

### 1. Aplicação (cálculo)
Um pacote estratificado tem três camadas: 2 m com k = 1×10⁻⁴ m/s, 1 m com k = 1×10⁻⁷ m/s e 3 m com k = 1×10⁻⁴ m/s. Calcule a condutividade equivalente horizontal e a vertical, e comente a razão entre elas.

<details>
<summary>Ver resolução</summary>

**Horizontal — média aritmética ponderada:**
kh,eq = Σ(ki·Hi)/ΣHi = [(1×10⁻⁴×2) + (1×10⁻⁷×1) + (1×10⁻⁴×3)]/6
kh,eq = (2×10⁻⁴ + 1×10⁻⁷ + 3×10⁻⁴)/6 = 5,001×10⁻⁴/6 = **8,34×10⁻⁵ m/s**

**Vertical — média harmônica:**
kv,eq = ΣHi/Σ(Hi/ki) = 6/[(2/1×10⁻⁴) + (1/1×10⁻⁷) + (3/1×10⁻⁴)]
kv,eq = 6/(20.000 + 10.000.000 + 30.000) = 6/10.050.000 = **5,97×10⁻⁷ m/s**

**Razão:** kh,eq/kv,eq ≈ 8,34×10⁻⁵/5,97×10⁻⁷ ≈ **140**

**Comentário:** a camada de argila de apenas 1 m, com k mil vezes menor, praticamente não afeta o fluxo horizontal (a água simplesmente contorna por cima e por baixo, e a média aritmética é dominada pelas camadas permeáveis), mas **domina completamente** o fluxo vertical, porque toda a água é obrigada a atravessá-la — na média harmônica o termo 1/k da camada impermeável esmaga os demais. Daí a anisotropia induzida de cerca de duas ordens de grandeza num pacote em que nenhuma camada individual é anisotrópica (Aula 04).
</details>

---

### 2. Múltipla escolha
Numa escavação abaixo do nível d'água, o engenheiro constata vazão de infiltração baixa e conclui que não há risco hidráulico. Essa conclusão é:

a) Correta — vazão baixa indica gradientes baixos
b) Incorreta — o que governa a estabilidade do fundo é o gradiente de saída, não a vazão
c) Correta apenas se o solo for argiloso
d) Incorreta, porque vazão baixa sempre indica gradiente alto

<details>
<summary>Ver resposta</summary>

**Resposta: b**

Vazão e gradiente são grandezas distintas: a vazão depende de k e da geometria da rede de fluxo, enquanto a estabilidade do fundo depende do **gradiente de saída** comparado ao gradiente crítico. Um solo pouco permeável pode ter vazão desprezível e, ainda assim, gradiente de saída próximo de icr — exatamente o caso do exemplo trabalhado da aula, com 1,2 L/s de vazão e fator de segurança de 1,04. A alternativa "d" inverte o erro sem corrigi-lo: não há relação fixa entre vazão baixa e gradiente alto (Aula 04).
</details>

---

### 3. Verdadeiro ou Falso
"Levantamento de fundo (*heave*) e erosão regressiva (*piping*) são dois nomes para o mesmo fenômeno, ambos ocorrendo quando o gradiente atinge o valor crítico."

<details>
<summary>Ver resposta</summary>

**Falso.**

São mecanismos distintos. O **heave** é o levantamento em bloco de uma massa de solo quando σ' zera numa área ampla, e é de fato governado por icr. O **piping** é uma erosão **progressiva e localizada**, que inicia num ponto de saída concentrada e avança para montante escavando um tubo — e pode iniciar-se em gradientes locais bem **abaixo** do icr médio. Por isso a defesa contra piping não é apenas manter o gradiente médio baixo, mas instalar **filtros graduados** que deixem a água sair retendo as partículas; e por isso os fatores de segurança usuais contra piping (3 a 4) são bem maiores que os aplicados ao heave (Aula 04).
</details>

---

### 4. Aplicação (cálculo)
Uma camada de argila normalmente adensada tem 3 m de espessura, e0 = 1,10, Cc = 0,40 e cv = 1,5 m²/ano. A tensão efetiva vertical inicial é σ'v0 = 80 kPa e um aterro impõe Δσ = 100 kPa. A camada é drenada apenas pela face superior. Calcule o recalque primário e o tempo para atingir 50% dele.

<details>
<summary>Ver resolução</summary>

**Recalque.** Solo normalmente adensado → toda a trajetória na reta virgem, uma só parcela com Cc:

ρ = (Cc·H)/(1+e0) × log[(σ'v0+Δσ)/σ'v0]
ρ = (0,40 × 3)/(1 + 1,10) × log(180/80)
ρ = (1,20/2,10) × log(2,25) = 0,5714 × 0,35218 = **0,201 m ≈ 20,1 cm**

**Tempo.** Drenagem por **uma só** face → Hd = H = **3,0 m** (não 1,5 m).

Para U = 50%, Tv = 0,197:
t = Tv·Hd²/cv = 0,197 × (3,0)²/1,5 = 0,197 × 9/1,5 = **1,18 ano**

*Observação:* se a camada fosse drenada pelas duas faces, Hd seria 1,5 m e o tempo cairia para 0,197 × 2,25/1,5 = 0,30 ano — quatro vezes menor, com recalque final idêntico (Aula 05).
</details>

---

### 5. Múltipla escolha
Uma argila tem σ'v0 = 120 kPa e σ'p = 300 kPa. Uma obra imporá Δσ = 100 kPa. O recalque por adensamento primário deve ser calculado:

a) Inteiramente com Cc, pois toda carga adicional causa compressão virgem
b) Inteiramente com Cr, pois a tensão final permanece abaixo de σ'p
c) Em duas parcelas, uma com Cr e outra com Cc
d) Não há recalque, pois o solo é sobreadensado

<details>
<summary>Ver resposta</summary>

**Resposta: b**

A tensão final é σ'vf = 120 + 100 = 220 kPa, ainda **abaixo** da tensão de pré-adensamento σ'p = 300 kPa. O solo permanece em todo o percurso dentro do trecho de recompressão — refazendo um caminho que já percorreu na sua história —, e portanto usa-se **apenas Cr**. A alternativa "c" só valeria se σ'vf ultrapassasse σ'p (caso do exemplo trabalhado da aula). A alternativa "d" confunde recalque pequeno com recalque nulo: há recalque, apenas de magnitude bem menor, tipicamente uma fração do que ocorreria na reta virgem, já que Cr é usualmente 5 a 10 vezes menor que Cc (Aula 05).
</details>

---

### 6. Dissertativa curta
Um aterro é construído sobre argila mole e outro talude é obtido por corte numa argila rija. Explique, em até cinco linhas, por que o momento crítico de estabilidade é o oposto nos dois casos.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** no **aterro** (carregamento), o carregamento gera excesso de poropressão **positivo**; σ' é mínima e a resistência disponível é a menor de toda a vida da obra no **fim da construção**. Com o tempo o excesso dissipa, σ' cresce e a obra fica mais segura — o crítico é o **curto prazo**. No **corte** (descarregamento), o alívio gera poropressões **negativas** que conferem estabilidade temporária; à medida que elas se equilibram com o tempo, σ' cai e a resistência diminui — o crítico é o **longo prazo** (Aula 06).

**Comentário:** esse é o motivo pelo qual taludes de corte podem romper anos após executados, sem qualquer mudança aparente de carregamento, e por que a análise de um corte em argila deve usar parâmetros efetivos (c', φ') em condição drenada, enquanto a de um aterro sobre argila mole usa su em condição não drenada.
</details>

---

### 7. Aplicação (cálculo)
Dois ensaios triaxiais CD numa areia limpa (c' = 0) romperam em σ'3 = 100 kPa → σ'1 = 300 kPa. Determine φ' e, com ele, preveja σ'1 na ruptura para um corpo de prova ensaiado a σ'3 = 250 kPa.

<details>
<summary>Ver resolução</summary>

Com c' = 0, a relação em tensões principais reduz-se a σ'1 = σ'3·Nφ, com Nφ = tan²(45°+φ'/2):

Nφ = σ'1/σ'3 = 300/100 = **3,00**

tan(45° + φ'/2) = √3,00 = 1,7321 → 45° + φ'/2 = 60,0° → φ'/2 = 15,0° → **φ' = 30,0°**

**Previsão para σ'3 = 250 kPa:**
σ'1 = 250 × 3,00 = **750 kPa**

*Observação:* com c' = 0 a envoltória passa pela origem, e a razão σ'1/σ'3 na ruptura é **constante** para qualquer confinamento — propriedade que só vale no caso sem intercepto de coesão. Com c' > 0 a razão varia com σ'3, e é preciso resolver o sistema completo, como no exemplo trabalhado da aula (Aula 06).
</details>

---

### 8. Dissertativa curta
Uma campanha de investigação executou 20 furos de SPT numa área, todos com amostragem pelo próprio amostrador do SPT, e nenhum outro ensaio. O projeto exige prever o recalque por adensamento de uma camada de argila mole identificada nos furos. Avalie a suficiência da campanha.

<details>
<summary>Ver resposta comentada</summary>

**Resposta esperada:** a campanha é insuficiente. O SPT fornece perfil estratigráfico, posição do nível d'água e amostras **deformadas** — adequadas para identificar e classificar a argila, mas não para determinar parâmetros de compressibilidade. O cálculo de recalque exige e0, Cc, Cr, σ'p e cv, todos obtidos em **ensaio edométrico sobre amostra indeformada**, coletada com amostrador de parede fina (Shelby). Sem essa amostragem, nenhum dos parâmetros do cálculo está disponível, e correlações empíricas com NSPT em argila mole são pouco confiáveis. Recomenda-se complementar com amostragem indeformada e ensaios de adensamento, e considerar CPTu para delimitar continuamente a camada mole e ensaio de palheta para su (Aula 06, com os parâmetros da Aula 05).

**Comentário:** o caso ilustra o ponto de "O que não concluir" da aula — mais furos não é sinônimo de melhor investigação. Uma campanha eficaz distribui esforço entre estratigrafia, parâmetros e continuidade lateral; vinte furos sem uma única amostra indeformada não permitem calcular um recalque.
</details>

---

### Gabarito resumido

| Questão | Resposta |
|---|---|
| 1 | kh,eq ≈ 8,34×10⁻⁵ m/s; kv,eq ≈ 5,97×10⁻⁷ m/s; razão ≈ 140 |
| 2 | b |
| 3 | Falso |
| 4 | ρ ≈ 20,1 cm; t ≈ 1,18 ano |
| 5 | b |
| 6 | ver comentário |
| 7 | φ' = 30,0°; σ'1 = 750 kPa |
| 8 | ver comentário |
