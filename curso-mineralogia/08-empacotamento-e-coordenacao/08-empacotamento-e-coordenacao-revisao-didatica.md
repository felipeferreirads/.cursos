# Revisão didática: Módulo 08 — Cristaloquímica I: raios iônicos, coordenação e regras de Pauling

**Revisado em:** 2026-10-06  ·  **Modo:** review-and-fix
**Material:** `curso-mineralogia/08-empacotamento-e-coordenacao/` — aulas 01 a 06 e figuras 1 a 6, depois da auditoria científica
**Veredito:** Bem ensinado com ressalvas → **ressalvas 🟠 e 🟡 corrigidas**

## Resumo

🔴 0 bloqueiam · 🟠 2 prejudicam · 🟡 2 atrito · 🔵 3 sugestões

**Carga estimada por aula** (contagem de `gerador-de-aula`; palavras de corpo depois das correções):

| Aula | Conceitos novos | Pré-requisitos reativados | Exemplos | Visuais | Duração |
|---|---|---|---|---|---|
| 01 | 3 (raio efetivo e âncora; dependência do NC; carga e spin) | 3 | 1 (4 casos) | 1 figura + 1 tabela | ~28 min (1.598) |
| 02 | 2 (razão de raios e limites; limites da regra) | 2 | 1 (4 casos) | 1 figura + 2 tabelas | ~28 min (1.327) |
| 03 | 3 (camada e empilhamentos; interstícios e contagem; pilhas de ânions) | 2 | 1 (4 itens) | 1 figura + 1 tabela | ~30 min (1.250) |
| 04 | 3 (regra 1; regra 2 e força de ligação; iso/aniso/mesodésmico) | 2 | 1 (3 casos) | 1 figura | ~30 min (1.407) |
| 05 | 3 (regra 3 e distâncias; regra 4; regra 5) | 2 | 1 (3 itens) | 1 figura + 1 tabela | ~27 min (1.332) |
| 06 | 7 estruturas, mas como reaplicação das aulas 02 a 05 | 4 | 1 (4 itens) | 1 figura + reaproveitada + 1 tabela | ~30-32 min (1.497) |

Todas no teto de ~1.600 palavras ou abaixo; a carga está na geometria (aulas 02, 03 e 05) e no volume de exemplos da aula 06.

## Achados

### 🟠 1. Aula 01 acima do teto de palavras (LC-02)

**Tipo:** sobrecarga leve / contrato de nível
**Onde:** aula 01 (1.627 palavras de corpo depois da auditoria, que acrescentou o aviso sobre a analogia)
**Problema:** o contrato `ensino-medio-sem-geologia-v1` põe o teto em ~1.600. A aula já tem três ideias novas e uma tabela de consulta.
**Correção aplicada:** a explicação de "por que o raio cresce com o NC" foi condensada (mesmo conteúdo, sem repetir o enunciado da aula 04), a frase da distância prevista e um erro comum foram encurtados. Resultado: 1.598 palavras. Nenhum fato novo.
**Escopo:** correção local.

### 🟠 2. Aula 06: quadro-síntese antes de qualquer explicação

**Tipo:** abstração antes do concreto / sobrecarga
**Onde:** aula 06 · O quadro geral
**Problema:** a aula abre com uma tabela de 8 linhas e 6 colunas (fórmula, grupo espacial, coordenação, descrição, isoestruturais). Lida de cara, é uma parede de dados; o aluno tende a tentar decorá-la.
**Correção aplicada:** frase de orientação antes do quadro ("Não tente decorar o quadro de uma vez: ele é o mapa do módulo…") e indicação de que a seção da perovskita, a mais longa e com o fator de tolerância, pode ficar para uma segunda sessão. Não se dividiu a aula: cada estrutura é aplicação direta das aulas 02 a 05, e o exemplo trabalhado não depende da perovskita.
**Escopo:** correção local.

### 🟡 3. Salto no exemplo geométrico da aula 05

