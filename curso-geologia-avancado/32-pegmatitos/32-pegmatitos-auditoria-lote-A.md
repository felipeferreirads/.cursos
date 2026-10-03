# Auditoria científica — Módulo 32 (Pegmatitos) — LOTE A: Aulas 01–09

**Status:** relatório PARCIAL (lote A de 3). Não é o relatório final do módulo. Os blocos `audit`/`didactic_review` do módulo 32 no `course-state.yaml` **não** foram gravados; a consolidação ocorre depois dos lotes B (Aulas 10–?) e C.
**Data:** 2026-09-24
**Modo:** audit-and-fix · **Profundidade:** full
**Escopo:** `32-pegmatitos-aula-01` a `32-pegmatitos-aula-09`. As Aulas 10–26 não foram auditadas.
**Material derivado:** o módulo 32 ainda não tem questionário nem flashcards, então não houve propagação para esses arquivos. Também não havia baralho importado no Anki.
**Veredito do lote:** **Aprovado com correções.** Todos os achados 🔴/🟠/🟡 foram corrigidos nos arquivos das aulas. Ficam em aberto três 🔵 de baixo impacto, todos com o texto já reescrito com a incerteza explícita (ver "Pendências").

## Resumo por severidade

| Severidade | Qtde | Corrigidos | Abertos |
|---|---|---|---|
| 🔴 Erro | 10 | 10 | 0 |
| 🟠 Impreciso | 38 | 38 | 0 |
| 🟡 Desatualizado | 2 | 2 | 0 |
| 🔵 Sem fonte | 7 | 5 (reescritos com ressalva ou removidos) | 2 (+1 adiado para o lote B) |
| ⚪ Controverso | 4 | 4 (reescritos mostrando as posições) | 0 |
| **Total** | **61** | | |

### Inversões de sentido perigosas (prioridade para quem for gerar questionário/flashcards)

1. **A09-3:** a aula dizia que a monazita é "mais suscetível a metamictização" e montava o exemplo trabalhado sobre isso. É o contrário: a monazita praticamente não se torna metamítica.
2. **A09-1 / A09-2:** "Trebilcock" e "44069" apareciam como padrões de columbita-tantalita e de cassiterita. Os dois são padrões de **monazita**.
3. **A04-1:** a reação estava escrita como "espodumênio = eucriptita + 2 quartzo". A forma balanceada é Spd = Ecr + Qtz, e a reação principal, Pet = Spd + 2 Qtz, não aparecia. O erro vem de um lapso no próprio texto de London (1984, p. 999); a Tabela 3 do artigo tem a forma correta.
4. **A05-7:** o exemplo trabalhado atribuía **classes** de profundidade (moscovita–elementos raros) a corpos de um mesmo campo com base no grau de fracionamento. Classe é profundidade/fácies; o que muda dentro de um campo é o **tipo**.
5. **A02-2:** "espodumênio secundário" era usado para o produto de *alteração* do espodumênio. Na literatura o termo significa o oposto: espodumênio formado por substituição.
6. **A06-2:** o paradoxo dos cristais gigantes aparecia como "resolvido" por Nabelek et al. (2010), o que contraria a diretriz do hub de apresentar o debate como aberto.

### Bibliografia corrigida (pedido específico do principal)

- **Brisbin (1986):** a Aula 08 já citava *American Mineralogist* 71(3-4):644-651. **Correto**, confirmado. A Aula 07 também cita Brisbin em "Próxima aula" sem periódico, o que está ok.
- **Thomas & Davidson (2013):** as Aulas 06 e 07 citam *Journal of Geosciences* 58:183-200. **Correto**, confirmado. A Aula 03 tinha uma citação vaga ("Thomas, R. & Davidson, P. — trabalhos sobre…"), agora completada com o periódico certo. Nenhuma das Aulas 06–08 citava *Mineralogy and Petrology*.
- **Corrigidos:** Aula 07, autoria da síntese sveconorueguesa (era "Sørensen, Grimes et al.", o certo é **Müller, Romer & Pedersen 2017**); Aula 07, trabalho de dois estágios completado (**Rosing-Schow et al. 2023**, *Precambrian Research* 384:106944); Aula 06, páginas de Nabelek et al. 2010 (de 317-334 para **313-325**); Aula 03, Manning (1981) trata do **flúor**, não de B e P (entraram Pichavant 1987 para B e London et al. 1993 para P); Aula 04, "Roda-Robles et al." passou a **Dias, Lima & Roda-Robles (2019)**, *Can. Mineral.* 57(5):731-732; Aula 02, "Simmons et al." (incompleto) passou a **Webber et al. (1997, 1999)**, e "Morgan, G. B. VI" passou a "Morgan, G. B."; Aula 01, Haüy de 1801 para **1822**.

---

## Achados por aula

Formato compacto: **claim_id** · severidade · natureza · onde · o que estava escrito → correção · fonte (nível; confiança) · desfecho.

### Aula 01 — Definição e hierarquia

**A01-1** `PEG-M32-A01-ETIMOLOGIA-001` · 🔴 · erro_factual · Conteúdo §1, Recap, Fontes
Estava escrito: "cunhado em 1801 pelo mineralogista francês René Just Haüy". Correção: Haüy usou o termo na 2ª ed. do *Traité de Minéralogie* (1822) para o granito gráfico, e Haidinger (1845) o ampliou.
Fonte: London (2008, p. 4) via síntese; Wikipedia/New World Encyclopedia (consultadas 2026-09-24) · revisada por pares + geral · provável · **Corrigido.**

