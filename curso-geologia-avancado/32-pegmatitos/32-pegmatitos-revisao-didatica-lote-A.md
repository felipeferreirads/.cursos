# Revisão didática: Módulo 32 (Pegmatitos) — LOTE A, Aulas 01–09

**Status:** relatório PARCIAL (lote A de 3). O bloco `didactic_review` do módulo 32 no `course-state.yaml` **não** foi gravado; a consolidação ocorre depois dos lotes B e C.
**Revisado em:** 2026-09-24 · **Modo:** review-and-fix
**Material:** `32-pegmatitos/32-pegmatitos-aula-01` … `-aula-09`
**Ordem:** feita **depois** da auditoria científica do lote A (`32-pegmatitos-auditoria-lote-A.md`), já sobre o texto corrigido.
**Veredito do lote:** **Bem ensinado com ressalvas.** Nenhum defeito didático bloqueia o aprendizado. As ressalvas são carga alta em quatro aulas de vocabulário e catálogo e o limite de 30 min, que as correções factuais tinham estourado e foi restaurado por enxugamento.

## Resumo

🔴 0 bloqueiam · 🟠 6 prejudicam · 🟡 7 atrito · 🔵 3 sugestões. Todos os 🟠 e 🟡 corrigíveis localmente foram corrigidos; D-13 (carga) fica como observação para o orquestrador.

**Carga estimada** (duração = palavras do corpo ÷ 84 palavras/min, mesmo método do redator; valores **após** a revisão):

| Aula | Palavras | Duração | Conceitos novos centrais (aprox.) | Exemplo trabalhado |
|---|---|---|---|---|
| 01 | 2218 | ~26 min | 3 (definição textural, relações de campo, hierarquia) | sim, bom |
| 02 | 2487 | ~30 min | 7–8 (4 zonas, substituição, miarolítica, 3 texturas) | sim, bom |
| 03 | 2536 | ~30 min | 4 (fracionamento, fluxante, camada-limite, exsolução/bolsão) | sim |
| 04 | 2469 | ~29 min | 8+ (grupos minerais + geobarômetro + prévia NYF) | sim |
| 05 | 2444 | ~29 min | 5 (classes, subclasses/tipos, famílias, WMS 2022, indicadores) | sim, reescrito |
| 06 | 2474 | ~30 min | 3 (J&B, subresfriamento/CZR, proposta de Nabelek) | sim, bom |
| 07 | 2517 | ~30 min | 3 (fracionamento, anatexia, imiscibilidade) | sim, bom |
| 08 | 2122 | ~26 min | 3 (fraturamento hidráulico, forma × reologia, localização de fluxo) | sim, bom |
| 09 | 2425 | ~29 min | 6 (geocronômetros + 3 armadilhas + padrões de idade) | sim, reescrito |

## Achados

### 🟠 D-01. Limite de 30 min estourado depois das correções factuais
**Tipo:** sobrecarga / dimensionamento · **Onde:** Aulas 04 (32,4 min), 05 (31,8), 06 (31,2), 07 (31,4), 09 (32,0) antes desta revisão.
**Problema:** as correções da auditoria acrescentaram ressalvas e contrapontos necessários, e cinco aulas passaram do teto de 30 min do curso.
**Correção aplicada:** enxugamento de passagens prolixas **sem** remover conteúdo auditado: repetições de ideias já ditas, frases-ponte longas, apostos redundantes (por exemplo, a lista de nomes antigos da columbita, a história editorial de Wise et al., os parágrafos de "Materiais de referência" e "Pb comum" da Aula 09). Todas voltaram a ≤30 min. Os campos `Duração estimada` do cabeçalho e `duracao_estimada_min`/`palavras_corpo` do rodapé foram sincronizados.
**Escopo:** correção local.

### 🟠 D-02. A abertura da Aula 07 contradiz a definição da Aula 01
**Tipo:** inconsistência que ensina modelo errado · **Onde:** Aula 07, "Uma pergunta anterior à da Aula 06".
**Problema:** "um pegmatito é, **por definição textural** (Aula 01), a fração mais evoluída e tardia de um sistema granítico". A Aula 01 insiste que a definição é textural e **não** genética. O aluno recebe duas definições incompatíveis bem no ponto em que o curso vai discutir origens não graníticas.
**Correção aplicada:** "a associação de campo com granitos (Aula 01) sugere… Mas a definição de pegmatito é textural, não genética…". **Escopo:** local.

### 🟠 D-03. Contradição interna na seção de Thomas & Davidson (Aula 07)
**Tipo:** inconsistência interna · **Onde:** Aula 07, parágrafo de abertura da proposta e 3º bullet.
**Problema:** o texto dizia que o modelo explica a evolução "sem um salto composicional abrupto" e, dois parágrafos depois, que "a desmistura permite um salto composicional relativamente abrupto".
**Correção aplicada:** a abertura passou a "como o sistema passa do fundido granítico 'comum' ao fundido pegmatítico extremamente enriquecido". **Escopo:** local.

