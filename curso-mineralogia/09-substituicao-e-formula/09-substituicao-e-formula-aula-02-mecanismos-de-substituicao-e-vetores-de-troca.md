# Aula 02: Mecanismos de substituição e vetores de troca

**ID:** mineralogia-m09-a02
**Módulo:** [[09-substituicao-e-formula-modulo|Módulo 09 — Cristaloquímica II: substituição iônica, solução sólida e fórmula estrutural]]
**Duração estimada:** ~27 min
**Nível:** ensino médio, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** classificar uma substituição como simples, acoplada, intersticial ou por omissão, escrever o vetor de troca correspondente e conferir que ele mantém a neutralidade.
**Pré-requisito:** [[09-substituicao-e-formula-aula-01-quem-substitui-quem-regras-de-goldschmidt-e-de-ringwood|Aula 01]] (regras de substituição) e [[01-fundamentos-quimicos-aula-03-ions-e-estados-de-oxidacao-fe-mn-e-s|módulo 01, aula 03]] (neutralidade de carga).

## Vocabulário desta aula

| Termo | O que quer dizer |
|---|---|
| **substituição simples (homovalente)** | troca de um íon por outro de mesma carga, num mesmo sítio. |
| **substituição acoplada** | duas trocas simultâneas, em sítios iguais ou diferentes, cujas variações de carga se anulam. |
| **substituição intersticial** | um íon passa a ocupar um espaço normalmente vazio da estrutura (um interstício ou um canal), compensando a carga de outra troca. |
| **substituição por omissão** | um sítio fica vazio (vacância, símbolo □) para compensar a carga de outra troca. |
| **vetor de troca** | a troca escrita como uma "fórmula" com índices negativos para o que sai: FeMg₋₁ quer dizer "entra um Fe, sai um Mg". |

## Antes de começar, você precisa saber

- A regra da carga de Goldschmidt: cargas que diferem de uma unidade só se trocam com compensação ([[09-substituicao-e-formula-aula-01-quem-substitui-quem-regras-de-goldschmidt-e-de-ringwood|aula 01]]).
- Neutralidade e regra da soma dos estados de oxidação ([[01-fundamentos-quimicos-aula-03-ions-e-estados-de-oxidacao-fe-mn-e-s|módulo 01, aula 03]]).
- Interstícios e sítios vazios numa estrutura ([[08-empacotamento-e-coordenacao-aula-03-empacotamento-compacto-e-intersticios|módulo 08, aula 03]]).

## Ao final você vai conseguir

- `mineralogia-m09-oa02` — Classificar os mecanismos de substituição (simples, acoplada, intersticial, por omissão) e escrever o vetor de troca correspondente.

## Conteúdo

### A regra de ouro: a carga tem de fechar

Todo mecanismo de substituição obedece a uma só exigência: o mineral continua neutro. Se a troca não muda a carga, ela é simples. Se muda, alguma outra coisa tem de mudar junto, e há três maneiras de fazer isso.

### 1. Substituição simples

Um íon entra no lugar de outro de **mesma carga**. Na olivina, Fe²⁺ por Mg²⁺: de Mg₂SiO₄ (forsterita) a Fe₂SiO₄ (faialita), passando por qualquer (Mg,Fe)₂SiO₄. Outros exemplos: Mn²⁺ por Fe²⁺; Rb⁺ por K⁺; Hf⁴⁺ por Zr⁴⁺.

### 2. Substituição acoplada

Duas trocas ao mesmo tempo, que se compensam. O exemplo clássico é o **plagioclásio**: da albita, NaAlSi₃O₈, à anortita, CaAl₂Si₂O₈.

- no sítio grande, Ca²⁺ entra no lugar do Na⁺: **+1** de carga;
- num tetraedro, Al³⁺ entra no lugar do Si⁴⁺: **−1**.

