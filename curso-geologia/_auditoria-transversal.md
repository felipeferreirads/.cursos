# Auditoria transversal — Curso de Geologia

**Data:** 2026-08-16
**Modo:** `audit-and-fix` · **Profundidade:** `cross-course`
**Escopo:** módulos **00, 01, 02 e 03** — os quatro que têm aulas escritas no contrato `iniciante-absoluto-v1`. Os módulos 04 a 30 ainda não têm aulas e não entram.
**Total auditado:** 28 aulas · **189 alegações auditáveis** declaradas.

> [!warning] Este relatório é parcial por construção A auditoria transversal definitiva só faz sentido com o curso inteiro escrito. Esta é a rodada que fecha o **bloco I (Fundamentos e Terra sólida)** mais o módulo 00. Ela deve ser **reexecutada** ao fim de cada bloco, e uma última vez no fechamento do curso.

## Veredito

✅ **Aprovado, sem achado 🔴 ou 🟠 em aberto.**

| Severidade | Total nos 4 módulos | Em aberto |
|---|---|---|
| 🔴 erro factual | 0 | **0** |
| 🟠 impreciso | 4 | **0** — todos corrigidos |
| 🟡 desatualizado | 0 | 0 |
| 🔵 sem fonte | 4 | **0** — todos resolvidos |
| 🔵 controverso (deferido) | 8 | 8, com módulo de destino definido |
| ⚪ observação | 2 | 2, não bloqueantes |

**Consequência:** os gates estão liberados. Questionários e baralhos dos módulos 00, 01, 02 e 03 podem ser gerados ou reconciliados.

> [!success] Atualização de 2026-08-16 — bloco I completo Os quatro módulos passaram a ter avaliação e memorização. O M00, último pendente, recebeu questionário final (19 questões, 40 pontos) e baralho (101 cards), ambos gerados sobre o texto já corrigido. O achado transversal `XC-F01` (crosta continental **30 a 50 km**) foi conferido nos dois materiais novos do M00: ambos usam o valor harmonizado, consistente com M01-a05, M02-a02 e o card `GG-M02-B013`.

## O que só a auditoria transversal pegou

Este é o valor específico desta rodada — achados que **nenhuma auditoria de módulo isolado veria**.

### 🟠 `XC-F01` — Espessura da crosta continental: o curso dizia duas coisas

O achado mais importante da rodada.

| Aula | Dizia | Situação |
|---|---|---|
| `M01-a05` | 30 a 50 km | ✅ correto |
| `M02-a02` | 30 a 50 km | ✅ correto |
| `M00-a04` | 30 a **40** km | ❌ corrigido para 30–50 |
| `M02-a04` | 30 a **40** km | ❌ corrigido para 30–50 |

O aluno que estudasse os quatro módulos na ordem encontraria o mesmo fato com dois valores diferentes — inclusive **duas vezes dentro do módulo 02**, entre a aula 02 e a aula 04.

A fonte normativa resolve a favor da faixa mais larga: o USGS dá 30–50 km para regiões continentais estáveis, e as compilações de espessura crustal põem mais de 90% das determinações entre 24 e 56 km.

**Corrigido em:** `00-partida-do-zero-aula-04-terra-por-dentro.md` (tabela e recap) e `02-sistema-terra-tectonica-aula-04-modelo-em-camadas.md` (lista da Moho).
**Propagação verificada:** o flashcard `GG-M02-B013` já dizia 30–50 km — foi gerado a partir da aula 02, que estava do lado certo. Nenhum material derivado herdou o erro.

### Padrão a registrar

É a **segunda vez** que a inconsistência numérica entre aulas é o achado mais grave de uma rodada. A primeira foi `M02-F01` (taxa de espalhamento da Elevação do Pacífico Leste, auditoria de 2026-08-15).

Nos dois casos, o defeito era invisível aula a aula e óbvio em conjunto. **A prática de auditar as aulas em conjunto, e não isoladamente, está pagando.** Manter.

Nos dois casos, também, a regra **LC-05** (ordem de grandeza em vez de precisão de laboratório) foi o que impediu a reincidência: onde o texto passou a dizer "centímetros por ano" em vez de um número, a classe de erro deixou de existir. Onde ainda há faixa numérica — como a espessura crustal — a divergência ainda é possível, e é onde a auditoria transversal precisa olhar.

