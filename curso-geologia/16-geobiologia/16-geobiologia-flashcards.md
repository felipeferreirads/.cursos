# Flashcards — Módulo 16: Geobiologia

Baralho do módulo, cobrindo as sete aulas (01, 02, 03a, 03b, 04, 05a, 05b). Importe os CSVs separadamente como tipos de nota Anki **Basic** e **Cloze**.

| Tipo | IDs | Quantidade | Cobertura |
|---|---|---:|---|
| Basic | `geologia-m16-fb001`–`geologia-m16-fb037` | 37 | OA-01–OA-05 |
| Cloze | `geologia-m16-fc001`–`geologia-m16-fc021` | 21 | OA-01–OA-05 |

## Distribuição por objetivo (Basic)

| Objetivo | Cards | IDs |
|---|---:|---|
| OA-01 — coevolução | 5 | `fb001`–`fb004`, `fb030` |
| OA-02 — estromatólitos e biogenicidade | 8 | `fb005`–`fb009`, `fb031`–`fb033` |
| OA-03 — ciclos biogeoquímicos | 5 | `fb010`–`fb014` |
| OA-04 — biomineralização | 7 | `fb015`–`fb019`, `fb034`, `fb035` |
| OA-05 — origem da vida e astrobiologia | 12 | `fb020`–`fb029`, `fb036`, `fb037` |

## Rastreabilidade

- Aulas de origem: `geologia-m16-a01`, `-a02`, `-a03a`, `-a03b`, `-a04`, `-a05a`, `-a05b`.
- Fontes factuais: Lyons, Reinhard & Planavsky (2014), Nature; Holland (2006), Phil. Trans. R. Soc. B; Allwood et al. (2007), Precambrian Research; Stüeken et al. (2015), Nature; Bosak, Knoll & Petroff (2013), Annu. Rev. Earth Planet. Sci.; Moody et al. (2024), Nature Ecology & Evolution; Martin et al. (2008), Nature Reviews Microbiology; Catchpole & Forterre (2019), Mol. Biol. Evol.; NASA Science (Europa Clipper); McKay et al. (1996) e literatura subsequente sobre ALH84001.

## Histórico de revisões

**2026-08-18 — auditoria científica.** Os cards `fb004`, `fb013`, `fb019`, `fb020`, `fb021`, `fb022`, `fc005`, `fc008`, `fc009`, `fc013`, `fc014`, `fc015`, `fc016`, `fc018`, `fc019` e `fc021` tiveram o conteúdo factual corrigido — ver [[16-geobiologia-auditoria|relatório de auditoria]]. Nenhum ID foi aposentado ou renumerado.

**2026-08-18 — pós-revisão didática.** Correções de forma, sem alteração de conteúdo científico:

- **Atomicidade (achado 8a).** Cinco cards pediam múltiplas respostas num card só, o que produz acerto parcial constante e degrada o agendamento da repetição espaçada. Cada um foi quebrado, mantendo o ID original para a primeira metade (preserva o histórico de agendamento no Anki) e criando IDs novos para as demais:

  | Card original | Ficou como | Cards novos |
  |---|---|---|
  | `fb004` (retroalimentação positiva **e** negativa) | só a negativa (carbonato-silicato) | `fb030` (positiva, gelo-albedo) |
  | `fb006` (estromatólito **vs.** trombólito) | só a fábrica do trombólito | `fb031` (identificar estromatólito por laminação) |
  | `fb008` ("cite três critérios") | só o critério de morfologia 3D | `fb032` (coerência ambiental), `fb033` (química/isótopos) |
  | `fb017` ("cite três famílias") | só a carbonática | `fb034` (silicosa), `fb035` (fosfática) |
  | `fb025` ("cite dois corpos") | só Marte | `fb036` (Europa e Encélado), `fb037` (Europa Clipper) |

- **Dependência de contexto (achado 8b).** `fb002` ("...conforme a Aula 01") e `fb026` ("...cite um exemplo do registro terrestre da Aula 05") tinham a numeração da aula na **frente** do card, o que os torna irrespondíveis meses depois, fora do contexto do curso. Ambos foram reformulados sem a referência numérica. Os cards Cloze citam a aula apenas no campo extra (o verso), o que é contexto legítimo e não foi alterado.
- **Religação com as aulas divididas.** O campo `Aula` foi reetiquetado de `a03`/`a05` para `a03a`/`a03b`/`a05a`/`a05b` nos cards Basic e Cloze afetados, acompanhando a divisão das aulas 03 e 05.
- **Reparo de CSV.** As linhas `fc004` e `fc012` continham ponto-e-vírgula dentro do campo de texto, o que quebrava a delimitação e teria corrompido a importação no Anki (8 e 7 campos em vez de 5). Os separadores internos foram substituídos por ` · `. Defeito pré-existente, encontrado nesta passagem.

> [!warning] Se você já importou este baralho no Anki Reimportar os CSVs não sobrescreve nem apaga cards existentes de forma confiável. Confira à mão: - **Versos com conteúdo factual alterado na auditoria:** `fb020`/`fc015` (idade do LUCA) e `fb022`/`fc016` (girase reversa). - **Frentes reescritas nesta rodada:** `fb002`, `fb004`, `fb006`, `fb008`, `fb017`, `fb025`, `fb026`. Se você já os estudava na versão antiga, o card continua válido — a versão nova só ficou mais curta. - **Cards novos a importar:** `fb030`–`fb037`. - **Nenhum ID foi aposentado.** Não há card a suspender ou apagar.

## Instruções de importação

1. Importe `16-geobiologia-flashcards-basic.csv` como tipo de nota **Basic** (pergunta + resposta). Separador: `;`. Campos: ID, Frente, Verso, Aula, Objetivo.
2. Importe `16-geobiologia-flashcards-cloze.csv` como tipo de nota **Cloze** (lacunas `{{c1::texto}}`). Mesmos cinco campos.
3. Use o campo ID como chave de identificação na importação, para que reimportações atualizem em vez de duplicar.
4. Estude os Basic primeiro (consolidação de conceito), depois os Cloze (recuperação em contexto).

## Notas de qualidade

- **Atomicidade:** após a revisão de 2026-08-18, nenhum card Basic pede mais de um fato ou item de lista. Os cards Cloze mantêm múltiplas lacunas de propósito — no Anki, cada lacuna vira um cartão independente, então a atomicidade é preservada pelo próprio tipo de nota.
- **Independência de contexto:** nenhuma frente de card Basic depende de saber de que aula ele veio.
- **Alinhamento com as aulas:** a terminologia dos cards foi conferida contra o texto das sete aulas. Ver os CSVs para o conteúdo integral.

Arquivos: `16-geobiologia-flashcards-basic.csv` · `16-geobiologia-flashcards-cloze.csv`
