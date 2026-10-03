# Revisão didática: Módulo 28 — Análise instrumental I

**Revisado em:** 2026-09-23  ·  **Modo:** review-and-fix
**Material:** `28-analise-instrumental-i/` (hub + 5 aulas na entrada; 6 aulas na saída)
**Veredito:** Bem ensinado com ressalvas (todas corrigidas nesta passagem)

A revisão rodou depois da auditoria científica do mesmo dia (1 vermelho, 11 laranjas, 1 amarelo, todos corrigidos; ver [[28-analise-instrumental-i-auditoria|relatório de auditoria]]). As três observações que a auditoria encaminhou (Aula 05 sobrecarregada; Aula 04 sem calibração; pré-requisitos do hub) foram tratadas aqui como achados 001, 002 e 007.

## Resumo

🔴 0 bloqueiam · 🟠 5 prejudicam · 🟡 6 atrito · 🔵 2 sugestões

Todos os 🟠 e 🟡 foram corrigidos. As duas sugestões 🔵 ficaram registradas, sem aplicação.

**Carga estimada (depois da revisão, contagem por script a ~84 palavras/min):**

| Aula | Conceitos novos | Pré-requisitos reativados | Exemplos | Palavras | Duração |
|---|---|---|---|---|---|
| 01 Amostragem | 4 (FSE de Gy, heterogeneidade de constituição e regra d³, cadeia de subamostragem, contaminação) | estatística básica | 1 (pórfiro × basalto, agora com passo numérico) | 2075 | ~25 min |
| 02 Preparação | 4 (cadeia de redução, fusão × digestão, LOI, controle de qualidade) | Aula 01 | 1 (andesito × sedimento) | 2111 | ~25 min |
| 03 AAS | 4 (quantização/absorção × emissão, arranjo de AAS, chama × forno, interferências) | estrutura eletrônica | 1 (Ca por AAS) | 1867 | ~22 min |
| 04 ICP | 4 (plasma, ICP-OES, ICP-MS, interferências e calibração) | Aula 03 | 1 (granitoides) | 2326 | ~28 min |
| 05 XRF (nova Parte 1) | 3 (camadas internas/Moseley, WD × ED, efeitos de matriz) | Aulas 02-04 | 1 (três formas de medir, novo) | 1593 | ~19 min |
| 06 Estatística (nova Parte 2) | 3 (Poisson, propagação, LOD/LOQ) | Aulas 02, 04, 05 | 1 (Nb, agora com cálculo) | 1704 | ~20 min |

## Achados

### 🟠 1. Aula 05 com seis blocos independentes e acima de 30 minutos
**ID:** `DID-M28-A05-SOBRECARGA-SEIS-BLOCOS-001`
**Tipo:** excesso de conceitos novos / dificuldade desproporcional
**Onde:** antiga Aula 05 inteira
**Problema:** 2633 palavras (~31 min; declarada ~27 min) e seis blocos que não dependem uns dos outros: física de camadas internas e Moseley, WDXRF × EDXRF, efeitos de matriz, estatística de Poisson, propagação de erros e LOD/LOQ. Duas aulas numa só. A metade estatística nem é de XRF: ela fecha o módulo inteiro e ficava presa ao fim de uma aula de instrumentação. As correções 10-13 da auditoria deixaram a aula ainda mais longa.
**Correção aplicada:** divisão em **Aula 05 — Fluorescência de raios X** (Parte 1: física, aparelhagem, efeitos de matriz; ~19 min) e **Aula 06 — Estatística de contagens, propagação de erros e limites de detecção** (Parte 2; ~20 min). Texto das seções transportado na íntegra (conferido por script, parágrafo a parágrafo). A Parte 1 ganhou um exemplo trabalhado próprio, "três perguntas, três formas de medir por XRF" (pérola × pXRF × pastilha), que só recombina fatos já auditados e prepara o exemplo do Nb da Parte 2. Callouts de Parte 1/2, recaps separados, "Próxima aula" encadeando 04 → 05 → 06 → Módulo 29.
**Decisões de implementação:** o ID `m28-a05` ficou com a Parte 1 e o arquivo foi **renomeado** para `...-aula-05-fluorescencia-de-raios-x.md` (o nome antigo anunciava a estatística); a Parte 2 é o arquivo novo `...-aula-06-estatistica-de-contagens-limites-de-deteccao.md` com ID `m28-a06`. Os `claim_id` não mudaram: A05-001/002/003/007 vivem na Aula 05 e A05-004/005/006 na Aula 06. O manifesto de auditoria teve os caminhos atualizados e o relatório ganhou aviso no topo.
**Escopo:** exigiu dividir a aula.

