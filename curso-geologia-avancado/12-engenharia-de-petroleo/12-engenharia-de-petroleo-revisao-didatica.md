# Revisão didática: Módulo 12 — Engenharia de petróleo

**Revisado em:** 2026-09-02  ·  **Modo:** `review-and-fix`
**Material:** `12-engenharia-de-petroleo/` — 5 aulas (a01 a a05)
**Veredito:** **Bem ensinado com ressalvas**

## Resumo

🔴 0 bloqueiam · 🟠 1 prejudica · 🟡 0 atrito · 🔵 1 sugestão

**Carga estimada:** conceitos novos por aula: 4–6 (dentro da faixa já estabelecida pelo curso
para módulos avançados, ~1980–2060 palavras de corpo em todas as cinco aulas — a dispersão entre
elas é de apenas 4%, a mais uniforme do curso até agora) · pré-requisitos reativados: 1 externo
(Módulo 11, Aula 02 — vocabulário de perfil sônico/densidade) · exemplos trabalhados: 5, um por
aula, todos quantitativos · duração estimada: ~30 min por aula, consistente com o padrão do curso.

Esta auditoria didática rodou **depois** da auditoria científica (veredito aprovado, 1 achado
laranja bibliográfico já corrigido) e não encontrou nenhum problema factual — os dois achados
abaixo são puramente pedagógicos.

## Achados

### 🟠 1. Dois dos três objetivos declarados da Aula 02 não tinham demonstração numérica

**claim_id:** `DID-M12-A02-EXEMPLO-001`
**Tipo:** exemplo insuficiente / desalinhamento objetivo–demonstração
**Onde:** a02 · "Ao final você vai conseguir" (cabeçalho) + "Exemplo trabalhado"
**Problema:** o cabeçalho da a02 promete três habilidades de cálculo: "identificar zonas
reservatório e **estimar seu volume de argila** a partir do perfil de raios gama; **calcular
porosidade** a partir da combinação nêutron-densidade; e **aplicar a equação de Archie** para
estimar a saturação de água". O corpo da aula explica as três fórmulas (IGR, φD, Archie) com
clareza — mas o único "Exemplo trabalhado" da aula demonstrava **apenas a terceira** (Sw/Sh por
Archie), com φ = 0,20 entregue pronto no enunciado, sem mostrar de onde esse número viria na
prática. Um leitor que segue o exemplo até o fim sabe aplicar Archie com números já dados, mas
nunca praticou os dois primeiros cálculos que o próprio cabeçalho prometeu — e é justamente o
tipo de assimetria que um questionário de aplicação (não só de definição) expõe depois, na hora
de avaliar oa02. Como as outras quatro aulas do módulo mantêm a disciplina de um exemplo que
cobre o(s) objetivo(s) de cálculo declarado(s) por inteiro (a01: pressão hidrostática completa;
a03: OOIP completo; a04: J e extrapolação completos; a05: ganho de EOR completo), a a02 destoava
do próprio padrão do módulo.
**Correção aplicada:** o "Exemplo trabalhado" foi reestruturado em três itens (a, b, c) sobre o
**mesmo** intervalo de rocha, na ordem em que os cálculos acontecem na prática profissional: (a)
GR = 25 API contra GRmin/GRmax fecha IGR = 0,05 (zona limpa, justificando o uso da forma de
Archie sem correção de argila); (b) densidade (ρformação = 2,32 g/cm³) e nêutron (NPHI = 0,21)
convergem para φ ≈ 0,20, sem afastamento de gás; (c) esse mesmo φ = 0,20 alimenta o cálculo de
Archie que já existia, preservado sem alteração de método ou de resultado. Nenhum fato novo foi
introduzido — os números são ilustrativos (como os demais exemplos do módulo, ex. Rw = 0,05,
Rt = 20), e as fórmulas usadas (IGR, φD) já estavam auditadas no corpo da própria aula. A
"Situação" foi reescrita para fornecer os dados de entrada dos três cálculos de uma vez, e a
"Resolução" ganhou os itens (a) e (b) antes do (c), que é o texto original.
**Escopo:** correção local, dentro do próprio exemplo trabalhado — não exigiu dividir a aula nem
criar conteúdo novo fora do que as fórmulas já auditadas permitem calcular.

### 🔵 2. "Interpretar um relatório PVT básico" fica só no plano conceitual

**Tipo:** sugestão (oportunidade de reforço, não defeito)
**Onde:** a03 · "Ao final você vai conseguir" + "PVT: como o fluido se comporta ao sair do
reservatório"
**Observação:** a a03 promete "interpretar um relatório PVT básico (Bo, Rs)". O corpo entrega
isso bem no nível conceitual — define Bo e Rs, explica o comportamento de cada um acima e abaixo
do ponto de bolha, e ilustra com um diagrama esquemático (Bo subindo até Pb, caindo depois; Rs
constante até Pb, caindo depois). O "Exemplo trabalhado" da a03, no entanto, usa Bo como dado de
entrada já pronto (1,25 bbl/STB "de análise PVT") para o cálculo de OOIP, sem pedir para o
leitor **ler** esse valor de uma tabela ou gráfico PVT — a habilidade de interpretação fica
demonstrada por explicação, não por prática. Isso é mais leve que o achado 1 (aqui o objetivo é
"interpretar", um verbo de reconhecimento, não "calcular"), e a explicação textual é sólida o
suficiente para não bloquear nem prejudicar o aprendizado — por isso fica como sugestão, não
como achado corrigido nesta passagem. **Não corrigido.** Se o gerador de questionários quiser
avaliar essa habilidade de fato, uma questão de aplicação do tipo "dado este ponto do gráfico Bo
× pressão, o reservatório está acima ou abaixo do ponto de bolha, e o que isso implica para a
extrapolação de J na a04" cobriria o objetivo sem exigir mudança na aula.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Situação após esta revisão |
|---|---|---|---|
| `geologia-avancado-m12-oa01` — perfuração e completação de poço | a01, inteira | sim (pressão hidrostática/janela operacional) | coberto por inteiro |
| `geologia-avancado-m12-oa02` — perfis geofísicos (porosidade, saturação, litologia) | a02, inteira | sim, agora as três frentes (Vsh, porosidade, Sw) | coberto por inteiro (achado 1 corrigido) |
| `geologia-avancado-m12-oa03` — propriedades de rocha/fluido, mecanismos de produção, FR | a03 (propriedades, PVT, OOIP) + a04 (mecanismos, testes de poço, IP/IPR) | sim em ambas (OOIP; J/IPR) | coberto por inteiro, sem corte no meio |
| `geologia-avancado-m12-oa04` — recuperação secundária e avançada | a05, inteira | sim (ganho de EOR sobre OOIP/FR da a03) | coberto por inteiro |