**A01-2** `PEG-M32-A01-DEFINICAO-LONDON-002` · 🟠 · impreciso · §1, Recap
Estava escrito: "rocha ígnea holocristalina … e/ou (b) forte tendência a formar intercrescimentos gráficos". Correção: definição de London (2008): "rocha essencialmente ígnea, comumente granítica … granulação extremamente grossa, mas variável, **ou** abundância de cristais com hábitos esqueléticos, gráficos ou fortemente direcionais". "Holocristalina" não faz parte da definição.
Fonte: London 2008, texto da definição confirmado por busca · confirmado · **Corrigido.**

**A01-3** `PEG-M32-A01-ESPECTRO-006` · 🟠 · inconsistencia_interna · §1
Estava escrito: "espectro de rochas ígneas félsicas a intermediárias", logo antes de citar pegmatitos gabroicos. Correção: "do félsico ao máfico". · **Corrigido.**

**A01-4** `PEG-M32-A01-GRAFICO-HEBRAICO-007` · 🟠 · impreciso · §1 (e Aula 02, Textura gráfica)
Estava escrito: "lembra caracteres cuneiformes ou hieróglifos (por isso … 'granito hebraico')". O nome vem da semelhança com a escrita hebraica, e a frase não fechava. Correção: "lembra uma escrita antiga — letras hebraicas, runas ou caracteres cuneiformes". · **Corrigido nas duas aulas.**

**A01-5** `PEG-M32-A01-AUSENCIA-PLUTON-004` · 🔵 · evidencia_insuficiente · §2
Estava escrito: "(Greenbushes e Pilgangoora) não há um plúton aflorante evidente". Há granitoides expostos na região de Pilgangoora; o que falta é um parental **demonstrado**. Reescrito como "não há um plúton parental identificado com segurança — pode haver granitos na região, mas nenhum demonstrado como fonte". · **Corrigido com ressalva.** A verificação plena fica para a Aula 13 (lote B).

**A01-6** `PEG-M32-A01-HIERARQUIA-003` · 🔵 · evidencia_insuficiente · §3
A hierarquia de cinco níveis é adaptação do curso. Alguns autores inserem "distrito" como nível próprio, e o termo também tem uso mineiro. Não foi possível ler o texto primário de Černý nesta rodada. Acrescentada a ressalva no texto. · **Corrigido com ressalva.**

Verificado e correto: London (2008) = *Can. Mineral.* Special Publication 10; Černý (1991a) = *Geoscience Canada* 18:49-67; cinturão estanho-espodumênio de Kings Mountain; zonamento regional (os corpos mais distantes do plúton são mais fracionados).

### Aula 02 — Zonamento e texturas

**A02-1** `PEG-M32-A02-NUCLEO-008` · 🟠 · inconsistencia_interna / certeza_indevida · Núcleo de quartzo
Estava escrito: "resíduo final da cristalização fracionada … dominado pelo componente menos reativo e mais persistente em solução — a sílica". Isso é um mecanismo *ad hoc*, e o parágrafo seguinte diz que a aula "não entra no mecanismo". Correção: descrição puramente espacial ("última zona primária a se formar"), com o mecanismo remetido às Aulas 06–07. · **Corrigido.**

**A02-2** `PEG-M32-A02-SUBSTITUICAO-002` · 🟠 · impreciso (terminologia invertida) · Unidades de substituição
Estava escrito: "o chamado 'espodumênio secundário' ou pseudomorfos de albita + muscovita + quartzo sobre espodumênio". Correção: pseudomorfos de eucriptita + albita ou muscovita ± albita ± argilominerais, mais o alerta de que "espodumênio secundário" designa espodumênio *formado* por substituição (por exemplo, o SQUI sobre petalita).
Fonte: London (1984), confirmado na fonte primária (substituição de petalita por Spd/Ecr + Qtz); London & Burt (1982a), *Am. Mineral.* 67:97-113 · provável · **Corrigido.**

**A02-3** (ver A01-4).

**A02-4** `PEG-M32-A02-USST-LINEROCK-005` · 🟠 · impreciso · Textura unidirecional
A sigla estava como "USST". A corrente é UST (*unidirectional solidification texture*). · **Corrigido.**

**A02-5** `PEG-M32-A02-USST-LINEROCK-005` · 🟠 · impreciso · *Line rock*
Estava escrito: "caso particular de textura unidirecional: camadas de turmalina…". Correção: *line rock* é aplito rítmico de albita + quartzo com linhas de granada (almandina-espessartita) e/ou turmalina, típico da lapa dos diques de San Diego, interpretado como nucleação oscilatória controlada por difusão. É uma textura aparentada, não um caso de UST.
Fonte: Webber et al. (1999), *Am. Mineral.* 84:708-717; Webber et al. (1997), título confirmado via USGS · revisada por pares · confirmado · **Corrigido.**

**A02-6** `PEG-M32-A02-LINEROCK-BR-009` · 🔵 · evidencia_insuficiente
Estava escrito: "vários corpos da Província Oriental brasileira exibem *line rock* bem desenvolvido". Não foi encontrada fonte. **Removido.**

