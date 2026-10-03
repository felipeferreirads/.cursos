# Flashcards — Módulo 00: Partida do zero

**Módulo:** [[00-partida-do-zero-modulo|Módulo 00]]
**Total:** 97 cards — 59 Basic + 38 Cloze
**Faixa de IDs:** `geologia-m00-fb001`–`B062` · `geologia-m00-fc001`–`C039`
**Auditoria:** ✅ aprovada em 2026-08-16, sem achados 🔴/🟠 em aberto — gate liberado.
**Gerado em:** 2026-08-16, contra as 6 aulas já corrigidas pela auditoria científica do módulo.

> [!info] Primeira geração O módulo 00 nasceu na repartida de 2026-08-16 e nunca teve baralho. Não há migração a fazer, nem IDs antigos a aposentar: importe os dois CSVs em deck limpo.

## Arquivos para importar

| Arquivo                                   | Tipo de nota no Anki | Campos                                  |
| ----------------------------------------- | -------------------- | --------------------------------------- |
| `00-partida-do-zero-flashcards-basic.csv` | Basic                | id, frente, verso, tags, aula, objetivo |
| `00-partida-do-zero-flashcards-cloze.csv` | Cloze                | id, texto, tags, aula, objetivo         |

> [!tip] Importação no Anki Importe os dois **separadamente**. Marque "Campos separados por vírgula", ative "Permitir HTML nos campos" e mapeie `id` como primeiro campo. As tags são hierárquicas (`geologia::m00::interior`).

## Distribuição

| Aula | Objetivo | Basic | Cloze | Total |
|---|---|---|---|---|
| a01 — Pondo os nomes no lugar | `oa01` | 11 | 6 | 17 |
| a02 — Os três tipos de rocha | `oa02` | 12 | 7 | 19 |
| a03 — Ordens de grandeza | `oa03` | 10 | 7 | 17 |
| a04 — A Terra por dentro | `oa04` | 10 | 7 | 17 |
| a05 — O mapa geológico | `oa05` | 10 | 7 | 17 |
| a06 — Observar, descrever, inferir | `oa06` | 9 | 5 | 14 |

Cobertura: os **seis** objetivos do módulo têm card. Nenhum objetivo descoberto, nenhum card órfão.

A aula 02 recebe o maior bloco porque é a única do módulo em que o aluno precisa reter **listas fechadas** (três famílias, três vias sedimentares, quatro pares protólito–produto). A aula 06 recebe o menor porque é a mais conceitual: o que ela ensina é um hábito, e hábito se treina no questionário e no campo, não em card.

## Critérios aplicados

- **O baralho é de vocabulário, e por isso prioriza distinções.** Mineral × rocha; cristalino × com cara de cristal; mineral × vidro; face crescida × superfície desgastada; camada × foliação; magma × lava; crosta × placa; escala grande × área grande; observação × interpretação. Cada uma dessas tem card próprio, porque cada uma é um erro que o curso inteiro paga se não for corrigido aqui.
- **Nada de matemática além do contrato `iniciante-absoluto-v1`.** As contas dos cards de ordem de grandeza (`B025`, `B033`) são somas e subtrações de expoentes, como a aula 03 as faz. Nenhum card exige logaritmo ou calculadora.
- **Valores só em ordem de grandeza (LC-05).** Nenhum card cobra 6.371 km, 12.262 m ou 538,8 Ma. Os cards pedem ~6.400 km, ~12 km e ~539 Ma, que é o que as aulas afirmam.
- **O erro-alvo tem card próprio.** `B037` (o manto não é líquido), `B040` (o núcleo interno é sólido apesar do calor), `B043` (placa não é crosta), `B022` (cor não classifica) e `B009` (lapidado não é cristal) existem porque são as cinco concepções erradas que este módulo foi escrito para desmontar.
- **O que está em aberto é cardificado como aberto.** `B011` responde que **não existe norma formal** de idade para o termo "fóssil" — a resposta é a ausência de norma, não um número.

## Achados de auditoria respeitados

