# Revisão didática: Módulo 31 — Rochas ígneas alcalinas: petrologia e mineralizações

**Revisado em:** 2026-09-24  ·  **Modo:** review-and-fix
**Material:** `31-rochas-igneas-alcalinas/` (7 aulas e o hub), revisado **depois** da auditoria científica da mesma data ([[31-rochas-igneas-alcalinas-auditoria]]).
**Veredito:** **Bem ensinado com ressalvas**

## Resumo
🔴 0 bloqueiam · 🟠 1 prejudica · 🟡 8 atrito · 🔵 3 sugestões

**Carga estimada** (recontada por script depois da última edição; palavras do corpo, de "## Conteúdo" a "## Fontes", a ~84 palavras/min):

| Aula | Palavras | Duração | Conceitos novos centrais | Exemplos |
|---|---|---|---|---|
| 01 | 1783 | ~21 min | 4 (três sentidos de "alcalino"; Shand; QAPF inferior; TAS e clãs) + topônimos | 1 (classificação) |
| 02 | 1813 | ~22 min | 3 (grau de fusão e pressão; metassomatismo; ambientes) | 1 (dois cenários) |
| 03 | 1599 | ~19 min | 3 (plano crítico; hiato de Daly; imiscibilidade) | 1 (suíte com hiato) |
| 04 | 1682 | ~20 min | 3 (spidergram e ETR; componentes mantélicos; fusão em lote, Rayleigh e AFC) | 1 (cálculo) |
| 05 | 1954 | ~23 min | 3 (IA e peralcalinidade; miaskítico × agpaítico; minerais exóticos e depósitos) | 1 (cálculo) |
| 06 | 1843 | ~22 min | 3 (cumulatos; lamprófiros; ultrapotássicas) | 1 (cálculo) |
| 07 | 1921 | ~23 min | 3 (associação carbonatito-silicato; zoneamento; Plataforma Sul-Americana) | 1 (furo) |
| **Total** | **12.595** | **~150 min** | | 7 |

O total subiu de ~132 min, na redação, para **~150 min**. A auditoria acrescentou texto em 05, 06 e 07 (índice agpaítico, critérios de Foley, rotas do carbonatito, províncias brasileiras). Nenhuma aula passa de 25 min nem de 2.000 palavras, mas as Aulas 05 e 07 estão **no teto** (ver 🔵 10).

## Achados

### 🟠 1. Objetivo da Aula 07 copiado do OA04, com uma parte que a aula não ensina

**Tipo:** objetivo não coberto (cabeçalho desalinhado)
**Onde:** Aula 07 · cabeçalho, "Objetivo"
**Problema:** O objetivo era o texto do `oa04` ("distinguir as séries miaskítica e agpaítica e relacionar..."), mas a distinção miaskítica/agpaítica é ensinada na Aula 05. A Aula 07 ensina outra coisa: associação carbonatito-silicato, zoneamento e contexto regional. Quem lê o cabeçalho espera um conteúdo que não vem, e o "Ao final você vai conseguir" da própria aula não bate com o objetivo.
**Correção aplicada:** Objetivo reescrito para o que a aula ensina, com a remissão explícita: "parte do objetivo `oa04`; a distinção miaskítica/agpaítica foi ensinada na Aula 05 e é aplicada aqui".
**Escopo:** correção local

### 🟡 2. Termos usados antes de definidos

**Tipo:** termo indefinido na primeira ocorrência
**Onde:** Aula 01 ("normativos"); Aula 02 ("ETR leves", sigla sem introdução); Aula 04 ("elementos de alto campo de força", definido só na Aula 05)
**Correção aplicada:** Apostos curtos: "normativo = mineral calculado a partir da análise química de rocha total pela norma CIPW, e não observado na lâmina"; "elementos terras raras (ETR) pesadas"; "(HFSE, cátions pequenos e de carga alta, como Nb, Ta, Zr, Hf e Ti)". São definições, sem fato novo.
**Escopo:** correção local

### 🟡 3. "Um magma-fonte mantélico [...] funde em lote"

**Tipo:** termo que ensina modelo errado (o que funde é a fonte, uma rocha; o magma é o produto)
**Onde:** Aula 04 · "Exemplo trabalhado", Situação
**Correção aplicada:** "Uma fonte mantélica (manto metassomatizado, Aula 02) funde em lote".
**Escopo:** correção local

### 🟡 4. Revisão de texto

**Tipo:** atrito (erros de digitação e de concordância)
**Onde e correção aplicada:** Aula 01: "Uma sienogranito peralcalino" → "Um granito peralcalino". Aula 02: "amfibolíticos" (2×) → "anfibolíticos"; "manho" → "manto"; "hidrosalinos" → "hidrossalinos"; "apatito" → "apatita" (padrão do curso); "Rifte Ativo do Leste Africano" → "Sistema de Riftes do Leste Africano". Aula 05: "uma intercrescimento" → "um intercrescimento". Os erros de digitação da Aula 01 ("córindon", "uma clinopiroxenito", "a fonolito") e da Aula 03 ("distribição", "cinéticamente") já saíram nas edições da auditoria.
**Escopo:** correção local

