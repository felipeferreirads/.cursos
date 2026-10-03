# Auditoria científica — Módulo 12: Engenharia de petróleo

**Auditado em:** 2026-09-02 · **Modo:** `audit-and-fix` · **Profundidade:** `full`
**Material:** `12-engenharia-de-petroleo/` — 5 aulas (a01 a a05)
**Veredito:** **Aprovado com correção aplicada** — nenhum achado 🔴 ou 🟠 em aberto.

## Nota sobre o histórico desta auditoria

Uma tentativa anterior de auditar este módulo foi interrompida pelo limite de sessão da API
depois de já ter editado o texto das cinco aulas, mas antes de produzir relatório, manifesto ou
atualizar o estado do curso — os `content_hash` registrados ficaram divergentes do conteúdo em
disco sem nenhum registro do que havia sido verificado ou corrigido. Por isso esta execução
tratou o material como **nunca auditado**: nenhuma alegação foi aceita por já "parecer"
corrigida, e todo cálculo do módulo foi refeito do zero, independentemente do que a tentativa
anterior possa ter alterado. O resultado abaixo reflete o que existe **no conteúdo atual dos
arquivos em disco**, verificado de novo, não uma continuação do trabalho interrompido.

## Resumo

🔴 0 erros · 🟠 1 impreciso · 🟡 0 desatualizados · 🔵 0 sem fonte · ⚪ 0 controversos

**Total: 1 achado**, de natureza bibliográfica (data de edição citada), não conceitual. As 25
alegações auditáveis declaradas pelas cinco aulas foram usadas como ponto de partida e todas
reverificadas contra fonte primária; nenhuma delas continha erro. Módulo tecnicamente limpo.

**O que dominou o esforço desta auditoria, dado o pedido explícito de rigor quantitativo, foi o
recálculo independente de todo exemplo numérico do módulo — nenhum resultado foi aceito por
estar "declarado no texto".** Os cinco exemplos trabalhados (conversão de peso de lama e janela
operacional na a01; equação de Archie para Sw/Sh na a02; OOIP volumétrico na a03; índice de
produtividade J e extrapolação por IPR na a04; ganho volumétrico de EOR sobre o OOIP/FR da a03
na a05) foram recalculados do zero, dígito a dígito, e **todos batem exatamente com o valor
publicado no texto** — inclusive a cadeia de herança a03→a05, que é o ponto mais sensível a
propagação de erro silenciosa neste módulo (ver seção de recálculo abaixo). Isso é consistente
com duas explicações não excludentes: a tentativa anterior interrompida já havia corrigido
eventuais erros de cálculo antes de ser cortada, ou o material nunca teve erro de cálculo. Como
a auditoria não herdou registro algum da tentativa anterior, não há como distinguir as duas —
mas o efeito prático é o mesmo: o conteúdo atual em disco está numericamente correto, verificado
de forma independente.

---

## Achados 🔴

Nenhum.

---

## Achados 🟠

### 🟠 1. Ano de edição de Craft & Hawkins (rev. Terry & Rogers) citado como 2013

