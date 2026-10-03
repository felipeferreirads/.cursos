# Aula 04: Percolação de água em meios porosos e fissurados: equações e determinação em campo e laboratório

**ID:** geologia-avancado-m06-a04
**Módulo:** [[06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]]
**Duração estimada:** ~29 min
**Nível:** avançado (especialização em geologia)
**Objetivo:** formular o problema de percolação em solos e maciços fissurados pela equação de Laplace, interpretar redes de fluxo para obter vazão e poropressão, calcular a força de percolação e o risco de piping, e selecionar o ensaio adequado — laboratório (carga constante, carga variável), campo (Lugeon, slug test) — para determinar a condutividade hidráulica.

**Pré-requisito:** Aula 03 deste módulo (tensão efetiva, gradiente crítico); lei de Darcy e condutividade hidráulica, do Módulo 01, Aula 02; lei cúbica de fluxo em descontinuidades, do Módulo 05, Aula 04.

## Antes de começar, você precisa saber

- A lei de Darcy na forma v = k·i, com i = Δh/L o gradiente hidráulico e k a condutividade hidráulica (Módulo 01, Aula 02).
- Que carga hidráulica total é a soma da carga de elevação e da carga de pressão (h = z + u/γw), e que a água flui de carga total maior para menor — nunca simplesmente "de cima para baixo".
- Que a vazão através de uma fratura plana é proporcional ao cubo da abertura (lei cúbica, Módulo 05, Aula 04).

## Conteúdo

### Da hidrogeologia à geotecnia: a mesma lei, outra pergunta

O Módulo 01 tratou o fluxo subterrâneo com a pergunta do hidrogeólogo: quanta água há, de onde vem, quanto se pode extrair. Aqui a lei de Darcy é a mesma, mas a pergunta é do geotécnico e tem duas partes: **quanta água atravessa a obra** (vazão a bombear de uma escavação, perda por sob uma barragem) e, mais importante, **que poropressão o fluxo instala no maciço** — porque, pela Aula 03, é u que define σ' e, portanto, a estabilidade. Em geotecnia a água raramente é o produto; é a variável que decide se a obra fica de pé.

### A equação de Laplace e a rede de fluxo

Combinando a lei de Darcy com a continuidade (o que entra num elemento de solo sai dele, em regime permanente e meio saturado incompressível), obtém-se, para meio homogêneo e isotrópico, a **equação de Laplace** em duas dimensões:

∂²h/∂x² + ∂²h/∂z² = 0

Sua solução gráfica clássica é a **rede de fluxo** (*flow net*): duas famílias de curvas ortogonais entre si — as **linhas de fluxo**, que traçam o caminho da água, e as **linhas equipotenciais**, que unem pontos de mesma carga hidráulica total. Traçada corretamente com "quadrados" curvilíneos, a rede fornece diretamente dois resultados:

- **Vazão:** Q = k · H · (Nf/Nd), onde H é a perda de carga total entre montante e jusante, Nf o número de canais de fluxo e Nd o número de quedas de potencial.
- **Poropressão em qualquer ponto:** conta-se quantas quedas de potencial ocorreram até o ponto, obtém-se a carga total ali, e subtrai-se a cota (u = γw·(h − z)).

É o segundo resultado que importa mais em estabilidade. A rede de fluxo é, na prática, uma máquina de gerar o campo de poropressões que a análise de tensão efetiva vai consumir.

> [!important] Fluxo não segue "para baixo", segue o gradiente de carga total
> Numa escavação escorada abaixo do NA, a água desce do lado de fora, contorna a ficha da parede e **sobe** do lado de dentro — fluxo ascendente exatamente onde está o fundo da escavação, que é a região crítica da Aula 03. O sentido do fluxo é dado pela queda de h = z + u/γw, não pela gravidade isoladamente.

### Anisotropia e estratificação

Solos sedimentares são quase sempre estratificados, e a condutividade horizontal (kh) costuma superar a vertical (kv) por uma ordem de grandeza ou mais — camadas finas de silte intercaladas atuam como barreiras ao fluxo vertical, mas não ao horizontal. Para um pacote de n camadas de espessuras Hi e condutividades ki, as condutividades equivalentes são:

