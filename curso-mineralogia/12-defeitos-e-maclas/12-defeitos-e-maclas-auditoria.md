# Auditoria científica: Módulo 12 — Defeitos cristalinos e maclas

**Auditado em:** 2026-10-06
**Material:** `curso-mineralogia/12-defeitos-e-maclas/` — as 6 aulas (`-aula-01` a `-aula-06`) e as figuras 1 a 3 (lidas pelo código SVG); cruzamento com o módulo 05 (simetria, Miller), o módulo 08 (aula 06: halita e fluorita), o módulo 09 (substituição acoplada) e o módulo 10 (aulas 01, 02 e 03: transformações, sanidina–ortoclásio–microclínio, politipismo)
**Modo:** audit-and-fix
**Profundidade:** full, com recálculo em Python de n/N = exp(−E/kT) a 500 K e 1000 K, do módulo de b da halita e do quartzo, do ângulo (110)∧(1̄10) da aragonita (com a cela do *Handbook of Mineralogy*) e das contas de anel cíclico
**Escopo:** as 41 alegações dos rodapés e as afirmações de risco do corpo: defeitos pontuais (Schottky, Frenkel, substitucional, centros de cor, não estequiometria); discordâncias, vetor de Burgers, sistemas de deslizamento, crescimento em espiral; defeitos planares; definição, elementos e tipos de macla; origem das maclas (quartzo α–β, leucita, microclínio, calcita, coríndon); leis dos feldspatos; leis de quartzo, espinélio, rutilo, estaurolita, calcita e gipsita; as três figuras. Questionário e baralho ainda não existiam.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)
**Segunda passagem:** 2026-10-06, sobre as alegações acrescentadas pela revisão didática; 2 achados 🟠 corrigidos (13 e 14), estado final mantido em Aprovado. Ver a seção no fim do relatório.
**Terceira passagem:** 2026-10-06, sobre os questionários (parcial 1, parcial 2 e final; 34 questões) e o baralho (111 Basic + 9 Cloze); 🟠 5 corrigidos (achados 15 a 19), um deles com ajuste mínimo nas aulas 02 e 03; estado final mantido em Aprovado. Ver "Auditoria de questionários e baralho" no fim.

## Resumo

🔴 1 erro · 🟠 10 imprecisões · 🟡 0 desatualizados · 🔵 0 sem fonte · ⚪ 1 controverso
Verificadas e corretas: 32 alegações dos rodapés (41 no total; ver o manifesto `.json`), todas as contas e as três figuras.

Os pontos que o autor marcou como frágeis passaram, com duas exceções: a estaurolita (os índices {032}/{232} são os da orientação clássica; o *Handbook of Mineralogy* usa {031}/{231}, e a cruz mais comum é a de 60°) e a pirrotita (Fe₇S₈ não é o extremo da faixa). Os outros achados vieram do corpo: um exemplo de pirita fisicamente impossível, a origem dos contornos de antifase na pigeonita, a omissão do Dauphiné de crescimento e uma certeza indevida sobre a partição do coríndon.

**Contas conferidas (Python, 2026-10-06):**

| O quê | Resultado | Onde |
|---|---|---|
| kT e E/kT para E = 1,0 eV (k = 8,617333 × 10⁻⁵ eV/K) a 1000 K e 500 K | 0,08617 e 0,04309 eV; 11,605 e 23,209 | a01 |
| n/N = exp(−E/kT) a 1000 K; a 500 K; razão | 9,125 × 10⁻⁶; 8,326 × 10⁻¹¹; 1,096 × 10⁵ (texto: 9 × 10⁻⁶, 8 × 10⁻¹¹, 1,1 × 10⁵ ✔) | a01 |
| \|b\| = a/√2 da halita (a = 5,640 Å) | 3,988 Å (texto: 3,99 ✔) | a02 |
| \|b\| = a do quartzo | 4,913 Å; HoM a = 4,9135 Å ✔ | a02 |
| (110)∧(1̄10) da aragonita = 2·arctan(b/a), com a = 4,9611 e b = 7,9672 (HoM) | 116,18° / 63,82° (texto: 116,2° / 63,8° ✔); desvio de 3,83° por passo em relação a 60° | a03 |
| Anel idealizado: 360/120, 360/90, 360/60, 360/45 | 3, 4, 6, 8 indivíduos ✔ | a03, a06 |
| Variantes do quartzo: ordem(622)/ordem(32) | 12/6 = 2 ✔ | a04 |
| Correspondência de índices: calcita (c estrutural = 4 × c morfológico); estaurolita (l clássico = 2 × l moderno) | {01̄18} ↔ {01̄12}; {032} ↔ {031}, {232} ↔ {231} | a06 |

> [!note] Limite da verificação nesta sessão
> O texto dos verbetes do *Handbook of Mineralogy* (estaurolita, pirrotita, wüstita, calcita, quartzo, aragonita, gipsita, rutilo, cassiterita, pirita, coríndon, leucita, ortoclásio) foi lido diretamente dos PDFs. O Mindat e o RRUFF (Min. Mag.) não abriram por conexão; o que dependia deles foi conferido por busca. **Não conferido na fonte primária:** o eixo c da orientação clássica da estaurolita (a relação "c clássico = 2 × c moderno" foi derivada da correspondência {032}↔{031} e {232}↔{231}, e não lida numa tabela de razões axiais; por isso a aula fala em "corresponde a" e o manifesto marca confiança "provável" nesse ponto); o espinélio no HoM (o PDF não abriu; a lei {111} e os espelhos de m3̄m são de manual e do módulo 05).

## Achados

### 🟠 1. Os "cubos vazios" da fluorita estavam rotulados errado

**claim_id:** `CRI-DEFPT-FLUOR-001`  ·  **Tipo:** erro factual (menor)  ·  **Onde:** aula 01 · Antes de começar
**Está escrito:** "na fluorita (CaF₂) os F⁻ ocupam os centros de cubos menores, enquanto os centros de metade dos cubos de Ca²⁺ ficam vazios"
**Problema:** os cubos dos quais metade fica vazia são os cubos de **8 F⁻** (os F⁻ formam uma rede cúbica simples; metade desses cubos tem Ca²⁺ no centro). Os oito cubos menores da cela de Ca²⁺ estão todos ocupados por F⁻. O rótulo errado contamina a explicação do Frenkel de ânion, que manda o F⁻ "para o centro de um dos cubos vazios".
**Correção aplicada:** "os F⁻ ocupam os centros dos oito cubos menores da cela de Ca²⁺ (todos os vazios tetraédricos); vistos os F⁻ como uma rede de cubos, metade desses cubos de 8 F⁻ tem um Ca²⁺ no centro e a outra metade tem o centro vazio"
**Fonte:** módulo 08, aula 06 ("Ca em cF, F em todos os tetraédricos"); Klein & Dutrow  ·  **Confiança:** confirmado

