# Aula 13: Cálculo de fórmulas estruturais de tectossilicatos e proporções An–Ab–Or

**ID:** geologia-avancado-m40-a13
**Módulo:** [[40-mineralogia-dos-tectossilicatos-modulo|Módulo 40 — Mineralogia dos tectossilicatos]]
**Duração estimada:** ~30 min
**Nível:** avançado (graduação plena / pós-graduação em geologia)
**Objetivo:** converter uma análise química em percentagens de óxidos numa fórmula estrutural distribuída por sítios cristalográficos, usar as somas dos sítios como teste de qualidade da própria análise, e extrair da fórmula as proporções de membros finais que posicionam o mineral no ternário dos feldspatos.

## Antes de começar, você precisa saber

- Da [[40-mineralogia-dos-tectossilicatos-aula-05-feldspatos-quimica-estrutura-e-ternario|aula 05]]: a fórmula geral dos feldspatos, **MT₄O₈**, com o sítio tetraédrico **T** (Si, Al, eventualmente Fe³⁺) e o sítio grande **M** (K, Na, Ca, Ba, Sr); e o ternário An–Ab–Or.
- Da [[40-mineralogia-dos-tectossilicatos-aula-11-feldspatoides|aula 11]]: a fórmula da leucita, KAlSi₂O₆.
- Que **cela unitária** e **fórmula mínima** são coisas distintas, e que **Z** é o número de fórmulas mínimas contidas na cela unitária.
- Aritmética de peso molecular: saber montar o PM de um óxido a partir dos pesos atômicos.

## Conteúdo

### O problema: análises vêm em óxidos, estruturas se descrevem em cátions

Análises químicas de minerais em que o **O é o ânion principal ou único** — o caso de todos os silicatos — são convencionalmente expressas em **percentagens em peso de óxidos**. Na prática, com frequência se medem percentagens em peso de *elementos*, depois convertidas para óxidos por critérios estequiométricos. Assim, KAlSi₃O₈ pode ser escrito como ½(K₂O) · ½(Al₂O₃) · 3(SiO₂).

Por que essa convenção sobrevive? Porque o O é **quantitativamente enorme** — perfaz entre **20 e 50 % em peso** da maioria dos silicatos — e porque as valências dos cátions comuns na crosta são em geral constantes. Isso permite avaliar, por estequiometria, **o quanto uma análise se aproxima dos 100 % esperados, sem precisar dosar o oxigênio analiticamente**. É um controle de qualidade embutido.

> [!warning] A exceção que sempre atrapalha
> O **Fe** aparece ora como FeO, ora como Fe₂O₃, e nos dois estados de oxidação em muitos minerais. Nos tectossilicatos o problema é pequeno — quando há Fe, ele entra essencialmente como **Fe³⁺** substituindo Al no sítio T. O procedimento desta aula vale para silicatos anidros em que o Fe aparece **num único estado de oxidação**. Silicatos hidratados ou com outros ânions exigem etapas adicionais (Apêndices de Deer, Howie & Zussman, 1992).

O preço da convenção é que **ler óxidos esconde as proporções entre átomos**. Dez por cento em peso de CaO contêm bem mais átomos de Ca do que 10 % de BaO contêm de Ba, simplesmente porque o Ba é muito mais pesado. Mas uma estrutura cristalina não conta gramas: ela mantém **proporções constantes entre sítios atômicos**. Para entender a distribuição dos elementos numa estrutura, é preciso pensar em **proporções relativas entre cátions e ânions**.

### A fórmula mínima e o número de oxigênios de referência

KAlSi₃O₈, K₂Al₂Si₆O₁₆ e K₄Al₄Si₁₂O₃₂ são **todas equivalentes**: as proporções entre K, Al, Si e O são idênticas. A composição de um mineral é expressa convencionalmente pela sua **fórmula mínima** — no caso, KAlSi₃O₈.

O cálculo, na prática, se faz contando os cátions presentes **para um número convencionado de oxigênios**. A escolha desse número segue **Z**, o número de fórmulas mínimas na cela unitária:

| Mineral | Fórmula mínima | Z | O de referência |
|---|---|:---:|:---:|
| Feldspatos | MT₄O₈ | **4** | **32** |
| Leucita | KAlSi₂O₆ | 16 | **6** (usa-se a fórmula mínima) |

