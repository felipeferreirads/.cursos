# Auditoria científica: Módulo 04 — Simetria e morfologia cristalina

**Auditado em:** 2026-10-04
**Material:** `curso-mineralogia/04-simetria-e-morfologia/` — as 7 aulas (`04-simetria-e-morfologia-aula-01` a `-aula-07`)
**Modo:** audit-and-fix
**Profundidade:** full, com checagem rigorosa de nomenclatura de Hermann-Mauguin, número de classes por sistema e classe de cada mineral citado como exemplo
**Escopo:** as 60 alegações dos rodapés `alegacoes_auditaveis`, mais as afirmações de risco do corpo: as 8 famílias e os 32 grupos, as ordens de cada grupo, os símbolos completo e curto, as direções de cada posição, as 11 classes centrossimétricas e as 10 polares, a contagem por sistema (2, 3, 3, 7, 5, 7, 5), as equivalências de rotoinversão e cada passo dos exemplos trabalhados. Questionário e baralho ainda não existiam.
**Veredito:** Requer correção → **correções aplicadas; estado final: Aprovado** (nenhum achado aberto)

## Resumo

🔴 1 erro · 🟠 2 imprecisões · 🟡 3 imprecisões menores · 🔵 0 sem fonte · ⚪ 0 controversos
Verificadas e corretas: 54 alegações (53 confirmadas, 1 provável).

O núcleo formal passou sem erro: as 32 classes e sua dedução em oito famílias (5 + 5 + 3 + 4 + 4 + 3 + 3 + 5 = 32), a distribuição por sistema (2 + 3 + 3 + 7 + 5 + 7 + 5 = 32), as ordens (1 a 48), os símbolos completos (4/m 3̄ 2/m, 2/m 3̄, 3̄ 2/m, 4/m 2/m 2/m, 6/m 2/m 2/m, 2/m 2/m 2/m), as direções de cada posição por sistema, as 11 classes centrossimétricas, as 10 polares, as equivalências 1̄ = centro, 2̄ = m, 3̄ = 3 + 1̄, 6̄ = 3/m, e as holoedrias. Os erros estavam nos lugares onde a teoria encontra o texto corrido: um exemplo trabalhado, uma implicação lógica e um nome de notação.

**Exemplos minerais por classe** — conferidos um a um (grupo espacial → grupo pontual). As espécies raras (pinnoíta, cahnita, diaboleíta, escolecita, clinoedrita, petzita, ullmannita, benitoíta, e a gratonita descartada) foram conferidas por busca em Mindat/Wikipedia nesta sessão; as comuns, pelo conhecimento consolidado dos livros-texto (Klein & Dutrow, Handbook of Mineralogy): cianita P1̄, microclínio C1̄, albita C1̄; escolecita Cc, clinoedrita Cc; gipsita C2/c, ortoclásio C2/m, muscovita C2/c, diopsídio C2/c; epsomita P2₁2₁2₁; hemimorfita Imm2; forsterita Pbnm, topázio Pbnm, barita Pnma, aragonita Pmcn; pinnoíta P4₂; cahnita I4̄; scheelita I4₁/a; cristobalita de baixa P4₁2₁2; diaboleíta P4mm; calcopirita I4̄2d; zircão I4₁/amd, rutilo e cassiterita P4₂/mnm; dolomita e ilmenita R3̄; quartzo P3₁21/P3₂21, cinábrio P3₁21; turmalina R3m; calcita, coríndon e hematita R3̄c; nefelina P6₃; apatita P6₃/m; quartzo de alta P6₂22/P6₄22; zincita e wurtzita P6₃mc; benitoíta P6̄c2; berilo P6/mcc, grafita e molibdenita P6₃/mmc; ullmannita P2₁3; pirita Pa3̄; petzita I4₁32; esfalerita F4̄3m, tetraedrita I4̄3m; halita, fluorita, galena, ouro Fm3̄m, granadas Ia3̄d, espinélio e diamante Fd3̄m. No rascunho, a gratonita tinha sido cogitada para a classe 3 e foi descartada antes de entrar no texto: é 3m (R3m). Vesuvianita foi retirada da linha 4/mmm porque parte das amostras é P4/n. As classes 1, 2, 3 e 6̄ ficaram como "raro", sem exemplo.