Total: zero. As duas trocas sempre andam juntas. Outro exemplo é o **componente de Tschermak** dos piroxênios (silicatos de cadeias de tetraedros, como o diopsídio do módulo 06, estudados no módulo 34): um Al³⁺ entra num octaedro no lugar de um Mg²⁺ (+1) e outro Al³⁺ entra num tetraedro no lugar de um Si⁴⁺ (−1).

### 3. Substituição intersticial

Um íon entra num espaço normalmente **vazio**. No **berilo**, Be₃Al₂Si₆O₁₈, os anéis de tetraedros empilhados deixam canais abertos ao longo do eixo c. Quando um Li⁺ entra no tetraedro do Be²⁺ (−1), um íon alcalino (Na⁺ ou Cs⁺) entra no canal (+1) para compensar. É por isso que berilos de pegmatitos ricos em lítio costumam ter Na e Cs.

### 4. Substituição por omissão

Um sítio fica **vazio**. Na **pirrotita**, Fe₁₋ₓS, parte do ferro é Fe³⁺: para cada 2 Fe³⁺ que entram no lugar de 2 Fe²⁺ (+2), um sítio de Fe fica vazio (−2, porque sai um Fe²⁺ inteiro). Daí a fórmula com menos de um Fe por S. Nos anfibólios, o mecanismo aparece no sentido contrário: um sítio grande que costuma ficar vazio, o sítio A, recebe um Na⁺ quando um Al³⁺ entra no lugar de um Si⁴⁺ (módulo 34).

> [!question] Pare e explique
> Por que a substituição de Li⁺ por Be²⁺ no berilo não pode acontecer sozinha? Qual das quatro formas de compensação ela usa?

### Vetores de troca: uma notação que soma

Escrever "entra Fe, sai Mg" toda vez é cansativo. A notação de **vetor de troca** (J. B. Thompson, 1982) escreve a troca como uma fórmula em que o que sai leva índice negativo:

| Mecanismo | Exemplo | Vetor de troca | Conferência da carga |
|---|---|---|---|
| simples | olivina | **FeMg₋₁** | +2 − 2 = 0 |
| simples | feldspato K | **RbK₋₁** | +1 − 1 = 0 |
| acoplada | plagioclásio | **CaAlNa₋₁Si₋₁** | +2 + 3 − 1 − 4 = 0 |
| acoplada | piroxênio (Tschermak) | **Al(VI)Al(IV)Mg₋₁Si₋₁** | +3 + 3 − 2 − 4 = 0 |
| acoplada | feldspato K com Ba | **BaAlK₋₁Si₋₁** | +2 + 3 − 1 − 4 = 0 |
| intersticial | berilo | **LiNa□₋₁Be₋₁** (o Na ocupa um vazio do canal) | +1 + 1 − 0 − 2 = 0 |
| por omissão | pirrotita | **Fe³⁺₂□Fe²⁺₋₃** | +6 + 0 − 6 = 0 |
| omissão (inverso) | anfibólio (edenita) | **NaAl□₋₁Si₋₁** | +1 + 3 − 0 − 4 = 0 |

Um vetor **soma-se a uma fórmula**: albita + 1 × (CaAlNa₋₁Si₋₁) = NaAlSi₃O₈ + Ca + Al − Na − Si = **CaAl₂Si₂O₈**, a anortita. Somar meio vetor dá a composição do meio da série. Toda solução sólida pode ser escrita como **um membro final mais múltiplos de vetores de troca**, e a conferência da carga do vetor (soma zero) é o teste rápido de que o mecanismo é possível.

## Exemplo trabalhado

**Problema.** (a) Partindo do diopsídio, CaMgSi₂O₆, some uma vez o vetor de Tschermak e confira a fórmula e a carga. (b) Partindo de 8 FeS, aplique uma vez o vetor da pirrotita e escreva a fórmula. (c) Classifique a substituição de Cr³⁺ por Al³⁺ no coríndon e escreva o vetor.

