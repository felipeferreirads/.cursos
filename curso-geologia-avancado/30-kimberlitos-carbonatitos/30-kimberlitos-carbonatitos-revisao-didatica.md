# Revisão didática: Módulo 30 — Petrologia de kimberlitos e carbonatitos e mineralizações associadas

**Revisado em:** 2026-09-23  ·  **Modo:** review-and-fix
**Material:** `30-kimberlitos-carbonatitos/` (6 aulas e o hub), revisado **depois** da auditoria científica da mesma data (`30-kimberlitos-carbonatitos-auditoria.md`)
**Veredito:** **Bem ensinado com ressalvas**

## Resumo
🔴 0 bloqueiam · 🟠 0 prejudicam · 🟡 9 atrito (todos corrigidos) · 🔵 3 sugestões (não aplicadas)

**Carga estimada** (contagem por script depois da última edição, palavras do corpo a ~84 palavras/min):

| Aula | Palavras | Duração | Blocos de conteúdo | Exemplos trabalhados |
|---|---|---|---|---|
| 01 | 1671 | ~20 min | 4 (histórico; definições; rochas associadas; tabela) | 1 (classificação IUGS A-D) |
| 02 | 1669 | ~20 min | 5 (manto; geoterma; heterogeneidade; metassomatismo; veios) | 1 (janela do diamante, 2 geotermas) |
| 03 | 1579 | ~19 min | 6 (fácies; mineralogia; KIMs; lamproíto/UML/kamafugito; carbonatitos; guia de lâmina) | 1 (lâmina + granada G10) |
| 04 | 1521 | ~18 min | 5 (ressalva da rocha total; maiores e traços; isótopos; três rotas; contínuo) | 1 (εNd(t) de 2 amostras) |
| 05 | 1354 | ~16 min | 6 (ascensão; kimberlito; carbonatito; magma-brine; sítios; supergênico) | 1 (Rayleigh + residual) |
| 06 | 1626 | ~19 min | 5 (transportador; Clifford; ciclo de exploração; carbonatitos; Brasil) | 1 (estoque de diamante e de Nb) |
| **Total** | **9420** | **~112 min** | | 6 |

Nenhuma aula passa de 25 min nem de 2000 palavras. **Nenhuma aula foi dividida.**

## Achados

### 🟡 1. Fo, LREE e HREE usados sem definição na primeira ocorrência
**ID:** `DID-M30-TERMOS-FO-LREE-001`
**Tipo:** termo técnico antes de definido
**Onde:** Aula 02, "O manto que amostramos" ("olivina com Fo em torno de 92-93") e "Metassomatismo" ("assinaturas de LREE altas"); Aula 04, "Elementos maiores e traços" ("LREE em relação a HREE")
**Problema:** São siglas que o aluno avançado provavelmente conhece, mas nenhuma aula anterior do curso as define. A Aula 02 usa Fo para sustentar o argumento da flutuabilidade da quilha.
**Correção aplicada:** apostos curtos: "Fo (teor de forsterita, em % molar)"; "LREE (terras raras leves)"; "HREE (terras raras leves e pesadas)". Nenhum fato novo.
**Escopo:** correção local

### 🟡 2. REE na Aula 05 e ETR na Aula 06 e no hub
**ID:** `DID-M30-A05-ETR-REE-002`
**Tipo:** terminologia inconsistente entre aulas
**Onde:** Aula 05, 10 ocorrências de "REE" no corpo
**Problema:** O mesmo grupo de elementos aparece com duas siglas em aulas vizinhas, e "REE" nunca é expandido. Quem estuda a Aula 06 logo depois pode achar que são coisas diferentes.
**Correção aplicada:** "ETR" no corpo da Aula 05, com "elementos terras raras (ETR; em inglês, REE)" na primeira ocorrência. Os metadados de auditoria mantêm o texto original, como registro.
**Escopo:** correção local

