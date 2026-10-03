# Flashcards — Módulo 01: Fundamentos químicos

**Módulo:** [[01-fundamentos-quimicos-modulo|Módulo 01 — Fundamentos químicos: átomo, tabela periódica e ligação]]
**Total:** 134 cards — 75 Basic + 59 Cloze
**Faixa de IDs:** `mineralogia-m01-fb001`–`fb075` · `mineralogia-m01-fc001`–`fc059`
**Auditoria:** ✅ aprovada em 2026-09-30, sem achados 🔴/🟠 em aberto — gate liberado.
**Didática:** ✅ revisão concluída em 2026-09-30
**Questionário:** ✅ gerado em 2026-10-03 (18 questões, 6 objetivos cobertos)
**Gerado em:** 2026-10-03, contra as 6 aulas já auditadas e revisadas do módulo.

> [!info] Primeira geração O módulo 01 é a primeira série de aulas do curso e não há baralho prévio. Todos os IDs são novos. Importe os dois CSVs em deck limpo.

## Arquivos para importar

| Arquivo                                         | Tipo de nota no Anki | Campos                            |
| ----------------------------------------------- | -------------------- | --------------------------------- |
| `01-fundamentos-quimicos-flashcards-basic.csv`  | Basic                | id, frente, verso, tags, objetivo, aula, dificuldade, fonte |
| `01-fundamentos-quimicos-flashcards-cloze.csv`  | Cloze                | id, texto, tags, objetivo, aula, dificuldade, fonte |

> [!tip] Importação no Anki Importe os dois **separadamente**. Marque "Campos separados por ponto-e-vírgula", ative "Permitir HTML nos campos" e mapeie `id` como primeiro campo. As tags são hierárquicas (`mineralogia::m01::atomo::configuracao`).

## Distribuição

| Aula | Objetivo | Basic | Cloze | Total |
|---|---|---|---|---|
| a01 — O átomo por dentro | `oa01` | 9 | 7 | 16 |
| a02 — A tabela periódica | `oa02` | 11 | 6 | 17 |
| a03 — Íons e estados de oxidação | `oa03` | 9 | 8 | 17 |
| a04 — Ligação química (forte) | `oa04` | 20 | 11 | 31 |
| a05 — Ligações fracas | `oa04` | 13 | 14 | 27 |
| a06 — Mol, massa molar e unidades | `oa05–oa06` | 13 | 13 | 26 |

**Cobertura:** os seis objetivos do módulo têm card. Nenhum objetivo descoberto, nenhum card órfão.

## Critérios aplicados

- **O baralho é de vocabulário e conceitos, com ênfase em distinções e transferência para mineralogia.** Órbita vs. orbital; camada vs. subcamada; Fe²⁺ vs. Fe³⁺; iônica vs. covalente vs. metálica; van der Waals vs. ponte de hidrogênio. Cada uma dessas distinções tem card próprio, porque cada uma é um erro que o curso inteiro paga se não for corrigido aqui.
- **Todos os valores de referência estão auditados e confirmados contra NIST ASD, Shannon, IUPAC e CRC Handbook.** Configurações eletrônicas (Fe, Mn), energias de ionização (Na, Mg, Al, Fe), raios iônicos (Fe²⁺/Fe³⁺, Si⁴⁺, O²⁻, Cl⁻), eletronegatividades (Pauling, Allred 1961), massas atômicas (CIAAW 2024), constante de Avogadro (BIPM 2019).
- **Nenhuma matemática além do contrato `ensino-medio-sem-geologia-v1`.** Os cards de unidades e cálculos (B067, B074, B075) usam regra de três e conversão de unidades. Nenhum card exige integral, derivada ou logaritmo (a fórmula de Pauling é e^x, calculável em qualquer calculadora científica).
- **Ordem de grandeza (LC-05).** Nenhum card cobra ~1,62340 Å; cobram ~1,62 Å. Pressão no centro da Terra é ~360 GPa (não 363,7).
- **O erro-alvo tem card próprio.** B021 (Fe²⁺ e Fe³⁺ convivem porque EI cresce devagar), B039 (Au é metal apesar de χ próximo ao S), B042 (dureza não depende só do tipo de ligação, talco vs. quartzo), B054 (clivagem é pelo plano mais fraco, diamante tem {111} apesar de ligações fortes em 3D).
- **Tags hierárquicas.** `mineralogia::m01::atomo::fe` para cards sobre configuração do ferro; `mineralogia::m01::ligacao::pauling` para a fórmula de caráter iônico.

