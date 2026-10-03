# Aula 14: DiamondView, fotoluminescência e triagem

**ID:** gemologia-m02-a14
**Módulo:** Diamantes
**Duração estimada:** ~30 min
**Objetivo:** entender como funcionam os dois instrumentos que fecham a pergunta de origem de crescimento e como um laboratório organiza a triagem em torno deles.
**Pré-requisito:** [[02-diamantes-aula-13-crescimento-cvd|Aula 13 — crescimento CVD]].

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **triagem** (*screening*) | exame rápido que separa "liberado" de "precisa de exame adicional". |
| **passa / refere** | as duas saídas possíveis de um aparelho de triagem. |
| **falso negativo** | deixar passar como natural algo que não é. O erro que a triagem existe para impedir. |
| **falso positivo** | referir para exame algo que é natural. O erro que a triagem aceita pagar. |
| **melê** (*melee*) | diamantes pequenos, tipicamente abaixo de 0,20 ct, vendidos em lotes. |
| **UV profundo** | ultravioleta de comprimento de onda muito curto, abaixo de cerca de 230 nm. |
| **77 K** | temperatura do nitrogênio líquido, cerca de −196 °C. |

## Antes de começar, você precisa saber

- As assinaturas do HPHT (padrão em cruz, fluxo metálico, tipo Ib, tensão fraca): [[02-diamantes-aula-12-crescimento-hpht|Aula 12]].
- As assinaturas do CVD (estrias paralelas, tipo IIa, tensão em bandas, SiV⁻ em ~737 nm): [[02-diamantes-aula-13-crescimento-cvd|Aula 13]].
- Que cerca de 98% dos diamantes naturais são tipo Ia, com o centro N3 absorvendo a 415 nm: [[02-diamantes-aula-04-tipos-ia-ib-iia-iib|Aula 04]].

## Ao final você vai conseguir

- `gemologia-m02-oa14` — Interpretar imagens de DiamondView e espectros de fotoluminescência e situar os equipamentos de triagem no fluxo de um laboratório.

## Conteúdo

Num aeroporto, ninguém abre todas as malas. Todas passam por um raio X rápido; a esmagadora maioria segue direto, e uma minoria é aberta. O raio X não decide o que há dentro da mala — ele decide **quais malas merecem ser abertas**. Se ele errar deixando passar algo perigoso, o sistema falhou. Se ele errar abrindo malas inocentes, o sistema apenas ficou mais lento.

A triagem de diamantes é exatamente esse desenho, com a mesma assimetria deliberada de erros. Entender isso é entender por que "referido" não significa "sintético".

### O DiamondView: por que UV profundo

A ideia parece simples — iluminar a pedra com ultravioleta e fotografar a fluorescência. O truque está no comprimento de onda.

Uma lâmpada UV comum de bancada (365 ou 254 nm) atravessa o diamante inteiro. A fluorescência que se vê é a soma de tudo o que a pedra emite, de ponta a ponta — um borrão, sem estrutura espacial.

O DiamondView usa **ultravioleta abaixo de cerca de 230 nm**. Nessa faixa, o diamante absorve fortemente, e a radiação **penetra apenas uma camada finíssima** logo abaixo da superfície. A fluorescência registrada vem só dessa fatia rasa — e por isso a imagem revela a **estrutura de crescimento** com nitidez, em vez de somar tudo.

O instrumento também registra **fosforescência**, fotografando a pedra logo após desligar a fonte, o que é especialmente útil nos tipo IIb.

O que a imagem entrega, agora reunido:

| Padrão observado | Leitura |
|---|---|
| Zonas **concêntricas** e irregulares, geralmente azuis (N3) | natural |
| **Cruz** ou quadrantes, seguindo setores de cubo e octaedro | HPHT |
| **Faixas paralelas**, regulares, frequentemente vermelho-alaranjadas (NV⁰) | CVD |

Duas ressalvas honestas: os padrões podem ser ambíguos em pedras muito pequenas ou de lapidação que corta os setores em ângulo desfavorável, e o GIA já documentou **diamante natural com padrão de fluorescência parecido com o de CVD**. Nem o DiamondView é uma sentença isolada.

### A fotoluminescência: por que o frio

A fotoluminescência mede a luz **emitida** pela gema após excitação por laser. Ela é a técnica mais sensível a defeitos que existe na gemologia — capaz de detectar centros presentes em concentrações de partes por bilhão, muito abaixo do que o FTIR alcança.

Duas exigências técnicas explicam por que ela mora no laboratório e não na bancada:

**O resfriamento a 77 K.** À temperatura ambiente, os átomos da rede vibram, e essa vibração **alarga** as linhas de emissão até que feições vizinhas se confundam num borrão. Resfriada em nitrogênio líquido, a rede se aquieta e as linhas ficam estreitas. O exemplo clássico da necessidade: os centros **H3** e **3H** emitem a cerca de 503,2 e 503,5 nm — três décimos de nanômetro de distância. Um deles é típico de material natural aquecido, o outro é típico de irradiação. Sem resfriamento e sem alta resolução, os dois são a mesma linha, e a leitura seria oposta à verdade.

**Vários lasers.** Nenhum comprimento de onda de excitação revela todos os defeitos. Um laboratório usa uma série — tipicamente algo entre 325 e 633 nm — porque cada laser "acende" um conjunto diferente de centros.

As feições que este módulo já encontrou, agora em tabela:

| Emissão | Centro | O que sugere |
|---|---|---|
| 503,2 nm | H3 | nitrogênio + vacância; comum em natural, e em material aquecido |
| 503,5 nm | 3H | irradiação |
| 575 nm | NV⁰ | comum em CVD; presente também em natural |
| 596 / 597 nm | não plenamente atribuído | **só relatado em CVD**; apagado por recozimento HPHT |
| 637 nm | NV⁻ | a **razão** NV⁰/NV⁻ é o que informa, não a presença |
| ~737 nm | SiV⁻ | silício do reator; **raro em natural**, forte indício de CVD |
| 741 nm | GR1 | vacância isolada; assinatura de irradiação (aula 15) |

### A arquitetura da triagem

Um laboratório não roda DiamondView e fotoluminescência em toda pedra que entra — seria caro e lento demais. Ele monta um funil:

**Etapa 1 — é diamante?** Densidade, condutividade, ou a checagem espectroscópica básica. Elimina simulantes.

**Etapa 2 — triagem por tipo.** Aqui mora a economia do sistema. Instrumentos como o **GIA DiamondCheck** medem o espectro infravermelho e separam:
- **Passa** — tipo I, com nitrogênio agregado. Como ~98% dos naturais são tipo Ia e as rotas de laboratório quase nunca produzem esse padrão, essas pedras seguem direto para graduação.
- **Refere** — tipo II e casos ambíguos, que vão para a etapa 3.

O **DiamondSure**, da De Beers, faz o equivalente pelo lado óptico: procura a linha de absorção de **415 nm** do centro N3. Presente → passa. Ausente → refere.

**Etapa 3 — identificação.** DiamondView, fotoluminescência, UV-Vis-NIR, FTIR de alta resolução, exame microscópico. É aqui, e só aqui, que a pergunta é respondida.

**Instrumentos de campo e de varejo.** O **GIA iD100** é o representante mais difundido: usa tecnologia espectroscópica para separar diamante natural de crescido em laboratório (HPHT e CVD) e de simulantes, funciona com pedras **soltas e montadas**, e alcança pedras muito pequenas — até a ordem de 0,005 ct, o que o torna útil para melê. Para lotes grandes de melê existem sistemas automatizados como o **AMS** da De Beers, e para pedras montadas há instrumentos de imagem de luminescência como o **SYNTHdetect**.

### A assimetria dos erros, e o que "referido" significa

Um aparelho de triagem é calibrado para **nunca** cometer um falso negativo. Deixar passar um sintético como natural destruiria a confiança em toda a cadeia. Para garantir isso, ele aceita cometer **muitos** falsos positivos: refere pedras naturais perfeitamente comuns.

A consequência prática precisa ser dita sem rodeios: **"referido" não é acusação.** É a etiqueta de "não foi possível liberar com o teste barato". Aproximadamente 1 a 2% dos diamantes naturais são tipo IIa (aula 04) — todos eles serão referidos, e todos eles são naturais.

Um comerciante que devolve ao cliente uma pedra dizendo "o aparelho acusou sintético" está reportando errado o resultado de um instrumento que não emite esse resultado.

## Exemplo trabalhado

Um lote de 500 diamantes melê de 0,01 a 0,05 ct, comprado de fornecedor novo, precisa ser verificado. Verificar um a um em laboratório é economicamente impossível.