**claim_id:** `PETRENG-M12-CRAFTHAWKINS-001` · **Tipo:** erro factual (data de publicação)
**Onde:** a03 · seção "Fontes" + manifesto (`PETRENG-M12-A03-OOIP-004`, `PETRENG-M12-A03-FR-005`) ·
a04 · seção "Fontes" + manifesto (`PETRENG-M12-A04-DRIVES-001`)
**Estava escrito:** "Craft, B. C. & Hawkins, M. (revisado por Terry, R. E. & Rogers, J. B.,
**2013**), *Applied Petroleum Reservoir Engineering*, 3ª ed., Prentice Hall" (a03); "Craft &
Hawkins (rev. Terry & Rogers, **2013**)" (a04, corpo e manifesto)
**Problema:** a 3ª edição de *Applied Petroleum Reservoir Engineering*, revisada por Ronald E.
Terry e J. Brandon Rogers (Pearson, ISBN 978-0-13-315558-7), foi publicada em agosto de 2014,
com copyright de 2015 — não 2013. O erro não afeta nenhuma afirmação técnica do corpo da aula
(porosidade/permeabilidade, PVT, método volumétrico e mecanismos de produção citados a partir
dela estão corretos e batem com a obra real), mas uma data de edição errada numa fonte que o
curso recomenda para aprofundamento é exatamente o tipo de detalhe que frustra quem tenta
localizar a obra a partir da citação.
**Correção aplicada:** ano corrigido para 2015 nas duas aulas (corpo/Fontes e manifesto), e o
nome da editora ajustado para "Pearson/Prentice Hall" (o selo Prentice Hall foi absorvido pela
Pearson; a edição revisada é publicada sob o catálogo Pearson).
**Fonte:** InformIT/Pearson, ficha do produto *Applied Petroleum Reservoir Engineering*, 3rd
Edition (ISBN 9780133155587), data de publicação 2 de agosto de 2014, copyright 2015. ·
**Nível:** base de referência (metadado editorial, confirmado na página oficial da editora).
**Confiança:** confirmado.
**Também aparece em:** a03 (Fontes + manifesto, dois claims) e a04 (Fontes + manifesto, um
claim). Não aparece na a05 (que cita Craig, Willhite, Satter & Thakur e Wiggins & Startzman,
não Craft & Hawkins).

---

## Recálculo independente dos cinco exemplos quantitativos

Verificação pedida explicitamente pela tarefa: nenhum resultado numérico do módulo foi aceito
por estar escrito no texto. Todos os cinco foram refeitos a partir dos dados de entrada.

**a01 — conversão de peso de lama e janela operacional.** Fator de conversão ppg→psi/ft:
7,48 gal/ft³ ÷ 144 in²/ft² = 0,0519 ≈ 0,052 (arredondamento padrão da indústria; checagem com
água doce 8,33 ppg × 0,052 = 0,433 psi/ft, correta). Gradiente da lama = 0,052 × 10,5 ppg =
0,546 psi/ft — confere. Profundidade 3.000 m = 9.842,5 ft ≈ 9.843 ft — confere. Pressão
hidrostática = 0,546 × 9.843 = 5.374,3 psi ≈ 5.374 psi — confere. Pressão de poros = 0,465 ×
9.843 = 4.577,0 psi — confere. Pressão de fratura = 0,80 × 9.843 = 7.874,4 psi ≈ 7.874 psi —
confere. Margem de sobrebalanço = 5.374 − 4.577 = 797 psi — confere. Margem até a fratura =
7.874 − 5.374 = 2.500 psi — confere. **Todos os valores batem.**

**a02 — equação de Archie (Sw/Sh).** Com φ = 0,20, a = 1, m = 2, n = 2, Rw = 0,05 Ω·m,
Rt = 20 Ω·m: φᵐ = 0,20² = 0,04; a/φᵐ = 25; Rw/Rt = 0,0025; produto = 0,0625; Sw = √0,0625 =
0,25 (25%) — confere. Sh = 1 − 0,25 = 0,75 (75%) — confere. Sensibilidade a m = 1,8: φ¹,⁸ =
0,20^1,8 = 0,0551; a/φᵐ = 18,15; produto = 0,0454; Sw = √0,0454 ≈ 0,213 (21%) — confere com o
"≈ 21%" declarado. Os expoentes e o coeficiente usados (a=1, m=2, n=2) estão dentro da faixa
padrão de Archie para arenito consolidado sem calibração local, consistente com Archie (1942) e
com a prática descrita em Schlumberger e Rider & Kennedy. **Todos os valores batem.**

**a03 — OOIP volumétrico.** OOIP = 7.758 × A × h × φ × (1−Sw) / Bo, com A = 800 acres, h = 25 ft,
φ = 0,22, Sw = 0,30, Bo = 1,25 bbl/STB. Numerador: 7.758×800 = 6.206.400; ×25 = 155.160.000;
×0,22 = 34.135.200; ×0,70 = 23.894.640. OOIP = 23.894.640 / 1,25 = 19.115.712 STB — confere
exatamente com o valor declarado ("≈ 19,1 milhões"). Reserva recuperável a FR = 18%:
19.115.712 × 0,18 = 3.440.828,16 ≈ 3.440.828 STB — confere. Sensibilidade a Bo = 1,35:
23.894.640 / 1,35 = 17.699.733,3 ≈ 17,7 milhões — confere; diferença = 19.115.712 − 17.699.733 =
1.415.979 ≈ "quase 1,4 milhão" — confere. A constante 7.758 bbl/acre-pé é a conversão padrão
SPE (1 acre-pé = 7.758,367 bbl); a fórmula análoga de OGIP com 43.560 (pés³/acre-pé) e Bg está
correta. **Todos os valores batem.**

