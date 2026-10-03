# Aula 01: Grandezas, unidades e medida — o que significa medir, e com que incerteza

**ID:** geologia-m27-a01
**Módulo:** [[27-fisica-geociencias-modulo|Módulo 27 — Física para geociências: grandezas, forças e energia]]
**Duração estimada:** ~30 min
**Nível:** ensino médio completo, sem geologia prévia (contrato `ensino-medio-sem-geologia-v1`)
**Objetivo:** distinguir grandeza, unidade e dimensão, converter unidades do SI e declarar a incerteza de uma medida.

## Antes de começar, você precisa saber

- Ordens de grandeza e notação científica — [[00-partida-do-zero-aula-03-ordens-de-grandeza|Módulo 00, aula 03]] (revisão recomendada, não exigida).
- Nenhum pré-requisito formal: este é o primeiro nó da trilha de apoio (Física), com `prerequisites: []`.

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Grandeza física** | Qualquer coisa que pode ser medida e expressa por um número: comprimento, massa, tempo, temperatura. |
| **Unidade** | O padrão de comparação usado para medir uma grandeza — o metro para comprimento, o quilograma para massa. |
| **Dimensão** | A natureza física de uma grandeza (comprimento, massa, tempo...), independente da unidade escolhida para medi-la. |
| **Algarismo significativo** | Cada dígito de uma medida que carrega informação real sobre a precisão do instrumento usado. |
| **Incerteza (erro)** | A faixa de valores dentro da qual o valor verdadeiro provavelmente está, dada a resolução do instrumento e do método. |
| **Precisão** | O quanto medidas repetidas do mesmo objeto concordam entre si. |
| **Exatidão** | O quanto uma medida está próxima do valor verdadeiro. |

## Conteúdo

### O que significa medir

Quando você compara o comprimento de uma mesa com uma régua, não está descobrindo um número absoluto — está comparando a mesa com um padrão já combinado: o centímetro. Toda medida é, no fundo, essa mesma comparação: pegar algo desconhecido e contar quantas vezes um padrão conhecido cabe nele. Esse padrão é a **unidade**, e a característica que ela mede — comprimento, massa, tempo, temperatura — é a **grandeza física**.

Grandezas diferentes não se misturam: comprimento e massa são **dimensões** diferentes, e não faz sentido somar 5 metros com 3 quilogramas, mesmo que os números pareçam compatíveis. Em geociências isso importa o tempo todo — a espessura de uma camada (comprimento), a idade de uma rocha (tempo) e a densidade de um mineral (massa por volume) são três dimensões distintas, cada uma com sua própria unidade no Sistema Internacional (SI): metro (m) para comprimento, quilograma (kg) para massa, segundo (s) para tempo, kelvin (K) para temperatura.

### Convertendo unidades sem perder o controle

Uma receita culinária escrita em xícaras só funciona se você souber quantos mililitros cabem numa xícara — é essa mesma lógica de **fator de conversão** que transforma uma medida de uma unidade em outra. Em geociências, a mesma grandeza aparece com unidades diferentes conforme a escala: espessura de uma lâmina delgada em micrômetros (µm), espessura de uma camada em metros, espessura crustal em quilômetros; idade de um mineral em anos, de uma formação em milhões de anos (Ma), da Terra em bilhões de anos (Ga, ver [[03-tempo-geologico-geocronologia-modulo|Módulo 03]]).

O procedimento é sempre o mesmo: multiplicar pelo fator que transforma a unidade de origem na unidade de destino, mantendo a grandeza (a dimensão) intacta. Por exemplo, 2,5 km de espessura crustal equivalem a 2.500 m — o fator 1.000 m/km não muda **o que** está sendo medido, só **em que unidade** o resultado é expresso. Um erro clássico de conversão (esquecer uma potência de dez) é o tipo de engano que pode transformar uma espessura de camada razoável em algo fisicamente absurdo — por isso conferir a ordem de grandeza do resultado, como já visto no Módulo 00, é sempre o último passo.

### Toda medida vem com uma incerteza

Nenhuma medida é perfeitamente exata — nem a mais cuidadosa. Se você mede a espessura de uma camada sedimentar com uma trena marcada em centímetros, o melhor que consegue afirmar é que a espessura está entre duas marcas vizinhas: a resolução do instrumento limita quão fina pode ser a sua leitura. Essa faixa de dúvida em torno do valor lido é a **incerteza**, também chamada de erro (não no sentido de "engano", mas no sentido técnico de margem inevitável).