- **Paralelo às camadas (horizontal):** k_h,eq = Σ(ki·Hi)/ΣHi — uma **média aritmética ponderada**, dominada pela camada **mais permeável** (o fluxo escolhe o caminho fácil e passa por ela).
- **Perpendicular às camadas (vertical):** k_v,eq = ΣHi/Σ(Hi/ki) — uma **média harmônica**, dominada pela camada **menos permeável** (toda a água é obrigada a atravessar o gargalo).

Essa assimetria explica por que uma única camada delgada de argila num pacote arenoso muda pouco o fluxo horizontal e muda radicalmente o vertical. Quando kh ≠ kv, a equação de Laplace só volta a valer após uma **transformação de escala** do desenho (comprimindo o eixo x pelo fator √(kv/kh)), traçando a rede no domínio transformado e usando k_eq = √(kh·kv) no cálculo da vazão.

### Força de percolação e piping

A água em movimento arrasta os grãos. Essa ação, distribuída no volume, é a **força de percolação** (*seepage force*), com valor por unidade de volume:

j = i · γw

Ela atua na direção do fluxo. Fluxo descendente comprime o esqueleto e aumenta σ'; fluxo ascendente alivia e reduz σ'. Quando o gradiente ascendente atinge o gradiente crítico icr = γsub/γw (Aula 03), a força de percolação iguala o peso submerso e a tensão efetiva zera.

Dois modos de ruptura hidráulica devem ser distinguidos:

- **Levantamento de fundo (*heave*):** a massa de solo sobe em bloco quando σ' zera numa área ampla. É o fenômeno diretamente descrito por icr.
- **Erosão regressiva (*piping*):** a erosão começa num ponto de saída concentrada (pé de barragem, junto a uma estrutura) e progride **para montante**, escavando um tubo. É um mecanismo progressivo e localizado, que pode iniciar-se em gradientes locais bem abaixo de icr médio, e é a causa histórica mais comum de ruptura de barragens de terra.

Por isso o projeto não se contenta com "gradiente médio menor que 1": aplica-se um fator de segurança (usualmente FS ≥ 3 a 4 contra piping) e, sobretudo, instalam-se **filtros de proteção** graduados, que deixam a água sair mas retêm as partículas — a defesa efetiva contra erosão regressiva não é reduzir o fluxo, é controlar a saída.

### Determinação em laboratório

- **Permeâmetro de carga constante** (ASTM D2434): mantém-se Δh fixa e mede-se o volume coletado num intervalo. k = (Q·L)/(A·Δh·t). Adequado a solos **granulares** (k > 10⁻⁵ m/s aproximadamente), onde a vazão é medível em tempo razoável.
- **Permeâmetro de carga variável** (ASTM D5084 e correlatos): acompanha-se a queda do nível num tubo fino de área a, ao longo do tempo. k = (a·L)/(A·t) · ln(h1/h2). Adequado a solos **finos** (siltes, argilas), onde a vazão é pequena demais para o método de carga constante.
- **Indiretamente**, pelo ensaio de adensamento (Aula 05), a partir do coeficiente de adensamento cv — útil justamente na faixa de argilas onde a medição direta é mais lenta e difícil.

> [!warning] Ensaio de laboratório mede o corpo de prova, não o maciço
> A condutividade de um maciço real é dominada por feições que não cabem num corpo de prova de 10 cm: fissuras, lentes arenosas, raízes, juntas, contatos de camadas. Não é incomum que k de campo exceda o de laboratório em uma a três ordens de grandeza no mesmo material. Ensaio de laboratório dá o valor da matriz; para o maciço, ensaie o maciço.

### Determinação em campo, em solos e em maciços fissurados