## Consistências verificadas e aprovadas

Fatos afirmados em mais de um módulo, conferidos entre si:

| Fato | Onde aparece | Resultado |
|---|---|---|
| Idade da Terra, 4,54 Ga | M00-a03 · M01-a04 · M03-a04 · M03-a05 | ✅ idêntico nos quatro |
| Limite manto-núcleo, ~2.900 km | M00-a04 · M01-a05 · M02-a04 | ✅ consistente |
| Crosta oceânica, 5–10 km (~7 km típico) | M00-a04 · M01-a05 · M02-a02 · M02-a04 | ✅ consistente |
| Idade máxima da crosta oceânica, ~200 Ma | M01-a05 · M02-a04 · M02-a07 | ✅ consistente |
| Perfuração mais profunda, ~12 km | M00-a04 · M02-a02 | ✅ consistente — 12,26/6.371 = 0,19%, confere com "menos de 0,2%" |
| Proporção do Pré-cambriano | M01-a06 (">80%") · M03-a06 ("~88%") · M03-a07 (88 de 100 m) | ✅ compatíveis |
| Base do Cambriano | M00-a03 (~539 Ma) · M03-a06 (~540 Ma) | ✅ compatíveis; ICS v2024/12 dá 538,8 ± 0,6 Ma |
| Limite K-Pg, 66 Ma | M00-a03 · M03-a06 · M03-a07 | ✅ consistente |
| Núcleo externo líquido; elementos leves em debate | M00-a04 · M01-a01 · M02-a03 · M02-a04 | ✅ consistente; **nenhuma fecha a questão** (`M02-F07`) |
| Manto sólido que flui por convecção | M00-a04 · M02-a04 · M02-a05 | ✅ consistente |
| Relações de corte ("o que corta é mais novo") | M00-a05 · M01-a03 · M03-a01 | ✅ enunciado consistente nos três |
| Rocha mais antiga preservada | M00-a03 · M01-a04 · M03-a05 | ✅ **nenhuma arbitra a disputa** `M01-F02` |
| 5 cm/ano → 5.000 km em 100 Ma | M00-a03 (exemplo a) · M01-a06 | ✅ mesmo cálculo, mesmo resultado |

### As três réguas de tempo profundo

Ponto que merecia checagem específica, porque três módulos usam réguas diferentes para a mesma coisa:

| Módulo | Régua | Alvo didático |
|---|---|---|
| M00-a03 | 4,54 metros (1 mm = 1 Ma) | dar tamanho corporal à escala |
| M01-a06 | ano-calendário comprimido | intuição de proporção |
| M03-a07 | corredor de 100 metros | desfazer a distorção da carta impressa |

**Verificado:** as três são deliberadamente distintas, cada uma declarada como recurso didático arredondado, e **não se contradizem** — recalculadas, dão as mesmas proporções. O M03-a07 inclusive declara por escrito que não repete a régua do M01. Boa prática; manter.

## Verificação de progressão (conceito usado antes de ensinado)

Varredura dos blocos "Antes de começar, você precisa saber" contra a ordem dos módulos:

| Verificação | Resultado |
|---|---|
| Todos os wikilinks de pré-requisito apontam para aulas **anteriores** na progressão | ✅ |
| Os 5 nomes de arquivo do M00 citados por M01, M02 e M03 existem com o nome exato | ✅ — o contrato `inbound_links_note` foi respeitado |
| Aulas-ponte vêm **antes** do conteúdo que dependem delas | ✅ — M02-a01 (ondas) antes de M02-a02; M03-a03 (átomos) antes de M03-a04 |
| M03-a03 (ponte de átomos) declarada como pré-requisito do M04 | ✅ — anunciado no fecho de M03-a07 |
| Nenhuma aula usa matemática sem ponte (LC-06) | ✅ — M03-a04 trabalha por contagem de meias-vidas, sem exponencial nem logaritmo |

## Achados deferidos em aberto (🔵)

Nenhum é defeito. São controvérsias reais, tratadas no texto como questão em aberto conforme a regra **LC-08**, e agendadas para o módulo em que o aluno terá nível para arbitrá-las.