| Achado | Como o baralho respeita |
|---|---|
| `XC-F01` (🟠, corrigido) | `B036` e `C022` usam **30 a 50 km** para a crosta continental — o valor harmonizado com M01-a05 e M02-a02. Nenhum card diz 30 a 40. |
| `M00-F01` (🟠, corrigido) | `B032` traz a régua com a história escrita em **cinco milésimos de milímetro**, o valor corrigido, ao lado dos ~3 mm do gênero *Homo* — que é justamente a confusão que gerou o achado. |
| `M00-F02` (🔵, resolvido) | `B060` e `C038` atribuem a hipótese de estimação a **Chamberlin, 1890**, com autor e ano conferidos contra a referência completa. |
| `M00-F03` (🔵, resolvido) | `C018` usa ~4,54 Ga, ~539 Ma e ~66 Ma — valores conferidos contra a carta ICS v2024/12 na auditoria. |
| `M00-F04` (⚪, aceito) | `B011` cardifica o limite de idade do fóssil **como convenção sem norma formal**, e não como número a recuperar. |
| `M01-F02` (🔵, aberto no M01) | Nenhum card pergunta qual é a rocha mais antiga do planeta nem cobra essa idade como valor. |
| `M02-F07` (🔵, aberto no M02) | `B039` e `C024` dizem "ferro, com níquel e uma parcela de elementos mais leves", sem nomear nem quantificar os elementos leves, que seguem em discussão. |
| LC-08 (regra de questões em aberto) | Nenhum card cobra a temperatura do centro da Terra nem a organização da convecção do manto — os dois pontos que a aula 04 declara explicitamente em aberto. |

## Amostra (tabela de conferência)

| ID | Frente | Verso |
|---|---|---|
| B001 | Diferença entre mineral e rocha | Mineral é a espécie; rocha é o agregado. Tijolo está para parede. |
| B005 | Todo mineral é cristalino? | Sim, por dentro. Nem todo tem cara de cristal — depende de ter havido espaço. |
| B016 | O que o tamanho do grão de uma ígnea revela | Grão grande = lento = fundo. Grão fino = rápido = superfície. |
| B019 | Camada × foliação | Camada = empilhamento (sedimentar). Foliação = minerais alinhados por pressão (metamórfica). |
| B026 | Quantas vezes um bilhão é maior que um milhão? | Mil vezes. |
| B037 | O manto é líquido? | Não. Rocha sólida que flui. Lava vem de bolsões locais. |
| B043 | Placa é o mesmo que crosta? | Não. Corte por material × corte por comportamento mecânico; não coincidem. |
| B047 | Estilos de linha no mapa | Contínua = observado; tracejada = inferido; pontilhada = encoberto. |
| B056 | Teste de bolso da observação | Alguém sem geologia poderia conferir isso olhando? |
| B062 | Interpretar é errado? | Não. Interpretar sem rotular é. |

*(Tabela parcial. Os 101 cards estão nos CSVs.)*

## Formato Spaced Repetition (Obsidian)