> [!note] Limite da verificação nesta sessão
> Conferência por busca na web (Mindat, páginas de minerais da Wikipedia, verbete "Form" do *Online Dictionary of Crystallography* da IUCr), cruzada com o conhecimento consolidado dos livros-texto. Não houve acesso ao texto integral das *International Tables*, vol. A, nem a Klein & Dutrow; as tabelas de grupos pontuais foram conferidas por consistência interna (somas, ordens, centros, polares) e contra o conhecimento consolidado. Recomenda-se, numa sessão com acesso, conferir as classes das espécies comuns da tabela da aula 05 numa única consulta ao Mindat.

## Achados

### 🔴 1. Operação errada no exemplo da calcita

**claim_id:** `CRI-CLS-ESCALENO-001`
**Tipo:** erro factual
**Onde:** aula 05 · Exemplo trabalhado, passo 3
**Está escrito:** "Girando 120°, o cristal coincide. Girando 60° e invertendo, também"
**Problema:** girar 60° e inverter é a operação **6̄** (= 3/m), que exige um espelho horizontal, ausente na classe 3̄m. A operação do eixo 3̄ é **girar 120° e inverter**. O efeito geométrico descrito (conjunto de baixo deslocado de 60°) estava certo; a operação que o produz, não. Num exemplo trabalhado que ensina o procedimento, o erro seria copiado pelo aluno e contradiz a tabela da aula 03.
**Correção aplicada:** "Girando 120° e invertendo pelo centro, também: cada face de cima tem, embaixo, uma face paralela a ela, e o conjunto de baixo fica deslocado de 60° em relação ao de cima."
**Fonte:** *International Tables for Crystallography*, vol. A (operações de 3̄ e 6̄)  ·  **Nível:** normativa
**Confiança:** confirmado
**Também aparece em:** só na aula 05. A tabela da aula 03 ("3̄: gira 120° e inverte") estava correta.

### 🟠 2. "Sem espelho e sem centro, por isso quiral"

**claim_id:** `CRI-SIM-ESPELHO-001`
**Tipo:** erro factual (implicação inválida)
**Onde:** aula 02 · Reflexão: o plano de simetria
**Está escrito:** "Um objeto que não tem nem espelho nem centro (abaixo) e que, por isso, não coincide com sua imagem no espelho é quiral"
**Problema:** a ausência de espelho e de centro não basta. A classe 4̄ não tem nenhum dos dois e não é quiral, porque 4̄ é uma operação imprópria. A aula 03 já dava a regra correta ("quiral = sem nenhum elemento impróprio"); a aula 02 a contradizia.
**Correção aplicada:** "Um objeto que não coincide com sua imagem no espelho é quiral (ou enantiomorfo). Para isso, ele não pode ter espelho nem centro (abaixo), nem a rotoinversão da aula 03."
**Fonte:** *International Tables*, vol. A (classes enantiomórficas: 1, 2, 222, 4, 422, 3, 32, 6, 622, 23, 432)  ·  **Nível:** normativa
**Confiança:** confirmado

### 🟠 3. Notação A/P/C chamada de "Bravais-Miller"

**claim_id:** `CRI-SIM-CUBO-001`
**Tipo:** erro factual (atribuição)
**Onde:** aula 02 · O cubo como laboratório
**Está escrito:** "isso se escreve na notação de Bravais-Miller, com A para eixo, P para plano e C para centro"
**Problema:** "Bravais-Miller" é o nome consagrado dos índices de quatro números (hkil) do sistema hexagonal, que o módulo 05 vai ensinar. Usar o nome para a lista A/P/C criaria um conflito direto de terminologia no módulo seguinte.
**Correção aplicada:** "Em livros mais antigos (e em muitos textos em português), essa lista se escreve com A para eixo, P para plano e C para centro". As contagens (3A₄ 4A₃ 6A₂ 9P C) estavam corretas.
**Fonte:** Klein & Dutrow, *Manual of Mineral Science*, 23ª ed. (índices de Miller-Bravais)  ·  **Nível:** livro-texto
**Confiança:** confirmado

### 🟡 4. Anidrita "forma blocos" quase cúbicos

**claim_id:** `CRI-SIS-ANIDRITA-001`  ·  **Onde:** aula 06
**Problema:** o aspecto quase cúbico é dos fragmentos de clivagem (três clivagens em ângulo reto); os cristais são tabulares a prismáticos.
**Correção aplicada:** "parte em blocos de aparência quase cúbica (tem três clivagens em ângulo reto)".  ·  **Confiança:** confirmado