| ID | Questão | Retomar em | Status |
|---|---|---|---|
| `M01-F02` | Rocha mais antiga: Acasta × Nuvvuagittuq | M03, **M26** | M03 ✅ atendido; M26 pendente |
| `M01-F03` | Origem da Lua por impacto gigante | **M25** | pendente |
| `M01-F04` | Precisão de espessura crustal e do limite manto-núcleo | **M20** | escopo reduzido por LC-05 e por `XC-F01` |
| `M02-F04` | Geometria da convecção do manto | **M19**, **M20** | pendente |
| `M02-F05` | Origem das plumas e fixidez dos pontos quentes | **M11**, **M19**, **M25** | pendente |
| `M02-F06` | Balanço entre slab pull, ridge push e basal drag | **M19**, **M20** | pendente |
| `M02-F07` | Natureza das LLSVPs; elementos leves do núcleo | **M10**, **M20** | pendente |
| `M03-F02` | Conforme relatório do M03 | ver relatório | pendente |
| `M00-F04` | Limite de idade para o termo "fóssil" | **M16** | tratado corretamente sob LC-08 |

**Regra que continua valendo:** nenhum questionário ou flashcard pode cobrar esses pontos como fato fechado. Só em formato que peça ao aluno **reconhecer a questão como aberta**.

## Observações não factuais

⚪ **1.** Três alegações do arquivo da aula 06 do M01 carregam prefixo de `claim_id` da aula 04. Conteúdo correto; só a âncora não bate com o arquivo. Não alterado — `claim_id` não se recicla.

⚪ **2.** A aula 05 do M00 é a única que ensina leitura de mapa geológico antes do M21. Quando o M21 for escrito, conferir que ele **retoma** em vez de repetir.

## Relatórios por módulo

- [[00-partida-do-zero-auditoria|Módulo 00]] — 46 alegações · 0 🔴 · 2 🟠 corrigidos
- [[01-fundamentos-e-metodo-auditoria|Módulo 01]] — 31 alegações · 0 🔴 · 0 🟠
- [[02-sistema-terra-tectonica-auditoria|Módulo 02]] — 60 alegações · 0 🔴 · 1 🟠 corrigido
- [[03-tempo-geologico-geocronologia-auditoria|Módulo 03]] — 52 alegações · 0 🔴 · 2 🟠 corrigidos

Os relatórios das auditorias anteriores, referentes ao texto de nível antigo, estão preservados em `_arquivo-nivel-antigo/` dentro de cada módulo.

## Próxima execução

Reexecutar esta auditoria transversal ao fim do **bloco II (Materiais da Terra — módulos 04, 05, 06)**. Pontos a olhar já identificados:

1. A definição de mineral do M00-a01 e do M01-a01 contra a definição formal que o **M04** vai dar. É o candidato mais provável a divergência de definição do curso.
3. `M02-F07` (elementos leves do núcleo) quando o **M10** o retomar.
4. Os pares protólito-produto do M00-a02 contra a classificação formal do **M09**.

---

## Chave de leitura — renumeração de 2026-08-25

Em **2026-08-25** a gemologia saiu deste curso e os módulos **07–29 foram renumerados para 06–28**.
Os números de módulo **no corpo deste relatório já estão atualizados** para a numeração nova, com
duas exceções que valem registrar:

- O antigo **M06 (Gemologia)** deixou de existir aqui. A linha "Gemas que não são minerais" e o item
  de próxima execução que comparava M00-a01 com o M06 foram **removidos**, porque o conteúdo
  gemológico vive hoje em `../curso-gemologia`. A alegação correspondente na aula M00-a01
  (`GEO-M00-A01-GEMA-NAOMINERAL-005`) também foi retirada — ver o relatório do módulo 00.
- O cabeçalho diz "módulos 04 a 30 ainda não têm aulas": isso valia em 2026-08-16 e não vale mais.
  Hoje o curso tem 29 módulos (00–28), praticamente todos com aulas escritas.

**Esta auditoria transversal continua sendo de 2026-08-16 e cobre apenas os módulos 00–03.**
Ela precisa ser reexecutada sobre o curso inteiro na numeração nova.