1. **Passagem no equipamento automatizado de triagem de melê.** As 500 pedras são processadas. Resultado: 482 **passam**, 18 são **referidas**.
2. **Interpretação do número.** 18 em 500 é cerca de 3,6%. Isso está na ordem de grandeza esperada para a fração natural de tipo II mais casos ambíguos de leitura — não é, por si só, sinal de lote contaminado.
3. **O erro a não cometer.** Reportar "18 sintéticos encontrados". Nenhuma das 18 foi identificada como coisa alguma. Elas apenas não foram liberadas.
4. **Segunda etapa nas 18.** DiamondView. Doze mostram zoneamento concêntrico irregular — padrão natural. Quatro mostram **faixas paralelas** — CVD. Duas dão imagem ambígua, por serem pequenas demais e mal orientadas.
5. **Terceira etapa nas 6 restantes** (4 suspeitas + 2 ambíguas). Fotoluminescência a 77 K. As quatro suspeitas mostram forte SiV⁻ em ~737 nm: **CVD confirmado**. Das duas ambíguas, uma mostra espectro compatível com natural e é liberada; a outra também mostra SiV⁻ e entra no grupo CVD.
6. **Resultado final.** 495 compatíveis com natural, **5 identificadas como CVD**. O lote estava contaminado — em 1%, e não nos 3,6% que a triagem sinalizou.
7. **Custo do desenho.** Foram feitas 500 triagens baratas, 18 imagens e 6 espectros de fotoluminescência, em vez de 500 exames completos. É exatamente por isso que a arquitetura de funil existe.

Conclusão registrável: "lote de 500 melê; 5 pedras identificadas como diamante crescido em laboratório por processo CVD; 495 sem evidência de crescimento em laboratório. As 13 pedras referidas na triagem e não confirmadas são naturais e devem ser reintegradas ao lote".

## Erros comuns

- **Ler "referido" como "sintético".** É o erro mais comum e o mais injusto com o vendedor honesto.
- **Usar lâmpada UV de bancada esperando ver padrão de crescimento.** Ela atravessa a pedra e borra tudo; é preciso UV abaixo de ~230 nm.
- **Fazer fotoluminescência sem resfriar.** As linhas alargam e feições vizinhas se fundem — H3 e 3H são o caso escolar.
- **Usar um só laser na fotoluminescência.** Cada excitação revela um conjunto diferente de centros.
- **Tratar o DiamondView como sentença.** Já houve natural com padrão parecido com CVD, e pedras pequenas dão imagem ambígua.
- **Achar que triagem substitui laboratório.** Ela decide quem vai ao laboratório; não decide o que a pedra é.

## O que não concluir

- Nenhum instrumento de triagem, de bancada ou de varejo, **identifica** um diamante como crescido em laboratório. Ele apenas separa "liberado" de "não liberado".
- A ausência de assinatura não prova naturalidade: o GIA documenta casos de CVD com pouquíssimas feições diagnósticas, e a dificuldade tende a crescer conforme a tecnologia de crescimento melhora.
- Taxas de referência variam com o lote, o instrumento e a calibração. O 3,6% do exemplo é ilustrativo.
- A fotoluminescência é extremamente sensível, mas a atribuição de alguns centros a defeitos específicos ainda é **objeto de pesquisa ativa** — o dupleto de 596/597 nm, usado na prática, não tem atribuição estrutural plenamente estabelecida.

## Recap relâmpago

- O DiamondView usa UV abaixo de ~230 nm, que penetra só uma camada rasa, revelando a estrutura de crescimento: concêntrico = natural, cruz = HPHT, faixas paralelas = CVD.
- A fotoluminescência mede emissão após laser, com a pedra a 77 K, porque o frio estreita as linhas — H3 (503,2 nm) e 3H (503,5 nm) só se separam assim.
- Feições-chave: 575 (NV⁰), 596/597 (só CVD), 637 (NV⁻), ~737 (SiV⁻, indício de CVD), 741 (GR1, irradiação).
- A triagem é um funil: identidade → tipo (DiamondCheck, DiamondSure) → identificação (DiamondView, PL).
- Instrumentos de campo e varejo: GIA iD100 (solto e montado, até ~0,005 ct), AMS para melê, SYNTHdetect para montadas.
- A calibração aceita muitos falsos positivos para nunca ter falso negativo — logo, **"referido" não é "sintético"**.

## Próxima aula

Na [[02-diamantes-aula-15-tratamentos-e-laudos|Aula 15]], a quarta categoria — nem natural intocado, nem simulante, nem crescido: o diamante tratado, e o que o laudo diz sobre ele.

## Fontes consultadas