### 🟡 3. Anglicismo "degassing"/"degassa"
**ID:** `DID-M30-A05-DEGASSING-003`
**Tipo:** vocabulário
**Onde:** Aula 05, objetivo e "Diferenciação no kimberlito", item 1
**Correção aplicada:** "desgaseificação" no objetivo; "perde voláteis" no corpo.
**Escopo:** correção local

### 🟡 4. Remissão da equação de Rayleigh a um módulo que não a ensina
**ID:** `DID-M30-A05-REMISSAO-RAYLEIGH-004`
**Tipo:** remissão errada / pré-requisito mal apontado
**Onde:** Aula 05, Fontes ("ver Módulo 26")
**Problema:** O Módulo 26 não trata o fracionamento de Rayleigh. O conceito aparece, na forma qualitativa, no Módulo 27, Aula 04 (zoneamento de Mn em granada). A aula em si é autossuficiente: o exemplo dá a equação e define D e F. Só a remissão mandava o aluno procurar no lugar errado.
**Correção aplicada:** a remissão foi corrigida nas Fontes da Aula 05, e o hub registra a conexão com o Módulo 27.
**Escopo:** correção local

### 🟡 5. Fórmula do εNd não escrita no exemplo que a aplica
**ID:** `DID-M30-A04-FORMULA-ENDT-005`
**Tipo:** salto no exemplo trabalhado (leve)
**Onde:** Aula 04, "Exemplo trabalhado", Passo 2
**Problema:** O Passo 2 aplica a fórmula direto aos números e só remete ao Módulo 26. Com a fórmula escrita, o aluno reconhece o que está sendo calculado.
**Correção aplicada:** uma linha com εNd(t) = [(¹⁴³Nd/¹⁴⁴Nd)amostra(t) / (¹⁴³Nd/¹⁴⁴Nd)CHUR(t) − 1] · 10⁴ (definição do Módulo 26).
**Escopo:** correção local

### 🟡 6. "Websterítica" sem definição; "arqueon" sem o termo inglês e sem o critério de idade
**ID:** `DID-M30-A06-TERMOS-006`
**Tipo:** termo técnico antes de definido
**Onde:** Aula 06, "O diamante não nasce no kimberlito" e "A regra de Clifford e o conceito de arqueon"
**Problema:** "websterítica" é a única das três populações de diamante sem nenhuma pista do que significa. "Arqueon" aparecia como "o cráton estabilizado e com raiz espessa", sem o critério de idade que o define (conferido na auditoria: Janse, 1994, embasamento com mais de 2,5 Ga) e sem o termo *archon*, que é o que o aluno vai encontrar na literatura.
**Correção aplicada:** "websterítica, esta de websterito, piroxenito com orto e clinopiroxênio"; "arqueon (em inglês, *archon*): o cráton com embasamento arqueano, mais velho que 2,5 Ga, e raiz espessa".
**Escopo:** correção local

### 🟡 7. Pipe calculado como cilindro sem aviso
**ID:** `DID-M30-A06-VOLUME-CILINDRO-007`
**Tipo:** exemplo que só funciona no caso mais simples
**Onde:** Aula 06, "Exemplo trabalhado", Alvo 1
**Problema:** A Aula 03 ensina que o diatrema tem forma de cenoura, mas o Alvo 1 multiplica a área de superfície pela profundidade, como se o pipe fosse um cilindro. Sem aviso, o aluno sai com um modo de cálculo que superestima o volume.
**Correção aplicada:** uma frase depois do passo 4 diz que o cilindro superestima o volume de um pipe que se estreita para baixo, e que a modelagem do corpo (passo 4 do ciclo de exploração) corrige isso. Nenhum número mudou.
**Escopo:** correção local