### 🟡 5. Pré-requisitos do Módulo 30 não declarados

**Tipo:** salto de pré-requisito (leve: o Módulo 30 precede este na trilha)
**Onde:** Aulas 04 e 06 (cabeçalho); hub
**Problema:** A Aula 04 usa Rayleigh "já usada no Módulo 30", e a Aula 06 retoma lamproítos, kamafugitos, lamprófiros ultramáficos e a APIP "sem reensinar". Nenhuma das duas declarava o Módulo 30, e o hub só lista o 26.
**Correção aplicada:** Pré-requisitos das Aulas 04 (Módulo 30, Aula 05) e 06 (Módulo 30); linha "Conexões usadas nas aulas" no hub. O campo `prerequisites` do estado **não** foi alterado: é decisão curricular, e o 30 já precede o 31 (mesma conduta do Módulo 30, DID-M30-HUB-PREREQ-008).
**Escopo:** correção local

### 🟡 6. Durações do cabeçalho divergentes dos metadados

**Tipo:** atrito (informação de planejamento errada para o aluno)
**Onde:** cabeçalhos das sete aulas (24, 25, 22, 23, 22, 21 e 20 min) contra os metadados (21, 20, 19, 21, 18, 17 e 16)
**Correção aplicada:** Recontagem por script depois da última edição. Cabeçalho, `palavras_corpo` e `duracao_estimada_min` foram sincronizados: 21, 22, 19, 20, 23, 22 e 23 min.
**Escopo:** correção local

### 🟡 7. Exemplo da Aula 06: título do passo e "potássica comum"

**Tipo:** atrito
**Onde:** Aula 06 · "Exemplo trabalhado"
**Correção aplicada:** "Passo 2 — calcular a razão K₂O/Na₂O (molar e em % peso)", coerente com o tratamento do 🔵 26 da auditoria; "rocha potássica comum (não ultrapotássica)" → "rocha potássica, mas não ultrapotássica".
**Escopo:** correção local

### 🟡 8. "A Aula 03 (em duas partes)"

**Tipo:** atrito (remissão ambígua depois da divisão)
**Onde:** Aula 02 · "Próxima aula"
**Correção aplicada:** "As Aulas 03 e 04 (Partes 1 e 2 do mesmo tema) acompanham...". A Aula 04 dizia "A Aula 05 (em duas partes)", o que foi corrigido na auditoria (🟠 8).
**Escopo:** correção local

### 🟡 9. OA03: a "química mineral" não entra em nenhuma modelagem

**Tipo:** objetivo parcialmente coberto
**Onde:** `oa03` ("Interpretar dados geoquímicos elementais e isotópicos **e de química mineral** em modelagens petrogenéticas") contra as Aulas 03 e 04
**Problema:** A química mineral aparece de forma qualitativa: na Aula 05, para decidir miaskítico × agpaítico; na Aula 06, com kaersutita e clinopiroxênio titanífero. Nenhuma aula a usa **numa modelagem** (termometria, coeficientes de partição mineral/líquido medidos, zoneamento de clinopiroxênio).
**Correção:** **não aplicada.** Exige conteúdo novo, que teria de passar pelo auditor, e as Aulas 04 e 05 estão perto do teto. **Restrição para a avaliação:** não cobrar modelagem quantitativa com química mineral. Cobrar só o uso qualitativo (assembleia acessória, anfibólio/piroxênio diagnóstico) e o D mineral/líquido como parâmetro dado no enunciado de Rayleigh.
**Escopo:** exige nova seção ou aula. Decisão curricular do orquestrador. Não bloqueia.

### 🔵 10. Aulas 05 e 07 no teto de densidade

A Aula 05 tem 1.954 palavras e a 07 tem 1.921, ambas perto do limite de 2.000. **Nenhuma passagem futura deve acrescentar texto a elas sem cortar equivalente.** Se a 07 precisar crescer, dividir em Parte 1 (associação e zoneamento) e Parte 2 (Plataforma Sul-Americana).

### 🔵 11. Apoio visual

Dois esboços ajudariam: (a) o triângulo inferior do QAPF e o TAS com os campos alcalinos (Aula 01); (b) um corte de complexo alcalino-carbonatítico zonado, com a mineralização por zona (Aula 07). Se forem feitos, seguir Le Maitre (2002) e Le Bas et al. (1986) para (a) e a zonação corrigida na auditoria (🟠 22) para (b).

### 🔵 12. Aula 01 densa em vocabulário