### 🟠 2. Expoente da concentração de defeitos que nascem em par

**claim_id:** `CRI-DEFPT-EQUIL-001`  ·  **Tipo:** omissão que gera erro  ·  **Onde:** aula 01 · O cristal real tem defeitos
**Está escrito:** "n / N ≈ exp(−E / kT), em que E é a energia para criar um defeito"
**Problema:** para defeitos que só se formam em par (Schottky num cristal iônico, com E = energia do par), a fração de cada vacância é exp(−E/2kT). Sem a ressalva, a fórmula aplicada ao Schottky da própria aula dá um expoente com o dobro do valor.
**Correção aplicada:** acrescentado "(Quando o defeito só pode nascer em par, como o par de vacâncias de Schottky, e E é a energia do par, o expoente fica −E/2kT.)". A conta do exemplo (E hipotético de um defeito isolado) não muda.
**Fonte:** Univ. Kiel, *Defects in Crystals*, cap. 2 (equilíbrio de Schottky, n = N·exp(−E/2kT)), por busca  ·  **Confiança:** confirmado

### 🟠 3. Centro F e as cores da halita e da fluorita

**claim_id:** `CRI-DEFPT-COR-001`  ·  **Tipo:** omissão que gera erro  ·  **Onde:** aula 01 · Defeitos e cor
**Está escrito:** "Cor por centros assim é a explicação aceita para a cor de certas halitas e fluoritas expostas à radiação"
**Problema:** o centro F dá o amarelo-âmbar da halita irradiada. As cores mais conhecidas, o azul da halita e o roxo de muitas fluoritas, são atribuídas a um estágio seguinte: partículas coloidais de Na ou de Ca metálico formadas a partir dos elétrons presos. O aluno sairia achando que a halita azul é "centro F".
**Correção aplicada:** "os centros F dão o amarelo-âmbar da halita irradiada, e o azul da halita e o roxo de muitas fluoritas vêm de um estágio seguinte, em que os elétrons presos reduzem o metal e formam partículas coloidais de Na ou de Ca"
**Fonte:** HAL Sorbonne, "Sodium nanoparticles in alkali halide minerals: why is villiaumite red and halite blue?"; Gaft e colaboradores, "Red photoluminescence and purple color of naturally irradiated fluorite" (Ca coloidal), por busca  ·  **Confiança:** confirmado
**Conferido sem mudança:** quartzo-fumê = centro [AlO₄]⁰ (buraco no O vizinho de Al³⁺ substitucional, com H⁺/Li⁺/Na⁺ compensando), confirmado (*Am. Mineral.* 70, 1180; Nassau).

### ⚪ 4. Sítio do ferro na ametista

**claim_id:** `CRI-DEFPT-COR-002`  ·  **Tipo:** certeza indevida  ·  **Onde:** aula 01 · Defeitos e cor; e o recap
**Está escrito:** "a ametista, a Fe³⁺ substituindo Si⁴⁺ e ionizado pela radiação"
**Problema:** o centro de cor da ametista é atribuído a Fe⁴⁺ formado por radiação, mas há divergência sobre o sítio: Cox (1976, 1977) defende Fe substitucional; Cohen (1985) e experimentos de eletrodifusão apontam Fe intersticial. O texto escolhia um lado.
**Correção aplicada:** "a ametista, a ferro (Fe³⁺) que a radiação oxida a Fe⁴⁺; se esse ferro ocupa o lugar do Si⁴⁺ ou um interstício ainda é debatido na literatura"; no recap, "Al substituindo Si e Fe no quartzo, com radiação".
**Fonte:** Czaja (Mössbauer de prasiolita e ametista, revisão do debate Cox × Cohen); Rossman (1994, *Rev. Mineral.* 29), por busca  ·  **Confiança:** em disputa

### 🟠 5. Fe₇S₈ não é o extremo da pirrotita

**claim_id:** `CRI-DEFPT-NAOES-001`  ·  **Tipo:** impreciso  ·  **Onde:** aula 01 · Defeitos e condutividade
**Está escrito:** "a pirrotita é Fe₁₋ₓS, que chega a Fe₇S₈ no extremo pobre em ferro"
**Problema:** o *Handbook of Mineralogy* dá Fe₁₋ₓS com x = 0 a 0,17; Fe₇S₈ (x = 0,125) é a composição da variedade monoclínica comum (4C), não o extremo da faixa.
**Correção aplicada:** "a pirrotita é Fe₁₋ₓS, com x de 0 até cerca de 0,17 (a variedade monoclínica comum tem composição perto de Fe₇S₈, x = 0,125)"
**Fonte:** *Handbook of Mineralogy*, pyrrhotite (Mineral Data Publishing, 2001–2005), lido em 2026-10-06  ·  **Confiança:** confirmado
**Conferido sem mudança:** wüstita Fe₁₋ₓO com vacâncias de Fe²⁺ compensadas por Fe³⁺ (x ≈ 0,05–0,15); HoM wüstita Fm3̄m.

### 🟠 6. "b é sempre um vetor da rede"