### 🟠 2. Calibração prometida e usada, mas nunca ensinada
**ID:** `DID-M28-A04-CALIBRACAO-NAO-ENSINADA-002`
**Tipo:** termo central usado antes de definido / promessa de título não cumprida
**Onde:** Aula 04 (título: "métodos qualitativos e quantitativos"); Aula 03 ("calibração [...] tratada com rigor estatístico na Aula 05"); Aula 05 antiga (LOD = 3σ/m, "inclinação (sensibilidade) da curva de calibração")
**Problema:** o cálculo central do OA-04 divide pela **sensibilidade**, a inclinação da curva de calibração, e nenhuma aula dizia o que é uma curva de calibração nem como se passa do sinal à concentração. A Aula 03 remetia à Aula 05, que não tratava do assunto. O título da Aula 04 prometia métodos quantitativos que o corpo não mostrava.
**Correção aplicada:** seção curta "Do sinal à concentração: identificação e calibração" na Aula 04 (identificação pela linha ou pela m/z; padrões de concentração conhecida na mesma matriz ácida; reta sinal × concentração; inclinação = sensibilidade; padrão interno trabalhando por razão), bullet de recap e item no "Ao final". A remissão da Aula 03 agora aponta para a Aula 04 (calibração) e a Aula 06 (limites). Conteúdo definicional, registrado como claim `ANINST-M28-A04-CALIBRACAO-QUALI-QUANTI-010`.
**Escopo:** correção local.

### 🟠 3. Interferência do ICP-OES ausente, embora o OA-02 peça as de cada técnica
**ID:** `DID-M28-OA02-INTERFERENCIA-OES-AUSENTE-003`
**Tipo:** objetivo parcialmente coberto
**Onde:** Aula 04, seção ICP-OES
**Problema:** o OA-02 pede "as interferências típicas de cada técnica". AAS, ICP-MS e XRF tinham as suas; do ICP-OES só se dizia que o plasma "reduz interferências químicas". O questionário teria de cobrar algo que a aula não ensinou, ou deixar uma técnica de fora.
**Correção aplicada:** quatro frases sobre a interferência espectral (sobreposição direta ou de asa, fundo elevado; contorno por linha alternativa e correção de fundo nos dois lados do pico), e o mesmo no recap. Por ser fato novo, foi **verificado nesta revisão** (Inorganic Ventures, *ICP Operations Guide*, "Spectral Interference: Types, Avoidance and Correction"; ScienceDirect Topics, "Spectral overlap") e registrado como claim `ANINST-M28-A04-INTERFERENCIA-ESPECTRAL-OES-009`, com a fonte acrescentada às Fontes da aula. A próxima auditoria deve reconferir.
**Escopo:** correção local.

### 🟠 4. OA-04 pede cálculo e o exemplo não calcula
**ID:** `DID-M28-OA04-CALCULO-NAO-PRATICADO-004`
**Tipo:** exemplo insuficiente
**Onde:** exemplo do Nb (hoje Aula 06)
**Problema:** o objetivo é "calcular e reportar erros, propagação de incertezas e limites de detecção". O único número trabalhado no bloco era o de Poisson; o LOD e o LOQ chegavam prontos no boletim, e a "incerteza relativa grande demais" nunca era quantificada. O aluno saía sem ter visto um LOD sair de σ e m, nem uma propagação em razão.
**Correção aplicada:** passo "Quanto é 'grande demais'" no exemplo, só com aritmética sobre os valores já dados: σ_branco/m = 1 ppm a partir do LOD, conferência do LOQ = 10 ppm, ~25% de erro relativo a 4 ppm (com a hipótese declarada de que, perto do branco, a incerteza é da ordem da do branco) e propagação em quadratura para Nb/Y com um erro de Y suposto só para o cálculo (3%), mostrando que o termo mais incerto domina a razão. Recap ganhou o bullet de propagação.
**Escopo:** correção local.

### 🟠 5. "Calcular a massa mínima" prometido e nunca feito
**ID:** `DID-M28-A01-CALCULO-MASSA-PROMETIDO-005`
**Tipo:** objetivo declarado não coberto
**Onde:** Aula 01, "Ao final você vai conseguir" e exemplo trabalhado
**Problema:** a aula prometia "calcular, num caso simples, a massa mínima de amostra", mas o exemplo era inteiramente qualitativo e a fórmula de Gy nunca aparece com números (de propósito, e com razão, no nível do módulo). Um questionário alinhado ao cabeçalho cobraria um cálculo que a aula não mostra.
**Correção aplicada:** "Ao final" reformulado para "estimar, pela regra do cubo do diâmetro, quanto cresce a massa mínima"; passo "Ordem de grandeza pela regra do cubo" no exemplo: (8/0,5)³ = 16³ ≈ 4100 vezes, com a ressalva explícita de que os demais fatores de Gy mudam entre as rochas, e o raciocínio inverso (reduzir o tamanho à metade divide a massa mínima por oito, por isso se brita antes de subamostrar). Nenhum fato novo: é a regra d³ já auditada.
**Escopo:** correção local.