**a04 — índice de produtividade J e extrapolação por IPR.** J = q/(Pr−Pwf) = 450/(3.200−2.750) =
450/450 = 1,0 bbl/dia/psi — confere. Extrapolação a Pwf = 2.400 psi: q = 1,0×(3.200−2.400) =
1,0×800 = 800 bbl/dia — confere. A ressalva de que a extrapolação só vale enquanto Pwf permanece
acima do ponto de bolha, com a curva de IPR deixando de ser linear abaixo dele (regime coberto
por Vogel 1968), está tecnicamente correta e é o cuidado esperado neste tipo de cálculo.
**Todos os valores batem.**

**a05 — ganho de EOR sobre o OOIP/FR herdados da a03 (verificação de propagação, pedida
explicitamente pela tarefa).** OOIP herdado = 19.115.712 STB (idêntico ao valor fechado na a03 —
**herança correta, sem erro propagado**). (a) Volume recuperado até o fim da secundária =
19.115.712 × 0,32 = 6.117.027,84 ≈ 6.117.028 STB — confere. (b) Volume adicional do EOR =
19.115.712 × 0,12 = 2.293.885,44 ≈ 2.293.885 STB — confere. (c) FR final = 32% + 12% = 44%;
volume total = 19.115.712 × 0,44 = 8.410.913,28 ≈ 8.410.913 STB — confere, e bate com
6.117.028 + 2.293.885 = 8.410.913 (consistência interna entre os três subitens). Comparação com
o ganho da secundária isolada (32%−18% = 14 p.p. → 19.115.712×0,14 = 2.676.199,68 ≈ "cerca de
2,68 milhões") — confere. **Todos os valores batem, e a cadeia de herança a03→a05 está intacta:
nenhum número foi alterado, arredondado de forma inconsistente ou recalculado a partir de uma
premissa diferente entre as duas aulas.**

---

## Verificação de vocabulário cruzado com o Módulo 11 (pedida explicitamente pela tarefa)

A a02 declara, no pré-requisito e na abertura, que reaproveita — sem redefinir — o vocabulário
de perfil sônico, perfil de densidade, sismograma sintético e amarração poço-sísmica (*well
tie*) já ensinado no Módulo 11, Aula 02. Comparação direta dos dois textos:

- **Perfil sônico (DT)** — M11 a02: "mede o tempo de trânsito de uma onda elástica através de um
  intervalo fixo de rocha (...), o inverso da velocidade". M12 a02 não redefine; usa "sônico"
  apenas como insumo de velocidade já estabelecido. **Sem conflito.**
- **Perfil de densidade (RHOB)** — M11 a02: "mede a densidade da formação por atenuação de
  radiação gama". M12 a02: "já visto no Módulo 11 como insumo do sismograma sintético", reutiliza
  a mesma grandeza (densidade eletrônica da formação) para derivar porosidade por densidade
  (φD), um uso adicional e não uma redefinição. **Sem conflito.**
- **Sismograma sintético / well tie** — M12 a02 não usa esses termos para nada além de uma
  referência de contexto ("os perfis sônico e de densidade continuam relevantes"); não reintroduz
  nem redefine a construção por convolução com a wavelet, que permanece exclusiva do Módulo 11.
  **Sem conflito.**
- Nenhum dos quatro termos aparece com sentido diferente, unidade diferente ou mecanismo
  diferente nas duas ocorrências. A cadeia de pré-requisito declarada ("este curso já introduziu
  (...); esta aula não repete essa base") corresponde exatamente ao que o Módulo 11 ensinou.

**Nenhuma redefinição conflitante encontrada.**

---

## Verificado e correto

Além dos cinco recálculos e da checagem de vocabulário acima, o restante das 25 alegações
auditáveis declaradas (e as afirmações de risco não declaradas ao redor delas) foi conferido
contra fonte e **mantido sem alteração**:

- **Brocas tricônica e PDC**, funções do fluido de perfuração (remoção de cascalho,
  resfriamento/lubrificação, controle de pressão, sustentação de parede com mudcake), janela
  operacional entre gradiente de poros e de fratura, fases de revestimento (condutor, superfície,
  intermediária, produção) e as três funções da cimentação (a01) — todos conformes a Bourgoyne
  et al. (1986) e Rabia (2001).
- **Índice de raios gama (IGR) e volume de argila (Vsh)**, incluindo a direção correta da
  distorção (relação linear Vsh=IGR superestima Vsh; correções não lineares tipo Larionov
  distinguem rocha terciária de mais antiga) (a02) — conforme Rider & Kennedy (2011).
  **Resistividade como resposta ao fluido, não à matriz**, e a leitura profunda (Rt) como a
  menos afetada por invasão de filtrado (a02) — conforme Schlumberger e Ellis & Singer (2007).
  **Equação de Archie** com a atribuição correta a Archie (1942), *Transactions of the AIME*
  146(1), p. 54–62 — citação exata confirmada. **Nêutron-densidade e efeito de gás** (*gas
  crossover*, nêutron subestimando fortemente a porosidade em zona de gás) — conforme Rider &
  Kennedy. **Testemunhagem como calibração** dos parâmetros de Archie, Vsh-IGR e porosidade por
  densidade, não como substituto da perfilagem — conforme Ellis & Singer (a02).
- **Porosidade e permeabilidade como propriedades independentes** (folhelho: porosidade
  moderada, permeabilidade muito baixa; arenito limpo: as duas altas), lei de Darcy (1856),
  unidade darcy/milidarcy — conforme Tiab & Donaldson. **Saturação de água irredutível (Swi)**,
  faixa 10–40% e sua relação com textura — conforme Ahmed. **PVT**: definição de Bo (sempre >1
  para óleo vivo, 1,1–1,5 bbl/STB), definição de Rs, e o comportamento em torno do ponto de
  bolha — Rs constante e Bo **subindo** levemente acima de Pb (expansão do óleo subsaturado),
  Bo máximo (Bob) exatamente em Pb, ambos mudando de regime abaixo dele — está descrito com o
  sinal fisicamente correto nos dois trechos (corpo e Recap), conforme Dake (1978) e Ahmed
  (2019) (a03).
- **Os quatro mecanismos de produção primária** (depleção por gás em solução, capa de gás,
  influxo de água, drenagem gravitacional) com faixas de FR consistentes com Ahmed e Craft &
  Hawkins, e a ressalva de nomenclatura sobre a expansão de rocha e fluido como possível quinto
  mecanismo (Ahmed, cap. 4) — correta e verificada, incluindo a atribuição a Ahmed. **Injeção de
  água** como recuperação secundária dominante e o fenômeno de canalização preferencial
  (*channeling*) por heterogeneidade — conforme Craft & Hawkins. **Drawdown, buildup e fator de
  película (skin)** — conforme Lee (1982). **Definição de J e a condição de linearidade da IPR
  acima do ponto de bolha**, com a correlação de Vogel (1968) corretamente restrita ao regime
  abaixo dele — citação exata de Vogel (1968), *JPT* 20(1), p. 83–92, confirmada (a04).
- **Completação a poço revestido/canhoneado vs. poço aberto**, e a distinção explícita entre
  telas de contenção isoladas e *gravel pack* (não sinônimos), com o controle de areia
  corretamente associado a rocha de **alta** permeabilidade mal consolidada — conforme Bellarby
  (2009). **Os três métodos de elevação artificial** (bombeio mecânico, ESP, gas lift) com suas
  vantagens/limitações relativas — conforme Brown (1980). **As três famílias de EOR** (térmico,
  miscível, químico), o mecanismo físico de cada uma, e a direção correta da pressão mínima de
  miscibilidade (aumenta com densidade/viscosidade do óleo) — conforme Green & Willhite (2018,
  2ª ed. confirmada) e Lake (1989). **Gestão de reservatórios** como disciplina formalizada a
  partir de 1990–1996, distinta da literatura clássica de injeção de água dos anos 1970–80
  (Craig 1971; Willhite 1986) que a precede — atribuições e datas conferidas uma a uma (a05).
- **Citações verificadas contra a ficha editorial real** (autor, título, edição, editora, ano):
  Bourgoyne et al. (1986), Archie (1942), Schlumberger (2013), Rider & Kennedy (2011), Ellis &
  Singer (2007), Ahmed (2019, 5ª ed. — confirmada, jan/2019), Dake (1978), Vogel (1968), Green &
  Willhite (2018, 2ª ed. — confirmada), Lake (1989), Craig (1971), Willhite (1986), Satter &
  Thakur (1994), Wiggins & Startzman (1990, SPE-20747-MS — confirmada). Todas corretas, exceto a
  única exceção registrada no achado 🟠 1.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-02

| claim_id | Sev. | Desfecho | Arquivos alterados |
|---|---|---|---|
| `PETRENG-M12-CRAFTHAWKINS-001` | 🟠 | Corrigido | a03 (Fontes, manifesto — 2 claims), a04 (Fontes, manifesto — 1 claim) |

**Pendências:** nenhuma. Nenhum achado 🔵 ou ⚪ ficou aberto; `open_findings` vazio.

**Material derivado a propagar:** nenhum. O módulo 12 ainda não tem questionário nem baralho de
flashcards — a auditoria rodou antes deles, como manda a cadeia. Nada a reimportar no Anki.

---

## Advertências ao gerador de questionários e de flashcards

Diferente do Módulo 11, este módulo não deixa nenhum ponto de conteúdo tecnicamente errado para
sinalizar como distrator corrigido — o único achado é bibliográfico e não afeta nenhuma questão
de cálculo ou de conceito. Duas notas úteis para quem for gerar a avaliação:

1. **O módulo é fortemente quantitativo e a cadeia a03→a05 é a mais sensível a erro de
   propagação** (OOIP calculado na a03 é reutilizado literalmente na a05 para o cálculo de
   ganho de EOR). Vale incluir ao menos uma questão de aplicação que exija recalcular ou
   verificar essa herança (por exemplo, dado um FR diferente, pedir o volume incremental do EOR
   sobre o mesmo OOIP), já que é exatamente o tipo de erro que uma auditoria futura precisaria
   pegar se a a03 for editada sem revisar a a05.
2. **Distinções que valem questão de discriminação, não de decoreba:** RC de Archie exige os
   três parâmetros (a, m, n) calibrados, nunca universais; Bo sobe até o ponto de bolha e só cai
   depois dele (sinal frequentemente invertido por alunos); o controle de areia (telas/gravel
   pack) se aplica a rocha de **alta**, não baixa, permeabilidade — um erro intuitivo comum,
   porque "areia" soa como problema de baixa qualidade de reservatório quando na verdade é
   consequência de pouca consolidação em rocha de excelente permoporosidade.

## Fontes consultadas nesta auditoria

Além das fontes já citadas nas cinco aulas (relacionadas em cada arquivo), esta auditoria
consultou diretamente para verificação bibliográfica: ficha do produto *Applied Petroleum
Reservoir Engineering*, 3rd Edition, InformIT/Pearson (informit.com, consultado 2026-09-02);
ficha do produto *Enhanced Oil Recovery*, Second Edition, PennWell Books/SPE (pennwellbooks.com,
onepetro.org, consultado 2026-09-02); ficha do produto *Reservoir Engineering Handbook*, 5th
Edition, ScienceDirect/Gulf Professional Publishing (sciencedirect.com, consultado 2026-09-02);
SPE-20747-MS, "An Approach to Reservoir Management", OnePetro (onepetro.org, consultado
2026-09-02); Archie, G.E. (1942), ficha de citação em OnePetro/Google Scholar (consultado
2026-09-02); ficha do produto *Log Interpretation Charts*, 2013 Edition, SLB (slb.com,
consultado 2026-09-02).