**claim_id:** `CRI-DISC-BURGERS-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** aula 02 · Cunha e hélice
**Está escrito:** "Ele é sempre um vetor da rede (uma translação do cristal)"
**Problema:** vale só para a discordância perfeita. Discordâncias parciais (Shockley, Frank) têm b menor que uma translação e margeiam uma falha de empilhamento; a própria aula fala de "parciais" em "O que não concluir".
**Correção aplicada:** "Numa discordância **perfeita**, ele é um vetor da rede (...). Existem também discordâncias **parciais**, cujo b é só uma fração de uma translação; elas sempre margeiam uma falha de empilhamento (veja adiante)."
**Fonte:** Univ. Kiel, *Defects in Crystals*, 5.4 ("partial dislocations and stacking faults"); notas de Princeton MAE 324 (por busca)  ·  **Confiança:** confirmado

### 🟠 7. Contornos de antifase na pigeonita não vêm de ordem Mg/Fe

**claim_id:** `CRI-PLAN-ANTIF-001`  ·  **Tipo:** confusão de escopo  ·  **Onde:** aula 02 · Os defeitos planares; Exemplo trabalhado (d)(iii); recap
**Está escrito:** "São descritos (...) em minerais como a pigeonita e os plagioclásios cálcicos, que se ordenam na história térmica"; "(iii) domínios vizinhos (...) em pigeonita, mas com ordem Mg/Fe deslocada"
**Problema:** na anortita, os contornos de antifase vêm da ordenação Al–Si (e da transição I1̄ → P1̄). Na pigeonita, vêm da transição **deslocativa** C2/c → P2₁/c no resfriamento, em que a fase fria perde a translação C; não de uma ordem Mg/Fe.
**Correção aplicada:** a definição passou a incluir "ou que passam por uma transição em que a fase fria perde uma das translações da fase quente"; os exemplos ficaram "nos plagioclásios cálcicos (anortita), pela ordenação de Al e Si, e na pigeonita, pela transição deslocativa C2/c → P2₁/c no resfriamento"; o exercício (iii) passou a "com a estrutura de baixa temperatura (P2₁/c) deslocada de um para o outro"; o método geral e o recap, a "arranjo deslocado".
**Fonte:** estudos de pigeonita em alta temperatura (APB tipo L e H na transição C2/c → P2₁/c; *Am. Mineral.*/*Phys. Chem. Minerals*); Carpenter (domínios b, c em anortita), por busca  ·  **Confiança:** confirmado

### 🔴 8. Pirita em "dois cubos entrelaçados"

**claim_id:** `MIN-MACLA-PIRITA-001`  ·  **Tipo:** erro factual  ·  **Onde:** aula 03 · Exemplo trabalhado (a)(i)
**Está escrito:** "(i) cristais de pirita cúbica que se atravessam como dois cubos entrelaçados"
**Problema:** a macla de penetração da pirita tem eixo [001] e plano {011} (rotação de 90° em torno de [001]). Dois **cubos** relacionados por essa operação coincidem em forma; o que se vê como penetração é a "cruz de ferro" de dois **piritoedros** (dodecaedros pentagonais). "Cubos entrelaçados" é a imagem da fluorita (macla em [111]), já citada na própria aula.
**Correção aplicada:** "(i) dois piritoedros (dodecaedros pentagonais) de pirita que se atravessam, formando a 'cruz de ferro'". A resposta (penetração) não muda.
**Fonte:** *Handbook of Mineralogy*, pyrite ("Twin axis [001] and twin plane {011}, penetration and contact twins"); EJM 35, 333 (2023), "iron cross" de dois piritoedros  ·  **Confiança:** confirmado

### 🟠 9. Dauphiné também é macla de crescimento

**claim_id:** `MIN-MACLA-DAUPHINE-001` (o rascunho usava `MIN-MACLA-QTZ-DAUPH-001`, fora do padrão de 4 segmentos do schema; renomeado antes do primeiro registro)  ·  **Tipo:** omissão que gera erro  ·  **Onde:** aula 04 · Macla de transformação (quartzo) e Exemplo (c); aula 06 · Quartzo e tabela-resumo
**Está escrito:** "Mas a macla de Dauphiné também pode se formar por tensão mecânica"; "(c) O Dauphiné pode ser de transformação (β → α a 573 °C) ou de tensão"; tabela: "transformação ou mecânica"
**Problema:** o Dauphiné é comum como macla **de crescimento** em quartzo que já cristalizou como α (cristais hidrotermais), como registra Frondel (1945). Omitir isso inclina o aluno a ler Dauphiné como sinal de passagem pelo campo β. A própria aula 04, em "Erros comuns", já dizia "compatível com ambas e com tensão", o que deixava o texto inconsistente.
**Correção aplicada:** aula 04: "também se forma **durante o crescimento** de quartzo que já nasce α (é comum em cristais hidrotermais) e por **tensão mecânica**"; exemplo (c): "de transformação (...), de crescimento (quartzo que já nasceu α) ou de tensão"; aula 06: "pode ser de crescimento, de transformação (β → α) ou mecânica" e tabela "crescimento, transformação ou mecânica".
**Fonte:** Frondel (1945), *Am. Mineral.* 30, 447; *Am. Mineral.* 31, 456  ·  **Confiança:** confirmado
**Conferido sem mudança:** 573 °C a 1 atm (HoM: quartzo "stable below 573 °C"); β = 622 (12 operações), α = 32 (P3₁21/P3₂21, 6 operações); Dauphiné = rotação de 180° em torno de c.

### 🟠 10. Ortoclásio não é "de alta temperatura"

**claim_id:** `MIN-MACLA-MICRO-001`  ·  **Tipo:** inconsistência com o módulo 10  ·  **Onde:** aula 04 · Microclínio
**Está escrito:** "O feldspato potássico monoclínico de alta temperatura (sanidina, ortoclásio) vira triclínico"
**Problema:** o ortoclásio é parcialmente ordenado e característico de granitos e rochas metamórficas (HoM: "(Al,Si) commonly only partially ordered"); o módulo 10, aula 02, já o distingue da sanidina, essa sim desordenada e de alta temperatura.
**Correção aplicada:** "O feldspato potássico monoclínico (a sanidina, desordenada e de alta temperatura, ou o ortoclásio, parcialmente ordenado) vira triclínico"
**Fonte:** *Handbook of Mineralogy*, orthoclase; módulo 10, aula 02 (auditado)  ·  **Confiança:** confirmado

### 🟠 11. Partição do coríndon e definição de partição

**claim_id:** `MIN-MACLA-DEFORM-001`  ·  **Tipo:** certeza indevida + confusão de escopo  ·  **Onde:** aula 04 · Macla de deformação; recap
**Está escrito:** "a partição romboédrica do coríndon, que se dá por maclagem mecânica e é responsável pelas superfícies de partição em rubi e safira. Uma partição é uma fratura ao longo de um plano de macla, e não uma clivagem"
**Problema:** (i) a maclagem mecânica romboédrica e basal do coríndon é documentada em experimentos (Heuer, 1966), mas o *Handbook of Mineralogy* diz que a macla lamelar ∥ {10̄11} "pode ser um fenômeno de exsolução" e liga as partições em {0001} e {10̄11} a böhmita exsolvida; atribuir a partição natural só à maclagem mecânica é certeza que a fonte não sustenta. (ii) Partição não ocorre só em plano de macla: também em planos de lamelas de exsolução ou de fraqueza por tensão.
**Correção aplicada:** "as lamelas de macla romboédricas {10̄11} do coríndon (a maclagem mecânica do coríndon é documentada em experimentos, mas parte das lamelas naturais pode ter outra origem). Ao longo dessas lamelas e do plano basal, rubis e safiras mostram **partição**, que o *Handbook of Mineralogy* associa a böhmita exsolvida nesses planos. Uma partição é uma ruptura ao longo de um plano de fraqueza que nem todo exemplar tem (um plano de macla, ou de lamelas de exsolução), e não uma clivagem"; recap: "lamelas romboédricas do coríndon".
**Fonte:** *Handbook of Mineralogy*, corundum; Heuer (1966), *Phil. Mag.*, "Deformation twinning in corundum"; Mindat, glossário "parting"  ·  **Confiança:** confirmado
**Conferido sem mudança:** calcita, maclas *e* com tensão cisalhante crítica de ~10 MPa, quase independente de temperatura, usadas em paleopiezometria (Turner et al., 1954, valor de referência retomado nas revisões recentes de maclas de calcita).

### 🟠 12. Planos de macla da estaurolita: duas convenções, e a cruz mais comum é a de 60°

**claim_id:** `MIN-STAUR-MACLA-001`  ·  **Tipo:** omissão que gera erro  ·  **Onde:** aula 06 · Estaurolita; tabela-resumo; Exemplo (c); Erros comuns; recap
**Está escrito:** "Cruz de 90° (...): lei com plano {032}. Cruz de 60° (...): lei com plano {232}." e "Achar que a cruz de estaurolita é sempre de 90°. Há a de 60°."
**Problema:** {032} e {232} são os índices da orientação morfológica clássica. Na cela estrutural C2/m usada pelo *Handbook of Mineralogy* (a = 7,87; b = 16,6; c = 5,65 Å) os mesmos planos são {031} e {231}. O aluno que conferir a fonte normativa acharia outros índices sem aviso. Além disso, o HoM e a literatura de maclas dão a cruz de 60° como a **mais comum** e a de 90° como a menos frequente; o texto sugeria o contrário.
**Correção aplicada:** planos dados nas duas convenções ("{031} na cela estrutural moderna (...), escrito {032} na orientação morfológica dos manuais clássicos"; idem {231}/{232}), com a frequência de cada cruz e a explicação de que os índices clássicos têm o l dobrado; tabela, exemplo (c), "Erros comuns" ("que é até a mais frequente") e recap ajustados.
**Fonte:** *Handbook of Mineralogy*, staurolite (2001), lido em 2026-10-06; *Am. Mineral.* 22, 990 ({032}, cruz de 90° em menos de 5% dos casos); HAL Univ. Lorraine (cruz de 60° mais frequente)  ·  **Confiança:** confirmado (índices e frequência); provável (a leitura "c clássico = 2 × c moderno", derivada da correspondência de índices)

## Verificado e correto (seleção)

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `CRI-DEFPT-CALC-001` | n/N 9,1 × 10⁻⁶ (1000 K) e 8,3 × 10⁻¹¹ (500 K); razão 1,1 × 10⁵ | Python | confirmado |
| `CRI-DEFPT-FRENK-001` | Frenkel de cátion em AgCl e AgBr; Frenkel de ânion (F⁻ intersticial) no CaF₂ | literatura de química do estado sólido (busca) | confirmado |
| `CRI-DISC-SISTEMA-001` | halita {110}⟨1̄10⟩, b = a/2⟨110⟩ = 3,99 Å; quartzo basal (0001)⟨a⟩, b = 4,913 Å | busca; HoM; Python | confirmado |
| `CRI-DISC-FRANK-001` | Frank (1949), *Discuss. Faraday Soc.* 5, 48; BCF (1951), *Phil. Trans. A* 243, 299; espirais em SiC (Verma, 1951) | busca | confirmado |
| `MIN-MACLA-ARAG-001` | aragonita a = 4,96, b = 7,97 Å; 116,2°/63,8°; trilling pseudo-hexagonal em {110} | HoM; Python | confirmado |
| `MIN-MACLA-LEUC-001` | leucita tetragonal (I4₁/a) à temperatura ambiente, maclas repetidas de transformação | HoM | confirmado |
| `MIN-FELD-PERIC-001` | periclínio: eixo [010], plano de composição = seção rômbica irracional (h0l) | *Min. Mag.* 31 (busca) | confirmado |
| `MIN-FELD-BAVEN-001`, `MIN-FELD-MANEB-001` | Baveno (021) e Manebach (001), simples, sobretudo no K-feldspato; raras ou pouco frequentes no plagioclásio | HoM ortoclásio; NGT 42 | confirmado |
| `MIN-QTZ-MACLA-001` | Brasil {11̄20}, mãos opostas ("macla óptica"); Japão {11̄22}, eixos c a 84°33′ | HoM; *Int. Tables* D, 3.3 | confirmado |
| `MIN-RUT-MACLA-001` | rutilo em {011} (ou {031}), com 2, 6 ou 8 indivíduos; cassiterita {011} geniculada | HoM | confirmado |
| `MIN-CALC-MACLA-001` | plano *e* = {01̄18} (estrutural, c = 17,061 Å) = {01̄12} (morfológico); macla basal (0001) | HoM; literatura de deformação | confirmado |
| `MIN-GIPS-MACLA-001` | gipsita: contato em {100} (rabo de andorinha); "borboleta"/Montmartre em {101} | HoM; Rubbo et al. | confirmado |

## Figuras

- **Figura 1 (defeitos pontuais):** checada a paridade da rede xadrez. Em (a), as duas vacâncias são vizinhas e uma é de cátion (raio pequeno) e a outra de ânion (raio grande): par de Schottky correto. Em (b), a vacância está num sítio de cátion e o íon extra ocupa o centro de um quadrado de quatro íons (interstício): Frenkel de cátion correto, e a rede "tipo NaCl" é justamente a do AgCl/AgBr. Em (c), a impureza está num sítio de cátion. Sem erro conceitual. *Observação de desenho, sem correção:* o cátion intersticial foi desenhado com raio menor que o regular (6 contra 11); como o Frenkel envolve o mesmo íon, convém igualar os raios numa próxima regeração.
- **Figura 2 (discordância e Burgers):** metade superior com 7 colunas e inferior com 6 no mesmo comprimento (semiplano extra em cima, terminando sobre o plano de deslizamento); símbolo ⊥ com a haste voltada para o semiplano; circuito de 4 + 4 + 4 + 4 passos que fecha no cristal perfeito e não fecha em torno da discordância; falha de fechamento de um espaçamento, paralela ao plano de deslizamento e perpendicular à linha, desenhada do fim para o início do circuito, como diz a legenda. Correto.
- **Figura 3 (tipos de macla):** em (a) e (c), as setas dos indivíduos vizinhos são imagens especulares em relação ao plano de composição; (a) tem ângulos reentrantes em cima e embaixo; (d) tem três setores com setas a 30°, 150° e 270° (giros de 120°, 3 × 120° = 360°). Correto.

## Consistência interna e com o resto do curso

- **Módulo 08, aula 06:** halita a = 5,640 Å e fluorita "Ca em cF, F em todos os tetraédricos": a aula 01 agora descreve a fluorita do mesmo modo (achado 1).
- **Módulo 09:** substituição acoplada e balanço de carga (Ca²⁺ por Na⁺ com vacância) coerentes.
- **Módulo 10:** 573 °C e quartzo deslocativo (aula 01); sanidina desordenada, ortoclásio parcialmente ordenado, microclínio triclínico e a grade como macla de transformação (aula 02): coerentes depois do achado 10; politipo × falha de empilhamento (aula 03) coerente.
- **Entre as aulas deste módulo:** Dauphiné passou a ter as mesmas três origens nas aulas 04 e 06 (achado 9); a "discordância desloca um vetor inteiro" da aula 04 vale para a discordância perfeita, que é a tratada ali, e não contradiz mais a aula 02 (achado 6); a convenção dupla de índices aparece igual para calcita e estaurolita (achado 12).
- **curso-geologia-avancado, módulo 40** (por nome): nomes de leis (Carlsbad, albita, periclínio, Baveno, Manebach; Dauphiné, Brasil, Japão) mantidos.

## Correções aplicadas

**Aplicadas em:** 2026-10-06

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CRI-DEFPT-FLUOR-001` | 🟠 | Corrigido | aula-01 |
| `CRI-DEFPT-EQUIL-001` | 🟠 | Corrigido | aula-01 |
| `CRI-DEFPT-COR-001` | 🟠 | Corrigido | aula-01 |
| `CRI-DEFPT-COR-002` | ⚪ | Corrigido (divergência explicitada) | aula-01 |
| `CRI-DEFPT-NAOES-001` | 🟠 | Corrigido | aula-01 |
| `CRI-DISC-BURGERS-001` | 🟠 | Corrigido | aula-02 |
| `CRI-PLAN-ANTIF-001` | 🟠 | Corrigido | aula-02 |
| `MIN-MACLA-PIRITA-001` | 🔴 | Corrigido | aula-03 |
| `MIN-MACLA-DAUPHINE-001` | 🟠 | Corrigido | aula-04, aula-06 |
| `MIN-MACLA-MICRO-001` | 🟠 | Corrigido | aula-04 |
| `MIN-MACLA-DEFORM-001` | 🟠 | Corrigido | aula-04 |
| `MIN-STAUR-MACLA-001` | 🟠 | Corrigido | aula-06 |