### 🟡 8. Hub com pré-requisito incompleto e sem conexões
**ID:** `DID-M30-HUB-PREREQ-008`
**Tipo:** pré-requisito usado mas não declarado no hub
**Onde:** `30-kimberlitos-carbonatitos-modulo.md`, "Pré-requisitos"
**Problema:** A Aula 02 declara o Módulo 29, Aula 01 (estrutura térmica da litosfera), mas o hub só lista o Módulo 26. As remissões aos Módulos 9, 15, 16, 19, 20-22 e 27 não aparecem em lugar nenhum do hub.
**Correção aplicada:** o hub cita o Módulo 29, Aula 01, como pré-requisito da Aula 02 e ganhou uma linha "Conexões usadas nas aulas". A lista `prerequisites` do `course-state.yaml` **não** foi alterada, porque é decisão curricular e o Módulo 29 já precede o 30 na sequência.
**Escopo:** correção local (hub)

### 🟡 9. Durações declaradas desatualizadas depois da auditoria
**ID:** `DID-M30-DURACOES-009`
**Tipo:** metadado incoerente
**Onde:** cabeçalho e metadados das seis aulas
**Correção aplicada:** recontagem por script (tabela acima). Os cabeçalhos passaram de ~19/18/16/17/16/18 para ~20/20/19/18/16/19 min, com `palavras_corpo` e `duracao_estimada_min` atualizados.
**Escopo:** correção local

### 🔵 10. Visuais na Aula 03
**ID:** `DID-M30-A03-VISUAL-010`
Um esboço das classes de pipe (tipo Kimberley com as três zonas; Fort à la Corne; Lac de Gras) e outro do espinélio em atol (núcleo, "lagoa", borda) fixariam dois pontos que a auditoria corrigiu. **Não aplicado**, porque um desenho feito sem fonte arrisca ensinar geometria errada. Se for feito, deve seguir a Fig. 1 de Scott Smith et al. (2013).

### 🔵 11. A Aula 03 é a mais densa do módulo
**ID:** `DID-M30-A03-CARGA-011`
Tem seis blocos, dezenas de nomes de minerais e um só exemplo, que cobre só o kimberlito. Em ~19 min, fica dentro do limite, e o guia de decisão em lâmina consolida a leitura. **Não dividir agora.** Mas é o **teto**: nenhuma passagem futura deve acrescentar texto a ela sem cortar o equivalente. Se crescer, a divisão natural é Parte 1 (kimberlitos, lamproítos, UML, kamafugitos) e Parte 2 (carbonatitos e seus complexos).

### 🔵 12. Exercício de distinção kimberlito/orangeíto/lamproíto na Aula 01
**ID:** `DID-M30-A01-EXERCICIO-012`
O exemplo da Aula 01 só exercita carbonatitos. A distinção entre kimberlito, orangeíto e lamproíto (objetivo da aula) fica na tabela e só é praticada na Aula 03 (guia e exemplo) e na Aula 04 (isótopos). Isso é aceitável no conjunto do módulo, e o questionário deve cobrar essa distinção (ver plano abaixo). **Não aplicado**: um exercício novo exigiria dados petrográficos que teriam de passar pela auditoria.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| OA-01: classificar kimberlitos, carbonatitos e rochas insaturadas associadas; situar historicamente as definições | a01 (todas as seções); a03 (petrografia e guia de lâmina) | sim (a01 A-D; a03 lâmina) | questionário pendente |
| OA-02: metassomatismo, geotermas e heterogeneidade do manto na geração dos magmas | a02 (todas); a04 (isótopos, três rotas, contínuo) | sim (a02 janela do diamante; a04 εNd) | questionário pendente |
| OA-03: aspectos geológicos, petrográficos, mineralógicos e geoquímicos; processos de diferenciação | a03 (fácies, mineralogia, complexos); a04 (geoquímica); a05 (todas) | sim (a03 granada; a04 εNd; a05 Rayleigh e residual) | questionário pendente |
| OA-04: potencial diamantífero e mineralizações de Nb, ETR e fosfato | a06 (todas); ligação com a03 (KIMs) e a05 (laterização) | sim (a06 estoques) | questionário pendente |