São quatro eixos conceituais e cerca de quinze nomes de rocha e topônimos numa aula de ~21 min. Está dentro do limite, e o fio dos "três sentidos de alcalino" organiza bem o conjunto. O baralho deve **separar** topônimos de definições (um card por nome) e não cobrar a lista inteira de uma vez.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `oa01` classificar e nomear por clãs (IUGS) e histórico | Aula 01 (inteira); Aula 05 (índice e séries); Aula 06 (cumulatos, lamprófiros) | sim (Aulas 01 e 05) | pendente |
| `oa02` geração: fonte, metassomatismo, fusão, tectônica | Aula 02 (inteira); Aula 06 (ultrapotássicas, APIP) | sim (Aulas 02 e 06) | pendente |
| `oa03` geoquímica elemental/isotópica e modelagem | Aulas 03 e 04; química mineral só qualitativa (🟡 9) | sim (Aulas 03 e 04, com cálculo) | pendente |
| `oa04` miaskítico × agpaítico; ETR e HFSE | Aula 05; Aula 07 (zoneamento e depósitos) | sim (Aulas 05 e 07) | pendente |

## Decisão sobre a avaliação: questionários parciais + final cumulativo

**Decisão:** **dois parciais e um final cumulativo**, sem questionário único.

- **Parcial 1: Aulas 01-04** (classificação, geração, evolução, geoquímica e modelagem; `oa01`, `oa02`, `oa03`). Um bloco teórico e quantitativo: Shand/TAS, grau de fusão e pressão, plano crítico, hiato de Daly, fusão em lote, Rayleigh, componentes mantélicos.
- **Parcial 2: Aulas 05-07** (famílias de rochas e mineralizações; `oa01`, `oa02`, `oa04`). Índice agpaítico e assembleia, ultrapotássicas, lamprófiros, associação carbonatito-silicato, zoneamento e províncias brasileiras.
- **Final cumulativo, curto**, centrado em integração: (a) fonte metassomatizada (Aula 02) → baixo grau de fusão e Rayleigh (Aula 04) → concentração de HFSE e ETR e assembleia agpaítica (Aula 05); (b) rotas do carbonatito (Aula 03 e Módulo 30) → zoneamento e mineralização por zona (Aula 07).

**Por quê.**
1. **Peso real.** São 7 aulas e **~150 min** depois da auditoria, e não os ~132 min da redação. Isso é mais perto dos Módulos 26 e 27 (7 aulas, ~167 min, com parciais) que dos Módulos 29 (~124 min, único) e 30 (6 aulas, ~112 min, único).
2. **Três cálculos distintos** (fusão em lote com Rayleigh, índice agpaítico, razões das ultrapotássicas), mais o exemplo de classificação da Aula 01. Num único questionário, ou os cálculos expulsam a parte conceitual, ou o questionário fica longo demais.
3. **Costura natural entre a 04 e a 05:** processos (como o magma nasce e evolui) contra produtos (que rochas e que depósitos resultam). É diferente do Módulo 30, em que o ponto de dificuldade atravessava todas as aulas e cortar destruiria as questões de integração. Aqui, a integração cabe no final cumulativo.
4. **Carga de restrições.** A auditoria deixou 20 restrições obrigatórias, e várias pedem distinções finas (IA × assembleia; imiscibilidade × cristalização fracionada; Ponta Grossa × Poços de Caldas–Cabo Frio). Dividir reduz o risco de o gerador violar uma delas.

**Restrições para quem gerar a avaliação:** as 20 do fim do relatório de auditoria, **mais**: (21) não cobrar modelagem quantitativa com química mineral (🟡 9); (22) nos cálculos, dar no enunciado as equações e, nas ultrapotássicas, os três filtros, sem exigir que o aluno escolha a base da razão; (23) não cobrar desenhos (os visuais do 🔵 11 não existem).

## O que está bem feito

Registrado para que as próximas revisões **não estraguem**:
1. **O fio dos três sentidos de "alcalino"** (Aula 01) é retomado nas Aulas 04 e 05. É o melhor antídoto para a confusão que o hub aponta como ponto de dificuldade, e agora se estende ao índice agpaítico: química abre a porta, mineralogia classifica.
2. **Todo exemplo termina com "O que fixar"**, e três deles (Aulas 03, 05 e 06) dizem o que o dado **não** prova.
3. **A escada quantitativa entre módulos:** Rayleigh do Módulo 30 → fusão em lote e Rayleigh na Aula 04 (mesmo fator 3,14) → índice agpaítico na Aula 05 → razões das ultrapotássicas na Aula 06.
4. **As pontes com o Módulo 30** reaproveitam sem repetir. A auditoria alinhou as rotas do carbonatito, a sequência carbonatítica e as ETR por zona.
5. **Controvérsias marcadas como tais:** hiato de Daly, rota dominante do carbonatito, pluma de Trindade, EM1 × HIMU.

## Arquivos alterados nesta revisão

As sete aulas (cabeçalhos, durações e edições locais listadas acima) e o hub (status, conexões, registro e ponto de dificuldade). Questionário e flashcards não existem e **não** foram tocados.