Também foram atualizados: as seções "Fontes consultadas" das seis aulas (os "a conferir" viraram fonte conferida), os rodapés `alegacoes_auditaveis` (campo `audit:` de todas as 41 alegações, e o texto `claim:` das 9 corrigidas; YAML dos rodapés validado), o hub do módulo e o `course-state.yaml` (bloco `audit` do 12 e `content_hash` das aulas). Nenhuma figura foi alterada.

**Pendências:** nenhuma. Não há questionário nem baralho a propagar (ainda não existiam).

## Observações fora do escopo factual

- A aula 02 cresceu cerca de 60 palavras com as correções dos achados 6 e 7; vale a revisão didática conferir se continua dentro dos 30 minutos (o hub já previa possível divisão).

> [!note] Renumeração posterior (revisão didática, 2026-10-06)
> A revisão didática dividiu a aula 02 em Parte 1 (discordâncias, ID `mineralogia-m12-a02`, achado 6) e Parte 2 (defeitos planares, ID novo `mineralogia-m12-a07`, achado 7), e os arquivos foram renumerados. Neste relatório, "aula 03" = atual aula 04, "aula 04" = atual 05, "aula 05" = atual 06, "aula 06" = atual 07; os IDs não mudaram. Os caminhos de arquivo do manifesto `.json` foram atualizados para os nomes novos; o texto dos achados não foi alterado.