**Tipo:** salto no exemplo trabalhado
**Onde:** aula 05 · Exemplo trabalhado (a)
**Problema:** "O vizinho é o reflexo do primeiro por esse ponto" pressupõe que o aluno veja por que o segundo octaedro fica simétrico ao primeiro em relação ao meio da aresta.
**Correção aplicada:** "Os dois octaedros que dividem a aresta ficam simétricos em relação ao meio dela, e o centro do segundo fica do outro lado desse ponto, à mesma distância"; a face ganhou "pelo mesmo raciocínio de simetria".

### 🟡 4. Analogia da aula 01

**Observação:** coincidiu com o achado 🟠 2 da auditoria, que já corrigiu o sentido da analogia. Do ponto de vista didático, a versão corrigida é melhor do que a retirada: o aluno é avisado de que a intuição da espuma aponta para o lado errado, que é justamente o erro que ele cometeria.

### 🔵 5. Modelo físico de empacotamento

**Sugestão:** empilhar bolinhas de gude (ou laranjas) em camadas ABAB e ABCABC e procurar os buracos com uma bolinha menor deixa o "1 octaédrico e 2 tetraédricos por esfera" palpável.
**Desfecho:** aberto, não bloqueante.

### 🔵 6. Visualizador 3D das estruturas-tipo

**Sugestão:** um modelo girável (VESTA, módulo 07, ou um applet) para rutilo, corindo e espinélio, que a figura 6 não mostra (a figura cobre só as três estruturas cúbicas mais simples).
**Desfecho:** aberto, não bloqueante; as três estruturas não desenhadas estão descritas em texto com remissão às aulas 03 a 05.

### 🔵 7. Ponte para o módulo 09

**Sugestão:** a pergunta "Pare e explique" da aula 01 (Fe²⁺ × Fe³⁺ no lugar do Mg²⁺) e o "O que não concluir" da aula 06 (isoestrutural não implica solução sólida) são as portas do módulo 09; vale retomá-las explicitamente na aula 01 de lá.
**Desfecho:** registrado para o módulo 09.

## Cobertura de objetivos

| Objetivo | Ensinado em | Exemplo | Avaliado em |
|---|---|---|---|
| `mineralogia-m08-oa01` — raios efetivos (carga, NC, spin) | a01 | sim (4 distâncias) | (questionário a gerar) |
| `mineralogia-m08-oa02` — razão de raios e limites | a02 | sim (4 casos, 1 falha) | (questionário a gerar) |
| `mineralogia-m08-oa03` — empacotamentos e interstícios | a03 | sim (corindo, espinélio, olivina) | (questionário a gerar) |
| `mineralogia-m08-oa04` — cinco regras de Pauling | a04, a05 | sim (espinélio, magnetita, perovskita; TiO₂) | (questionário a gerar) |
| `mineralogia-m08-oa05` — estruturas-tipo | a06 | sim (espinélio genérico) | (questionário a gerar) |

Nenhum objetivo descoberto; nenhuma seção órfã. A seção "valência de ligação" (aula 04) é curta e serve ao `oa04` como limite da regra 2.

## O que está bem feito (manter)

- Os números são sempre **conferíveis pelo aluno**: cada distância prevista vem com a medida e a fonte, e o desvio é interpretado (óxidos × sulfetos).
- A razão de raios é ensinada **com as falhas** (zircão, espinélio, carbonato, pressão, taumasita) e com a estatística de George et al. (2020), o que evita a leitura da regra como lei.
- As aulas 03, 04 e 06 contam a mesma história por três caminhos (fração de interstícios, soma da regra 2, contagem de ligações) para corindo, espinélio e olivina: redundância deliberada que consolida.
- A figura 6 do módulo 06 foi reaproveitada para a coordenação 6:6, como a revisão daquele módulo sugeriu.

## Correções aplicadas

| # | Severidade | Desfecho | Arquivos |
|---|---|---|---|
| 1 | 🟠 | Corrigido | aula-01 |
| 2 | 🟠 | Corrigido | aula-06 |
| 3 | 🟡 | Corrigido | aula-05 |
| 4 | 🟡 | Já corrigido pela auditoria | aula-01 |
| 5-7 | 🔵 | 5 e 6 abertos; 7 registrado para o módulo 09 | — |

As mudanças da revisão foram conferidas pelo `auditor-cientifico` (seção "Segunda passagem" da auditoria do módulo): nenhuma introduziu fato novo.