- GIA, *Gems & Gemology*, [Laboratory-Grown Diamonds: An Update on Identification and Products Evaluated at GIA](https://www.gia.edu/gems-gemology/summer-2024-gia-update-on-laboratory-grown-diamonds) (Summer 2024).
- GIA, *Gems & Gemology*, [Analysis of Gemstones at GIA Laboratories](https://www.gia.edu/gems-gemology/winter-2024-gemstone-analysis) (Winter 2024) — fluxo de triagem e DiamondCheck.
- GIA, [GIA iD100 Gem Testing Device](https://www.gia.edu/UK-EN/id100) e [GIA Instruments](https://www.gia.edu/gia-instruments).
- GIA, *Gems & Gemology*, [Natural Diamond with CVD-Like Fluorescence Pattern](https://www.gia.edu/gems-gemology/summer-2023-lab-notes-natural-diamond-with-cvd-like-fluorescence-pattern) (Summer 2023).
- Welbourn, C. M. et al., "De Beers Natural versus Synthetic Diamond Verification Instruments", *Gems & Gemology* 32(3), 1996 (DiamondSure e DiamondView).
- Eaton-Magaña, S. & Breeding, C. M., "An Introduction to Photoluminescence Spectroscopy for Diamond and Its Applications in Gemology", *Gems & Gemology* 52(1), 2016.

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1600
cobertura:
  gemologia-m02-oa14: [Conteúdo, Exemplo trabalhado]
alegacoes_auditaveis:
  - claim_id: DIA-TRIAG-001
    claim: "O DiamondView usa ultravioleta de comprimento de onda abaixo de cerca de 230 nm, que e absorvido numa camada muito fina abaixo da superficie, permitindo formar imagem da estrutura de crescimento em vez da soma da fluorescencia de toda a pedra; tambem registra fosforescencia."
    risk: mecanismo
    source: "Welbourn et al., Gems & Gemology 32(3) 1996; GIA"
  - claim_id: DIA-TRIAG-002
    claim: "Padroes no DiamondView: zonas concentricas irregulares (frequentemente azuis, de N3) indicam natural; padrao em cruz ou por quadrantes indica HPHT; faixas paralelas, frequentemente vermelho-alaranjadas de NV0, indicam CVD."
    risk: classificacao
    source: "GIA, Summer 2024 update on laboratory-grown diamonds"
  - claim_id: DIA-TRIAG-003
    claim: "A fotoluminescencia e feita com a pedra resfriada a temperatura de nitrogenio liquido (cerca de 77 K) porque o resfriamento estreita as linhas de emissao; os centros H3 (cerca de 503,2 nm) e 3H (cerca de 503,5 nm) so podem ser separados assim."
    risk: numero
    source: "Eaton-Magana & Breeding, Gems & Gemology 52(1) 2016"
  - claim_id: DIA-TRIAG-004
    claim: "Feicoes de fotoluminescencia relevantes: 575 nm (NV0), 596/597 nm (so relatado em CVD), 637 nm (NV-), cerca de 737 nm (SiV-, indicio de CVD) e 741 nm (GR1, assinatura de irradiacao)."
    risk: numero
    source: "Eaton-Magana & Breeding 2016; GIA Gems & Gemology, CVD reviews"
  - claim_id: DIA-TRIAG-005
    claim: "O GIA DiamondCheck separa diamantes em Passa (tipo I) e Refere (tipo II e crescidos em laboratorio) a partir do espectro infravermelho; o DiamondSure da De Beers faz triagem equivalente pela presenca ou ausencia da linha de absorcao de 415 nm do centro N3."
    risk: mecanismo
    source: "GIA, Analysis of Gemstones at GIA Laboratories (Winter 2024); Welbourn et al. 1996"
  - claim_id: DIA-TRIAG-006
    claim: "O GIA iD100 usa tecnologia espectroscopica para separar diamante natural de crescido em laboratorio (HPHT e CVD) e de simulantes, opera com pedras soltas e montadas e alcanca pedras da ordem de 0,005 ct."
    risk: numero
    source: "GIA, GIA iD100 Gem Testing Device"
  - claim_id: DIA-TRIAG-007
    claim: "Os instrumentos de triagem sao calibrados para evitar falsos negativos ao custo de muitos falsos positivos; o resultado Refere nao identifica a pedra como sintetica, e os cerca de 1 a 2% de diamantes naturais tipo IIa sao sistematicamente referidos."
    risk: interpretacao
    source: "GIA, Analysis of Gemstones at GIA Laboratories (Winter 2024); GIA Summer 2024 update"
  - claim_id: DIA-TRIAG-008
    claim: "Ja foi documentado diamante natural com padrao de fluorescencia semelhante ao de CVD, e diamantes CVD com pouquissimas feicoes diagnosticas, de modo que nenhum instrumento isolado encerra a questao de origem de crescimento."
    risk: interpretacao
    source: "GIA, Natural Diamond with CVD-Like Fluorescence Pattern (Summer 2023); GIA, CVD-Grown Diamond with Few Diagnostic Features (Fall 2023)"
controversias:
  - id: DIA-PL-596-001
    questao: "A atribuicao estrutural do dupleto de 596/597 nm, usado na pratica como indicador de CVD nao tratado, ainda nao esta plenamente estabelecida na literatura."
    tratamento: "LC-08 — declarada em uma frase na tabela do corpo e detalhada em 'O que nao concluir'."
-->