**(a)** CaMgSi₂O₆ + Al(VI)Al(IV)Mg₋₁Si₋₁ = Ca **Al** (Al**Si**)O₆, o "Ca-Tschermak", CaAl(AlSi)O₆. Carga: Ca²⁺ + Al³⁺ (octaedro) + Al³⁺ + Si⁴⁺ (tetraedros) = 2 + 3 + 3 + 4 = **12** = 6 O × 2. ✔

**(b)** Fe₈S₈ + Fe³⁺₂□Fe²⁺₋₃: saem 3 Fe²⁺, entram 2 Fe³⁺ e fica 1 vacância → **Fe₇S₈**, com 2 Fe³⁺ e 5 Fe²⁺. Carga: 2 × 3 + 5 × 2 = **16** = 8 S × 2. ✔ Fe₇S₈ é Fe₁₋ₓS com x = 1/8.

**(c)** Mesma carga, mesmo sítio octaédrico: **simples**. Vetor **CrAl₋₁**. (Diferença de raio: 15%, na fronteira da regra 1; e é esse Cr que dá a cor vermelha do rubi, módulo 48.)

**Método geral:** (1) liste o que entra e o que sai, com cargas e sítios; (2) se a carga não fecha, procure a compensação: outra troca, um íon num espaço vazio ou uma vacância; (3) escreva o vetor com índices negativos; (4) confira: a soma das cargas do vetor é zero.

## Erros comuns

- **Escrever uma troca heterovalente sozinha** ("Ca no lugar de Na no plagioclásio") sem a troca que a compensa.
- **Confundir intersticial com por omissão.** Na primeira, aparece um íon onde não havia; na segunda, some um íon de onde havia.
- **Esquecer a vacância na conta da carga.** O □ vale zero, mas ocupa um sítio: conta como "sítio", não como "carga".
- **Somar vetores com sinais trocados.** CaAlNa₋₁Si₋₁ leva da albita à anortita; o inverso, NaSiCa₋₁Al₋₁, faz o caminho contrário.

## O que não concluir

- Que um vetor de troca diga **como** os átomos se movem fisicamente. Ele é contabilidade de composição, não mecanismo atômico.
- Que todo vetor escrito com carga zero aconteça na natureza. A carga é condição necessária, não suficiente; tamanho e estrutura também decidem (aula 01).
- Que a pirrotita "perca ferro" por falha de análise. As vacâncias são parte da estrutura.

## Recap relâmpago

- Simples: mesma carga, FeMg₋₁ (olivina).
- Acoplada: duas trocas que se anulam; CaAlNa₋₁Si₋₁ (plagioclásio), Al(VI)Al(IV)Mg₋₁Si₋₁ (Tschermak).
- Intersticial: íon num espaço vazio; berilo, Li no lugar de Be e Na/Cs no canal (LiNa□₋₁Be₋₁).
- Por omissão: sítio vazio; pirrotita, 2 Fe³⁺ + □ no lugar de 3 Fe²⁺ (Fe₇S₈).
- Vetor de troca: o que entra com índice positivo, o que sai com negativo; soma-se à fórmula; a carga do vetor é zero.

## Próxima aula

Em [[09-substituicao-e-formula-aula-03-solucao-solida-miscibilidade-e-isomorfismo|Aula 03 — Solução sólida, miscibilidade e isomorfismo]], o resultado coletivo das substituições: séries completas e limitadas, o papel da temperatura e a diferença entre minerais que se misturam e minerais que só têm a mesma estrutura.

## Fontes consultadas

- Thompson, J. B., Jr. (1982). Composition space: an algebraic and geometric approach. *Reviews in Mineralogy* 10, 1–31 (notação de vetores de troca) — conferido por busca em 2026-10-06.
- Berilo: Li⁺ no lugar de Be²⁺ com Na⁺ e Cs⁺ nos canais como compensação de carga — conferido por busca em 2026-10-06 (*Minerals* 9, 641, 2019; *Mineralogical Magazine* 88, 2024, série berilo-pezzottaíta).
- Klein & Dutrow, *Manual of Mineral Science*, 23ª ed. (substituição simples, acoplada, intersticial e por omissão; plagioclásio; pirrotita Fe₁₋ₓS).
- Hawthorne, F. C. et al. (2012), nomenclatura do supergrupo do anfibólio, *American Mineralogist* 97 (sítio A e edenita) — citado como remissão ao módulo 34.
- Contas de carga feitas em Python em 2026-10-06.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: 1079
cobertura:
  mineralogia-m09-oa02: [Conteúdo, Exemplo trabalhado]
