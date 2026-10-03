# Módulo 42 — Exploração mineral e avaliação de recursos

> [!info] Área X. Métodos quantitativos e geoinformação · destino Obsidian · status: **pendente** (0/8 aulas · só planejado em 2026-08-28)

## Objetivo do módulo
Percorrer o fluxo completo da pesquisa mineral — da geração de alvos à sondagem, à amostragem com QA/QC, ao cálculo de recursos e à classificação segundo os códigos internacionais — amarrando num processo único as ferramentas que os módulos 19, 20, 21 e 22 ensinam isoladamente.

Corresponde a duas disciplinas obrigatórias da grade do IGc-USP que não tinham cobertura em nenhum dos dois cursos: **GAA0405 — Exploração Mineral** (90 h) e **GAA0404 — Avaliação de Recursos Minerais** (60 h). Foi criado em 2026-08-28 no fechamento de lacunas contra essa grade.

> [!warning] Módulo ainda não gerado
> Nenhuma aula, questionário ou flashcard existe. Só o plano — títulos, objetivos e sequência — foi aprovado. O conteúdo será escrito na fase de build.

## Pré-requisitos
Módulos **19** (Geofísica aplicada na exploração mineral) e **21** (Modelagem geoestatística de depósitos minerais) deste curso. Pressupõe também o módulo **21 do curso base** ("Geologia — do essencial ao avançado": recursos minerais e geologia econômica), dependência que fica fora do grafo formal por ser de outro curso.

> [!important] Ordem de estudo em relação ao capstone
> Este módulo deve ser estudado **antes do módulo 41** (Estudos integrados: projetos em geologia aplicada), que é o capstone do curso e pressupõe o vocabulário de recurso, reserva e código de reporte ensinado aqui. Essa dependência **não** aparece no campo `prerequisites` porque o validador estrutural exige que todo pré-requisito tenha id numericamente menor que o do módulo, e renumerar o capstone custaria mais do que resolve. Trate-a como regra de estudo, não como trava.

## Objetivos de aprendizagem
- `geologia-avancado-m42-oa01` — Distinguir potencial, recurso e reserva e situar cada fase de um programa exploratório na curva risco–investimento–descoberta
- `geologia-avancado-m42-oa02` — Selecionar ambientes geológicos e gerar alvos exploratórios integrando dados regionais geológicos, geoquímicos e geofísicos em SIG
- `geologia-avancado-m42-oa03` — Escolher e justificar as técnicas de prospecção de superfície e de prospecção geoquímica adequadas ao alvo, ao clima e ao regolito
- `geologia-avancado-m42-oa04` — Planejar uma campanha de sondagem escolhendo o método de perfuração pelo objetivo, e descrever e amostrar testemunhos com critério
- `geologia-avancado-m42-oa05` — Aplicar procedimentos de amostragem e de QA/QC (padrões, brancos, duplicatas) e diagnosticar erro fundamental e viés numa base de dados de pesquisa mineral
- `geologia-avancado-m42-oa06` — Calcular recursos minerais por métodos clássicos e classificar recursos e reservas segundo os códigos CRIRSCO/JORC e o guia CBRR, justificando os fatores modificadores

## Aulas planejadas (8)
1. A exploração mineral como processo: potencial, recurso e reserva; fases da pesquisa, curva descoberta–tempo, risco e investimento; regime legal da pesquisa mineral no Brasil
2. Geração de alvos: seleção de ambientes geológicos, modelos exploratórios e integração de dados regionais em SIG (mapas metalogenéticos e previsionais, cadastro de ocorrências)
3. Prospecção de superfície: mapeamento de detalhe, sedimento de corrente e follow-up, prospecção em malha regular, poços e trincheiras
4. Prospecção geoquímica: solos e litoquímica, controles litológico, climático e pedogênico, geoquímica orientativa, métodos analíticos e tratamento de dados
5. Sondagem exploratória: trado, RAB, roto-percussiva, circulação reversa e rotativa diamantada; critérios de uso, confiabilidade, gestão da campanha e descrição de testemunhos
6. Amostragem e QA/QC: teoria de amostragem de Gy, erro fundamental, preparação de amostras, padrões, brancos, duplicatas e auditoria da base de dados
7. Cálculo de recursos por métodos clássicos: método dos fatores, dos blocos de lavra, dos perfis e analíticos, e sua comparação com os métodos geoestatísticos
8. Classificação e conversão: recursos medidos, indicados e inferidos, fatores modificadores, reservas provadas e prováveis; CRIRSCO, JORC, guia CBRR e a estrutura do relatório técnico

_As aulas serão escritas na fase de build, uma por vez, e linkadas aqui._

## Como este módulo não duplica os módulos 19, 20, 21, 22, 36, 37 e 41

Cada um daqueles módulos ensina **uma ferramenta**; este ensina o **processo** que decide quando usar cada uma e o que fazer com o resultado.

| Módulo | Pergunta que ele responde | O que fica de fora e cabe aqui |
| --- | --- | --- |
| 19 — Geofísica na exploração | Qual método geofísico para este alvo? | Onde a geofísica entra na sequência e o que vem antes e depois dela |
| 20 / 21 — Geoestatística | Como estimar teor por krigagem? | Os métodos **clássicos** (fatores, blocos de lavra, perfis, analíticos) e a comparação entre eles |
| 22 — Modelagem 3D | Como construir e criticar o modelo? | De onde vêm os dados que alimentam o modelo, e se eles são confiáveis |
| 36 / 37 — Microscopia e petrografia de minério | Que minerais estão na seção polida? | Como a amostra chegou até a seção — sondagem, preparação, QA/QC |
| 41 — Capstone | Como conduzir um projeto integrado e reportá-lo? | Como se chega ao número que o relatório reporta |

A prospecção geoquímica de superfície, a campanha de sondagem, a teoria de amostragem e a classificação recursos/reservas com fatores modificadores **não existiam em nenhum módulo** dos dois cursos antes deste.

## Pontos de dificuldade
A distinção entre recurso e reserva parece trivial e é a fonte de erro mais cara da área: o que separa os dois são os **fatores modificadores**, e entendê-los exige sair da geologia para lavra, metalurgia, economia e licenciamento (aulas 01 e 08). A teoria de amostragem de Gy é matematicamente densa e costuma ser pulada na prática — mas é ela que explica por que uma amostra mal preparada inviabiliza toda a estimativa a jusante (aula 06). E os métodos clássicos de cálculo de recurso soam obsoletos diante da krigagem, quando na verdade continuam sendo a checagem de sanidade do resultado geoestatístico (aula 07).

## Registro do módulo
- Auditoria científica: pendente
- Revisão didática: pendente
- Questionário: pendente
- Flashcards: pendente

## Navegação
Anterior: [[22-modelagem-geologica-3d/22-modelagem-geologica-3d-modulo|Módulo 22 — Modelagem geológica 3D]] Próximo: [[23-modelagem-numerica-geodinamica/23-modelagem-numerica-geodinamica-modulo|Módulo 23 — Introdução à modelagem numérica geodinâmica]] Índice: [[_curso|Voltar ao curso]]