Por convenção, uma medida completa se escreve como valor ± incerteza — por exemplo, "12,4 ± 0,1 m". Isso não significa que o geólogo "errou" a medida; significa que ele está sendo honesto sobre a resolução do que usou para medir. O número de **algarismos significativos** de uma medida já comunica parte dessa informação: escrever "12 m" sugere um instrumento menos fino que escrever "12,40 m" — o segundo afirma confiança até o centímetro, o primeiro não.

### Precisão não é exatidão

> [!tip] Uma analogia Pense em três tentativas de acertar o centro de um alvo. Se todos os tiros caem próximos uns dos outros, mas longe do centro, você tem **precisão** sem **exatidão** — o método é consistente, mas mal calibrado. Se os tiros caem espalhados, mas a média deles é o centro, você tem exatidão sem precisão. O ideal é ter as duas coisas: tiros próximos entre si **e** próximos do centro.

Em geocronologia (datação radiométrica, [[03-tempo-geologico-geocronologia-aula-04-meia-vida|Módulo 03, aula 04]]), essa distinção é concreta: um laboratório pode produzir idades muito consistentes entre repetições da mesma amostra (alta precisão) mas sistematicamente deslocadas da idade real por um problema de calibração do equipamento (baixa exatidão) — ou o contrário, medidas dispersas que, em média, acertam o valor certo. Um resultado de idade sempre vem publicado como "idade ± incerteza" exatamente para que outros pesquisadores possam avaliar os dois aspectos separadamente, e não só o número central.

### Notação científica: expressar magnitude e precisão juntas

A notação científica (já usada no Módulo 00 para ordens de grandeza) tem uma vantagem extra aqui: separa claramente a magnitude do número dos seus algarismos significativos. Escrever a idade de um zircão como 4,4 × 10⁹ anos deixa explícito que a medida tem dois algarismos significativos (4 e 4), sem o risco de ambiguidade que "4.400.000.000 anos" carregaria — quantos daqueles zeros são realmente conhecidos, e quantos são só posição decimal? Essa é a mesma razão pela qual, sob a regra **LC-05** deste curso, aulas introdutórias preferem "cerca de 30–50 km" de espessura crustal a um valor de precisão de laboratório: a ordem de grandeza correta comunica mais honestidade científica do que uma falsa precisão.

## Exemplo trabalhado

**Situação:** em campo, você mede a espessura de uma camada de arenito com uma trena graduada em centímetros. Você lê o topo da camada em 214 cm e a base em 96 cm, numa parede de afloramento vertical.

**Pergunta 1: qual é a espessura da camada, e com que incerteza deve ser reportada?**

A espessura é a diferença entre as duas leituras: 214 cm − 96 cm = 118 cm = 1,18 m. Como a trena tem resolução de 1 cm, cada leitura individual carrega uma incerteza de aproximadamente ± 0,5 cm; ao subtrair duas leituras, as incertezas se somam, resultando em uma incerteza total de aproximadamente ± 1 cm. A espessura deve ser reportada como 118 ± 1 cm (ou 1,18 ± 0,01 m) — não simplesmente como "118 cm", que esconderia essa margem.

**Pergunta 2: se um colega reportasse a mesma camada como tendo "118,347 cm" de espessura, o que estaria errado?**

O número tem mais algarismos significativos do que a trena consegue sustentar. Nenhuma trena graduada em centímetros permite ler frações de milímetro com confiança; reportar "118,347 cm" transmite uma falsa precisão — o instrumento simplesmente não suporta essa afirmação, mesmo que o cálculo aritmético "dê" esse número.

**A lição:** o instrumento usado limita quantos algarismos significativos uma medida pode honestamente carregar, e essa mesma lógica escala de uma trena de campo até um espectrômetro de massa em laboratório de geocronologia.

## Erros comuns

- **Tratar um valor sem incerteza declarada como se fosse exato.** Toda medida real tem uma margem; omitir a incerteza não a elimina, só a esconde.
- **Confundir precisão com exatidão.** Medidas muito consistentes entre si podem ainda estar sistematicamente erradas se o método ou o instrumento estiver mal calibrado.
- **Reportar mais algarismos significativos do que o instrumento sustenta.** A calculadora não sabe quantos dígitos você mediu de verdade — quem decide isso é a resolução do instrumento, não a quantidade de casas decimais que aparecem na tela.
- **Errar uma potência de dez ao converter unidades.** É o erro de conversão mais comum e o mais fácil de pegar conferindo se a ordem de grandeza do resultado faz sentido físico.