Nos feldspatos, Z = 4 e a cela contém 32 O — daí a escolha padrão. O **resultado relativo é o mesmo** se tomarmos 8 ou 16 O, e esses valores também aparecem na literatura; a base 32 é convenção, não necessidade. Já na leucita Z = 16 é grande demais para ser conveniente, e os cálculos se fazem sobre a própria fórmula mínima, com **6 O**.

> [!tip] Regra de bolso
> Escolha o número de O que faça as somas dos sítios darem **inteiros pequenos e memoráveis**. Nos feldspatos, 32 O ⇒ ΣT = 16 e ΣM = 4. Se a base escolhida produz somas como 7,3 e 1,8, você escolheu mal — ou não está lidando com um feldspato.

### O procedimento em quatro passos

Sempre com **pelo menos três casas decimais** nos passos intermediários; só o resultado final é arredondado. Na prática, quatro casas evitam que óxidos-traço (Fe₂O₃, BaO) sejam esmagados pelo arredondamento — é a única liberdade que tomamos aqui em relação ao guia.

**Passo 1 — proporções moleculares (moles).** Divida a % em peso de cada óxido pelo respectivo **peso molecular**. Arranje os óxidos em colunas, em ordem **decrescente do número de O na molécula** (SiO₂, Al₂O₃, Fe₂O₃, BaO, CaO, Na₂O, K₂O). O resultado é uma coluna de números de moles.

**Passo 2 — proporções catiônicas.** Multiplique cada proporção molecular pelo número de cátions da molécula. SiO₂ tem **1** cátion de Si ⇒ a proporção catiônica de Si é igual à molecular. Al₂O₃ tem **2** ⇒ a de Al é o dobro. Idem Fe₂O₃, Na₂O, K₂O (todos ×2); BaO e CaO (×1).

**Passo 3 — proporções de oxigênio.** Análogo, agora pelo número de O da molécula: Na₂O ⇒ ×1; SiO₂ ⇒ ×2; Al₂O₃ e Fe₂O₃ ⇒ ×3; BaO, CaO, K₂O ⇒ ×1.

**Passo 4 — normalização.** Some a coluna de oxigênios: obtém-se **ΣO**. As proporções catiônicas do passo 2 referem-se a esse total. Como queremos os cátions para um número específico de O, define-se o **fator de conversão**:

$$F = \frac{\text{n}^{\underline{\text{o}}}\text{ de O desejado}}{\Sigma\mathrm{O}} \qquad\text{(feldspatos: } F = 32/\Sigma\mathrm{O})$$

e multiplica-se cada proporção catiônica por **F**. É uma regra de três, nada mais.

### Da coluna de cátions à fórmula estrutural

A fórmula estrutural é a **representação da distribuição dos cátions e ânions pelos sítios** que caracterizam a estrutura. Nos feldspatos há dois sítios: o **tetraédrico T** e o **maior, M**.

Para 32 O e fórmula geral MT₄O₈, devemos ter **16 sítios T** e **4 sítios M**. Logo:

- **ΣT = Si + Al (+ Fe³⁺, se presente) ≈ 16**
- **ΣM = Ca + Na + K (+ Ba, Sr…) ≈ 4**

A fórmula por extenso se escreve com as frações de cada sítio entre parênteses, M primeiro, T depois — por exemplo, para um oligoclásio:

$$(\mathrm{Ca}_{0,8}\mathrm{Na}_{3,0}\mathrm{K}_{0,2})(\mathrm{Al}_{4,8}\mathrm{Si}_{11,2})\mathrm{O}_{32}$$

que, dividida por 4, é a mesma coisa que (Ca₀,₂Na₀,₇₅K₀,₀₅)(Al₁,₂Si₂,₈)O₈.

### As somas de sítio são o seu controle de qualidade

Este é o ponto que separa quem calcula fórmula de quem **usa** fórmula. As somas ΣT e ΣM não são só o fecho do cálculo — são um **teste da análise química**.

Se os números de cátions se afastam de 16 e 4 **significativamente**, isto é, além dos erros analíticos normais, uma de três coisas aconteceu:

1. há **erro analítico** na determinação de um ou mais elementos;
2. **nem todos os elementos presentes foram analisados** (um Ba, um Sr, um Fe esquecido);
3. **a análise não corresponde a um feldspato**.

A terceira possibilidade é a mais instrutiva e a mais esquecida. O cálculo estequiométrico é o primeiro filtro contra uma identificação errada.

Para **feldspatoides** o procedimento é idêntico, mudando só a referência. Na leucita, com **6 O**, o número calculado de **K** (e de outros cátions que o substituam) deve se aproximar de **1**, e o de **(Si + Al)** deve ficar próximo de **3**.

### Proporções relativas de membros finais

Trabalhar com solução sólida exige saber **em que proporção** os membros finais se combinam. Nos feldspatos comuns, queremos An, Ab e Or.

O atalho é bonito: nas fórmulas mínimas dos membros finais há **exatamente 1 cátion de Ca em An, 1 de Na em Ab e 1 de K em Or**. Portanto as proporções moleculares An : Ab : Or são **exatamente** as proporções catiônicas de Ca : Na : K já calculadas. Não há nenhuma conversão adicional a fazer:

$$\mathrm{An} = \frac{100 \times \mathrm{Ca}}{\mathrm{Ca+Na+K}};\quad \mathrm{Ab} = \frac{100 \times \mathrm{Na}}{\mathrm{Ca+Na+K}};\quad \mathrm{Or} = \frac{100 \times \mathrm{K}}{\mathrm{Ca+Na+K}}$$

Para (Ca₀,₈Na₃,₀K₀,₂)(Al₄,₈Si₁₁,₂)O₃₂ temos An₂₀Ab₇₅Or₅ — pronto para lançar no ternário da aula 05. Fazendo An + Ab + Or = 1 em vez de 100, escreve-se em **frações molares**: An₀,₂₀Ab₀,₇₅Or₀,₀₅. Essa é a representação usada na maioria dos estudos físico-químicos e cristaloquímicos.

Quando outras moléculas são significativas — o caso do Ba, que define a molécula **celsiana (Cs)**, BaAl₂Si₂O₈ — basta estender o denominador: An + Ab + Or + Cs = 100.

> [!warning] O que a proporção An–Ab–Or **não** diz
> Ela é **composição**, e composição sozinha não identifica a espécie. Or₉₀ pode ser sanidina, ortoclásio ou microclínio máximo — a diferença é **estado estrutural**, não química ([[40-mineralogia-dos-tectossilicatos-aula-06-ordem-desordem-nos-feldspatos-potassicos|aula 06]]). O cálculo desta aula responde "quanto de cada molécula", nunca "qual polimorfo".

## Exemplo trabalhado

**Situação.** Análise de um feldspato alcalino (F1, análise simplificada de Deer *et al.*, 1992). Calcule a fórmula estrutural para 32 O, as proporções de membros finais e classifique quimicamente o mineral.

| Óxido | % peso | PM | Moles | Cátions | Oxigênios |
|---|---:|---:|---:|---|---:|
| SiO₂ | 66,97 | 60,08 | 1,1147 | Si 1,1147 | 2,2294 |
| Al₂O₃ | 18,75 | 101,96 | 0,1839 | Al 0,3678 | 0,5517 |
| Fe₂O₃ | 0,88 | 159,69 | 0,0055 | Fe³⁺ 0,0110 | 0,0165 |
| CaO | 0,36 | 56,08 | 0,0064 | Ca 0,0064 | 0,0064 |
| Na₂O | 7,88 | 61,98 | 0,1271 | Na 0,2542 | 0,1271 |
| K₂O | 5,39 | 94,20 | 0,0572 | K 0,1144 | 0,0572 |
| **Total** | **100,23** | | | | **ΣO = 2,9883** |

**Passo 4.** F = 32 / 2,9883 = **10,7084**.

| Cátion | × F | Sítio |
|---|---:|---|
| Si | **11,937** | T |
| Al | **3,939** | T |
| Fe³⁺ | **0,118** | T |
| | **ΣT = 15,994** | |
| Ca | **0,069** | M |
| Na | **2,722** | M |
| K | **1,225** | M |
| | **ΣM = 4,016** | |