### 🟠 D-04. Pré-requisito da Aula 01 aponta para a aula errada
**Tipo:** pré-requisito mal declarado · **Onde:** cabeçalho da Aula 01.
**Problema:** "datação que vai aparecer a partir da Aula 06". A datação aparece na Aula 09. O Módulo 29 era chamado de "petrologia de granitos", mas o título real é "Granitos no ciclo de Wilson".
**Correção aplicada:** "Módulo 29 (granitos no ciclo de Wilson) e Módulo 27 (petrocronologia), para o vocabulário de granitos e fontes de fundido (Aulas 05–07) e de datação isotópica (Aula 09)". **Escopo:** local.

### 🟠 D-05. Termos de geocronologia usados sem definição no exemplo da Aula 09
**Tipo:** termo técnico antes de definido · **Onde:** Aula 09, exemplo trabalhado ("intersecção inferior da discórdia"). O texto só dizia "o chamado 'discordance'".
**Problema:** o exemplo depende de concórdia, discórdia e intersecção, que a aula nunca explica. O Módulo 27 cobre o tema, mas a aula não fazia a ponte e ainda usava o termo em inglês.
**Correção aplicada:** um aposto na seção de metamictização: idades ²⁰⁶Pb/²³⁸U e ²⁰⁷Pb/²³⁵U que não coincidem, pontos fora da concórdia, a reta chamada discórdia e suas intersecções, com remissão ao Módulo 27. **Escopo:** local.

### 🟠 D-06. Salto de inferência no exemplo trabalhado da Aula 03
**Tipo:** salto no exemplo · **Onde:** Aula 03, passo 1.
**Problema:** o passo concluía que B₂O₃ e F altos nas inclusões são "coerentes com o mecanismo de **camada-limite**". Uma inclusão mostra enriquecimento do fundido residual, mas não distingue enriquecimento local (camada-limite) de enriquecimento do fundido inteiro. É exatamente a distinção que a aula acabou de ensinar.
**Correção aplicada:** "(compatível com uma camada-limite, mas sem prová-la — a inclusão não diz se o enriquecimento era local ou do fundido inteiro)". **Escopo:** local.

### 🟡 D-07. Remissões cruzadas erradas
**Onde:** Aula 06 ("unidades de substituição descritas na Aula 03", duas vezes) e Aula 09 ("zona de substituição tardia (Aula 03)"). Unidades de substituição são da Aula 02. **Corrigido** (parte já na auditoria).

### 🟡 D-08. Meta-texto de pipeline no corpo da aula
**Onde:** Aula 06 ("esse julgamento cabe à **auditoria científica**") e Aula 05 ("sinalizados para verificação … na auditoria científica"). Para o aluno, "a auditoria" é um termo sem referente. **Removido** nas duas aulas.

### 🟡 D-09. Frase agramatical na Aula 04 (polucita)
"devem justamente a essa sigla ('Cs' no meio de 'Li-Cs-Ta') à presença de polucita" passou a "são arquétipos de pegmatito Li-Cs-Ta justamente por conterem polucita em quantidade explotável". **Corrigido.**

### 🟡 D-10. Erro de concordância na Aula 08
"é o assinatura clássica" passou a "é a assinatura clássica". **Corrigido.**

### 🟡 D-11. Cabeçalho × rodapé de duração divergentes
Aula 01 (24 × 26), Aula 04 (27 × 29), Aula 08 (27 × ~25). **Sincronizados** junto com D-01.

### 🟡 D-12. Prolixidade pontual
Parágrafos de abertura das Aulas 03, 04, 06, 07 e 09 com apostos que repetiam a ideia da frase anterior (exemplos: "um trabalho de síntese que se tornou o padrão de citação do campo"; "um caso histórico único de produtividade nomenclatural mineralógica"; o parágrafo de "Pb comum"). **Enxugados** junto com D-01, preservando a voz.

### 🟡 D-13. Carga cognitiva alta em aulas de vocabulário e catálogo (não corrigido, só reportado)
**Onde:** Aulas 02 (7–8 conceitos), 04 (8+ grupos minerais), 05 (5 blocos densos) e 09 (6 geocronômetros e armadilhas).
**Avaliação:** acima do limiar de 3–4 ideias independentes, mas são aulas de vocabulário com estrutura paralela (cada grupo mineral e cada geocronômetro segue o mesmo molde), recap consolidador e exemplo trabalhado que integra tudo. Isso mitiga a sobrecarga. **Não recomendo dividir**, porque o módulo já tem 26 aulas. Recomendo em vez disso que o **questionário parcial 1 (Aulas 01–05)** reserve questões de reconhecimento e aplicação para as Aulas 02 e 04, não só para a 05, e que os flashcards cubram os grupos minerais com cards atômicos. **Escopo:** decisão do orquestrador; nada foi alterado.