## O que não concluir

- **Que esta aula ensina como propagar incerteza através de cálculos complexos (soma de várias fontes de erro, médias ponderadas).** Essa ferramenta estatística mais completa fica para o [[28-matematica-geociencias-modulo|Módulo 28]], aula 04 (estatística descritiva), quando esse módulo for escrito.
- **Que declarar a incerteza substitui a prática de campo.** Saber a convenção "valor ± incerteza" não ensina, por si só, a escolher o instrumento certo ou a técnica de medição correta — isso é conteúdo do [[20-metodos-campo-mapeamento-modulo|Módulo 20]].

## Recap relâmpago

- Toda **grandeza física** (comprimento, massa, tempo, temperatura) é medida comparando-a com uma **unidade** padrão; grandezas de dimensões diferentes não se somam.
- **Converter unidades** significa multiplicar por um fator que preserva a grandeza, mudando só a unidade em que ela é expressa — sempre conferir a ordem de grandeza do resultado.
- Toda medida real carrega uma **incerteza**, ligada à resolução do instrumento; a convenção é reportá-la como valor ± incerteza.
- **Precisão** (consistência entre medidas) e **exatidão** (proximidade do valor verdadeiro) são propriedades independentes uma da outra.
- O número de **algarismos significativos** de uma medida comunica, por si só, o nível de confiança que ela sustenta — reportar dígitos além da resolução do instrumento é falsa precisão.

## Próxima aula

[[27-fisica-geociencias-aula-02-forca-massa-leis-de-newton|Aula 02 — Força, massa e as leis de Newton]]

## Fontes

- Sistema Internacional de Unidades (SI): Bureau International des Poids et Mesures (BIPM).
- Grandezas, unidades, algarismos significativos, precisão e exatidão: física geral básica (ex.: Halliday, Resnick & Walker, *Fundamentals of Physics*).
- Convenção de reportar idade radiométrica como valor ± incerteza: prática consolidada de geocronologia (ver também Módulo 03 deste curso).

<!--
nivel: ensino-medio-sem-geologia-v1
palavras_corpo: ~1450
bridge_lesson: false

mapa_objetivo_secao:
  OA-01: "O que significa medir" + "Convertendo unidades sem perder o controle" + "Toda medida vem com uma incerteza" + "Precisão não é exatidão" + "Notação científica: expressar magnitude e precisão juntas" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M27-A01-GRANDEZA-UNIDADE-001
    claim: "Uma grandeza física é medida por comparação com uma unidade padrão; grandezas de dimensões diferentes (ex.: comprimento e massa) não podem ser somadas entre si."
    risk: fato
    source: "física geral básica; SI (BIPM)"
  - claim_id: GEO-M27-A01-INCERTEZA-002
    claim: "Toda medida experimental carrega uma incerteza associada à resolução do instrumento, convencionalmente reportada como valor ± incerteza."
    risk: fato
    source: "física geral básica; prática de metrologia"
  - claim_id: GEO-M27-A01-PRECISAO-EXATIDAO-003
    claim: "Precisão (consistência entre medidas repetidas) e exatidão (proximidade do valor verdadeiro) são conceitos independentes: um conjunto de medidas pode ser preciso sem ser exato, ou exato sem ser preciso."
    risk: fato
    source: "física geral básica; metrologia"
  - claim_id: GEO-M27-A01-SIGFIG-004
    claim: "O número de algarismos significativos de uma medida deve refletir a resolução real do instrumento usado; reportar mais dígitos do que o instrumento sustenta constitui falsa precisão."
    risk: fato
    source: "física geral básica; convenções de notação científica"
  - claim_id: GEO-M27-A01-GEOCRON-INCERTEZA-005
    claim: "Idades radiométricas são convencionalmente publicadas como valor ± incerteza, permitindo avaliar separadamente a precisão e a exatidão do método de datação."
    risk: interpretacao
    source: "prática consolidada de geocronologia (consistente com o Módulo 03 deste curso)"

nota_trilha_apoio: >-
  Aula 1 de 6 do módulo 27 (trilha de apoio, opcional, não bloqueante), criada em
  2026-08-19. Primeira aula da trilha de apoio de Física; sem pré-requisito formal.
  Reativa e aprofunda a notação científica e a ordem de grandeza já vistas no
  Módulo 00, aula 03, com foco em incerteza de medida — preparo recomendado antes
  do Módulo 17 (Geologia estrutural) e de leitura crítica de dados geocronológicos.
-->