## Segunda passagem (alegações da revisão didática)

**Auditado em:** 2026-10-06  ·  **Modo:** audit-and-fix  ·  **Profundidade:** full, escopo restrito
**Escopo:** as 7 alegações que a revisão didática registrou com `audit: pendente` (`CRI-DEFPT-DIDAT-001`, `CRI-DISC-DIDAT-001`, `CRI-PLAN-ANTIF-002`, `MIN-MACLA-DIDAT-001`, `MIN-MACLA-DIDAT-002`, `MIN-FELD-DIDAT-001`, `MIN-QTZ-DIDAT-001`) e o restante do texto que a revisão alterou, conforme `12-defeitos-e-maclas-revisao-didatica.md`: glosas e o exemplo (b) da aula 01 (relida inteira, já que cresceu); vocabulário, glosas e o item (d) da aula 02; a aula 03 nova (ponte, analogia do piso, leitura de C/P, tabela, item (iv)); a ponte com o módulo 11 e as glosas da aula 04; a glosa da böhmita e o pré-requisito da aula 05; a glosa do anortoclásio da aula 06; as glosas e a notação m3̄m da aula 07. As 12 correções da primeira passagem foram conferidas: nenhuma foi revertida.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

🔴 0 · 🟠 2 · 🟡 0 · 🔵 0 · ⚪ 0  ·  Verificadas e corretas: 6 das 7 alegações pendentes (a sétima virou o achado 13), mais o texto alterado em volta delas.

### 🟠 13. "Quatrilling" não é um termo inglês

**claim_id:** `MIN-MACLA-DIDAT-001`  ·  **Tipo:** erro factual (menor, de nomenclatura)  ·  **Onde:** aula 04 · Os quatro tipos, item 4
**Está escrito:** "trilling de 120°, quatrilling de 90°, sixling de 60° (nomes do inglês para maclas de três, quatro e seis indivíduos)"
**Problema:** a glosa da revisão apresenta os três como termos ingleses. *Trilling* e *sixling* estão certos; a macla de quatro indivíduos é *fourling* em inglês. "Quatrilling" não aparece nos glossários consultados, e o aluno que buscar o termo não vai achá-lo.
**Correção aplicada:** "trilling de 120°, fourling de 90°, sixling de 60°"; o texto `claim:` do rodapé também foi ajustado, e a fonte foi acrescentada em "Fontes consultadas".
**Fonte:** Minerals.net, *Mineral Glossary* (fourling, trilling, sixling); Merriam-Webster (fourling), por busca em 2026-10-06  ·  **Confiança:** confirmado
**Conferido sem mudança, na mesma alegação:** 2·arctan(a/b) + 2·arctan(b/a) = 180° (arctan x + arctan 1/x = 90°); a ponte com o módulo 11, aula 04, que escreve 2·arctan(a·senβ/b), igual a 2·arctan(a/b) quando β = 90° (portanto "lá foi escrito o primeiro" está certo); com a cela do HoM, 63,8° e 116,2°, como antes; esqueletismo = arestas e vértices crescem mais rápido que o centro das faces (cristais em funil, *hopper*).

### 🟠 14. Glosa de supersaturação restrita a solução