**Leitura do controle de qualidade.** ΣT = 15,99 contra 16 ideais; ΣM = 4,02 contra 4. Desvios de 0,04 % e 0,4 % — dentro do erro analítico. **A análise é boa e o mineral é mesmo um feldspato.** Note que o Fe³⁺ (0,118 apfu) fecha o sítio T: sem ele, ΣT seria 15,88 e a análise pareceria pior do que é.

**Fórmula estrutural:**

$$(\mathrm{Ca}_{0,07}\mathrm{Na}_{2,72}\mathrm{K}_{1,23})(\mathrm{Al}_{3,94}\mathrm{Fe}^{3+}_{0,12}\mathrm{Si}_{11,94})\mathrm{O}_{32}$$

**Membros finais.** ΣM = 0,069 + 2,722 + 1,225 = 4,016.

- An = 100 × 0,069 / 4,016 = **1,7**
- Ab = 100 × 2,722 / 4,016 = **67,8**
- Or = 100 × 1,225 / 4,016 = **30,5**

**An₁,₇Ab₆₇,₈Or₃₀,₅.**

**Classificação química.** Ca desprezível, e Na e K ambos abundantes com Na dominante: é um **feldspato alcalino sódico** — composicionalmente, **anortoclásio**. No ternário da aula 05, o ponto cai na aresta Ab–Or, a cerca de um terço do caminho rumo ao Or.

> [!note] Guarde este número
> **An₁,₇Ab₆₇,₈Or₃₀,₅** volta na [[40-mineralogia-dos-tectossilicatos-aula-14-relacoes-de-fases-binarias|aula 14]]: é a composição que vamos cristalizar no diagrama Ab–Or. Lá você vai descobrir que, antes de plotá-la, ainda falta uma conversão — de **molar para peso**.

### A pegadinha da Tabela 1 do guia

O guia traz um segundo exemplo, um feldspato alcalino baritífero, e vale examiná-lo porque ele contém um **erro aritmético instrutivo**. Análise: SiO₂ 65,76; Al₂O₃ 20,23; Fe₂O₃ 0,18; **BaO 0,63**; CaO 1,29; Na₂O 8,44; K₂O 3,69 (total 100,22). Daí ΣO = 2,990 e F = 32/2,990 = 10,702.

A tabela publicada converte corretamente Si, Al, Fe, Ca, Na e K — mas registra **Ba = 0,004** na fórmula final, que é a proporção catiônica **antes** da multiplicação por F. O valor correto é 0,004 × 10,702 = **0,043**.

O erro se propaga: ΣM sai 4,007 (publicado) em vez de **4,035**, e a proporção de celsiana sai **Cs₀,₁** em vez de **Cs₁,₁** — uma ordem de grandeza. As proporções corretas são **An₆,₁Ab₇₂,₁Or₂₀,₇Cs₁,₁** (o guia publica An₆,₁Ab₇₂,₈Or₂₀,₉Cs₀,₁).

**A lição não é que o guia errou** — é que **você tem como saber**. Um Ba de 0,63 % em peso não pode dar 0,004 apfu num sítio com 4 posições: seria 0,1 % dos sítios M para um óxido que é 0,63 % da massa do mineral, num cátion pesadíssimo. A intuição de ordem de grandeza, somada ao teste ΣM ≈ 4, pega o erro antes da aritmética. Ver `TECTO-M40-A13-BARIO-006` no [[40-mineralogia-dos-tectossilicatos-auditoria|relatório de auditoria]].

## Erros comuns