**A02-7** `PEG-M32-A02-CRISTAIS-GIGANTES-006` · 🟠 · impreciso · Cristais gigantes
Estava escrito: "espodumênio de mais de 12 m" (correto, mas subestimado) e "microclínio de dezenas de metros (Karelia)". Correção: espodumênio de 14,3 × 0,8 m (Etta) e massas de microclínio com forma de cristal único de >2.000 t (Carélia).
Fonte: Rickwood (1981), *Am. Mineral.* 66:885-907, via busca · confirmado · **Corrigido.**

**A02-8** `PEG-M32-A02-ZONAMENTO-001` · 🟠 · omissao (atribuição) · Pegmatito zonado idealizado
O modelo de zonas (borda, mural, intermediárias, núcleo e unidades de substituição) foi formalizado por **Cameron, Jahns, McNair & Page (1949)**, *Econ. Geol. Monograph 2*. A aula atribuía tudo a "Jahns, anos 1950". · confirmado · **Corrigido (citação acrescentada).**

Verificado e correto: Jahns (1955), *Econ. Geol.* 50th Anniv. Vol.; classe miarolítica em Černý & Ercit (2005); London & Morgan (2012), *Elements* 8:263-268.

### Aula 03 — Fracionamento, fluxantes, fluidos

**A03-1** `PEG-M32-A03-FLUXANTES-002` · 🟠 · erro conceitual · Bullet do Li
Estava escrito: "não um formador de rede como B, P ou F". O F não é formador de rede (é ânion que substitui O). Correção: "cátion modificador … não um formador de rede como B ou P, nem um ânion que substitui o oxigênio, como F". · **Corrigido.**

**A03-2** `PEG-M32-A03-FLUXANTES-EXTRA-007` · 🔵 · "a literatura por vezes acrescenta … Cl e Rb" como fluxantes. Não foi encontrada fonte (Rb não é tratado como fluxante). **Removido** (substituído por "a lista exata varia entre autores").

**A03-3** `PEG-M32-A03-EXSOLUCAO-004` · 🟠 · impreciso · Inclusões de fundido
Estava escrito: "em geral vítreas ou parcialmente cristalizadas quando reaquecidas". É o contrário: em pegmatitos as inclusões de fundido costumam estar **cristalizadas** e são **reaquecidas até homogeneizar em vidro** para análise. · **Corrigido.**

**A03-4** `PEG-M32-A03-BOLSOES-005` · ⚪ · controversia · Formação dos bolsões
A expansão volumétrica do fluido/vapor exsolvido aparecia como "a leitura mais aceita", sem a alternativa. Correção: "leitura muito difundida", mais um parágrafo com a posição de London (crescimento no bolsão a partir de fundido residual hidratado e rico em fluxantes, com a fase aquosa só no fim).
Fonte: London & Morgan (2012); London (2013, *Rocks & Minerals* 88:527-538 — de memória) · em disputa · **Reescrito com as duas posições.**

**A03-5** `PEG-M32-A03-GEMAS-008` · 🟠 · impreciso · "elementos formadores de gemas (Be, B, F, ETR leves)". ETR leves não são formadores típicos de gema em bolsões LCT, e faltava o Li. Correção: Be (berilo), B (turmalina), F (topázio), Li (elbaíta, kunzita). · **Corrigido.**

**A03-6** `PEG-M32-A03-BIB-MANNING-009` · 🔴 · erro_factual (bibliográfico) · Fontes
Estava escrito: "Manning (1981) … efeito do boro e do fósforo". Manning (1981), *CMP* 76:206-215, trata do **flúor** (com 4% em peso de F, o mínimo do sistema cai de ~730 para ~630 °C). Correção: Manning 1981 (F), Pichavant 1987, *Am. Mineral.* 72:1056-1070 (B), e London et al. 1993, *CMP* 113:450-465 (P). · confirmado (Manning, Pichavant) / de memória (London 1993) · **Corrigido.**

Verificado: London (1992), *Can. Mineral.* 30:499-540 (de memória; consistente com a literatura secundária); o conceito de camada-limite enriquecida em fluxantes à frente da cristalização aparece confirmado no resumo de London & Morgan (2012).

### Aula 04 — Mineralogia

**A04-1** `PEG-M32-A04-GEOBAROMETRO-001` · 🔴 · erro_factual · Silicatos de lítio, Recap
Estava escrito: "espodumênio = eucriptita + 2 quartzo". A estequiometria está errada: o balanceado é LiAlSi₂O₆ = LiAlSiO₄ + SiO₂. Faltava também a reação-chave Pet = Spd + 2 Qtz, que o próprio London aponta como a mais importante. Na fonte primária, o campo Ecr + Qtz fica abaixo de ~320 °C e ~1,6 kbar, e a eucriptita + quartzo nunca foi identificada como assembleia magmática primária; o espodumênio primário se forma tipicamente em 3–5 kbar e 500–650 °C.
Fonte: London (1984), *Am. Mineral.* 69:995-1004, **lido na íntegra** (PDF MSA) · normativa experimental · confirmado · **Corrigido.**

**A04-2** `PEG-M32-A04-GEOBAROMETRO-USO-010` · 🟠 · certeza_indevida
Estava escrito: "funciona como um geobarômetro de razoável confiança". London (1984) adverte que a utilidade é **limitada**, porque o espodumênio persiste metaestavelmente dentro do campo Ecr + Qtz. · **Corrigido.**