### 🔵 S-1. Aula 04 — esboço do diagrama P-T espodumênio–petalita–eucriptita
Um esquema qualitativo dos três campos (Pet + Qtz em T alta/P baixa; Spd + Qtz em P alta; Ecr + Qtz em P e T baixas, <~320 °C e <~1,6 kbar) com a seta do resfriamento isobárico (Pet → Spd + Qtz) tornaria concreto o parágrafo mais denso da aula. Os dados estão conferidos na fonte primária (London 1984, Fig. 1).

### 🔵 S-2. Aula 05 — tabela-resumo das classes
Uma tabela com classe, fácies, P aproximada, subclasses e família associada substituiria bem a lista numerada. Os valores já estão verificados na auditoria (A05-3).

### 🔵 S-3. Aula 06 — quadro comparativo dos três modelos
Colunas J&B / London (CZR) / Nabelek et al. e linhas "meio de baixa viscosidade", "quando surge", "papel da H₂O", "papel de B-P-F-Li" e "evidência invocada". Isso materializaria a frase-chave da aula ("não é 'a água importa ou não', mas onde e quando") e ajudaria a manter visível que nenhum dos três é consenso.

## Cobertura de objetivos (lote A)

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `m32-oa01` zonamento, texturas, fracionamento/fluxantes/fluidos | Aulas 01 (definição/campo), 02 (zonas e texturas), 03 (química) | sim (A01, A02, A03) | — (questionário pendente; parcial 1) |
| `m32-oa02` assembleias minerais e classificação (Černý & Ercit; WMS 2022; indicadores) | Aulas 04 e 05 | sim (A04, A05) | — (parcial 1) |
| `m32-oa03` teorias de gênese e mecanismos de alojamento | Aulas 06, 07, 08 | sim (A06, A07, A08) | — (parcial 2) |
| `m32-oa05` geocronômetros, idade × granito parental, **debate de taxas** | Aula 09 (geocronômetros e idades); a parte "debate de taxas" fica na **Aula 10** (lote B) | sim (A09) | — (parcial 2) |

Nenhum objetivo do lote ficou sem seção que o ensine. Não há conteúdo órfão relevante. A seção de *line rock* e cristais gigantes da Aula 02 serve ao oa01.

## O que está bem feito (preservar)

- **Exemplos trabalhados como "exercício de classificação guiada":** relatório de mapeamento (Aula 01), testemunho de sondagem (Aula 02), corpo zonado lido pela mineralogia (Aula 04), campo A–E (Aula 05). Cada um obriga o aluno a aplicar o vocabulário recém-aprendido a dados concretos. É o melhor recurso didático do lote.
- **Aula 06, exemplo X × Y:** mostra que os dois modelos preveem o mesmo resultado observável por mecanismos diferentes e explica por que isso impede de fechar o debate com dados de campo simples. É didática de controvérsia bem feita.
- **Separação "o quê" × "porquê":** as Aulas 02 e 04 apresentam fatos (cristais gigantes, zonas) e adiam explicitamente o mecanismo para as Aulas 06–07. Reforçado na revisão com a correção do núcleo de quartzo (A02-1).
- **Seções "O que cada modelo prevê para a exploração" (Aula 07) e o passo 5 do exemplo da Aula 05:** conectam teoria e decisão prática.
- **Recaps:** destilam em vez de repetir. O da Aula 05 foi o único que precisou de ajuste (direção dos indicadores, A05-8 da auditoria).

## Observações para os lotes B e C e para a avaliação

- **Aula 10:** abrir retomando a pergunta que a Aula 09 agora deixa explícita ("a diferença U-Pb × Ar-Ar mede resfriamento regional, não duração da cristalização") e a que a Aula 06 deixa em aberto ("quão curtas são as escalas de tempo?"). A ponte já está escrita dos dois lados.
- **Limite de 30 min:** as aulas do lote A estão no teto (~30 min). Se a consolidação exigir acrescentar ressalvas nelas, será preciso enxugar em paralelo.
- **Questionário e flashcards (quando gerados):** priorizar as seis inversões listadas na auditoria (monazita não metamítica; Trebilcock/44069 = monazita; Pet = Spd + 2 Qtz e Spd = Ecr + Qtz; classe ≠ tipo; "espodumênio secundário"; paradoxo não resolvido). São os pontos em que um aluno que leu uma versão antiga, ou que raciocina por intuição, erraria.
- **Nomenclatura na avaliação:** usar columbita-(Fe) e tantalita-(Mn) com o nome antigo entre parênteses. Cobrar a distinção classe × tipo × família.
