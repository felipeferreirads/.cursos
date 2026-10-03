# Aula 07: Lendo o mapa — estruturas em mapas geológicos, Parte 2: falhas em mapa e seção geológica

**ID:** geologia-m17-a07
**Módulo:** [[17-geologia-estrutural-modulo|Módulo 17 — Geologia estrutural e deformação]]
**Duração estimada:** ~20 min
**Nível:** iniciante (contrato `iniciante-absoluto-v1`)
**Objetivo:** reconhecer o traço de uma falha em mapa geológico e construir a lógica de uma seção geológica simples a partir de dados de mapa, incluindo o conceito de mergulho aparente.

## Antes de começar, você precisa saber

- Direção (strike), mergulho (dip) e o símbolo de atitude em mapa geológico, e os dois padrões em "V" (regra do V e V do caimento) — [[17-geologia-estrutural-aula-06-mapas-e-secoes-estruturais-parte-1-atitude-e-padroes-de-afloramento|aula 06 (Parte 1) deste módulo]].
- Os tipos de falha (**normal**, **reversa/cavalgamento**, **transcorrente**) e os termos **bloco de teto** e **bloco de muro** — [[17-geologia-estrutural-aula-04-falhas-anatomia-e-classificacao|aula 04 deste módulo]].

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Traço da falha** | A linha, em mapa, onde o plano de falha intercepta a superfície topográfica — geralmente com símbolo indicando o bloco de teto (ticks ou bolinhas no lado que desceu, no caso de falhas normais). |
| **Seção geológica (perfil)** | Um corte vertical imaginário do terreno, ao longo de uma linha escolhida no mapa, que mostra como as unidades de rocha e as estruturas se organizam em profundidade. |
| **Mergulho aparente** | O ângulo de mergulho observado numa seção que não está exatamente perpendicular à direção da camada — sempre menor ou igual ao mergulho real (verdadeiro). |

## Conteúdo

### Como falhas aparecem em mapa

O **traço da falha** em mapa é a linha onde o plano de falha intercepta a topografia. Diferente de um simples contato entre unidades de rocha, o traço de falha costuma truncar abruptamente as camadas dos dois lados, em vez de seguir um contato gradual — um sinal visual de que há uma descontinuidade estrutural, não apenas uma mudança de unidade. Mapas geológicos padronizam símbolos para indicar o tipo de falha: por exemplo, pequenos traços perpendiculares (ticks) do lado do bloco que desceu, comuns em falhas normais, ou símbolos de "dentes" (triângulos) apontando para o bloco de teto, convencionalmente usados para indicar cavalgamentos.

### Da vista de cima ao corte vertical: construindo uma seção geológica

Um mapa mostra onde as estruturas afloram na superfície, mas a pergunta que frequentemente importa mais — para entender a geometria completa, ou para prever o que existe em profundidade — é como essas estruturas continuam **abaixo** da superfície. A ferramenta para responder isso é a **seção geológica (perfil)**: um corte vertical imaginário ao longo de uma linha escolhida no mapa, no qual se projetam, para baixo, as atitudes medidas (direção e mergulho, vistas na Parte 1) e os contatos observados na superfície.

A lógica básica de construção é: para cada unidade de rocha e cada estrutura (contato, falha, eixo de dobra) que a linha de seção cruza no mapa, projeta-se o mergulho observado (ou inferido) para baixo da superfície topográfica, mantendo a espessura das camadas e a geometria das dobras e falhas consistentes com o que foi medido. O resultado é uma imagem lateral da estrutura — o mesmo tipo de imagem que aparece nos diagramas de anticlinal/sinclinal e de falha normal/reversa usados nas aulas 03 e 04, mas agora derivada de dados reais de mapa, não desenhada de forma idealizada.

Um cuidado importante nessa construção é o **mergulho aparente**: se a linha de seção não for exatamente perpendicular à direção (strike) da camada, o ângulo de mergulho que aparece no corte não é o mergulho real medido em campo, mas um valor menor, chamado mergulho aparente. Ignorar essa diferença é uma fonte comum de erro ao transferir uma medida de campo diretamente para uma seção que corta a estrutura numa direção oblíqua.

## Erros comuns

- **Achar que o traço de uma falha em mapa é sempre uma linha reta.** Como qualquer outra superfície inclinada, o plano de falha também produz um traço que segue o relevo topográfico, exceto quando o plano de falha é exatamente vertical.
- **Usar o mergulho medido em campo diretamente numa seção que não é perpendicular à direção da camada.** Isso produz um ângulo incorreto na seção — o valor correto a usar, nesse caso, é o mergulho aparente, sempre menor ou igual ao mergulho real.