**A04-3** `PEG-M32-A04-SUBST-PET-SPD-011` · 🟠 · omissao_que_gera_erro · §Silicatos de Li e exemplo trabalhado
As substituições apareciam como simétricas ("petalita tardia substituindo espodumênio, ou vice-versa"). A relação típica é petalita → espodumênio + quartzo no resfriamento; a inversa é menos comum e exige descompressão. O exemplo (petalita substituindo espodumênio) foi mantido, mas passou a sinalizar que é o caso incomum. · **Corrigido.**

**A04-4** `PEG-M32-A04-POLUCITA-003` · 🟠 · erro de fórmula · Estava "(Cs,Na)₂Al₂Si₄O₁₂·H₂O". Correção: **·2H₂O** (Mindat); forma série com a analcima. · confirmado · **Corrigido.**

**A04-5** `PEG-M32-A04-BERILO-004` · 🟠 · impreciso · Estava escrito: "a maioria das esmeraldas … por processos metassomáticos **não pegmatíticos**". Muitos depósitos "tipo xisto" (Zâmbia, Brasil) são metassomatismo **ligado a pegmatitos/granitos** em rochas máficas-ultramáficas; os colombianos são hidrotermais sem relação magmática. Reescrito.
Fonte: Giuliani et al. (2019), *Minerals* 9:105 · confirmado · **Corrigido.**

**A04-6** `PEG-M32-A04-COLUMBITA-TANTALITA-005` · 🟡 · desatualizacao · Os nomes ferrocolumbita/manganotantalita etc. passaram aos nomes IMA **columbita-(Fe), columbita-(Mn), tantalita-(Fe), tantalita-(Mn)**, com os nomes antigos preservados. O mesmo foi aplicado ao exemplo trabalhado da Aula 04 e ao da Aula 05. · **Corrigido.**

**A04-7** `PEG-M32-A04-MICROLITA-012` · 🟡 · desatualizacao · "Microlita" é hoje nome de grupo no supergrupo do pirocloro (Atencio et al. 2010; espécies como a fluorcalciomicrolita). Acrescentado. · de memória consolidada · **Corrigido.**

**A04-8** `PEG-M32-A04-TANCO-TA-013` · 🟠 · impreciso · Estava escrito: "Tanco … microlita compete com ou supera a columbita-tantalita como minério principal". Correção: em Tanco o Ta está distribuído entre columbita-tantalita, wodginita e microlita, as duas últimas em boa parte substituições tardias.
Fonte: Van Lichtervelde et al. (2007), *Econ. Geol.* · provável · **Corrigido.**

**A04-9** `PEG-M32-A04-NYF-PREVIA-008` · 🟠 · impreciso · Estava escrito: "membros do grupo columbita … mais ricos em Nb e em Y-ETR". A columbita não é hospedeira de Y-ETR; os óxidos típicos são euxenita e aeschynita. · **Corrigido.**

**A04-10** `PEG-M32-A04-BIB-DIAS-014` · 🟠 · bibliográfico · "Roda-Robles et al." (sem ano) passou a Dias, Lima & Roda-Robles (2019), *Can. Mineral.* 57(5):731-732. · confirmado · **Corrigido.**

Verificado: London (1984), título, volume e páginas; lepidolita = série trilithionita–polylithionita; fórmula da turmalina XY₃Z₆(T₆O₁₈)(BO₃)₃V₃W; trifilita-lifilita e ambligonita-montebrasita.

### Aula 05 — Classificação

**A05-1** `PEG-M32-A05-CLASSES-001` · 🟠 · impreciso (estrutura do esquema) · Estava escrito: "subclasses (definidas pela família geoquímica: LCT, NYF ou mista)"; "classe → subclasse/família". Em Černý & Ercit (2005), as subclasses são REL-REE/REL-Li, MI-REE/MI-Li etc., e as **famílias** formam um sistema petrogenético **paralelo** (LCT = REL-Li + MI-Li; NYF = REL-REE + MI-REE). Reescrito, com os tipos e subtipos corretos.
Fonte: tabelas de Černý & Ercit (2005) reproduzidas em Simmons (2005, resumo MSA/Elba), lidas na íntegra · confirmado · **Corrigido.**

**A05-2** `PEG-M32-A05-LCT-NYF-002` · 🟠 · atribuição · Estava escrito: "família geoquímica, introduzida por Ginsburg et al. (1979)". Os termos LCT/NYF são de **Černý (1991a)**; a família mista é de Černý & Ercit (2005). · confirmado · **Corrigido** (também nas Fontes).

**A05-3** `PEG-M32-A05-CLASSES-FACIES-007` · 🟠 · impreciso · Moscovita: "gradiente da cianita (*kyanite-grade*)" passou a anfibolito barroviano de P alta (cianita–sillimanita, ~5–8 kbar). MSREL: foi retirado "parte de uma sequência de zonamento regional", que confunde classe com zonamento, e entrou ~3–7 kbar. REL: anfibolito de P baixa, tipo Abukuma (andaluzita–sillimanita), a xisto verde superior, ~2–4 kbar. Contexto histórico: 4 classes em 1991, MSREL a partir de 2004–2005. · confirmado · **Corrigido.**