- **Esquecer o multiplicador catiônico do passo 2.** Al₂O₃ dá **2** Al, Na₂O dá **2** Na, K₂O dá **2** K. Esquecer isso divide o sítio M pela metade e o ΣM denuncia na hora.
- **Arredondar cedo.** Três casas decimais é o **mínimo**; com óxidos-traço, use quatro. Arredondar Fe₂O₃ 0,0055 para 0,006 já move a terceira casa do ΣT.
- **Aplicar F a uns cátions e não a outros.** É exatamente o deslize da Tabela 1. Converta a **coluna inteira** de uma vez — numa planilha, uma única fórmula arrastada.
- **Usar 32 O para leucita.** Z = 16 torna a base 32 desconfortável; use 6 O e cheque K ≈ 1, (Si+Al) ≈ 3.
- **Confundir % molar de óxido com % de membro final.** SiO₂ 66,97 % em peso não é "67 % de alguma coisa" na fórmula. Só as proporções **catiônicas de Ca, Na e K** viram An, Ab e Or diretamente.
- **Aceitar ΣT = 16,4 como "quase 16".** Um desvio de 0,4 em 16 é enorme para uma análise moderna de microssonda. Investigue antes de publicar o número.
- **Ignorar o Fe³⁺ no sítio T.** Nos feldspatos ferríferos ele é essencial para fechar ΣT; jogá-lo em M arruína o cálculo e o ternário.

## O que não concluir

- **Que ΣT e ΣM perfeitos garantem uma boa análise.** Eles são condição necessária, não suficiente: erros compensatórios existem. E uma análise de mineral zonado pode fechar lindamente e mesmo assim não representar nenhum ponto real do cristal.
- **Que a base de 32 O tem significado físico especial.** É conveniência, atrelada a Z = 4. Oito ou dezesseis oxigênios dão as mesmas proporções relativas.
- **Que a fórmula estrutural prova a distribuição real dos cátions pelos sítios.** Ela **atribui** cátions a sítios por critério cristaloquímico (tamanho e carga). A ocupação real — em particular a distribuição Al/Si entre T₁O, T₁m, T₂O e T₂m, que é o cerne do estado estrutural — só se obtém por difração, não por aritmética ([[40-mineralogia-dos-tectossilicatos-aula-06-ordem-desordem-nos-feldspatos-potassicos|aula 06]]).
- **Que An₂₀ significa "20 % de anortita física" no cristal.** É a proporção do **componente** anortítico numa solução sólida homogênea, não uma mistura de dois minerais — a menos que haja exsolução, que é outra história ([[40-mineralogia-dos-tectossilicatos-aula-07-solvus-e-exsolucao-pertitas|aula 07]]).
- **Que uma análise que não fecha em feldspato está "perdida".** Ela pode estar identificando corretamente outra coisa — uma zeólita, um feldspatoide, uma mistura de fases sob o feixe.

## Recap relâmpago

- Análises vêm em **% em peso de óxidos** porque o O é 20–50 % da massa e as valências são constantes — o total próximo de 100 % é controle de qualidade sem dosar O. Preço: as proporções atômicas ficam escondidas.
- Fórmulas equivalentes (KAlSi₃O₈ = K₄Al₄Si₁₂O₃₂) diferem só pela base; a convenção é a **fórmula mínima**.
- Base de O escolhida por **Z**: feldspatos Z = 4 ⇒ **32 O**; leucita Z = 16 ⇒ usar a **fórmula mínima, 6 O**.
- **Quatro passos:** (1) % peso ÷ PM = **moles**; (2) × n° de cátions da molécula = **proporções catiônicas**; (3) × n° de O da molécula = **proporções de O**; (4) **F = 32/ΣO**, multiplicar toda a coluna catiônica por F. Mínimo três decimais; quatro com óxidos-traço.
- **Sítios:** ΣT = Si + Al (+Fe³⁺) ≈ **16**; ΣM = Ca + Na + K (+Ba, Sr) ≈ **4**. Escrita: (M…)(T…)O₃₂. Feldspatoides: leucita a 6 O ⇒ K ≈ 1, (Si+Al) ≈ 3.
- **As somas são teste da análise.** Desvio significativo ⇒ erro analítico, elemento não analisado, **ou não é feldspato**.
- **Membros finais sem conversão:** 1 Ca por An, 1 Na por Ab, 1 K por Or ⇒ An : Ab : Or = Ca : Na : K. Com Ba: An + Ab + Or + **Cs** = 100. Em frações molares, soma 1.
- **Exemplo F1:** ΣO = 2,9883, F = 10,708 ⇒ (Ca₀,₀₇Na₂,₇₂K₁,₂₃)(Al₃,₉₄Fe³⁺₀,₁₂Si₁₁,₉₄)O₃₂, ΣT 15,99 / ΣM 4,02 ⇒ **An₁,₇Ab₆₇,₈Or₃₀,₅**, **anortoclásio**.
- **Composição ≠ espécie.** An–Ab–Or não distingue sanidina de microclínio; isso é estado estrutural.

