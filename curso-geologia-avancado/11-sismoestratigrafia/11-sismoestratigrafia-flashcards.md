# Baralho de Flashcards — Módulo 11: Sismoestratigrafia

**ID do baralho:** `geologia-avancado-m11-flashcards`
**Módulo:** [[11-sismoestratigrafia-modulo|Módulo 11 — Sismoestratigrafia]]
**Data de geração:** 2026-08-31
**Cards totais:** 132 (66 Basic + 66 Cloze)

---

## Convenção

Os flashcards deste baralho são entregues em dois formatos, ambos prontos para importação no Anki:

- **CSV Basic** (`11-sismoestratigrafia-flashcards-basic.csv`): Pergunta e resposta simples. Ideal para perguntas de definição, "o que é", "cite", "diferencie".
- **CSV Cloze** (`11-sismoestratigrafia-flashcards-cloze.csv`): Cards com lacunas (`{{c1::...}}`, `{{c2::...}}`, etc.). Ideal para aprender conceitos interligados, nomenclatura e retenção de detalhes numéricos.

Nomenclatura de IDs:
- Basic: `geologia-avancado-m11-fb0XX`
- Cloze: `geologia-avancado-m11-fc0XX`

Os IDs estão automaticamente inseridos no campo de ID do Anki em cada card.

---

## Cobertura dos objetivos

Este baralho foi gerado a partir das seis aulas do módulo e cobre os quatro objetivos declarados:

### Objetivo 01: Fundamentos do método sísmico (Aulas 01-02)
- Propagação de ondas, impedância acústica, coeficiente de reflexão
- Aquisição por cobertura múltipla (CMP)
- Processamento sísmico: deconvolução → NMO/empilhamento → migração
- Resolução sísmica vertical (λ/4 Rayleigh, λ/8 Widess) e horizontal (zona de Fresnel)
- Perfilagem de poço (sônico, densidade), sismograma sintético, amarração poço-sísmica

### Objetivo 02: Padrões de terminação de refletores (Aula 03)
- Refletor como aproximação de linha de tempo
- Onlap (transgressão, preenchimento de topografia)
- Downlap (progradação)
- Baselap (critério de inclinação relativa)
- Toplap (bypass, sem erosão)
- Truncamento erosivo (discordância, remoção de material)
- Conexão com Módulo 10 (borda flexural, discordância de ruptura)

### Objetivo 03: Sismofácies e sistemas deposicionais (Aula 04)
- Definição e atributos de sismofácies
- Cinco configurações principais (paralela, divergente, progradacional, caótica, transparente)
- Clinoformas (topset, foreset, bottomset; sigmoide vs. oblíqua)
- Sistemas siliciclásticos (deltas, turbiditos)
- Sistemas carbonáticos: plataforma estratificada vs. buildup recifal (Bubb & Hatlelid 1977)
- Afogamento de plataforma (give-up), construção topográfica autogênica

### Objetivo 04: Estratigrafia de sequências e aplicação (Aulas 05-06)
- Espaço de acomodação, sequência deposicional
- Quatro tratos de sistemas: LST, TST, HST, FSST
- Superfícies-chave: discordância de sequência (SB), superfície de inundação máxima (MFS)
- Diagrama de Wheeler
- Previsão de elementos de sistema petrolífero por trato
- Critério de deformação sinsedimentar vs. pós-deposicional
- Margem continental brasileira: sin-rifte (geradora lacustre), sag (carbonatos + sal), drift
- Topo de sal como feição deposicional (não reológica)
- Desacoplamento infra-sal / supra-sal

---

## Avisos de auditoria

Este baralho foi gerado após auditoria científica completa do módulo (2026-08-31). A auditoria corrigiu 10 achados (3 vermelho, 7 laranja), todos resolvidos antes da geração dos flashcards. Sete pontos mudaram de forma que **gerar cards a partir da versão anterior produziria gabarito errado**:

1. **Widess é λ/8, não λ/4.** O λ/4 é Rayleigh. Flashcards evitam a confusão separando explicitamente os dois limiares.
2. **RC é razão de amplitudes, não de energias.** A energia refletida é RC². Destacado em vários cards.
3. **Ordem de processamento: deconvolução → empilhamento → migração.** (Não NMO primeiro.) Enfatizado nos cards de processamento.
4. **Topo plano do sal é deposicional.** Fluxo salífero torna o topo irregular. Explicado nos cards finais.
5. **Quatro tratos: LST, TST, HST, FSST.** O FSST (não SMST) é o trato de queda. Diferenciado explicitamente.
6. **Downlap e toplap se definem por *updip*/*downdip* e inclinação relativa**, não inclinação absoluta da ponta da camada. Vários cards reforçam isso.
7. **Carbonatos têm duas assinaturas opostas.** Plataforma estratificada (refletores fortes) vs. buildup recifal (refletor-livre, diagnóstico pelo entorno). Bubb & Hatlelid 1977, não Brown & Fisher. Claramente separado nos cards.

---

## Estrutura do arquivo CSV

Cada linha do arquivo CSV tem o formato:

```
frente;verso
```

Para importação no Anki: Arquivo → Importar → selecionar CSV → tipo "Basic" ou "Cloze" conforme o arquivo.

---

## Como usar

1. **No Anki (recomendado para repetição espaçada):**
   - Abra Anki.
   - Arquivo → Importar.
   - Selecione `11-sismoestratigrafia-flashcards-basic.csv`.
   - Escolha o tipo de card "Basic" ou "Cloze" conforme necessário.
   - Repita o processo para ambos os arquivos.

2. **Revisão rápida (sem Anki):**
   - Abra o arquivo CSV num editor de texto ou numa planilha.
   - Tape a coluna "verso" para testar recuperação antes de olhar a resposta.

3. **Integração com o curso:**
   - Estes flashcards cobrem ALL os conceitos-chave das seis aulas.
   - Use-os após completar cada aula ou como revisão integrada do módulo inteiro.
   - Combine com os questionários do módulo (2 parciais + 1 final) para avaliação mais completa.

---

## Verificação de qualidade

Todos os 132 cards foram gerados manualmente a partir das aulas corrigidas (pós-auditoria). Foram conferidos contra:
- A lista de "Advertências ao gerador de flashcards" da auditoria (seção final de `11-sismoestratigrafia-auditoria.md`)
- O padrão de formato do módulo 10 (referência de estrutura CSV)
- A resolução de validação sísmicos automática (`validate_flashcards.py`)

---

## Próximos passos

- Importar este baralho no Anki ou no SRS de sua preferência.
- Começar a revisar o módulo 12 (próximo módulo do curso).
- Retornar a este baralho em intervalos conforme o algoritmo de repetição espaçada sugerir (tipicamente algumas horas, depois um dia, uma semana, um mês, e assim por diante).

---

## Referência rápida: IDs dos cards

**Basic (66 cards):** `geologia-avancado-m11-fb001` a `geologia-avancado-m11-fb066`
**Cloze (66 cards):** `geologia-avancado-m11-fc001` a `geologia-avancado-m11-fc066`

Procure por um ID específico para rastrear um card individual no Anki.

---

## Métadados

| Campo | Valor |
|-------|-------|
| Módulo | 11 — Sismoestratigrafia |
| Aulas cobertas | Aulas 01–06 |
| Total de cards | 132 |
| Tipos | Basic (66) + Cloze (66) |
| Data de geração | 2026-08-31 |
| Auditoria | 10 achados corrigidos, 0 em aberto |
| Status | Pronto para uso |

---

**Navegação:**
[[11-sismoestratigrafia-modulo|← Voltar ao módulo]]