## O que não concluir

- **Que esta aula ensinou a construir seções geológicas complexas com múltiplas dobras e falhas superpostas, ou a usar métodos gráficos avançados (como projeção estereográfica) para essa reconstrução.** O tratamento aqui cobriu a lógica conceitual básica — projetar atitudes de superfície para um corte vertical — que é o alicerce sobre o qual métodos mais avançados se apoiam, fora do escopo deste módulo introdutório.

## Recap relâmpago

- O **traço de falha** trunca contatos abruptamente e tem símbolos próprios (ticks, dentes) para indicar tipo e bloco de teto.
- Uma **seção geológica** projeta as atitudes medidas em mapa (direção e mergulho, Parte 1) para um corte vertical, mantendo a espessura das camadas e a geometria de dobras e falhas consistentes com o observado na superfície.
- Atenção ao **mergulho aparente**: quando a linha de seção não é perpendicular à direção da camada, o ângulo que aparece no corte é sempre menor ou igual ao mergulho real medido em campo — usar o valor errado distorce a seção.
- Direção, mergulho, regra do V e padrões de dobra em mapa (Parte 1) mais traço de falha, seção geológica e mergulho aparente (Parte 2) formam, juntos, a leitura integrada de mapas e seções que fecha o Módulo 17.

## Próxima aula

Este é o encerramento do Módulo 17 — Geologia estrutural e deformação. O curso segue no [[18-tectonica-global-geodinamica-modulo|Módulo 18 — Tectônica global e geodinâmica]].

## Anterior

[[17-geologia-estrutural-aula-06-mapas-e-secoes-estruturais-parte-1-atitude-e-padroes-de-afloramento|Aula 06 (Parte 1) — Atitude e padrões de afloramento em mapa]]

## Fontes

- Traço de falha e símbolos convencionais em mapa geológico: Davis, G. H., Reynolds, S. J. & Kluth, C. F. (2012), *Structural Geology of Rocks and Regions* (3ª ed.), Wiley, capítulo 3.
- Construção de seções geológicas e mergulho aparente: Fossen, H. (2016), *Structural Geology* (2ª ed.), Cambridge University Press, capítulo 3.

<!--
nivel: iniciante-absoluto-v1
palavras_corpo: ~675
bridge_lesson: false

mapa_objetivo_secao:
  OA-05: "Como falhas aparecem em mapa" + "Da vista de cima ao corte vertical: construindo uma seção geológica"

alegacoes_auditaveis:
  - claim_id: GEO-M17-A07-MERGULHO-APARENTE-004
    claim: "O mergulho aparente, observado numa seção geológica que não é perpendicular à direção de uma camada, é sempre menor ou igual ao mergulho real (verdadeiro) medido em campo perpendicularmente à direção."
    risk: fato
    source: "Fossen 2016, Structural Geology, cap. 3; Rowland, Duebendorfer & Schiefelbein 2007, Structural Analysis and Synthesis, cap. 3"
  - claim_id: GEO-M17-A07-SECAO-GEOLOGICA-005
    claim: "Uma seção geológica (perfil estrutural) é construída projetando, para um corte vertical ao longo de uma linha escolhida no mapa, as atitudes de direção e mergulho medidas na superfície, mantendo consistência de espessura de camadas e geometria de dobras e falhas."
    risk: fato
    source: "Fossen 2016, Structural Geology, cap. 3; Davis, Reynolds & Kluth 2012, Structural Geology of Rocks and Regions, cap. 3"

nota_repartida: >-
  Segunda metade da antiga aula 06 única (Lendo o mapa: estruturas em mapas e
  seções geológicas), dividida pela revisão didática de 2026-08-18 por passar do
  teto de 1.600 palavras do LC-02 (2.071 palavras no corpo original). Completa o
  OA-05 (traço de falha em mapa, construção de seção geológica e mergulho
  aparente), continuando diretamente da Parte 1 (direção, mergulho, regra do V,
  padrão de dobras em mapa) e fechando o módulo 17. A seção "Como falhas aparecem
  em mapa" foi realocada da Parte 1 para cá, para equilibrar o tamanho das duas
  partes abaixo do teto do LC-02. Os claim_ids GEO-M17-A06-MERGULHO-APARENTE-004 e
  GEO-M17-A06-SECAO-GEOLOGICA-005 do arquivo original foram renumerados para
  GEO-M17-A07-* nesta parte, sem alteração de conteúdo. Nenhum conteúdo foi
  adicionado ou removido em relação ao texto original — apenas reorganizado.
-->