**claim_id:** `CRI-DISC-SUPERSAT-001` (novo; o trecho não estava listado em `CRI-DISC-DIDAT-001`)  ·  **Tipo:** confusão de escopo  ·  **Onde:** aula 02 · Discordâncias e crescimento em espiral
**Está escrito:** "isso só acontece com bastante supersaturação (excesso de material dissolvido, módulo 03)"
**Problema:** o parágrafo trata do crescimento de cristais em geral, e o exemplo citado logo adiante (espirais em SiC, Verma, 1951), assim como o paradoxo que Frank e a teoria BCF resolveram, é de crescimento **a partir de vapor**. A glosa só com "material dissolvido" levaria o aluno a concluir que os cristais de SiC cresceram de uma solução.
**Correção aplicada:** "supersaturação (excesso de material dissolvido, ou de vapor, além do que o equilíbrio admite; módulo 03)". `palavras_corpo` da aula 02 passou de 1.266 para 1.275. Alegação registrada no rodapé.
**Fonte:** Verma (1951), *Phil. Mag.* (7) 42, n. 332; Burton, Cabrera & Frank (1951), *Phil. Trans. R. Soc. A* 243, 299 (a supersaturação exigida pela nucleação bidimensional no crescimento a partir de vapor), por busca em 2026-10-06; módulo 03, aula 04 (definição para soluções)  ·  **Confiança:** confirmado

### Verificado e correto (segunda passagem)

| claim_id | O que foi conferido | Fonte | Confiança |
|---|---|---|---|
| `CRI-DEFPT-DIDAT-001` | exp(x) = eˣ, e ≈ 2,718; eV como unidade de energia; não estequiometria = composição fora da proporção de inteiros da fórmula ideal; relógios isotópicos = idades por decaimento radioativo; Na/Ca coloidal (achado 3 mantido); exemplo (b): M³⁺ + 2 vacâncias no lugar de 3 Na⁺ (+3 = +3), declarado hipotético; "O que não concluir" agora com o sentido certo (prever, não prevenir) | definições usuais; conta de carga | confirmado |
| `CRI-DISC-DIDAT-001` | [110] = diagonal de face, a√2; a/2⟨110⟩ = (½, ½, 0), centro da face, translação do retículo cF da halita; [100]∧[110] = 45° num cúbico (cos 45° = 1/√2), logo mista; extinção ondulante: a extinção "varre" o grão ao girar a platina, por subgrãos levemente desorientados | módulo 06, aula 02; geometria; definição de *undulose extinction* (busca) | confirmado |
| `CRI-PLAN-ANTIF-002` | na pigeonita, os domínios de antifase diferem pela translação de centragem C perdida em C2/c → P2₁/c: vetor de deslocamento ½(a + b), que é a centragem C (½, ½, 0) do módulo 06; analogia do piso xadrez coerente (deslocar uma lajota é translação do piso desordenado, não do ordenado), com o limite declarado | *Am. Mineral.* 58, 540 (1973) e estudos de DRX em alta temperatura da pigeonita, por busca; módulo 06, aula 02 | confirmado |
| `MIN-MACLA-DIDAT-002` | böhmita = γ-AlO(OH), oxi-hidróxido de alumínio, espécie IMA válida; partições do coríndon em {0001} e {10̄11} "from exsolved böhmite"; "exsolução" coerente com a definição do módulo 09, aula 03 | *Handbook of Mineralogy*, corundum (lido em 2026-10-06); White (1979), *Am. Mineral.* 64, 1300; Mindat/IMA (boehmite), por busca | confirmado |
| `MIN-FELD-DIDAT-001` | anortoclásio = (Na,K)AlSi₃O₈, triclínico (C1̄), com Na > K; grade de albita + periclínio em {100}. Para a IMA, não é espécie (é tratado como variedade ou membro intermediário da série alcalina); a glosa não o chama de espécie, então fica como está, e o detalhe é do módulo 36 | *Handbook of Mineralogy*, anorthoclase (lido em 2026-10-06); Mindat/Wikipedia (status IMA), por busca | confirmado |
| `MIN-QTZ-DIDAT-001` | quartzo direito e esquerdo giram o plano de vibração da luz em sentidos opostos (base da "macla óptica" do Brasil); *macle* = diamante triangular achatado, maclado em (111) pela lei do espinélio; selenita = variedade transparente e incolor da gipsita (nome de Wallerius, 1747; não é espécie); m3̄m com espelhos {100} e {110}, agora escrito como nos módulos 04 e 05 | *International Tables for Crystallography* D, 3.3.6.3; GIA, *Gems & Gemology*, outono de 2025 ("macle diamonds"); Mindat (selenite), por busca | confirmado |

Também conferido no texto alterado, sem achado: a definição de MET e a frase "o contorno de uma macla é um quarto tipo de defeito planar", em que a orientação muda (aula 03); a remissão da exsolução ao módulo 09, aula 03, onde o termo é definido (aulas 04 e 05); a glosa de tensão de cisalhamento e SiC = carbeto de silício (aula 02).

### Correções aplicadas (segunda passagem)

**Aplicadas em:** 2026-10-06

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `MIN-MACLA-DIDAT-001` | 🟠 | Corrigido | aula-04 (corpo, rodapé, Fontes consultadas) |
| `CRI-DISC-SUPERSAT-001` | 🟠 | Corrigido | aula-02 (corpo, rodapé com alegação nova, Fontes consultadas, `palavras_corpo`) |
| `CRI-DEFPT-DIDAT-001`, `CRI-DISC-DIDAT-001`, `CRI-PLAN-ANTIF-002`, `MIN-MACLA-DIDAT-002`, `MIN-FELD-DIDAT-001`, `MIN-QTZ-DIDAT-001` | — | Verificado (rodapé `audit:` de "pendente" para "verificado") | aulas 01, 02, 03, 05, 06, 07 (só rodapé; na aula 02 também Fontes) |

Também atualizados: o manifesto `.json` (2 achados novos, 6 alegações verificadas, contagens do resumo) e o `course-state.yaml` (bloco `audit` do módulo 12; `content_hash` das aulas tocadas e `palavras_corpo` da aula 02). Nenhuma figura foi alterada. O relatório da revisão didática não foi editado: o "quatrilling" citado nele (🟡 7) é registro histórico do que a revisão aplicou, e o achado 13 registra a correção.

**Pendências:** nenhuma. Não há questionário nem baralho a propagar (ainda não existem). Quando forem gerados, devem usar *fourling* e a glosa de supersaturação corrigida.

## Auditoria de questionários e baralho