Mineral ::: substância natural, sólida, receita química fixa, átomos em padrão repetido — a espécie Rocha ::: agregado de grãos de mineral; pode ser de um mineral só — o corpo Cristal ::: mineral que teve espaço para crescer e ganhou faces planas Vidro natural ::: sólido sem padrão repetido; obsidiana esfriou rápido demais e por isso não é mineral Fóssil corporal ::: parte do organismo — concha, osso, dente, tronco Fóssil de vestígio ::: marca de comportamento — pegada, toca, mordida Ígnea ::: estava derretido e esfriou Sedimentar ::: grãos soltos que se acumularam e endureceram Metamórfica ::: já era rocha e se transformou sem derreter Grão grande ::: esfriamento lento, formou-se fundo — granito Grão fino ::: esfriamento rápido, formou-se na superfície — basalto Marcas da sedimentar ::: camadas e fósseis Foliação ::: minerais alinhados por pressão; não confundir com camada Pares protólito-produto ::: calcário→mármore, arenito→quartzito, folhelho→ardósia, granito→gnaisse Ciclo das rochas ::: tipo de rocha é estágio, não identidade permanente Expoente ::: conta os zeros; multiplicar soma, dividir subtrai Bilhão × milhão ::: mil vezes — 11 dias e meio contra 32 anos ka, Ma, Ga ::: 10³, 10⁶ e 10⁹ anos Notação científica ::: um algarismo, vírgula, resto × 10 elevado ao número de casas andadas Comparar números ::: expoente primeiro, sempre; cada degrau vale dez vezes Raio da Terra ::: cerca de 6.400 km Camadas da Terra ::: crosta → manto (~2.900 km) → núcleo externo líquido (~5.100 km) → núcleo interno sólido Crosta continental ::: ~30 a 50 km; oceânica ~5 a 10 km; menos de 1% do raio Manto ::: rocha sólida que flui por convecção — não é mar de lava Sólido que flui ::: como a geleira; depende da escala de tempo em que se observa Núcleo ::: metal — ferro com níquel e elementos mais leves Núcleo interno sólido ::: a pressão vence a temperatura Campo magnético ::: gerado pelo núcleo externo líquido em movimento Placa não é crosta ::: uma divisão é por material, a outra por comportamento mecânico Mapa geológico ::: que rocha existe em cada ponto, ignorando solo e vegetação Legenda ::: ordenada por idade, mais antiga embaixo — lida de baixo para cima é a história da região Linha contínua ::: contato observado Linha tracejada ::: contato inferido Linha pontilhada ::: contato encoberto Símbolo de atitude ::: direção + sentido de mergulho + ângulo; a terceira dimensão no plano Simetria em espelho ::: indica dobra Escala 1:50.000 ::: 1 cm = 500 m Exagero vertical ::: o perfil transforma rampa em penhasco; confira o fator antes de interpretar Relação de corte ::: o que corta é mais novo que o cortado Observação × interpretação ::: a observação sobrevive; a interpretação é substituível A escada ::: observação → descrição → inferência → interpretação, incerteza crescente Teste da observação ::: alguém sem geologia poderia conferir isso olhando? Palavras-vírus ::: de praia, vulcânica, fluvial, intrusão, erodido Roteiro de descrição ::: cor fresca → grão → seleção → arredondamento → o que se reconhece → estrutura → comportamento Hipótese de estimação ::: Chamberlin 1890; antídoto são hipóteses múltiplas As três perguntas ::: de que outro jeito? o que eu esperaria ver? eu procurei?

## Navegação

[[00-partida-do-zero-modulo|← Hub do módulo]] · [[00-partida-do-zero-questionario-final|← Questionário]] · [[00-partida-do-zero-auditoria|Auditoria do módulo]] · [[01-fundamentos-e-metodo-flashcards|Baralho do M01 →]]

<!--
last_id_basic: 62
last_id_cloze: 39
gerado_em: "2026-08-16"
tipo: primeira_geracao
motivo: >-
  Módulo criado na repartida de 2026-08-16 e nunca cardificado. Gerado depois da
  auditoria científica do módulo, contra o texto já corrigido, e depois do
  questionário final, para não repetir literalmente os enunciados dele.
auditoria_referencia: "00-partida-do-zero-auditoria.json (2026-08-16, verdict: approved, gate_released: true)"
nivel: iniciante-absoluto-v1
achados_respeitados: [XC-F01, M00-F01, M00-F02, M00-F03, M00-F04, M01-F02, M02-F07]
-->

## Nota de 2026-08-25 — separação dos cursos

Quatro cards foram **aposentados** quando o conceito de gema saiu da aula 01: `geologia-m00-fb007`, `geologia-m00-fb008`, `geologia-m00-fb009` e `geologia-m00-fc005`. Se você já tinha importado a versão anterior, apague-os no Anki — senão continuam aparecendo na revisão sem aula de referência. Os IDs não serão reciclados. O assunto vive hoje no curso de Gemologia, módulo 01.