**A05-4** `PEG-M32-A05-EXEMPLOS-NYF-003` · 🔴 · erro_factual · Estava escrito: "Evje-Iveland (associado ao complexo anortosítico-gabroico de Bamble-Telemark)". Correção: setor Telemark; hospedado em gnaisses anfibolíticos, anfibolitos gabroicos de Iveland–Gautestad e metadioritos; origem anatética por fusão desses anfibolitos. Acrescentado também que Ytterby está ligado ao granito de Estocolmo (tipo I) e South Platte ao sistema Pikes Peak (tipo A).
Fontes: Müller et al. (2017); trabalho experimental sobre Evje-Iveland (Lithos 2021, via busca); tabela de famílias de Černý & Ercit (2005) · confirmado · **Corrigido.**

**A05-5** `PEG-M32-A05-MISTA-008` · 🔵 · Estava escrito: "Alguns distritos do sul da Califórnia … exemplos de assinatura mista". Não foi encontrada fonte. Substituído pela origem que Černý & Ercit (2005) dão à família mista (plútons NYF contaminados por supracrustais) e pela menção a pegmatitos de Madagascar discutidos por Martin & De Vito (2005). · **Corrigido com ressalva.**

**A05-6** `PEG-M32-A05-WISE-MULLER-SIMMONS-004` · 🟠 · impreciso · O Grupo 3 estava descrito como "sem afinidade clara … afinidade com a encaixante", com nota meta de verificação pendente. Correção: o Grupo 3 é **exclusivamente anatético** (DPA), fortemente peraluminoso, com Kfs + Qtz + Pl e biotita, muscovita, granada ou turmalina, sem mineralização de elementos raros; os Grupos 1 e 2 podem ser residuais de granitos S, A e I **ou** DPA. A crítica, antes apresentada como "central" e "circular", foi reformulada para incluir a omissão da anatexia.
Fonte: resumo de Wise et al. (2022) via ADS/busca · confirmado · **Corrigido.**

**A05-7** `PEG-M32-A05-EXEMPLO-006` · 🔴 · confusao_de_escopo · Exemplo trabalhado
Estava escrito: corpo A "fora da classe rare-element"; B "coerente com a classe moscovita-elementos raros" por ter muscovita. Classe = profundidade/fácies, e todos os corpos de um mesmo campo, na mesma faixa metamórfica, estão na **mesma classe**. Reescrito: A e B são estéreis; C é do tipo berilo (berilo-columbita); D e E são do tipo complexo. O corpo E trocou petalita por lepidolita, porque petalita × espodumênio é indicador de P, não de fracionamento (Aula 04). · **Corrigido.**

**A05-8** `PEG-M32-A05-ZONAMENTO-INDICADORES-005` · 🟠 · inconsistencia_interna · Recap: "indicadores … que aumentam sistematicamente com a distância", sendo que K/Rb e Nb/Ta *diminuem*. · **Corrigido.**

Verificado: Černý & Ercit (2005), *Can. Mineral.* 43:2005-2026; Müller et al. (2022) Part I, 60:203-227; Wise et al. (2022), 60:229-248; LCT e NYF (elementos e granitos associados); Ytterby com quatro elementos (Y, Yb, Er, Tb); K/Rb >100–150 em granito pouco fracionado e <10–20 em pegmatito muito evoluído (ordem de grandeza).

### Aula 06 — Gênese I (Jahns-Burnham × London) — atenção especial

**Diagnóstico de equilíbrio (pedido do principal):** a aula já apresentava J&B e London sem declarar vencedor na parte teórica, e a evidência de cada lado estava atribuída corretamente (J&B: saturação em água, fluido separado, cristalização de equilíbrio; London: Tanco, fluxantes, exsolução tardia). Havia três desequilíbrios: (i) o paradoxo dos cristais gigantes aparecia como **"resolvido"**, e o argumento de Nabelek como "alinhado a London"; (ii) a crítica de London aparecia sem nenhum contraponto (quem contesta London); (iii) "dias a poucos anos" aparecia como fato, antecipando a Aula 10. Todos foram corrigidos.

**A06-1** `PEG-M32-A06-CRISTAIS-006` · 🔴 · erro_factual + inconsistencia_interna · Estava escrito: "cristais de espodumênio de dezenas de metros", o que contradiz a Aula 02 e o recorde de 14,3 m; e "folhelhos de mica", sendo que folhelho é *shale*. Correção: "placas de mica"; "mais de uma dezena de metros (~14 m na Etta Mine)". · **Corrigido.**

**A06-2** `PEG-M32-A06-NABELEK-2010-004` · ⚪ · certeza_indevida · Objetivo, título da seção, texto e recap diziam "resolve/resolvem o paradoxo". Reescrito como "propõe(m) resolver … proposta influente, não consenso". Também passou a constar que Nabelek et al. põem a **H₂O** como protagonista, e não os fluxantes B-P-F-Li de London, e entrou a síntese de London & Morgan (2012): "o quebra-cabeça está longe de resolvido". · **Reescrito.**

**A06-3** `PEG-M32-A06-JAHNS-BURNHAM-001` · 🟠 · Estava escrito: "duas fases distintas, ambas em estado supercrítico". O fundido silicático continua líquido; só o fluido aquoso é supercrítico. · **Corrigido.**

**A06-4** `PEG-M32-A06-CRITICA-LONDON-002` · 🟠 · cronologia · Estava escrito: "A partir do início dos anos 1990". As raízes estão em Fenn (1977) e Swanson (1977), e o trabalho de London em Tanco é de 1986. · Fenn/Swanson/London 1986 de memória consolidada · **Corrigido.**