### 🟡 6. Durações e palavras declaradas não batiam com o texto
**ID:** `DID-M28-DURACOES-DECLARADAS-006`
**Tipo:** metadado de carga incorreto
**Problema:** a redação declarou 1720/1780/1850/1920/2050 palavras; a contagem real depois da auditoria era 1923/2022/1859/2003/2633. A antiga Aula 05 estava declarada em ~27 min e tinha ~31.
**Correção aplicada:** recontagem por script depois da última edição (~84 palavras/min, convenção dos módulos 26-27) nas seis aulas, com o valor antigo registrado em `recontagem_didatica` nos metadados. Aula 04 em ~28 min **não** foi dividida (arco único plasma → OES → MS → escolha); nenhuma passagem futura deve acrescentar texto a ela sem cortar equivalente.

### 🟡 7. Referências cruzadas de número de aula e pré-requisitos do hub
**ID:** `DID-M28-REFERENCIAS-CRUZADAS-007`
**Tipo:** título/remissão que não corresponde
**Problema:** com a divisão, cinco remissões à "Aula 05" (precisão instrumental, precisão de método, Currie, rigor estatístico das interferências e da calibração) passaram a apontar para a aula errada. O hub dizia "Nenhum [pré-requisito] dentro deste curso" sem mencionar as conexões que as aulas fazem com os Módulos 20, 26 e 27.
**Correção aplicada:** remissões redirecionadas para a Aula 06 (ou Aula 04, no caso da calibração) nas Aulas 01, 02 e 03; "Próxima aula" da Aula 04 reescrita; hub com "Nenhum obrigatório" mais as conexões e o que se assume de fora do curso. As remissões à Aula 05 que tratam de XRF, pérola e pastilha continuam corretas e não foram mexidas.

### 🟡 8. "Métodos analíticos clássicos" no título, sem correspondência no corpo
**ID:** `DID-M28-A02-METODOS-CLASSICOS-TITULO-008`
**Onde:** Aula 02
**Problema:** o título (vindo da ementa) promete métodos clássicos; o corpo trata de preparação e chama fusão e digestão de "clássicas" sem dizer em que sentido. O aluno procura gravimetria e volumetria e não encontra.
**Correção aplicada:** uma frase de escopo: "clássicas" no sentido de virem da análise por via úmida; os procedimentos gravimétricos e volumétricos dessa tradição estão sistematizados em Jeffery & Hutchison (1981), já citado e conferido pela auditoria, e não são detalhados.

### 🟡 9. WDXRF usado antes de definido
**ID:** `DID-M28-A02-WDXRF-ANTES-DE-DEFINIDO-009`
**Onde:** Aula 02, "Duas rotas"
**Problema:** "espectrômetro de fluorescência de raios X de comprimento de onda dispersivo" aparece três aulas antes de a variante ser definida, sem função no argumento.
**Correção aplicada:** "de laboratório".

### 🟡 10. Frase da LOI dizia que ela "mede" a oxidação do Fe
**ID:** `DID-M28-A02-LOI-OXIDACAO-AMBIGUA-010`
**Onde:** Aula 02, "Perda ao fogo"
**Problema:** a frase listava a oxidação de Fe²⁺ entre as coisas que a LOI "mede" e, entre parênteses, dizia que ela aumenta a massa. O leitor sai sem saber para que lado ela empurra o número.
**Correção aplicada:** reescrita em duas frases: a LOI mede sobretudo água estrutural e CO₂; a oxidação de Fe²⁺ age no sentido oposto e mascara parte da perda. Mesmo fato, mesma fonte.

### 🟡 11. "Valor certificado" logo depois da ressalva de que não é certificado
**ID:** `DID-M28-A02-MRC-VALOR-CERTIFICADO-011`
**Onde:** Aula 02, item MRC e último bullet do recap
**Problema:** a correção 4 da auditoria explicou que os materiais do USGS não são certificados em sentido estrito, mas a frase seguinte e o recap continuavam falando em "valor certificado" e chamavam o BHVO-2 de MRC. O recap é o que vira flashcard, e a restrição 6 da auditoria proíbe cobrar "certificado pelo USGS".
**Correção aplicada:** "valor de referência" (que cobre os dois casos) no texto e no recap; o recap distingue MRC em sentido estrito de materiais com valores multilaboratoriais como o BHVO-2.

