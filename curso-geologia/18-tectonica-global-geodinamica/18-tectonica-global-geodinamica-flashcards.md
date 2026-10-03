# Flashcards — Módulo 18: Tectônica global e geodinâmica

Baralho modular para revisão ativa. Os CSVs são separados por tipo de nota Anki: [Basic](18-tectonica-global-geodinamica-flashcards-basic.csv) e [Cloze](18-tectonica-global-geodinamica-flashcards-cloze.csv).

## Resumo do baralho

| Tipo | Quantidade | IDs | Cobertura |
|---|---:|---|---|
| Basic | 22 | `geologia-m18-fb001`–`fb022` | 4–5 cards por OA |
| Cloze | 17 | `geologia-m18-fc001`–`fc017` | 3–4 cards por OA |

Todos os cards são atômicos, têm aula e objetivo de origem, usam tags hierárquicas e foram derivados das seis aulas do módulo. Não há cards dependentes de imagem.

## Cobertura por objetivo

| Objetivo | Aula(s) | Basic | Cloze | Núcleo recuperado |
|---|---|---:|---:|---|
| OA01 — margens de placa e geodinâmica do manto | 01, 02 | 4 | 3 | polo de Euler, forças motrizes, pluma mantélica, Havaí–Imperador |
| OA02 — tectônica e bacias sedimentares | 03 | 4 | 3 | rifte, margem passiva, antepaís, antearco/retroarco |
| OA03 — orogênese | 04 | 5 | 4 | sutura, ofiolito, acresção de terrenos, colisão continental, ciclo de Wilson |
| OA04 — crátons, escudos e estabilização continental | 05 | 4 | 3 | cráton, quilha litosférica, escudo, bacia cratônica |
| OA05 — ciclo dos supercontinentes | 06 | 5 | 4 | Pangeia, Rodínia, Columbia/Nuna, subducção extrovertida, cenários futuros (Pangeia Ultima / Novopangeia / Amásia / Aurica) |

## Convenções de importação

- Separador: `;`.
- Encoding: UTF-8 sem BOM.
- Basic: colunas `id;frente;verso;tags;objetivo;aula;dificuldade;fonte`.
- Cloze: colunas `id;texto;extra;tags;objetivo;aula;dificuldade;fonte`.
- Todas as lacunas Cloze usam a sintaxe numerada `{{c1::texto}}`.

## Fontes de conteúdo

As aulas mantêm as referências completas. O baralho reutiliza apenas fatos presentes nelas, principalmente USGS, Forsyth & Uyeda (1975), Allen & Allen (*Basin Analysis*), Coney, Jones & Monger (1980), Li et al. (2008), Nance, Murphy & Santosh (2014), Tarduno et al. (2003), Davies, Green & Duarte (2018) e Mitchell, Kilian & Evans (2012), além das sínteses explicitamente citadas nas aulas.

> [!warning] Revisão pós-auditoria (2026-08-18) A auditoria científica do módulo alterou o card `fb020` (cenários do próximo supercontinente: agora três, com o modo de fechamento de cada um) e o campo *extra* do card `fc003`. Se o baralho já foi importado no Anki, **reimportar o CSV não corrige automaticamente cards já existentes** — localize esses dois cards pelo `id` e atualize ou remova-os à mão. Ver `18-tectonica-global-geodinamica-auditoria.md`.

> [!note] Cobertura corrigida (2026-08-18) A revisão didática apontou que o baralho não cobria o ciclo de Wilson (testado em Q07 do questionário) nem Columbia/Nuna (testado em Q12). Adicionados os cards `fb021`/`fc016` (ciclo de Wilson, OA03/Aula 04) e `fb022`/`fc017` (Columbia/Nuna, OA05/Aula 06).