**A06-5** `PEG-M32-A06-CONTRAPONTO-007` · ⚪ · controversia (omissão de um lado) · Foi acrescentado que Thomas e colaboradores contestam London com base em inclusões de fundido (a troca de 2015 é detalhada na Aula 07). · **Reescrito.**

**A06-6** `PEG-M32-A06-ESCALA-TEMPO-008` · 🟠 · certeza_indevida · "(dias a poucos anos …)" passou a ser estimativa de modelos térmicos de diques finos, contestada, com o debate remetido à Aula 10. · **Corrigido.**

**A06-7** `PEG-M32-A06-BIB-NABELEK-009` · 🟠 · bibliográfico · As páginas 317-334 passaram a **313-325**. · confirmado · **Corrigido.**

Verificado: Jahns & Burnham (1969), *Econ. Geol.* 64:843-864. CZR como camada-limite enriquecida em fluxantes à frente da cristalização (London & Morgan 2012), com o risco antes marcado `a_verificar` agora confirmado em substância.

### Aula 07 — Gênese II (fracionamento × anatexia × imiscibilidade) — atenção especial

**Diagnóstico de equilíbrio:** a estrutura era equilibrada (fracionamento, depois anatexia, depois síntese). Problemas: o caso sveconorueguês aparecia como algo que "demonstra" a anatexia, sem atribuir a interpretação aos autores, sem a exceção de Østfold e sem o limite lógico da evidência negativa; o lado do fracionamento não tinha nenhum exemplo concreto; e a posição de Thomas & Davidson ficava ambígua, quando na verdade reforça a **via granítica**. Tudo corrigido.

**A07-1** `PEG-M32-A07-BIB-MULLER2017-006` · 🔴 · erro_factual (autoria) · A atribuição "Sørensen, B. E., Grimes, S. et al." passou a **Müller, A., Romer, R. L. & Pedersen, R.-B. (2017)**, *Can. Mineral.* 55(2):283-315, DOI 10.3749/canmin.1600075. · confirmado · **Corrigido.**

**A07-2** `PEG-M32-A07-BIB-ROSING-SCHOW-007` · 🟠 · bibliográfico incompleto · "(… ScienceDirect)" passou a Rosing-Schow, Romer, Müller, Corfu, Škoda & Friis (2023), *Precambrian Research* 384:106944. Acrescentados os dois grupos de idade (1100–1030 e 930–890 Ma), Tørdal 946 ± 4 Ma (~40 Ma mais antigo, confirmado) e a exceção de Østfold. · confirmado · **Corrigido.**

**A07-3** `PEG-M32-A07-BAIXO-GRAU-008` · 🟠 · ambiguidade terminológica · "fusão parcial de baixo grau" (confundível com grau metamórfico) passou a "fusão parcial de pequena fração". · **Corrigido.**

**A07-4** `PEG-M32-A07-SVECONORUEGUESA-002` · ⚪ · atribuição/certeza · "ele demonstra que … a anatexia é o mecanismo mais coerente" passou a "para os autores que o estudaram…", com a exceção de Østfold e o limite lógico explícitos (ausência de granito é evidência negativa; idade discordante exclui só os granitos datados). Acrescentado também: >5.000 pegmatitos, maioria NYF. No lado do fracionamento entraram exemplos concretos citados por Černý & Ercit (2005): Greer Lake, Osis Lake, Preissac-Lacorne. · **Reescrito.**

**A07-5** `PEG-M32-A07-THOMAS-DAVIDSON-004` · 🟠 · impreciso · Estava escrito: desmistura em "um fundido rico em silicatos e um fluido aquoso de baixa densidade". Correção: fundidos **conjugados** (um mais pobre e outro muito rico em água) mais fluido, com a separação ocorrendo entre líquidos silicáticos. Acrescentado que o resumo de 2013 apresenta a evidência como ligação genética **pegmatito–granito**. Troca de 2015 citada: Thomas & Davidson, *Lithos* 212-215:462-468; London, 469-484. · confirmado · **Corrigido.**

**A07-6** `PEG-M32-A07-EXEMPLO-005` · 🟠 · certeza_indevida · "é a evidência mais forte a favor de anatexia" passou a "importante, mas não conclusiva — um granito oculto contemporâneo também produziria a coincidência". · **Corrigido.**

**A07-7** `PEG-M32-A07-HP-HT-009` · 🔵 · **aberto** · A associação de campos específicos a metamorfismo de alta P (empilhamento) e de alta T (underplating) veio de resumos secundários e não foi conferida no texto integral de Rosing-Schow et al. (2023). O texto da aula foi mantido; a ressalva está nas Fontes.

### Aula 08 — Mecânica de alojamento

**A08-1** `PEG-M32-A08-FLUXO-ESPONTANEO-004` · 🟠 · impreciso + fonte ausente · O mecanismo de auto-reforço era atribuído a "aquecimento localizado, alívio de tensão localizado". A referência primária do conceito para pegmatitos é **Plunder et al. (2022)**, *Lithos* 416-417:106652: fluxo bifásico (Stokes + Darcy não linear), ondas de porosidade e condutos tubulares. O mecanismo foi reescrito (a permeabilidade cresce com a porosidade e o fundido dilata a matriz viscosa). · confirmado (título, autores, método) · **Corrigido.**

**A08-2** `PEG-M32-A08-FORMA-PROFUNDIDADE-002` · 🔵 · A ponte entre forma do corpo e classes de Černý & Ercit é síntese do curso e agora está explicitada como tal no texto e no recap. · **Corrigido com ressalva.**