Nenhum objetivo fica sem aula, e nenhuma seção substancial fica sem objetivo. Não há conteúdo órfão.

## Decisão: questionário único ou parciais

**Questionário único cumulativo, sem parciais.**

- **Peso real.** São 6 aulas e ~112 min, o menor arco dos módulos 26-30 (o Módulo 29 tinha ~124 min e ficou com questionário único; os Módulos 26 e 27, com 7 aulas e ~167 min, usaram parciais). A contagem de aulas está na fronteira, mas o volume de estudo não.
- **Arco integrado.** O ponto de dificuldade do módulo (o kimberlito transporta o diamante, mas não o forma) atravessa a02 (janela do diamante), a03 (xenocristal × fenocristal, G10), a05 (ascensão rápida e preservação) e a06 (Clifford, exploração). A classificação da a01 só se fecha com a petrografia da a03 e com os isótopos da a04. Um parcial a01-a03 e outro a04-a06 cortariam exatamente as questões de integração mais valiosas: granada G10 → janela do diamante → regra de Clifford; classificação por lâmina → assinatura isotópica.
- **Carga não justifica divisão.** Nenhuma aula passa de 20 min, e o módulo cabe numa sessão de revisão.

**Orientação de cobertura para o gerador de questionários** (registrada também em `course-state.yaml`, `assessment.plan`):
- **OA-01:** classificação IUGS com **cálculo** (razão CaO/(CaO + MgO + FeO + Fe₂O₃ + MnO) e silicocarbonatito); distinção kimberlito/orangeíto/lamproíto por mineralogia; leitura histórica: Grupos I e II = Smith 1983, orangeíto = Wagner/Mitchell, tuffisítico = nome antigo.
- **OA-02:** **cálculo** da entrada na janela do diamante com a reta de Kennedy e Kennedy, com geoterma, conversão km/GPa e reta dadas no enunciado; metassomatismo modal × críptico; modelo de veios de Foley.
- **OA-03:** leitura de lâmina (guia de decisão); **cálculo** de εNd(t) com CHUR na idade; sequência do carbonatito; Rayleigh com D < 1 e D > 1.
- **OA-04:** **cálculo** de estoque contido (quilates ou Nb), com a ressalva de estoque × reserva; Clifford/archon; tipos de depósito de Nb, ETR e fosfato; panorama brasileiro sem cobrar números de produção exatos.
- **Pelo menos duas questões de integração:** (a) granada G10 (a03) → manto compatível com diamante (a02) → prospecção em cráton (a06), sem confundir indicador com teor; (b) classificação por lâmina (a01 + a03) contra assinatura isotópica (a04), com a lição de Sarkar et al. (2023) de que isótopos sozinhos não classificam a rocha.
- **Restrições:** as 17 restrições do fim do relatório de auditoria são obrigatórias.

## O que está bem feito

Registro para que as próximas passagens **não** estraguem:

1. **O ponto de dificuldade atravessa o módulo.** "O diamante não nasce no kimberlito" é anunciado no hub, preparado na a01 (xenocristais), quantificado na a02 (janela), reconhecido na a03 (G10 não é teor), explicado na a05 (ascensão rápida) e aplicado na a06 (exploração).
2. **Todo exemplo termina com o que ele não prova**: a granada não garante diamante; estoque não é reserva; as faixas isotópicas não são fronteiras rígidas; a geoterma real tem curvatura.
3. **A nomenclatura é tratada como história**, e isso é a ferramenta certa para ler a literatura antiga. Depois da auditoria, a aula também deixa claro qual nome é o antigo e qual é o atual.
4. **As controvérsias aparecem como controvérsias**: o contínuo carbonatito-kimberlito, as três rotas, a transição magma-brine, Bayan Obo e o carbonado.
5. **O paralelo do "fator 3" na a05** (Rayleigh × enriquecimento residual) ensina que processos diferentes produzem números parecidos por razões físicas diferentes.