alegacoes_auditaveis:
  - claim_id: CRQ-SUB-TIPOS-001
    claim: "Mecanismos: simples (homovalente), acoplada, intersticial (ion num espaco vazio) e por omissao (vacancia)."
    risk: conceito
    source: "Klein & Dutrow"
    audit: "verificado em 2026-10-06"
  - claim_id: CRQ-SUB-PLAG-001
    claim: "Plagioclasio albita NaAlSi3O8 - anortita CaAl2Si2O8 por Ca2+ Al3+ no lugar de Na+ Si4+; vetor CaAlNa-1Si-1."
    risk: fato
    source: "Klein & Dutrow"
    audit: "verificado em 2026-10-06"
  - claim_id: CRQ-SUB-TSCH-001
    claim: "Componente de Tschermak dos piroxenios: Al(VI)Al(IV)Mg-1Si-1; diopsidio + vetor = CaAl(AlSi)O6 (Ca-Tschermak)."
    risk: fato
    source: "Klein & Dutrow; Morimoto (1988)"
    audit: "verificado em 2026-10-06"
  - claim_id: CRQ-SUB-BERILO-001
    claim: "Berilo Be3Al2Si6O18: Li+ no lugar de Be2+ compensado por Na+ ou Cs+ nos canais paralelos a c; vetor LiNa[]-1Be-1."
    risk: fato
    source: "busca: Minerals 9, 641 (2019); Mineral. Mag. 88 (2024)"
    audit: "corrigido em 2026-10-06 (🟡: vetor escrito sem a vacancia do canal, inconsistente com a notacao da edenita; agora LiNa[]-1Be-1). Mecanismo conferido por busca (Minerals 9, 641; Mineral. Mag. 88)"
  - claim_id: CRQ-SUB-PIRROT-001
    claim: "Pirrotita Fe(1-x)S: 2 Fe3+ e uma vacancia no lugar de 3 Fe2+; 8 FeS + vetor = Fe7S8 (2 Fe3+, 5 Fe2+)."
    risk: fato
    source: "Klein & Dutrow; calculo"
    audit: "verificado em 2026-10-06 (calculo Fe7S8: 2x3 + 5x2 = 16)"
  - claim_id: CRQ-SUB-EDENITA-001
    claim: "Anfibolios: sitio A normalmente vazio recebe Na quando Al entra no lugar de Si (vetor edenita NaAl[]-1Si-1)."
    risk: fato
    source: "Hawthorne et al. (2012)"
    audit: "verificado em 2026-10-06"
  - claim_id: CRQ-SUB-VETOR-001
    claim: "Notacao de vetores de troca (Thompson, 1982): o que sai leva indice negativo; vetor soma-se a formula; carga do vetor = 0; albita + CaAlNa-1Si-1 = anortita."
    risk: conceito
    source: "Thompson (1982), Rev. Mineral. 10"
    audit: "verificado em 2026-10-06 (busca: Thompson 1982, Rev. Mineral. 10, 1-31)"
  - claim_id: CRQ-SUB-CELSIANA-001
    claim: "Ba entra no feldspato K pelo vetor BaAlK-1Si-1 (membro final celsiana BaAl2Si2O8)."
    risk: fato
    source: "Klein & Dutrow; Handbook of Mineralogy"
    audit: "verificado em 2026-10-06"
  - claim_id: CRQ-SUB-RUBI-001
    claim: "Cr3+ substitui Al3+ no corindon (substituicao simples, vetor CrAl-1); e o Cr que da a cor do rubi."
    risk: fato
    source: "Klein & Dutrow"
    audit: "verificado em 2026-10-06"
-->