Verificado: Brisbin (1986), *American Mineralogist* 71(3-4):644-651. Corpos tabulares em regime frágil com anisotropia; corpos lenticulares a irregulares em nível profundo, dúctil e hidrostático (resumo confirmado).
Adiado para o lote B: controle por zona de cisalhamento em Greenbushes e Pilgangoora (Aula 13).

### Aula 09 — Geocronologia — atenção especial (fronteira com a Aula 10)

**Diagnóstico de fronteira:** o texto teórico não antecipava conclusões do debate de taxas ("potencialmente rápida"). O exemplo trabalhado, porém, lia a diferença de 14 Ma entre U-Pb e Ar-Ar como resfriamento do pegmatito "pouco depois" da cristalização, o que sugere implicitamente uma duração que é objeto da Aula 10. Corrigido (A09-7).

**A09-1** `PEG-M32-A09-COLUMBITA-CASSITERITA-001` · 🔴 · erro_factual · "Trebilcock" é padrão de **monazita** (pegmatito de Topsham, Maine, ~272 Ma; Tomascak et al. 1996), e não de columbita-tantalita de Manitoba. Substituído por **Coltan139** (Che et al. 2015; ID-TIMS ~506–508 Ma). · confirmado · **Corrigido.**

**A09-2** `PEG-M32-A09-RM-CASSITERITA-007` · 🔴 · erro_factual · "44069" é o padrão de **monazita** USGS 44069 (Wilmington Complex, Delaware, 424,9 Ma; Aleinikoff et al. 2006). Substituído por cassiterita **AY-4** (Yuan et al. 2011, ~158 Ma), com a ressalva da redatação a ~152 Ma (Carr et al. 2020). · confirmado · **Corrigido.** O texto agora também alerta que nomes de padrões circulam entre minerais.

**A09-3** `PEG-M32-A09-ZIRCAO-MONAZITA-APATITA-002` · 🔴 · erro_factual (inversão) · Estava escrito: "o alto teor de Th e U também a torna mais suscetível a metamictização", e o exemplo trabalhado se apoiava nisso. A monazita praticamente **não** fica metamítica (recupera o dano em baixa T). As armadilhas reais são o excesso de ²⁰⁶Pb por ²³⁰Th e a dissolução-reprecipitação por fluidos. A lista de minerais metamícticos foi corrigida (zircão, torita, óxidos de Nb-Ta-Ti-ETR), e no exemplo a monazita foi trocada por zircão rico em U-Hf.
Fonte: "The absence of metamictisation in natural monazite" (*Sci. Rep.* 2020); Meldrum et al. (1998, *GCA*) · confirmado · **Corrigido.**

**A09-4** `PEG-M32-A09-COLTAN-U-MATRIZ-008` · 🟠 · "U tipicamente baixo" passou a teor variável, e entrou o **efeito de matriz** dependente de Ta/(Nb+Ta), que é a principal limitação da datação LA-ICP-MS de columbita-tantalita. · confirmado · **Corrigido.**

**A09-5** `PEG-M32-A09-ZIRCAO-009` · 🟠 · Estava escrito: "zircão geralmente escasso … Zr relativamente compatível em relação aos fluxantes". Correção: nos pegmatitos evoluídos o zircão costuma ser rico em Hf-U, metamítico e discordante, e pode ser herdado. · provável · **Corrigido.**

**A09-6** `PEG-M32-A09-IDADE-PEGMATITO-GRANITO-005` · 🟠 · inconsistencia_interna · O objetivo (4) promete "mais antiga", mas só havia três padrões, nenhum com o pegmatito mais antigo. Acrescentado o padrão "pegmatito mais antigo, exclui o granito candidato". O padrão "mais jovem" passou a incluir a anatexia (caso Tørdal), e o intervalo "represado" foi rotulado como hipótese controversa. · **Corrigido.**

**A09-7** `PEG-M32-A09-ARAR-RESFRIAMENTO-010` · 🟠 · omissao_que_gera_erro (fronteira com a Aula 10) · A diferença de ~14 Ma entre U-Pb (coltan) e Ar-Ar (muscovita) mede o **resfriamento regional** da encaixante abaixo do fechamento do Ar, e **não** a duração da cristalização do pegmatito. Texto acrescentado, com remissão explícita à Aula 10. · **Corrigido.**

**A09-8** `PEG-M32-A09-EXEMPLO-006` · 🟠 · certeza_indevida · "essa data não deve ser interpretada como um quarto evento geológico real" (categórico) passou a "o intercepto inferior pode registrar um evento real ou ser artefato de perda contínua; decidir exige evidência independente". · **Corrigido.**

Verificado: Stacey & Kramers (1975) para a correção de Pb comum; temperaturas de fechamento relativas (Ar-Ar e Rb-Sr em micas < U-Pb em zircão; apatita U-Pb mais baixa).

---

## Correções aplicadas

**Aplicadas em:** 2026-09-24