### 🟡 5. "Dodecaedro" de quartzo

**claim_id:** `CRI-FOR-QUARTZO-001`  ·  **Onde:** aula 07 · Erros comuns
**Problema:** a expressão não descreve o cristal (18 faces com as duas pontas) e se confunde com o dodecaedro rômbico ensinado na mesma aula.
**Correção aplicada:** "As seis faces de cada ponta do quartzo parecem uma pirâmide hexagonal, mas são dois romboedros; com o prisma, o cristal tem três formas, não uma."  ·  **Confiança:** confirmado

### 🟡 6. Data da notação de Hermann-Mauguin

**claim_id:** `CRI-HM-HIST-001`  ·  **Onde:** aula 04
**Problema:** "no fim dos anos 1920" só cobre Hermann (1928); Mauguin publicou em 1931.
**Correção aplicada:** "Carl Hermann (1928) e Charles-Victor Mauguin (1931) propuseram um símbolo compacto".  ·  **Confiança:** confirmado

## Verificado e correto (seleção das alegações de maior risco)

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `CRI-GP-32-001` | 32 grupos pontuais; Hessel (1830), Gadolin (1867) | Burke (1966); *Int. Tables* A | confirmado |
| `CRI-GP-FAMILIAS-001` | Oito famílias somando 32 | *Int. Tables* A | confirmado |
| `CRI-GP-CENTRO-001` | 11 classes centrossimétricas (lista) | *Int. Tables* A | confirmado |
| `CRI-CLS-POLARES-001` | 10 classes polares (lista) | *Int. Tables* A; Nye (1985) | confirmado |
| `CRI-CLS-ORDENS-001` | Ordens dos 32 grupos | *Int. Tables* A | confirmado |
| `CRI-HM-DIRECOES-001` | Direções das três posições por sistema | *Int. Tables* A | confirmado |
| `CRI-HM-CUBO-001` | 4/m 3̄ 2/m = m3̄m; reconstrução dos elementos | *Int. Tables* A | confirmado |
| `CRI-HM-CURTOS-001` | mmm, 4/mmm, 6/mmm; 2ª posição cúbica = 3 ou 3̄ | *Int. Tables* A | confirmado |
| `CRI-ROT-EQUIV-001` | 1̄ = centro; 2̄ = m; 3̄ = 3 + 1̄; 6̄ = 3/m; 4̄ novo | *Int. Tables* A | confirmado |
| `CRI-COMB-REGRAS-001` | Quatro regras de combinação | Klein & Dutrow; Nesse | confirmado |
| `CRI-SIS-TABELA-001` | Simetria característica; 2, 3, 3, 7, 5, 7, 5 classes | *Int. Tables* A | confirmado |
| `CRI-SIS-HOLOEDRIA-001` | Holoedrias dos sete sistemas | IUCr *Online Dictionary* | confirmado |
| `CRI-SIS-FAMILIAS-001` | 7 sistemas, 6 famílias, 7 sistemas reticulares | IUCr *Online Dictionary* | confirmado |
| `CRI-SIS-QZRETIC-001` | Quartzo trigonal com retículo hexagonal | P3₁21/P3₂21 | confirmado |
| `CRI-SIS-LEUCITA-001` | Leucita pseudocúbica (tetragonal à temperatura ambiente) | Deer, Howie & Zussman | confirmado |
| `CRI-CLS-PIRITA-001` | Pirita m3̄; estrias reduzem 4 a 2 e eliminam espelhos diagonais | Klein & Dutrow | confirmado |
| `CRI-CLS-TABELA-001` | Classe de cada representante (lista acima) | Mindat; Handbook of Mineralogy | confirmado |
| `CRI-CLS-HOLANDESES-001` | Anedota da turmalina e das cinzas de cachimbo | fonte secundária | provável |
| `CRI-FOR-47-001` | 47 formas (48 separando domo e esfenoide) | IUCr *Online Dictionary*, "Form" | confirmado |
| `CRI-FOR-GERAL-001` | Faces da forma geral = ordem (48, 12, 2) | *Int. Tables* A | confirmado |
| `CRI-FOR-ABERTAS-001` | Formas abertas e fechadas, com nº de faces | Klein & Dutrow | confirmado |
| `CRI-EST-STENO-001` | Steno, 1669, quartzo | Burke (1966) | confirmado |
| `CRI-EST-HAUY-001` | Haüy, 1784, clivagem da calcita (queda como anedota) | Haüy (1784) | confirmado |
| `CRI-EST-QUASI-001` | Shechtman 1982; IUCr 1992; icosaedrita (IMA 2010-042) | IUCr (1992); Bindi et al. (2009) | confirmado |
| `CRI-EST-NORMAIS-001` | Ângulo entre normais; 60° no prisma hexagonal | Klein & Dutrow | confirmado |
| `CRI-SIM-TIJOLO-001` | Tijolo 3A₂ 3P C; caixa quadrada A₄ 4A₂ 5P C | dedução | confirmado |

