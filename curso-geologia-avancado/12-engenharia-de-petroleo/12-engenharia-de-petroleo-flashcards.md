# Baralho de Flashcards — Módulo 12: Engenharia de petróleo

**ID:** geologia-avancado-m12-flashcards  
**Módulo:** [[12-engenharia-de-petroleo-modulo|Módulo 12 — Engenharia de petróleo]]  
**Número de flashcards:** 239 totais
- Basic: 152 cards (IDs fb001–fb152)
- Cloze: 87 cards (IDs fc001–fc087)

**Formato:** CSV com separador `;`, pronto para importação em Anki (sem cabeçalho).

## Cobertura por objetivo de aprendizagem

- **oa01** (Descrever etapas de perfuração e completação): 35 cards (Basic + Cloze)
  - Conceitos: sondas, brocas, fluido de perfuração, peso de lama, janela operacional, fases de revestimento, cimentação, BOP, completação, controle de areia, elevação artificial.
  
- **oa02** (Interpretar perfis geofísicos): 38 cards (Basic + Cloze)
  - Conceitos: GR, IGR, Vsh, resistividade, Rt, equação de Archie, nêutron, densidade, porosidade, efeito de gás, testemunhagem.
  
- **oa03** (Relacionar propriedades de rocha-reservatório e fluidos aos mecanismos de produção): 74 cards (Basic + Cloze)
  - Conceitos: porosidade, permeabilidade, Sw irredutível, PVT, Bo, Rs, ponto de bolha, OOIP, fator de recuperação, propriedades de rocha, volumes in place.
  
- **oa04** (Comparar métodos de recuperação secundária e avançada): 92 cards (Basic + Cloze)
  - Conceitos: mecanismos de produção (4 drive mechanisms), recuperação primária e secundária, testes de poço, índice de produtividade, IPR, EOR (térmico, miscível, químico), gestão de reservatórios.

## Valores auditados (reutilizados sem erro)

- Gradiente de lama: **0,546 psi/ft** (10,5 ppg × 0,052)
- Pressão de poros (aula 01): **0,465 psi/ft** (referência normal)
- Pressão de fratura (aula 01): **0,80 psi/ft**
- Saturação de água (aula 02, Archie): **Sw = 25%** / **Sh = 75%** (com m = 2, a = 1)
- Saturação de água sensibilidade (aula 02, m = 1,8): **Sw ≈ 21%**
- OOIP (aula 03): **19.115.712 STB**
- OOIP sensibilidade (aula 03, Bo = 1,35): **17.699.733 STB**
- Índice de produtividade (aula 04): **J = 1,0 bbl/dia/psi**
- Volume recuperado primária + secundária (aula 05): **6.117.028 STB** (32% de OOIP)
- Ganho EOR (aula 05): **2.293.885 STB** (12% de OOIP)
- Volume total recuperado com EOR (aula 05): **8.410.913 STB** (44% de OOIP)

Nenhum novo número foi introduzido; todos os exemplos de cálculo reutilizam os valores já auditados e confirmados pela auditoria científica (2026-09-02, passagem única).

## Estrutura dos cards

### Basic (152 cards, fb001–fb152)

Formato: `pergunta ; resposta curta`

Cobertura:
- Definições (termos técnicos, nomenclatura)
- Fórmulas e conversões (com constantes)
- Conceitos-chave (função, mecanismo, resultado)
- Exemplos numéricos (valor auditado de cada aula)
- Comparações (diferenças entre dois conceitos, faixas típicas)

### Cloze (87 cards, fc001–fc087)

Formato: `texto com {{c1::lacuna}}}}` (notação Anki padrão)

Cobertura:
- Declarações de fato com termos-chave em lacuna
- Séries de conceitos (múltiplas lacunas numa sentença)
- Contexto para retenção de nuances (diferenças de regime, válidas só em certas condições)
- Sensibilidades (quando um parâmetro muda, como se comporta outra grandeza)

## Padrões de distração em cards críticos

Os seguintes distratores foram intencionalmente selecionados para alta qualidade (validados pela auditoria):

1. **Controle de areia:** rochas de ALTA permeabilidade (não baixa) — distrator comum, erro contrainstituito
2. **Bo acima vs. abaixo de Pb:** Bo sobe até Pb (regime subsaturado), depois cai (gás liberado domina) — regime distinct
3. **Mecanismos de produção e FR:** depleção por gás em solução dá 5-30% (mais baixo); influxo de água dá 35-75% (mais alto); drenagem gravitacional até 60-80% mas lenta
4. **Índice de produtividade:** linear apenas acima de Pb; abaixo, IPR não-linear (Vogel)
5. **Completação:** revestido/canhoneado oferece controle, aberto não; custos inversos

## Cobertura de conectividade entre aulas

- **A01 → A02:** BOP e controle de poço (A01) → lama como invasão de filtrado distorce perfis (A02)
- **A02 → A03:** Porosidade e Sw do perfil (A02) → entra na fórmula de OOIP (A03)
- **A03 → A04:** OOIP (A03) → guia fator de recuperação (A04); Bo e Pb (A03) → definem regime de IP (A04)
- **A04 → A05:** Mecanismos e FR primária/secundária (A04) → ganho incremental de EOR sobre OOIP (A05)

Cards de conexão cruzada-aula explícita: 18 cards contêm referências explícitas ao número da aula anterior ("conforme aula NN").

## Validação e histórico

- **Geração:** 2026-09-02, após gate de auditoria (0 vermelho/laranja em aberto)
- **Validação estrutural:** validate_flashcards.py (sintaxe Cloze, IDs únicos, separador)
- **Nenhuma duplicação:** cada card tem ID único fb/fc + número sequencial; cada conceito coberto uma única vez
- **Nenhuma reinserção de erro:** o único achado bibliográfico da auditoria (ano de Craft & Hawkins, 2015 não 2013) não reaparece em nenhum card

## Preparação para o Anki

1. Copie o conteúdo de `12-engenharia-de-petroleo-flashcards-basic.csv` para o Anki (tipo: Basic)
2. Copie o conteúdo de `12-engenharia-de-petroleo-flashcards-cloze.csv` para o Anki (tipo: Cloze)
3. Importe para o baralho do módulo 12
4. Revisor recomendado: espaçamento padrão (dia 1, 3, 7, 14, 30)

---

**Anterior:** [[12-engenharia-de-petroleo-aula-05-completacao-elevacao-artificial-e-eor|Aula 05 — Completação, elevação artificial e recuperação avançada]]  
**Volta ao hub:** [[12-engenharia-de-petroleo-modulo|Módulo 12 — Engenharia de petróleo]]