**Auditado em:** 2026-10-06  ·  **Modo:** audit-and-fix  ·  **Profundidade:** full, escopo restrito ao material derivado
**Material:** `12-defeitos-e-maclas-questionario-parcial-1.md` (Q1–Q9, 18 pts), `-parcial-2.md` (Q10–Q19, 19 pts), `-final.md` (Q20–Q34, 41 pts); `-flashcards-basic.csv` (fb001–fb111), `-flashcards-cloze.csv` (fc001–fc009) e `-flashcards.md`
**Critério:** todo gabarito, distrator comentado e card tem de ser verdadeiro e rastreável a uma frase das aulas atuais (versões já auditadas em duas passagens). Conferidos também: contas, cards com fato fora das aulas, sintaxe Cloze, quase-duplicatas, objetivo sem questão, IDs de aula (aula 03 = `a07`, 04 = `a03`, 05 = `a04`, 06 = `a05`, 07 = `a06`) e os termos já corrigidos (*fourling*; supersaturação inclui vapor).
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

🔴 0 · 🟠 5 · 🟡 0 · 🔵 0 · ⚪ 0

**Contas refeitas em Python (2026-10-06, k = 8,617333 × 10⁻⁵ eV/K):**

| Onde | Conta | Resultado | Gabarito |
|---|---|---|---|
| P1 Q9 (a) | n/N para E = 0,5 eV a 300 K e 600 K | E/kT 19,341 e 9,670; 3,98 × 10⁻⁹ e 6,31 × 10⁻⁵; razão 1,58 × 10⁴ | ✔ |
| P1 Q9 (b)(c)(d) | \|b\| = 4,20/√2; ângulos de [110] com [1 1̄ 0], [110] e [100] | 2,970 Å; 90°, 0° e 45° | ✔ |
| P2 Q19 (a)(b)(c) | 360/72; 2·arctan(8/5) e suplemento; 24/6 | 5; 115,99° e 64,01°; 4 | ✔ |
| F Q31 (a) | Schottky do Al₂O₃: 2 × (+3) retirados contra 3 × (−2) retirados | soma 0 | ✔ |
| F Q31 (c) | n/N para E = 0,6 eV a 400 K e 800 K | E/kT 17,407 e 8,703; 2,76 × 10⁻⁸ e 1,66 × 10⁻⁴; razão 6,02 × 10³ | ✔ |
| F Q31 (d) | Fe₀,₉₀O: a + b = 0,90; 2a + 3b = 2 | Fe³⁺ 0,20; Fe²⁺ 0,70 | ✔ |
| F Q33 (c) | 360/8 | 45° | ✔ |
| Cards fb035 e fb072 | a/√2 com a = 5,640 Å; 2·arctan(7,9672/4,9611) | 3,988 Å; 116,18° e 63,82° | ✔ |

**Cobertura:** os 5 objetivos têm questão no final; os parciais cobrem oa01–oa03 e oa04–oa05; as matrizes somam 18, 19 e 41 pontos (refeito item a item). Cada aula e cada objetivo têm cards. Nenhum card traz valor, plano, lei ou exemplo fora das aulas; os dados fora das aulas nos questionários (energias e celas hipotéticas; Schottky do coríndon como aplicação do método da aula 01) estão declarados como tais. Os termos corrigidos aparecem só na versão corrigida (fc004 usa *fourling*; fb041 inclui vapor; nenhuma ocorrência de "quatrilling"). Sintaxe Cloze válida (c1 a c3, sem chaves internas). As colunas `aula` dos CSVs usam os IDs certos. A tabela do `flashcards.md` confere campo a campo com os CSVs (120 de 120, conferido por script).

### 🟠 15. Parciais "sempre" margeiam falha de empilhamento, e a Q22 dizia que não têm papel em maclas e antifases

**claim_id:** `CRI-DISC-PARCIAL-001`  ·  **Tipo:** confusão de escopo  ·  **Onde:** questionário final · Q22 (enunciado, distratores e gabarito); origem na aula 02 (Cunha e hélice) e na aula 03 (Falha de empilhamento); card fb033
**Está escrito:** Q22: "As discordâncias parciais (...) sempre margeiam: a) um contorno de antifase. b) um contorno de macla. c) um contorno de grão de alto ângulo. d) uma falha de empilhamento." Gabarito: "a), b) e c) são outros defeitos planares, nos quais as discordâncias parciais não têm papel." Aula 02: "elas sempre margeiam uma falha de empilhamento"; aula 03: "a superfície que as discordâncias parciais da aula 02 sempre margeiam".
**Problema:** o gabarito afirma algo falso. A maclagem de deformação avança por parciais (parciais de Shockley em planos sucessivos) nos contornos de macla, e em fases ordenadas as superdiscordâncias se dissociam em superparciais separadas por um contorno de antifase. Dois distratores ficavam defensáveis. A origem é o "sempre" das aulas, que restringe a uma falha de empilhamento o que vale para um defeito planar.
**Correção aplicada:** aula 02: "elas sempre margeiam um defeito planar, em geral uma falha de empilhamento (aula 03)"; aula 03: "a superfície que as discordâncias parciais da aula 02 margeiam com mais frequência"; Q22: enunciado "margeiam, com mais frequência", distratores trocados por defeitos pontuais (vacância isolada, centro de cor, par de Schottky) e gabarito reescrito, com nota sobre maclas e antifases; fb033 (CSV e md): "sempre margeia um defeito planar, em geral uma falha de empilhamento". Rodapés das aulas 02 e 03 e "Fontes consultadas" da aula 02 atualizados.
**Fonte:** Hull & Bacon, *Introduction to Dislocations* (parciais e falhas planares; superdiscordâncias em ligas ordenadas); literatura de maclagem por parciais de Shockley em planos {111} sucessivos e de superparciais ½⟨110⟩ separadas por contorno de antifase no Ni₃Al (por busca, 2026-10-06)  ·  **Nível:** revisada por pares  ·  **Confiança:** confirmado
**Também aparece em:** aula 02, aula 03, questionário final, flashcards-basic.csv, flashcards.md

### 🟠 16. IDs de aula trocados pelo número do arquivo nos questionários