## Próxima aula

[[40-mineralogia-dos-tectossilicatos-aula-14-relacoes-de-fases-binarias|Aula 14 — Relações de fases binárias dos tectossilicatos: eutético, peritético, solução sólida completa e ponto de mínimo]]

## Anterior

[[40-mineralogia-dos-tectossilicatos-aula-12-zeolitas|Aula 12 — Zeólitas]]

## Fontes

- Convenção dos óxidos, papel quantitativo do O, ressalva sobre o Fe, equivalência de fórmulas e fórmula mínima, escolha do número de O a partir de Z (32 para feldspatos, 6 para leucita), os quatro passos do cálculo das proporções catiônicas, o fator F, a obtenção da fórmula estrutural por sítios T e M, o uso de ΣT ≈ 16 e ΣM ≈ 4 como avaliação da qualidade analítica, o procedimento para feldspatoides, e o cálculo das proporções relativas de membros finais An–Ab–Or–Cs: Vlach, S. R. F., *A Classe dos Tectossilicatos: Guia Geral da Teoria e Exercício*, IGc-USP, Série Didática USP, item VI e Tabela 1.
- Análise F1 do exemplo trabalhado: Tabela 2 do guia (item IX.2), "análises representativas para o grupo dos feldspatos (simplificadas de Deer *et al.*, 1992)". Fórmula estrutural, somas de sítio e proporções An–Ab–Or recalculadas nesta aula a partir dos dados brutos.
- Procedimento para silicatos hidratados e com outros ânions, e tabela de pesos moleculares: Deer, W. A., Howie, R. A. & Zussman, J. (1992), *An Introduction to the Rock-Forming Minerals*, 2ª ed., Apêndices (p. 682, Apêndice 2) — referência indicada pelo próprio guia.
- Correção aritmética da Tabela 1 do guia (conversão do Ba pelo fator F, com propagação para ΣM e para a proporção de celsiana): recálculo próprio, registrado como `TECTO-M40-A13-BARIO-006` no [[40-mineralogia-dos-tectossilicatos-auditoria|relatório de auditoria]].

<!--
nivel: avancado
palavras_corpo: ~2380

mapa_objetivo_secao:
  geologia-avancado-m40-oa06: "O problema: análises vêm em óxidos, estruturas se descrevem em cátions" + "A fórmula mínima e o número de oxigênios de referência" + "O procedimento em quatro passos" + "Da coluna de cátions à fórmula estrutural" + "As somas de sítio são o seu controle de qualidade" + "Proporções relativas de membros finais" + "Exemplo trabalhado"
  geologia-avancado-m40-oa03: "Proporções relativas de membros finais" + "Exemplo trabalhado" (classificação química no ternário An-Ab-Or)