Nenhum objetivo sem seção que o ensine e nenhuma seção órfã — a seção de "Gestão de
reservatórios" ao final da a05, embora não amarrada a um objetivo mensurável específico, funciona
como síntese de fechamento do módulo inteiro (mesmo papel que a a06 cumpriu no Módulo 11), não
como conteúdo solto.

## Cadeia de pré-requisitos

Verificada aula a aula: a01 assume apenas noção de bacia sedimentar/gradiente do Módulo 10 (sem
pré-requisito interno); a02 assume a01 (construção do poço) **e** declara explicitamente a
dependência externa do Módulo 11 Aula 02 (vocabulário de sônico/densidade), sem redefini-lo —
verificado termo a termo pela auditoria científica, sem conflito; a03 assume a02 (porosidade e
Sw por Archie); a04 assume a03 (OOIP, Bo, Rs, ponto de bolha); a05 assume a04 (mecanismos de
produção, injeção de água, FR). Cadeia linear e limpa, cada aula nomeando o que consome da
anterior — nenhum salto de pré-requisito encontrado, o defeito mais comum e mais grave nas
revisões anteriores deste curso.

## O que está bem feito

- A cadeia de herança numérica a03→a05 é um dos melhores exemplos do curso de como amarrar um
  cálculo entre aulas: a05 abre o exemplo trabalhado citando "o mesmo reservatório da Aula 03
  (OOIP = 19.115.712 STB)" — nome explícito da aula de origem e do número exato, sem obrigar o
  leitor a procurar. O ganho de EOR é comparado ao ganho da secundária isolada em barris
  absolutos, não só em pontos percentuais, o que é exatamente a forma como a decisão de negócio
  é tomada na prática.
- Todas as cinco aulas mantêm a mesma disciplina de um "Exemplo trabalhado" que ataca o
  objetivo de cálculo central da aula até o fim, com interpretação do resultado em vez de parar
  no número — inclusive as extrapolações de sensibilidade (m = 1,8 na a02; Bo = 1,35 na a03; FR
  primária isolada na a05) que testam se o leitor entende **por que** o número muda, não só que
  mudou.
- A ressalva de nomenclatura da a04 (quatro mecanismos "clássicos" vs. a expansão de rocha e
  fluido como possível quinto, conforme Ahmed) é um modelo de como sinalizar imprecisão de
  convenção sem confundir o leitor — isolada num parágrafo próprio, depois da lista principal já
  fechada, exatamente onde não atrapalha a primeira leitura.
- O bloco "Encerramento do módulo" ao final da a05 amarra as cinco aulas numa única frase por
  aula, o mesmo padrão de fechamento que funcionou bem no Módulo 11 (a06) — dá ao leitor o mapa
  de onde cada peça se encaixou antes de seguir para o próximo módulo.
- Nível de registro consistente entre as cinco aulas — mesma densidade de termo técnico
  destacado, mesma disciplina de definir por aposto na primeira ocorrência ("net pay — a
  espessura efetivamente porosa..."; "skin factor, s — um dano ou melhoria localizada..."), sem
  nenhum termo central usado antes de ser definido.
- Densidade de conceitos por aula extremamente uniforme (1980–2060 palavras de corpo, 4% de
  dispersão) — nenhuma aula do módulo ficou desproporcionalmente mais pesada ou mais leve que as
  outras quatro, ao contrário do padrão irregular que abriu achados em módulos anteriores.

## Decisão sobre questionário: único ou parciais

**Decisão: questionário único.**

O módulo tem 5 aulas — está na faixa (4-5 aulas) que este curso trata por padrão com
questionário único, e não na faixa de 6+ aulas que aciona a consideração de parciais (precedente
explícito nos Módulos 06, 08 e 09, todos de 6 aulas, contra os Módulos 02, 03, 04, 07 e 10, de
4-5 aulas, todos únicos). Isso já bastaria, mas a estrutura de objetivos reforça a mesma
conclusão por um caminho independente: o único ponto do módulo onde um corte poderia parecer
natural é entre a02 e a03 (fim da perfilagem, início das propriedades de reservatório) — e é
exatamente aí que um corte **preservaria** os quatro objetivos inteiros de cada lado (oa01+oa02
de um lado; oa03, que se estende por a03 e a04, e oa04 de a05, do outro). Não há, portanto,
nenhum corte que *force* a divisão por causa de um objetivo partido ao meio — o critério que
levou os Módulos 06/08/09 a adotar parciais neste curso. Com 5 aulas e nenhuma pressão estrutural
de objetivo, o módulo fica com o padrão default: **um questionário único, cumulativo, cobrindo
os quatro objetivos de aprendizagem.**