### 🔵 12. Esquemas dos três arranjos instrumentais
**ID:** `DID-M28-DIAGRAMAS-012`
Fonte → atomizador → monocromador → detector (AAS), tocha → policromador ou cones → quadrupolo (ICP) e tubo → amostra → cristal ou SDD (XRF) estão descritos só em prosa. Um esquema por técnica pouparia releitura. Não aplicado: figura fica para quem publicar o módulo.

### 🔵 13. Prática numérica de calibração e limites
**ID:** `DID-M28-PRATICA-CALIBRACAO-LOD-013`
Uma prática (gerador-de-praticas) com tabela sintética de padrões e de dez leituras de branco, pedindo a reta, a sensibilidade, o LOD, o LOQ e o julgamento de três resultados, fecharia o OA-04 com mãos na massa. Não aplicado: é material novo, não correção.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| OA-01 — planejar amostragem e preparação que controlem homogeneidade e contaminação | Aula 01 (todas as seções); Aula 02 (cadeia de redução, controle de qualidade) | sim (pórfiro × basalto, com a regra do cubo; andesito × sedimento) | — (questionário ainda não gerado) |
| OA-02 — princípios de absorção/emissão atômica e de raios X, com as interferências de cada técnica | Aula 03 (AAS e interferências); Aula 04 (ICP-OES com interferência espectral, ICP-MS e interferências); Aula 05 (XRF e efeitos de matriz) | sim (Ca por AAS; três formas de medir por XRF) | — |
| OA-03 — selecionar AAS, ICP ou XRF por elemento, matriz e concentração | Aula 02 (fusão × digestão); Aula 03 (lugar da AAS); Aula 04 (OES × MS); Aula 05 (WD × ED, pérola × pastilha) | sim (andesito × sedimento; granitoides; três formas de medir) | — |
| OA-04 — calcular erros, propagação e limites de detecção, julgando se o resultado sustenta a interpretação | Aula 04 (curva de calibração e sensibilidade); Aula 06 (Poisson, propagação, LOD/LOQ) | sim (Poisson 10 000 → 40 000; Nb com cálculo de σ/m, erro relativo e propagação em Nb/Y) | — |

Nenhum objetivo sem aula. O questionário deve cobrir as quatro; o OA-04 agora tem o que cobrar em cálculo.

## O que está bem feito

Registrado para que as próximas revisões não estraguem:

1. **Todo exemplo termina em decisão.** Massa de amostra, rota de preparação, chama, técnica de ICP, forma de medir por XRF, uso ou não de um teor: nenhum exemplo para no diagnóstico.
2. **O fio "precisão não é exatidão" atravessa o módulo** e é declarado no hub: amostragem (Aula 01), réplica de preparação × reinjeção (Aula 02), viés de ionização (Aula 03), padrão interno (Aula 04), erro de preparação dominando o de contagem (Aula 06).
3. **Trade-offs em vez de rankings.** Fusão × digestão, chama × forno, OES × MS, WD × ED, pérola × pastilha são sempre apresentados como troca de uma vantagem por um custo conhecido, e a aula diz qual.
4. **Viés sistemático distinguido de erro aleatório** em três lugares diferentes (amostragem incorreta, dissolução incompleta, ionização), o que prepara a leitura crítica de boletins.
5. As correções da auditoria foram bem costuradas: o exemplo do Ca ficou mais instrutivo com a justificativa da chama, e a borda de absorção deu ao item de matriz um critério em vez de uma regra falsa.

## Arquivos alterados

- Aulas 01, 02, 03, 04 (texto e metadados)
- Aula 05: arquivo renomeado e reescrito como Parte 1 (`28-analise-instrumental-i-aula-05-fluorescencia-de-raios-x.md`)
- Aula 06: arquivo novo, Parte 2 (`28-analise-instrumental-i-aula-06-estatistica-de-contagens-limites-de-deteccao.md`)
- Hub do módulo (pré-requisitos, lista de aulas, registro)
- `28-analise-instrumental-i-auditoria.json` (caminhos) e `.md` (aviso de numeração)
- `_curso.md` (contagem de aulas do módulo)
- `course-state.yaml` (lessons, didactic_review, assessment.plan)

Questionário e flashcards: não existem ainda; nada a alterar.