**claim_id:** `QST-M12-IDAULA-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** os três questionários · Cobertura ("Aulas sem questão"); final · "Como usar" e "Onde revisar"
**Está escrito:** parcial 1: "a03: Q5, Q7, Q9 (e)"; parcial 2: "a04: Q10 (...) · a07: Q11, Q14, Q15, Q19 (d)"; final: "a03: Q22, Q28, Q32 (...) a07: Q29, Q33, Q34 (b)(d)"; "Questões 29, 33, 34 (b)(d): Aula 07"; "As questões 27, 30, 31 e 34 ligam mais de uma aula".
**Problema:** a notação `aNN` é a dos IDs, mas foi usada com o número do arquivo: no `course-state.yaml`, `a03` é a aula 04 e `a07` é a aula 03, e assim por diante. Além disso, a Q34 (d) (lamelas do coríndon) é da aula 05, não da 07, e a Q31 usa só a aula 01, enquanto a Q33 liga as aulas 04 e 07.
**Correção aplicada:** "aula NN, `aXX`" com o ID certo nos três questionários, com nota sobre a numeração; Q34 (d) tirada da aula 07; "27, 30, 33 e 34".
**Fonte:** `course-state.yaml` (itens de `lessons` do módulo 12) e cabeçalhos `**ID:**` das aulas  ·  **Confiança:** confirmado
**Também aparece em:** os três questionários (o `flashcards.md` já trazia a tabela de correspondência certa)

### 🟠 17. Comentário do distrator d) da Q21 confundia intersticial com Na coloidal

**claim_id:** `QST-M12-CENTROF-001`  ·  **Tipo:** confusão de escopo  ·  **Onde:** questionário final · Q21, gabarito
**Está escrito:** distrator "d) um átomo de sódio num vazio da halita"; comentário: "d) o Na ou Ca coloidal vem de um estágio seguinte e explica o azul da halita e o roxo da fluorita."
**Problema:** o comentário sugere que o distrator descreve o Na coloidal. Um átomo isolado num vazio é um intersticial (aula 01); o Na coloidal são partículas de metal formadas num estágio seguinte ao centro F.
**Correção aplicada:** "d) descreve um intersticial, não um centro F (o azul da halita vem de um estágio seguinte, em que o Na metálico se reúne em partículas coloidais, e não de um átomo isolado num vazio)."
**Fonte:** aula 01 (intersticial; centros de cor), conferida com Nassau na primeira passagem (achado 3)  ·  **Confiança:** confirmado

### 🟠 18. Card da leucita não respondia à pergunta

**claim_id:** `FLC-M12-LEUC-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** fb081
**Está escrito:** frente "Que macla caracteriza a leucita, e como aparece em lâmina?"; verso "Cúbica em alta temperatura e tetragonal na ambiente, tem muitos domínios maclados: lamelas finas em mais de uma direção."
**Problema:** o verso não diz que macla é (de transformação, aula 05); o aluno decoraria uma resposta que não responde à frente.
**Correção aplicada:** verso "Macla de transformação: cúbica em alta temperatura e tetragonal na ambiente, sai com muitos domínios maclados, lamelas finas em mais de uma direção." (CSV e md)
**Fonte:** aula 05 (Leucita; `MIN-MACLA-LEUC-001`)  ·  **Confiança:** confirmado

### 🟠 19. Card Basic repetindo Cloze e quase-duplicata de Dauphiné

**claim_id:** `FLC-M12-DUPLIC-001`  ·  **Tipo:** inconsistência interna  ·  **Onde:** fc007 × fb095; fb079 × fb099
**Está escrito:** fc007, lacuna c2 "triclínico", o mesmo fato do verso de fb095 ("O feldspato é triclínico"); fb099 "Como é a lei de Dauphiné do quartzo quanto à mão e ao tipo?" / "Relaciona indivíduos da mesma mão (...)", o mesmo "mesma mão" de fb079.
**Problema:** contraria o critério declarado no `flashcards.md` ("Nenhum card Basic repete o fato de um Cloze") e faz dois cards competirem na revisão.
**Correção aplicada:** fc007 com a lacuna c2 em "(010)" e "triclínico" como texto fixo; fb099 passou a perguntar "quanto ao tipo e à visibilidade", com verso "De penetração, com limites irregulares; invisível a olho nu e em lâmina delgada comum (aparece por ataque químico, microscopia eletrônica ou difração)" (frase da aula 07). CSVs e md.
**Fonte:** aula 06 (regra de leitura); aula 07 (Dauphiné)  ·  **Confiança:** confirmado

### Verificado e correto (terceira passagem)

| claim_id | O que foi conferido | Fonte | Confiança |
|---|---|---|---|
| `QST-M12-CALC-001` | todas as contas dos gabaritos e dos cards (tabela acima) | Python, 2026-10-06 | confirmado |
| `QST-M12-GABAR-001` | os 34 gabaritos e os comentários de distratores, contra as aulas atuais; nenhum distrator defensável depois do achado 15 | aulas 01 a 07 | confirmado |
| `QST-M12-OA-001` | 5 de 5 objetivos com questão no final; matrizes de 18, 19 e 41 pontos; distribuição cognitiva e por tipo | course-state.yaml; matrizes | confirmado |
| `FLC-M12-RASTRO-001` | 120 cards rastreados a frases das aulas; nenhum fato fabricado; IDs de aula, objetivos e contagens por aula (26+2, 16+1, 14, 16+2, 17+1, 9+1, 13+2) | aulas 01 a 07; CSVs | confirmado |
| `FLC-M12-TERMOS-001` | *fourling* (fc004), supersaturação com vapor (fb041), −E/2kT (fb002), centro F âmbar e Na/Ca coloidal (fb017, fb018), pirrotita com x até ~0,17 (fb024), antifase da pigeonita por C2/c → P2₁/c (fb053, fb054), estaurolita {031}/{231} (fc008), calcita {01̄18}/{01̄12} (fc009) | achados 2, 3, 5, 7, 12, 13 e 14 | confirmado |

**Ajuste só de formato (sem claim_id):** no `flashcards.md`, as barras de \|b\| de fb035 e fb036 foram escapadas, porque partiam as colunas da tabela.

### Correções aplicadas (terceira passagem)

**Aplicadas em:** 2026-10-06

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CRI-DISC-PARCIAL-001` | 🟠 | Corrigido | aula-02 (corpo, rodapé, Fontes), aula-03 (corpo, rodapé), questionario-final (Q22), flashcards-basic.csv e flashcards.md (fb033) |
| `QST-M12-IDAULA-001` | 🟠 | Corrigido | questionario-parcial-1, questionario-parcial-2, questionario-final |
| `QST-M12-CENTROF-001` | 🟠 | Corrigido | questionario-final (Q21) |
| `FLC-M12-LEUC-001` | 🟠 | Corrigido | flashcards-basic.csv, flashcards.md (fb081) |
| `FLC-M12-DUPLIC-001` | 🟠 | Corrigido | flashcards-cloze.csv, flashcards-basic.csv, flashcards.md (fc007, fb099) |

Também atualizados: o registro de geração dos três questionários, o cabeçalho e o histórico do `flashcards.md`, o manifesto `.json` (5 achados, 5 alegações verificadas, contagens) e o `course-state.yaml` (bloco `audit`; `content_hash` das aulas 02 e 03; `palavras_corpo` da aula 02 de 1.275 para 1.280 e da aula 03 de 1.043 para 1.045). Nenhum ID de card ou de questão mudou. Se o baralho já tiver sido importado no Anki, os cards fb033, fb081, fb099 e fc007 precisam ser editados à mão: reimportar o CSV pode não sobrescrever cards existentes.

**Pendências:** nenhuma.