| Aula | Achados corrigidos | Arquivo |
|---|---|---|
| 01 | A01-1…A01-6 | `32-pegmatitos-aula-01-definicao-textural-hierarquia.md` |
| 02 | A02-1, 2, 4, 5, 6, 7, 8 (+ A01-4) | `32-pegmatitos-aula-02-zonamento-texturas-diagnosticas.md` |
| 03 | A03-1…A03-6 | `32-pegmatitos-aula-03-fracionamento-fluxantes-fluidos.md` |
| 04 | A04-1…A04-10 | `32-pegmatitos-aula-04-mineralogia-de-pegmatitos.md` |
| 05 | A05-1…A05-8 | `32-pegmatitos-aula-05-classificacao-cerny-ercit-wise-muller-simmons.md` |
| 06 | A06-1…A06-7 | `32-pegmatitos-aula-06-jahns-burnham-subresfriamento-london.md` |
| 07 | A07-1…A07-6 (A07-7 aberto) | `32-pegmatitos-aula-07-fracionamento-anatexia-imiscibilidade.md` |
| 08 | A08-1, A08-2 | `32-pegmatitos-aula-08-mecanica-de-alojamento.md` |
| 09 | A09-1…A09-8 | `32-pegmatitos-aula-09-geocronologia-de-pegmatitos.md` |

Em cada aula, o bloco `auditoria:` do rodapé passou de `pendente` para a data, o modo e este relatório. As alegações auditáveis afetadas foram anotadas com o desfecho, sem renumerar os `claim_id` originais. Os IDs novos criados pela auditoria usam sufixos a partir de 006.

**course-state.yaml:** apenas os `content_hash` das aulas 01–09 do módulo 32 foram atualizados (a edição muda o sha256). Os blocos `audit` e `didactic_review` **não** foram tocados.

## Pendências (para a consolidação)

1. **A07-7 (🔵, aberto):** conferir no texto integral de Rosing-Schow et al. (2023) a associação de campos a metamorfismo de alta P e de alta T.
2. **A01-5 / controle estrutural de Greenbushes e Pilgangoora (🔵, adiado):** verificar na Aula 13 (lote B) a ausência de parental demonstrado e o controle por zona de cisalhamento; manter a formulação cautelosa da Aula 01 coerente com a da Aula 13.
3. **Citações de memória consolidada, não conferidas por busca nesta rodada** (baixo risco, a rechecar na consolidação): London (1986, *Am. Mineral.* 71:376-395); London (1992, *Can. Mineral.* 30:499-540); London (2005, *Lithos* 80:281-303); London (2013, *Rocks & Minerals* 88:527-538); London et al. (1993, *CMP* 113:450-465); Fenn (1977); Swanson (1977); Atencio et al. (2010); volume e páginas de Van Lichtervelde et al. (2007) e de Che et al. (2015); periódico de Webber et al. (1997); Martin & De Vito (2005).

## Observações de continuidade para os lotes B e C

- **Aula 10 (taxas de cristalização):** a Aula 06 agora apresenta Nabelek et al. (2010) como *proposta*, e "dias a poucos anos" como estimativa contestada. A Aula 09 afirma que diferenças U-Pb × Ar-Ar medem resfriamento **regional**, não duração da cristalização. A Aula 10 precisa manter o debate aberto (Phelps et al. 2020 × Popov 2023) e não pode usar diferenças entre geocronômetros como medida direta da duração da cristalização. Webber et al. (1999) dão tempos de resfriamento de ~5 dias (Himalaya) a ~9 anos (Stewart) para diques de San Diego, e isso deve ser citado como modelo, não como medida.
- **Nomenclatura a manter no módulo:** columbita-(Fe), columbita-(Mn), tantalita-(Fe), tantalita-(Mn) (com os nomes antigos entre parênteses na primeira ocorrência); microlita como grupo (Atencio et al. 2010); polucita ·2H₂O; UST (não USST).
- **Tanco (Aula 12):** Ta distribuído entre columbita-tantalita, wodginita e microlita (Van Lichtervelde et al. 2007). Não afirmar que a microlita é o minério principal sem fonte.
- **Etta Mine (Aula 14):** espodumênio de 14,3 m (Rickwood 1981). Evitar "dezenas de metros".
- **Classificação nos estudos de caso (12–24):** a **classe** de Černý & Ercit é definida pela profundidade/fácies e não varia de um corpo para outro dentro de um campo; o que varia é tipo e subtipo. Famílias são um eixo paralelo. LCT/NYF = Černý (1991a), não Ginsburg.
- **Wise, Müller & Simmons (2022):** Grupo 3 = só anatexia, peraluminoso, estéril. Grupos 1/2 = residual granítico ou anatexia.
- **Sveconorueguesa / Evje-Iveland / Tørdal:** usar Müller, Romer & Pedersen (2017) e Rosing-Schow et al. (2023). Evje-Iveland é NYF, hospedado em anfibolitos, anatético; Tørdal granito 946 ± 4 Ma; exceção de Østfold.
- **Esmeralda (Aulas 18, 21–24):** a tipologia de Giuliani et al. (2019) distingue os depósitos "tipo xisto", ligados a pegmatito/granito em rochas máficas-ultramáficas, dos hidrotermais sem relação magmática (Colômbia). Não dizer "não pegmatítico" para os tipo xisto.
- **San Diego (Aula 23):** *line rock* = aplito bandado com granada/turmalina na lapa (Webber et al. 1997, 1999), abaixo da zona de bolsões.
- **Geocronologia nos estudos de caso:** Trebilcock e 44069 são padrões de **monazita**. Coltan139 (columbita) e AY-4 (cassiterita) são os usuais. A monazita não fica metamítica.
- **Thomas & Davidson:** o trabalho de 2013 reforça a ligação **granito → pegmatito**; a troca com London é de 2015 (*Lithos* 212-215).