As demais 28 alegações (todas com `audit: verificado em 2026-10-04` no rodapé) foram conferidas da mesma forma.

## Consistência interna e com o resto do curso

- **Aulas 02 × 03:** a regra de quiralidade agora é a mesma nas duas (achado 2).
- **Aulas 03 × 05:** a operação 3̄ é "girar 120° e inverter" nas duas (achado 1).
- **Aula 02 × módulo 05:** "Bravais-Miller" fica reservado para os índices hkil (achado 3).
- **Curso-geologia, módulo 04, aulas 04-05 (sete sistemas, qualitativo):** a aula 06 mantém "sete sistemas" e apresenta famílias e sistemas reticulares como refinamento, como pede o `_contexto.md`. Remissão só por nome.
- **Módulo 02:** a definição de cristal (aula 01) é coerente com a da aula 01 do módulo 02 ("cristalino = padrão regular nas três direções").

## Correções aplicadas

**Aplicadas em:** 2026-10-04

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CRI-CLS-ESCALENO-001` | 🔴 | Corrigido | aula-05 |
| `CRI-SIM-ESPELHO-001` | 🟠 | Corrigido | aula-02 |
| `CRI-SIM-CUBO-001` | 🟠 | Corrigido | aula-02 |
| `CRI-SIS-ANIDRITA-001` | 🟡 | Corrigido | aula-06 |
| `CRI-FOR-QUARTZO-001` | 🟡 | Corrigido | aula-07 |
| `CRI-HM-HIST-001` | 🟡 | Corrigido | aula-04 |

Também foram atualizados: os rodapés `alegacoes_auditaveis` das 7 aulas (campo `audit:` em cada uma das 60 alegações); o hub do módulo; `course-state.yaml` (bloco `audit`).

## Segunda passagem (depois da revisão didática)

**Em:** 2026-10-04. A revisão didática acrescentou glossas, duas figuras sugeridas (sem conteúdo factual novo além do que já estava auditado: eixos 4 da halita e 2 da pirita; elementos de 4mm, 4/mmm, 4̄2m e mmm), um ponto de pausa e enxugou a aula 05 (sem alterar fatos; a anedota da turmalina passou de "atrair" para "limpar" cinzas de cachimbo, que é a forma da fonte). Alegações novas conferidas:

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `CRI-REV-GLOSSAS-001` | clivagem = planos de quebra fácil que seguem planos de átomos | Klein & Dutrow | confirmado |
| `CRI-REV-GLOSSAS-002` | retículo = grade de pontos repetida por translação; macla = regiões de orientações diferentes unidas de modo regular | Klein & Dutrow; IUCr *Online Dictionary* | confirmado |

Total final: 62 alegações, 56 verificadas sem mudança e 6 corrigidas.

**Pendências:** nenhuma.

**Aviso de baralho já importado:** não se aplica; questionário e flashcards ainda não existiam.

## Correção posterior (auditoria do módulo 06, 2026-10-04)

| claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|
| `CRI-EST-CELA-001` | 🟡 | Corrigido | aula-01; flashcards (`fb011`, nos arquivos `-basic.csv` e `.md`) |

A aula 01 definia a cela unitária como "a menor unidade que, repetida por translação, reconstrói o cristal". O módulo 06 (aula 02) mostra que isso vale só para a cela **primitiva**; a cela convencional pode ter 2, 3 ou 4 vezes esse volume. Texto corrigido para "a unidade que [...] reconstrói o cristal (a menor delas é a cela primitiva)". Registro completo na auditoria do módulo 06 (achado cross-module).