alegacoes_auditaveis:
  - claim_id: TECTO-M40-A13-OXIDOS-001
    claim: "Analises quimicas de minerais em que o O e o anion principal ou unico sao expressas em percentagens em peso de oxidos; o O perfaz entre 20 e 50 % em peso na maioria dos silicatos e as valencias dos cations comuns na crosta sao em geral constantes (excecao do Fe, que aparece como FeO e Fe2O3), o que permite avaliar por estequiometria o quanto uma analise se aproxima de 100 % sem determinar o O analiticamente."
    risk: numero
    source: "Vlach, Guia dos Tectossilicatos, item VI"
  - claim_id: TECTO-M40-A13-ZETA-002
    claim: "O calculo de uma formula e feito considerando o numero de cations para um numero convencionado de O, escolhido a partir de Z, o numero de formulas minimas na cela unitaria. A cela unitaria dos feldspatos tem Z = 4, donde a escolha de 32 O, embora 8 ou 16 O deem o mesmo resultado relativo. Na leucita Z = 16 e os calculos se fazem sobre a formula minima, com 6 O."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item VI"
  - claim_id: TECTO-M40-A13-PROCEDIMENTO-003
    claim: "O procedimento tem quatro passos: (1) dividir a % em peso de cada oxido pelo peso molecular para obter proporcoes moleculares; (2) multiplicar pelo numero de cations da molecula para obter proporcoes cationicas; (3) multiplicar pelo numero de O da molecula para obter proporcoes de O; (4) somar as proporcoes de O e multiplicar as proporcoes cationicas pelo fator F = (n de O desejado)/(soma de O). Devem ser consideradas pelo menos tres casas decimais nos passos intermediarios."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item VI, Calculo das proporcoes cationicas"
  - claim_id: TECTO-M40-A13-SITIOS-004
    claim: "Na formula geral MT4O8 dos feldspatos, para 32 O ha 16 sitios T (ocupados por Si, Al e eventualmente Fe3+, soma proxima de 16) e 4 sitios M (Ca, Na, K, eventualmente Sr, Ba, soma proxima de 4). Numeros de cations significativamente diferentes de 16 e 4 implicam erro analitico, elemento nao analisado, ou que a analise nao corresponde a um feldspato. Para a leucita a 6 O, o numero de K deve se aproximar de 1 e o de (Si + Al) de 3."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item VI, Obtencao da formula estrutural"
  - claim_id: TECTO-M40-A13-MEMBROS-005
    claim: "Como cada molecula de An, Ab e Or contem exatamente 1 cation de Ca, Na e K respectivamente, as proporcoes moleculares An:Ab:Or sao identicas as proporcoes cationicas Ca:Na:K, e calculam-se por An = 100Ca/(Ca+Na+K), Ab = 100Na/(Ca+Na+K), Or = 100K/(Ca+Na+K). Com Ba significativo inclui-se a molecula celsiana: An + Ab + Or + Cs = 100. A formula (Ca0,8Na3,0K0,2)(Al4,8Si11,2)O32 corresponde a An20Ab75Or5, ou An0,20Ab0,75Or0,05 em fracoes molares."
    risk: fato
    source: "Vlach, Guia dos Tectossilicatos, item VI, Calculo das proporcoes relativas de membros finais"
  - claim_id: TECTO-M40-A13-BARIO-006
    claim: "A Tabela 1 do guia (feldspato alcalino baritifero: SiO2 65,76; Al2O3 20,23; Fe2O3 0,18; BaO 0,63; CaO 1,29; Na2O 8,44; K2O 3,69; total 100,22; soma de O = 2,990; F = 10,702) registra Ba = 0,004 na formula estrutural, que e a proporcao cationica antes da multiplicacao por F; o valor correto e 0,043. A correcao leva a soma M de 4,007 para 4,035 e as proporcoes de An6,1Ab72,8Or20,9Cs0,1 (publicadas) para An6,1Ab72,1Or20,7Cs1,1."
    risk: erro-na-fonte
    source: "Recalculo proprio a partir da Tabela 1 de Vlach, Guia dos Tectossilicatos, item VI; verificado por balanco de cargas (soma de cargas cationicas = 64 para 32 O)"
  - claim_id: TECTO-M40-A13-F1-007
    claim: "A analise F1 da Tabela 2 do guia (SiO2 66,97; Al2O3 18,75; Fe2O3 0,88; CaO 0,36; Na2O 7,88; K2O 5,39; total 100,23) da soma de O = 2,9883, F = 10,7084, e formula estrutural (Ca0,07Na2,72K1,23)(Al3,94Fe3+0,12Si11,94)O32, com soma T = 15,994 e soma M = 4,016, correspondendo a An1,7Ab67,8Or30,5 — composicionalmente um anortoclasio."
    risk: numero
    source: "Recalculo proprio a partir da Tabela 2 de Vlach, Guia dos Tectossilicatos, item IX.2 (analises simplificadas de Deer et al., 1992)"
  - claim_id: TECTO-M40-A13-LIMITE-008
    claim: "A formula estrutural atribui cations a sitios por criterio cristaloquimico de tamanho e carga, mas nao determina a distribuicao real de Al e Si entre os sitios T1O, T1m, T2O e T2m, que define o estado estrutural e so se obtem por difracao."
    risk: interpretacao
    source: "Decorrencia dos itens III.3 e IX.4 do guia (estado estrutural determinado por difratometria de raios X); consistente com Ribbe (1975)"
-->