- **Ensaios de bombeamento** em poço, com poços de observação (Módulo 01, Aula 05): fornecem a condutividade de um volume grande e representativo, e são a referência quando há aquífero explorável.
- **Slug test** (ensaio de carga instantânea): impõe-se uma variação brusca de nível num furo e acompanha-se a recuperação. Rápido e barato, adequado a investigação geotécnica de rotina e a solos de baixa a média permeabilidade; interpretado por soluções como Hvorslev ou Bouwer & Rice.
- **Ensaio Lugeon (ou de perda d'água sob pressão)**, em maciço rochoso: injeta-se água num trecho de furo isolado por obturadores (*packers*), sob pressão constante, e mede-se a absorção. Uma **unidade Lugeon (UL)** é definida como a absorção de 1 litro por metro de furo por minuto sob pressão de 1 MPa (≈10 bar), e corresponde a uma condutividade da ordem de 10⁻⁷ m/s. É o ensaio padrão para decidir tratamento de fundação de barragem por injeções de calda.

Em **meios fissurados**, o fluxo não é da matriz e sim das descontinuidades, e por isso obedece à **lei cúbica** (Módulo 05, Aula 04): a vazão é proporcional ao **cubo** da abertura hidráulica. A consequência prática é dramática — dobrar a abertura de uma fratura multiplica sua vazão por oito, e uma única fratura aberta pode conduzir mais água que todo o resto do maciço somado. Daí a característica que separa os dois meios: em solo, k é uma propriedade razoavelmente contínua do material; em rocha fraturada, a condutividade é **fortemente heterogênea e direcional**, controlada pela geometria e conectividade das famílias de descontinuidades — motivo pelo qual o ensaio Lugeon é feito trecho a trecho ao longo do furo, e não como valor único da sondagem.

## Exemplo trabalhado

**Situação:** uma escavação escorada tem parede-diafragma com ficha abaixo do fundo. A rede de fluxo traçada tem Nf = 4 canais de fluxo e Nd = 12 quedas de potencial, com perda de carga total H = 6 m. A areia tem k = 2×10⁻⁵ m/s, γsat = 20 kN/m³ e a extensão da escavação é 30 m. Estime (a) a vazão de infiltração e (b) o fator de segurança contra levantamento de fundo, sabendo que, junto ao fundo da escavação, o último elemento da rede tem 0,5 m de comprimento. Use γw = 9,81 kN/m³.

**Resolução:**

**(a) Vazão.** Por metro de comprimento da escavação:
q = k · H · (Nf/Nd) = 2×10⁻⁵ × 6 × (4/12) = 2×10⁻⁵ × 6 × 0,3333 = 4,0×10⁻⁵ m³/s por metro

Para os 30 m de extensão:
Q = 4,0×10⁻⁵ × 30 = 1,2×10⁻³ m³/s ≈ **1,2 L/s** (cerca de 72 L/min a bombear em regime permanente)

**(b) Gradiente de saída e fator de segurança.** A perda de carga em cada queda de potencial é:
Δh_por_queda = H/Nd = 6/12 = 0,5 m

No último elemento antes da saída, essa queda ocorre ao longo de L = 0,5 m, logo o gradiente de saída é:
i_saída = 0,5/0,5 = **1,0**

Gradiente crítico:
γsub = 20 − 9,81 = 10,19 kN/m³
icr = γsub/γw = 10,19/9,81 = **1,04**

Fator de segurança contra levantamento de fundo:
FS = icr/i_saída = 1,04/1,0 = **1,04**

**Interpretação:** a vazão é modesta e facilmente bombeável — não é o problema. O problema é o FS de 1,04: o fundo da escavação está praticamente no limiar da liquefação por fluxo ascendente, sem margem nenhuma. Um FS aceitável contra levantamento de fundo é da ordem de 1,5 a 2, e contra piping ainda maior. Este é o padrão típico do problema geotécnico de percolação: a vazão parece tranquilizadora enquanto o campo de poropressões que a acompanha está prestes a anular a tensão efetiva. As medidas corretivas atuam sobre o gradiente, não sobre a vazão — aprofundar a ficha da parede (alongando o caminho de percolação e reduzindo i), rebaixar o lençol por poços a montante, ou lastrear o fundo com filtro graduado.

## Erros comuns

- **Confundir vazão com perigo.** Vazão alta é um problema de bombeamento; gradiente de saída alto é um problema de estabilidade. Escavações rompem por gradiente, não por litros.
- **Usar média aritmética para condutividade vertical de um pacote estratificado.** A vertical é média harmônica, dominada pela camada menos permeável; usar a aritmética superestima kv em ordens de grandeza.
- **Traçar rede de fluxo em meio anisotrópico sem a transformação de escala**, e depois usar k em vez de √(kh·kv) na vazão.
- **Extrapolar k de laboratório para o maciço** sem reconhecer que fissuras e lentes dominam o fluxo real.
- **Verificar apenas heave e ignorar piping.** Piping inicia em gradientes locais bem abaixo do crítico médio e é a causa mais frequente de ruptura de barragens de terra; a defesa é filtro graduado, não apenas gradiente médio baixo.
- **Aplicar a lei de Darcy linear a fluxo turbulento** em enrocamentos, pedregulhos muito grossos ou fraturas de grande abertura sob alto gradiente — fora do regime laminar, a proporcionalidade v = k·i deixa de valer.

## O que não concluir

- **Que reduzir a vazão resolve o risco de erosão interna.** Uma cortina de vedação mal executada pode reduzir a vazão total e, ao mesmo tempo, **concentrar** o fluxo restante em pontos de saída, elevando gradientes locais e piorando o risco de piping.
- **Que uma unidade Lugeon corresponde a um k único e universal.** A conversão UL → k (≈10⁻⁷ m/s por UL) é uma aproximação de ordem de grandeza, dependente da geometria do trecho ensaiado e da hipótese de fluxo radial; o valor de projeto é a própria absorção medida, não a conversão.
- **Que a lei cúbica descreve fraturas reais com precisão.** Ela vale rigorosamente para placas paralelas lisas; rugosidade, tortuosidade e pontos de contato reduzem a vazão real, e a "abertura hidráulica" que satisfaz a lei é menor que a abertura mecânica medida.

## Recap relâmpago

- Em geotecnia a percolação importa menos pela vazão e mais pelo **campo de poropressões** que instala, porque é u que define σ' e a estabilidade.
- A equação de Laplace (∂²h/∂x² + ∂²h/∂z² = 0) resolve-se graficamente pela rede de fluxo: Q = k·H·(Nf/Nd), e a poropressão sai da contagem de quedas de potencial.
- Em pacotes estratificados, kh,eq é média **aritmética** ponderada (domina a camada mais permeável) e kv,eq é média **harmônica** (domina a menos permeável); com anisotropia, transforma-se a escala e usa-se √(kh·kv).
- Força de percolação j = i·γw; fluxo ascendente reduz σ'. **Heave** (levantamento em bloco, governado por icr) e **piping** (erosão regressiva localizada, que inicia abaixo de icr) são mecanismos distintos — a defesa contra piping é filtro graduado.
- Laboratório: carga constante para granulares, carga variável para finos. Campo: bombeamento, slug test em solo; **Lugeon** (1 L/m/min a 1 MPa) em rocha, trecho a trecho.
- Em meio fissurado o fluxo é das descontinuidades e segue a **lei cúbica** — a condutividade é heterogênea e direcional, não uma propriedade contínua do material.

## Próxima aula

[[06-elementos-de-geomecanica-aula-05-compressibilidade-adensamento-recalques|Aula 05 — Compressibilidade e adensamento: ensaio edométrico, cálculo de recalques e deformabilidade de maciços]]

## Anterior

[[06-elementos-de-geomecanica-aula-03-tensoes-totais-efetivas-neutras-k0|Aula 03 — Tensões totais, efetivas e neutras; pressões geostáticas e o coeficiente K0]]

## Fontes

- Equação de Laplace, redes de fluxo, condutividade equivalente de pacotes estratificados e força de percolação: Das, B. M. (2019), *Fundamentos de Engenharia Geotécnica*, 9ª ed., Cengage, cap. 7 e 9.
- Fundamentos de percolação, piping e filtros de proteção: Terzaghi, K., Peck, R. B. & Mesri, G. (1996), *Soil Mechanics in Engineering Practice*, 3ª ed., Wiley, cap. 2 e 4; Cedergren, H. R. (1989), *Seepage, Drainage, and Flow Nets*, 3ª ed., Wiley.
- Ensaios de laboratório: ASTM D2434 (permeâmetro de carga constante); ASTM D5084 (permeabilidade de materiais de baixa condutividade, carga variável e métodos correlatos).
- Ensaio de perda d'água sob pressão e a unidade Lugeon: Lugeon, M. (1933), *Barrages et Géologie*, Dunod; Houlsby, A. C. (1976), "Routine interpretation of the Lugeon water-test", *Quarterly Journal of Engineering Geology*, 9(4), p. 303–313.
- Interpretação de slug tests: Hvorslev, M. J. (1951), *Time Lag and Soil Permeability in Ground-Water Observations*, US Army Corps of Engineers, Bulletin 36; Bouwer, H. & Rice, R. C. (1976), "A slug test for determining hydraulic conductivity of unconfined aquifers", *Water Resources Research*, 12(3), p. 423–428.
- Lei cúbica e fluxo em meios fissurados: Witherspoon, P. A., Wang, J. S. Y., Iwai, K. & Gale, J. E. (1980), "Validity of cubic law for fluid flow in a deformable rock fracture", *Water Resources Research*, 16(6), p. 1016–1024 (retomando o Módulo 05, Aula 04).

<!--
nivel: avancado
palavras_corpo: ~1980

mapa_objetivo_secao:
  geologia-avancado-m06-oa02: "Da hidrogeologia à geotecnia: a mesma lei, outra pergunta" + "A equação de Laplace e a rede de fluxo" + "Anisotropia e estratificação" + "Força de percolação e piping" + "Determinação em laboratório" + "Determinação em campo, em solos e em maciços fissurados" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEOMEC-M06-A04-LAPLACE-001
    claim: "Para meio homogêneo, isotrópico e saturado em regime permanente, o fluxo obedece à equação de Laplace, e a rede de fluxo fornece Q=k·H·(Nf/Nd) e a poropressão por contagem de quedas de potencial."
    risk: fato
    source: "Das 2019, cap. 7; Cedergren 1989"
  - claim_id: GEOMEC-M06-A04-ESTRATIF-002
    claim: "Em pacotes estratificados, k horizontal equivalente é média aritmética ponderada (dominada pela camada mais permeável) e k vertical equivalente é média harmônica (dominada pela menos permeável); com anisotropia usa-se transformação de escala √(kv/kh) e k_eq=√(kh·kv)."
    risk: fato
    source: "Das 2019, cap. 7"
  - claim_id: GEOMEC-M06-A04-SEEPAGE-003
    claim: "A força de percolação por unidade de volume é j=i·γw, atuando na direção do fluxo; fluxo ascendente reduz a tensão efetiva."
    risk: fato
    source: "Das 2019, cap. 9; Terzaghi, Peck & Mesri 1996, cap. 2"
  - claim_id: GEOMEC-M06-A04-PIPING-004
    claim: "Heave (levantamento de fundo em bloco, governado por icr) e piping (erosão regressiva localizada, que pode iniciar em gradientes locais abaixo de icr) são mecanismos distintos; a defesa contra piping é o filtro graduado, com FS usual de 3 a 4."
    risk: fato
    source: "Terzaghi, Peck & Mesri 1996, cap. 2 e 4; Cedergren 1989"
  - claim_id: GEOMEC-M06-A04-ENSAIOS-005
    claim: "Permeâmetro de carga constante (ASTM D2434) aplica-se a solos granulares e o de carga variável (ASTM D5084 e correlatos) a solos finos; k de campo pode exceder o de laboratório em 1 a 3 ordens de grandeza por efeito de feições do maciço."
    risk: fato
    source: "ASTM D2434; ASTM D5084; Das 2019, cap. 7"
  - claim_id: GEOMEC-M06-A04-LUGEON-006
    claim: "Uma unidade Lugeon é a absorção de 1 litro por metro de furo por minuto sob pressão de 1 MPa (≈10 bar), correspondendo a condutividade da ordem de 10⁻⁷ m/s — conversão aproximada, dependente da geometria do trecho."
    risk: fato
    source: "Lugeon 1933; Houlsby 1976"
  - claim_id: GEOMEC-M06-A04-CUBICA-007
    claim: "Em meios fissurados o fluxo é dominado pelas descontinuidades e segue a lei cúbica (Q proporcional ao cubo da abertura hidráulica), tornando a condutividade heterogênea e direcional; a abertura hidráulica é menor que a mecânica por efeito de rugosidade e contatos."
    risk: fato
    source: "Witherspoon et al. 1980 (retomando Módulo 05, Aula 04)"
-->