## Achados de auditoria e revisão didática respeitados

| Achado / Revisão | Como o baralho respeita |
|---|---|
| QUI-ORB-ENERGIA-001 (🟠) | B021 explica que Fe²⁺ e Fe³⁺ coexistem porque as EI do Fe crescem devagar. Não é simplesmente "4s sai primeiro". |
| QUI-TAB-TERRASRARAS-001 (🟠) | Nenhum card sobre terras raras (módulo 08); não entra no escopo de módulo 01. |
| QUI-VAL-DEF-001 (🟠) | B019 liga a eletronegatividade do O ao prevalência de O nos minerais. Elétrons de valência (aula 01) conectam bem com ionização (aula 02). |
| QUI-SPIN-DEF-001 (🔵) | Vocabulário da aula 03 define spin alto e spin baixo; B023 refere a pirita (Fe²⁺ spin baixo) que é auditada. |
| QUI-LIG-METALREGRA-001 (🔵) | B029 codifica o critério prático: metais nativos e ligas (só metais) → metálica. B039 explica o limite (Au ~1,92 na escala de Allen). |
| Revisão didática, 2026-09-30 | QUI-TAB-GRUPOD-001 (generaliza regra do exemplo); QUI-SPIN-DEF-001 (define termos usados sem definição). Ambas são respeitadas: B009 (grupo do Fe no bloco d), B023 (Fe²⁺/Fe³⁺ como valência variável). |

## Alinhamento com learning outcomes

| Objetivo | Cards que cobrem |
|---|---|
| `oa01` — Descrever o átomo | B001–B008, C001–C007 |
| `oa02` — Prever tendências periódicas | B009–B019, C007–C013 |
| `oa03` — Determinar estado de oxidação | B020–B027, C014–C022 |
| `oa04` — Classificar ligações | B028–B055, C023–C043 |
| `oa05` — Calcular massa molar e óxidos | B056–B062, C044–C050 |
| `oa06` — Converter unidades | B063–B075, C051–C059 |

## Notas sobre o baralho

- **Cloze é preferido para facts no contexto.** B032 (energias de ligação em tabela-forma) vira C034 (com lacunas nos valores-chave). B038 (eletronegatividades de Cu, Ag, Au) é Basic porque a resposta é uma lista (formato não se presta a cloze bem).
- **Nenhum card é reversível por padrão.** Uma pergunta "O que é eletronegatividade?" existe (B028); a pergunta inversa "Defina escala de eletronegatividade de Pauling" não entra porque sabemos que está ligada a χ de tal jeito que a resposta é não-única (Pauling, Mulliken, Allred-Rochow diferem). A aula já diz "usamos sempre Pauling".
- **Não há image occlusion:** o módulo é sobre conceitos, não sobre estruturas cristalinas (que entram módulo 04+). Descrições de forma de orbital, geometria tetraédrica, etc., usam só palavras.
- **Duplicatas descartadas na revisão:** um card "Qual é a carga de Na?" e outro "Qual é a carga de Mg?" testam a mesma habilidade com fatos diferentes; aproveitei um de cada para cobrir os 6 elementos-chave (Na, K, Mg, Ca, Al, Si) + alguns especiais (Fe, Mn, S).

## Próximo passo

Os flashcards do módulo 01 encerram a trilha de memorização de fundamentos. O módulo 02 começa o trabalho sobre o objeto de estudo — a definição de mineral e a sua classificação — e pode se beneficiar deste baralho revisado periodicamente durante a leitura das aulas 01–06.
