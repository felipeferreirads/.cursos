# Auditoria científica — Módulo 34: Sistemas hidrotermais e metalogênese

**Curso:** geologia-avancado
**Módulo:** 34 — `34-sistemas-hidrotermais-metalogenese` (10 aulas; o currículo previa 7, e três foram divididas na redação)
**Modo:** `audit-and-fix` · **Profundidade:** `full`
**Auditado em:** 2026-09-29 · **Passagens:** 1
**Backup do estado antes da auditoria:** `course-state.yaml.bak-20260929-pre-m34-audit` (idêntico byte a byte ao estado no início desta passagem; hashes das 10 aulas no estado conferidos contra o disco antes de qualquer edição).
**Escopo:** as 10 aulas, o hub do módulo e os 72 `claim_id` declarados na redação (contagem em disco por script: a01 7, a02 7, a03 7, a04 7, a05 7, a06 7, a07 8, a08 9, a09 6, a10 7; sem duplicata). Não existem questionário, baralho nem glossário do módulo.
**Veredito:** **Aprovado após correções.** Foram levantados 5 vermelhos, 11 laranjas, 1 amarelo, 5 azuis e 0 brancos. Todos foram tratados nas aulas, e nada ficou em aberto.

---

## Resumo por severidade

| Severidade | Levantados | Corrigidos / tratados | Em aberto |
|---|---|---|---|
| 🔴 Erro | 5 | 5 | **0** |
| 🟠 Impreciso | 11 | 11 | **0** |
| 🟡 Desatualizado | 1 | 1 (nome antigo mantido como referência) | **0** |
| 🔵 Sem fonte | 5 | 5 (quatro confirmados com fonte e reescritos; um reescrito sem a afirmação não confirmada) | 0 |
| ⚪ Controverso | 0 | — | 0 |
| **Total** | **22** | **22** | **0** |

Gate de qualidade: **liberado** para o questionário e os flashcards (0 vermelhos e 0 laranjas em aberto), com as restrições do fim deste relatório.

### Inversões de sentido (as perigosas)

- **🔴 1 (Aula 02) — telescopagem ao contrário.** A aula dizia que, num sistema telescopado, o colapso "superpõe alteração de alta temperatura sobre alteração de baixa temperatura". É o contrário. O sistema esfria e a paleossuperfície é rebaixada durante a mineralização, então as isotermas recuam e a alteração **mais fria e mais rasa** (sericítica, argílica avançada) é que se superpõe à **mais quente e mais antiga** (potássica). É exatamente por isso que o *lithocap* e o halo sericítico aparecem sobre o núcleo potássico.
- **🔴 2 (Aula 05) — zonamento tectônico dos epitermais com a IS no lado errado.** A aula punha a sulfetação intermediária (IS) junto com a baixa (LS), em arcos extensionais, e punha a alta (HS) em arcos "em compressão". Sillitoe & Hedenquist (2003) põem **HS e IS** juntas, em arcos andesítico-dacíticos sob esforço **neutro a levemente extensional**, o mesmo ambiente dos pórfiros. A **LS** fica em riftes com vulcanismo **bimodal**. Um questionário tirado do texto antigo teria gabarito errado na pergunta mais óbvia do tema.
- **🔴 3 (Aula 10) — Islândia como campo geotérmico "de arco vulcânico".** A Islândia fica sobre a dorsal meso-atlântica emersa, com contribuição de pluma. Não é arco.

### Padrão dominante

É o mesmo dos Módulos 27–33. Os erros graves estavam em frases de ligação que soavam seguras e **não** estavam marcadas como risco: a direção da telescopagem, o zonamento tectônico dos epitermais e a Islândia. Houve também uma contradição com um módulo já auditado: a arquitetura do pórfiro em halos concêntricos (achado 22), que o Módulo 22 já tratava como modelo histórico. Os exemplos brasileiros marcados como risco moderado em geral **conferiram**. As exceções foram a unidade hospedeira de Morro Agudo (Grupo Vazante, não Bambuí) e a leitura de Posse como pórfiro/epitermal metamorfisado. As referências "de memória" erraram duas vezes: Juliani et al. (2005) está na *Chemical Geology*, não na *Mineralium Deposita*, e o "Lobato et al. (2001)" da Aula 08 misturava o título de uma série de 1998 da *RBG* com o ano e o volume de outra obra.

---

## Achados

### 🔴 1. Telescopagem descrita como superposição de alta temperatura sobre baixa temperatura (INVERSÃO)

**claim_id:** `HID-M34-A02-ZONAMENTO-006`
**Tipo:** erro factual (sentido invertido)
**Onde:** Aula 02 · "O zonamento como resultado de perda de acidez e calor", segunda ressalva
**Está escrito:** "o zonamento vertical de um mesmo sistema pode ser **telescopado**: o colapso do sistema, com erosão ou soerguimento, superpõe alteração de alta temperatura sobre alteração de baixa temperatura (Aulas 03 e 05)."
**Problema:** a telescopagem é o declínio térmico do sistema somado ao rebaixamento da paleossuperfície durante a própria mineralização (erosão, soerguimento, colapso do edifício vulcânico). As zonas mais frias e rasas migram para baixo e se superpõem às zonas mais quentes e mais antigas. Assim, sericítica e argílica avançada ficam sobre a potássica, e não o contrário.
**Correção proposta:** "à medida que o sistema esfria e a paleossuperfície é rebaixada durante a própria mineralização [...], as isotermas recuam e alteração de temperatura mais baixa, originalmente mais rasa (sericítica, argílica avançada), se superpõe à alteração de temperatura mais alta formada antes, como a potássica (Sillitoe, 2010; Aulas 03 e 05)."
**Fonte:** Sillitoe 2010, *Econ. Geol.* 105:3-41 (seções sobre telescopagem e evolução temporal; texto consultado 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** nenhum outro arquivo (as Aulas 03 e 05 não repetem a frase).

### 🔴 2. HS associada a compressão; IS associada a extensão, junto com LS

**claim_id:** `HID-M34-A05-TECTONICA-005`
**Tipo:** erro factual
**Onde:** Aula 05 · "Controle tectônico e caldeiras", os dois itens
**Está escrito:** "Arcos em **compressão** ou com regime neutro tendem a favorecer sistemas HS e pórfiros associados, porque a compressão confina o magma [...]"; "Arcos com **extensão** ou **transtensão** favorecem sistemas LS e IS [...]".
**Problema:** em Sillitoe & Hedenquist (2003), HS e IS ocorrem no **mesmo** ambiente: arcos andesítico-dacíticos sob esforço neutro a levemente extensional, o ambiente dos pórfiros, com os quais podem ter ligação genética. A LS se restringe a suítes bimodais (basalto-riolito) de riftes e ambientes extensionais. O texto separava IS de HS e atribuía à compressão um papel que a fonte não dá aos epitermais.
**Correção proposta:** reescrever os dois itens: HS e IS em arcos andesítico-dacíticos neutros a levemente extensionais, com os pórfiros; LS em riftes com vulcanismo bimodal.
**Fonte:** Sillitoe & Hedenquist 2003, SEG SP 10:315-343 (resumo e síntese secundária, consultados 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** metadados da Aula 05 (claim); o exemplo trabalhado (passo 5) continua compatível.

### 🔴 3. Islândia listada entre campos geotérmicos "de arcos vulcânicos"

**claim_id:** `HID-M34-A10-ANALOGOS-005`
**Tipo:** erro factual
**Onde:** Aula 10 · "Análogos modernos", segundo item
**Está escrito:** "**Campos geotérmicos** de arcos vulcânicos (por exemplo, sistemas na Nova Zelândia, na Islândia e nas Filipinas): análogos de epitermais de baixa sulfetação [...]".
**Problema:** a Islândia é um segmento emerso da dorsal meso-atlântica, com pluma mantélica; não é arco. A Nova Zelândia (Zona Vulcânica de Taupo, rifte de arco) e as Filipinas estão corretas. Broadlands-Ohaaki, na Zona Vulcânica de Taupo, é o caso clássico de precipitação atual de Au-Ag em sistema geotérmico, inclusive em tubulações de poços.
**Correção proposta:** "Campos geotérmicos de arcos vulcânicos e de riftes de arco (por exemplo, a Zona Vulcânica de Taupo, na Nova Zelândia, com o campo de Broadlands-Ohaaki, e sistemas das Filipinas) [...]", com uma frase curta que diz que a Islândia fica sobre a dorsal, não em arco.
**Fonte:** "Hydrothermal minerals and precious metals in the Broadlands-Ohaaki geothermal system: implications for understanding low-sulfidation epithermal environments", *Econ. Geol.* 95(5), 2000, a partir da p. 971 (título e resumo); síntese sobre ouro e prata nos sistemas da Zona Vulcânica de Taupo (*Geothermics*, 2015); geologia da Península de Reykjanes (literatura geral de tectônica)  ·  **Nível:** revisada por pares / geral
**Confiança:** confirmado
**Também aparece em:** metadados da Aula 10 (claim).

### 🔴 4. Juliani et al. (2005) citado na *Mineralium Deposita*

**claim_id:** `HID-M34-A05-TAPAJOS-006`
**Tipo:** erro factual (referência)
**Onde:** Aula 05 · Fontes; parágrafo "No Brasil, a Província Tapajós"; metadados
**Está escrito:** "Juliani, C. et al. (2005), 'Paleoproterozoic high-sulfidation mineralization in the Tapajós gold province, Amazonian Craton, Brazil', *Mineralium Deposita*, 40 (título completo e paginação a conferir na auditoria)."
**Problema:** o artigo existe, mas saiu na *Chemical Geology*, 215, 95-125, com título completo "[...]: geology, mineralogy, alunite argon age, and stable-isotope constraints". O conteúdo que a aula lhe atribui está correto: alunita magmático-hidrotermal datada por Ar-Ar, isótopos estáveis, brechas num complexo vulcânico riolítico de caldeiras aninhadas, e primeira evidência de alta sulfetação no Cráton Amazônico. Esse último ponto amarra bem a seção de caldeiras e foi acrescentado numa frase.
**Correção proposta:** referência completa corrigida; texto: "mineralização aurífera de alta sulfetação paleoproterozoica, com alunita magmático-hidrotermal em brechas de um complexo vulcânico riolítico de caldeiras aninhadas, datada por Ar-Ar em alunita e estudada com isótopos estáveis por Juliani et al. (2005), que a descreveram como a primeira evidência desse tipo no Cráton Amazônico".
**Fonte:** Juliani et al. 2005, *Chem. Geol.* 215:95-125 (ScienceDirect e repositório USGS/UNL, consultados 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** metadados da Aula 05.

### 🔴 5. Referência "Lobato et al. (2001)" híbrida, inexistente como citada

**claim_id:** `HID-M34-A08-BRASIL-006`
**Tipo:** erro factual (referência fabricada por mistura)
**Onde:** Aula 08 · "Distribuição no tempo e exemplos brasileiros" (Quadrilátero Ferrífero); Fontes; metadados
**Está escrito:** "Lobato, L. M. et al. (2001), 'Styles of hydrothermal alteration and gold mineralization associated with the Nova Lima Group of the Quadrilátero Ferrífero', *Revista Brasileira de Geociências*, 31 (Partes I e II; volume e paginação a conferir na auditoria)"; texto: "Morro Velho [...] e Cuiabá, discutidos em termos de controle estrutural, alteração e sulfetação em formações ferríferas (Lobato et al., 2001)".
**Problema:** a série "Styles of hydrothermal alteration [...]" (Partes I e II) é da *RBG* de **1998** (vol. 28). Em 2001, Lobato, Ribeiro-Rodrigues & Vieira publicaram "Brazil's premier gold province. Part II" na *Mineralium Deposita*, 36:249-277. A citação misturava o título de uma obra com o ano e o volume de outra. O texto também ficava vago e sugeria que Morro Velho é minério em formação ferrífera. Lobato et al. (2001) descrevem três estilos: substituição sulfetada de formação ferrífera com controle estrutural (Cuiabá é o exemplo), sulfetos disseminados em zonas de cisalhamento, e veios de quartzo-carbonato-sulfeto.
**Correção proposta:** citar Lobato, Ribeiro-Rodrigues & Vieira (2001), *Miner. Deposita* 36:249-277, e reescrever a frase com os três estilos, pondo Cuiabá como o exemplo em formação ferrífera.
**Fonte:** Lobato et al. 2001, *Miner. Deposita* 36:249-277 (Springer, resumo); Lobato et al. 1998, *RBG* 28(3):339-354 (PPeGeo)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** metadados da Aula 08. O Crixás, que estava no mesmo claim, virou claim próprio (achado 20).

### 🟠 6. Posse e Chapada tratados em bloco como "pórfiro/epitermal metamorfisado", sem fonte

**claim_id:** `HID-M34-A09-MARAROSA-005`
**Tipo:** omissão que gera erro / certeza indevida
**Onde:** Aula 09 · "Exemplo brasileiro: Mara Rosa e o Arco Magmático de Goiás"; Recap; Fontes ("fonte primária a definir"); Aula 10 (exemplos integrados)
**Está escrito:** "hospeda depósitos de Cu-Au e de Au (como Chapada e Posse), cuja interpretação como sistemas magmático-hidrotermais (do tipo pórfiro/epitermal) **metamorfisados** é discutida na literatura, com assembleias de alteração recristalizadas em cianita, granada, biotita e muscovita (informação de risco moderado, a conferir na auditoria)".
**Problema:** a parte de **Chapada** está certa e tem fonte forte. Oliveira et al. (2016) o tratam como pórfiro Cu-Au neoproterozoico metamorfisado, que preserva o zonamento de alteração em torno de dioritos porfiríticos, com as rochas ricas em cianita interpretadas como o halo **argílico** metamorfisado. Os autores propõem também um segundo evento de Cu-Au, em zona de cisalhamento, sobreposto ao primeiro. **Posse** é outro caso: ouro hospedado em zona de cisalhamento, descrito em relatórios técnicos como *lode gold* mesotermal, embora com um evento potássico precoce (Cu-Mo) seguido de um evento sericítico com ouro. A filiação de Posse segue aberta, e agrupá-lo com Chapada como "pórfiro/epitermal metamorfisado" é afirmar mais do que a literatura sustenta.
**Correção proposta:** reescrever o parágrafo: Chapada como pórfiro metamorfisado com evento de cisalhamento imposto (bom caso de herdado × imposto); Posse como ouro em zona de cisalhamento de filiação ainda discutida. Corrigir o recap e a Aula 10, e trocar a linha "fonte a definir" por Oliveira et al. (2016).
**Fonte:** Oliveira et al. 2016, *Ore Geol. Rev.* 72:1-21 (resumo, ScienceDirect/Semantic Scholar, consultado 2026-09-29); relatório técnico *Competent Persons' Report on the Posse Gold Project* (Hochschild, 2022) e síntese de mina (Posse)  ·  **Nível:** revisada por pares / geral (Posse)
**Confiança:** confirmado (Chapada); em disputa (filiação de Posse, já tratada como aberta no texto)
**Também aparece em:** Aula 09 (recap), Aula 10 ("Exemplos brasileiros integrados").

### 🟠 7. Fluido SEDEX apresentado como sempre oxidado

**claim_id:** `HID-M34-A06-SEDEX-005`
**Tipo:** certeza indevida
**Onde:** Aula 06 · "SEDEX: a salmoura de bacia no fundo anóxico"; tabela VHMS × SEDEX (linha Fluido)
**Está escrito:** "O fluido é uma **salmoura de bacia**, oxidada, de temperatura moderada [...]"; tabela: "salmoura de bacia, salina, oxidada".
**Problema:** Cooke et al. (2000) dividem os SEDEX em dois tipos de salmoura. O tipo **McArthur** (HYC/McArthur River, Mount Isa) vem de salmoura **oxidada**, dominada por sulfato. O tipo **Selwyn** (Sullivan, Rammelsberg, bacia de Selwyn) vem de salmoura **reduzida**, dominada por H₂S. A aula citava Sullivan e Rammelsberg como exemplos e ao mesmo tempo dava o fluido como sempre oxidado.
**Correção proposta:** "salmoura de bacia de temperatura moderada, que pode ser oxidada (tipo McArthur) ou reduzida (tipo Selwyn) (Cooke et al., 2000)"; tabela "oxidada ou reduzida"; Cooke et al. (2000) nas Fontes.
**Fonte:** Cooke, Bull, Large & McGoldrick 2000, *Econ. Geol.* 95:1-18 (resumo GeoScienceWorld, consultado 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** metadados da Aula 06.

### 🟠 8. *Black smokers* atribuídos a Corliss et al. (1979)

**claim_id:** `HID-M34-A06-VHMS-MOTOR-001`
**Tipo:** impreciso (atribuição)
**Onde:** Aula 06 · "VHMS", passo 3; Aula 10 · "Análogos modernos", primeiro item
**Está escrito:** "As chaminés ativas modernas, os *black smokers*, foram descobertas em cadeias meso-oceânicas no final dos anos 1970 (Corliss et al., 1979)"; Aula 10: "análogos diretos de VHMS (Corliss et al., 1979; Hannington et al., 2005)".
**Problema:** Corliss et al. (1979) descrevem as fontes **mornas** do Rifte de Galápagos, observadas em 1977. As chaminés de alta temperatura escurecidas por sulfeto, os *black smokers* propriamente ditos, foram descobertas em 1979 na Dorsal do Pacífico Leste a 21°N, com fluido a 380 ± 30 °C (Spiess et al., 1980). A década está certa, mas a atribuição não.
**Correção proposta:** separar as duas descobertas e citar Spiess et al. (1980), *Science* 207:1421-1433, nas duas aulas.
**Fonte:** Corliss et al. 1979, *Science* 203:1073-1083; Spiess et al. 1980, *Science* 207:1421-1433 (resumo, consultado 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 10 (texto, Fontes e metadados).

### 🟠 9. Continuum crustal limitado a "xisto-verde superior ao anfibolito"

**claim_id:** `HID-M34-A08-CONTINUUM-002`
**Tipo:** impreciso
**Onde:** Aula 08 · "Ouro orogênico: definição e modelo do continuum crustal"
**Está escrito:** "sob condições que variam do fácies xisto-verde superior ao anfibolito".
**Problema:** o continuum de Groves et al. (1998) vai do fácies **sub-xisto-verde ao granulito** e cobre profundidades de cerca de 2 a 20 km. A maioria dos depósitos está em fácies xisto-verde. A subdivisão é epizonal (<6 km), mesozonal (6-12 km) e hipozonal (>12 km). O texto cortava as duas pontas da faixa, e a raiz do modelo está justamente na amplitude.
**Correção proposta:** "de cerca de 2 a 20 km [...] do fácies sub-xisto-verde ao granulito, com a maioria dos depósitos em fácies xisto-verde; Groves et al. (1998) subdividem a coluna em epizonal, mesozonal e hipozonal".
**Fonte:** Groves et al. 1998, *Ore Geol. Rev.* 13:7-27 (resumo e sínteses secundárias, consultados 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** metadados da Aula 08.

### 🟠 10. Baixa sulfetação com "esfalerita, galena; Au-Ag, com Zn-Pb"

**claim_id:** `HID-M34-A05-TRES-TIPOS-002`
**Tipo:** impreciso
**Onde:** Aula 05 · tabela dos três tipos (linha LS); Recap
**Está escrito:** "pirita, esfalerita, galena; Au-Ag, com Zn-Pb"; recap: "baixa sulfetação: [...] Au-Ag com Zn-Pb".
**Problema:** a assembleia de LS em sentido estrito é pirita-pirrotita-arsenopirita com **esfalerita rica em Fe**, e os metais-base são **subordinados**. Zn-Pb com esfalerita pobre em Fe e galena é a marca da **IS**, e a própria tabela a trazia na linha seguinte. Do jeito que estava, a tabela apagava a diferença entre LS e IS que o texto pretende ensinar.
**Correção proposta:** LS "pirita, arsenopirita, pirrotita, esfalerita rica em Fe; Au-Ag, com metais-base subordinados"; recap "Au-Ag com poucos metais-base".
**Fonte:** Einaudi, Hedenquist & Inan 2003, SEG SP 10 (estados de sulfetação, % FeS da esfalerita); Sillitoe & Hedenquist 2003; Hedenquist, Arribas & Gonzalez-Urien 2000 (consultados 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 05 (recap).

### 🟠 11. Serrinha (Alta Floresta) usado como exemplo de IRGS sem dizer que o granito é cálcio-alcalino tipo I

**claim_id:** `HID-M34-A04-ALTAFLORESTA-006`
**Tipo:** omissão que gera erro
**Onde:** Aula 04 · parágrafo "No Brasil, a Província Aurífera de Alta Floresta"; Recap; Fontes (título)
**Está escrito:** "Serrinha é descrito por Moura et al. (2006) como depósito aurífero de tipo relacionado a granito [...]"; recap: "Exemplos brasileiros: [...] ouro associado a granitos em Alta Floresta (MT)" (dentro da seção de IRGS).
**Problema:** Moura et al. (2006) ligam Serrinha ao monzogranito Matupá, **cálcio-alcalino do tipo I** (1872 ± 12 Ma), e o aproximam de depósitos de ouro **de estilo pórfiro**, relacionados a intrusão. O IRGS em sentido estrito, que a mesma aula define, pede granitoide **reduzido** (série da ilmenita). Posto na seção de IRGS e sem essa ressalva, o exemplo leva o aluno a classificar Serrinha como IRGS reduzido. O título do artigo nas Fontes também estava alterado ("southern Amazonian Craton" em vez de "Southern Amazonia").
**Correção proposta:** acrescentar que o granito é cálcio-alcalino tipo I e que os autores o aproximam do estilo pórfiro, de modo que o exemplo ilustra a família "relacionada a intrusão" em sentido amplo, e não o IRGS reduzido; ajustar o recap e o título.
**Fonte:** Moura, Botelho, Olivo & Kyser 2006, *Econ. Geol.* 101:585-605 (resumo GeoScienceWorld, consultado 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 04 (recap e Fontes); a Aula 10 ("ouro relacionado a granitos em Alta Floresta") fica compatível.

### 🟠 12. Pórfiros com "parcela dominante" da produção de Cu **e** Mo

**claim_id:** `HID-M34-A03-DEFINICAO-001`
**Tipo:** impreciso
**Onde:** Aula 03 · "O que é um depósito do tipo pórfiro"
**Está escrito:** "Como classe, os pórfiros respondem por parcela dominante da produção mundial de cobre e Mo".
**Problema:** o número de referência é quase três quartos do Cu e cerca de metade do Mo (Sillitoe, 2010). "Dominante" serve para o Cu. Para o Mo, que tem cerca de metade, a palavra exagera.
**Correção proposta:** "fornecem perto de três quartos do cobre e cerca de metade do molibdênio produzidos no mundo (Sillitoe, 2010)".
**Fonte:** Sillitoe 2010, *Econ. Geol.* 105:3-41 (resumo)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟠 13. Classificação litoestratigráfica de VHMS incompleta

**claim_id:** `HID-M34-A06-CLASSIFICACAO-VHMS-003`
**Tipo:** omissão que gera erro
**Onde:** Aula 06 · parágrafo "Franklin et al. (2005) classificam os VHMS"
**Está escrito:** "(máficos, bimodais máficos, bimodais félsicos, siliciclásticos-félsicos)".
**Problema:** o esquema de Franklin et al. (2005) tem **cinco** tipos: bimodal-máfico, máfico, **pelítico-máfico**, bimodal-félsico e siliciclástico-félsico. A lista entre parênteses se apresentava como completa e omitia um tipo. Galley et al. (2007) acrescentam um sexto grupo, o bimodal-félsico híbrido, que não precisa entrar na aula.
**Correção proposta:** "(cinco tipos litoestratigráficos: bimodal-máfico, máfico, pelítico-máfico, bimodal-félsico e siliciclástico-félsico)".
**Fonte:** Franklin et al. 2005, SEG 100th Anniv. Vol.:523-560 (via sínteses de Ross & Mercier-Langevin e USGS OF 2009-1034, consultadas 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** metadados da Aula 06.

### 🟠 14. Termo "epitermal" atribuído a Simmons et al. (2005); profundidade "um a dois km"

**claim_id:** `HID-M34-A05-DEFINICAO-001`
**Tipo:** impreciso (atribuição e faixa)
**Onde:** Aula 05 · "Epitermal: um conceito de profundidade e temperatura"; Recap
**Está escrito:** "O termo **epitermal** foi proposto para depósitos formados em profundidade rasa (da ordem de poucas centenas de metros até cerca de um a dois quilômetros [...]) e a temperaturas [...] abaixo de aproximadamente 300 °C (Simmons et al., 2005)".
**Problema:** o termo vem de Lindgren (1922, 1933), que o definia para profundidades de até ~900 m e 50–200 °C. A definição moderna, de Hedenquist et al. (2000) e Simmons et al. (2005), é de profundidade até cerca de 1,5 km e temperaturas geralmente entre ~150 e ~300 °C. Do jeito que a frase estava, o leitor atribuía a Simmons a proposta do termo, e o teto de "dois quilômetros" ficava acima da faixa de referência.
**Correção proposta:** "O termo epitermal, introduzido por Lindgren no início do século XX, designa hoje depósitos formados em profundidade rasa (até cerca de 1,5 km [...]) e a temperaturas geralmente entre ~150 e ~300 °C (Hedenquist et al., 2000; Simmons et al., 2005)"; recap alinhado.
**Fonte:** Simmons, White & John 2005; Hedenquist et al. 2000; resumo da definição em Wang et al. 2019, *Ore Geol. Rev.* (revisão de IS) (consultados 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 05 (recap e metadados).

### 🟠 15. Exemplo da Aula 09: "argílica avançada acima e clorítica abaixo" como o par clássico, inclusive de VHMS

**claim_id:** `HID-M34-A09-EXEMPLO-006`
**Tipo:** confusão de escopo
**Onde:** Aula 09 · Exemplo trabalhado, passo 3
**Está escrito:** "Argílica avançada acima e clorítica abaixo é o par clássico de um sistema vulcanogênico ou epitermal-pórfiro: topo ácido e fundo clorítico (Aulas 02, 05 e 06)."
**Problema:** o par "argílica avançada em cima, clorítica embaixo" é o arranjo dos sistemas pórfiro-epitermais. Em VHMS, o que se espera é o **núcleo clorítico** da zona de alimentação envolvido por **halo sericítico/aluminoso** (Aula 06). Além disso, o enunciado do exemplo diz que as lentes estão **lado a lado** e discordantes, sem dar posição vertical. O passo tirava uma conclusão ("acima/abaixo") que os dados não dão.
**Correção proposta:** dizer que um corpo aluminoso ao lado de um magnesiano-ferroso é o par esperado de um sistema hidrotermal antigo, e mostrar as duas leituras: VHMS (núcleo clorítico e halo sericítico/aluminoso) e pórfiro-epitermal (argílica avançada no topo). A escolha entre elas depende da posição original e das associações (sulfeto maciço e exalito apontam para VHMS).
**Fonte:** Franklin et al. 2005; Galley et al. 2007; Sillitoe 2010; Bonnet & Corriveau 2007  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🟡 16. Morro Agudo "em carbonatos neoproterozoicos do Grupo Bambuí"

**claim_id:** `HID-M34-A07-MVT-BRASIL-004`
**Tipo:** desatualização
**Onde:** Aula 07 · parágrafo de exemplos de MVT; metadados
**Está escrito:** "o Zn-Pb de Morro Agudo (Minas Gerais), hospedado em carbonatos neoproterozoicos do Grupo Bambuí, é frequentemente citado como MVT, e o depósito de Vazante (Zn, em willemita), no mesmo contexto regional, tem classificação **discutida** entre MVT e outros modelos hidrotermais (a conferir na auditoria)".
**Problema:** Morro Agudo está hospedado nos dolomitos do **Grupo Vazante**, uma sequência carbonática de idade meso a neoproterozoica ainda discutida. A literatura antiga incluía essas rochas no Grupo Bambuí. Morro Agudo já foi classificado como SEDEX, tipo irlandês e MVT. Cordeiro et al. (2018) o tratam como o maior MVT conhecido do Brasil, epigenético, formado por mistura de salmouras de bacia metalíferas com água do mar ou conata. **Vazante** está certo como "discutido", mas por outro motivo. É o maior depósito hipogênico de willemita conhecido, controlado pela zona de cisalhamento de Vazante, e a discussão é sobre o modelo de Zn não sulfetado hidrotermal, e não "MVT ou não".
**Correção proposta:** "Morro Agudo (Paracatu) está hospedado em dolomitos do Grupo Vazante (idade meso a neoproterozoica discutida; na literatura antiga, incluído no Grupo Bambuí); já foi classificado como SEDEX, tipo irlandês e MVT, e os estudos mais recentes o tratam como MVT epigenético (Cordeiro et al., 2018). Vazante é minério de willemita hipogênico controlado por zona de cisalhamento (Monteiro et al., 2006)."
**Fonte:** Cordeiro et al. 2018, *Ore Geol. Rev.* 101:437-452; Monteiro et al. 2006, *Ore Geol. Rev.* 28:201-234; revisão do distrito de Vazante (*Minerals* 8:22, 2018) (consultados 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 07 (recap, que continua correto: "Morro Agudo (MG) é citado como MVT; Vazante tem classificação discutida").

### 🔵 17. Clorita "mais rica em Mg" como vetor para o centro de um VHMS

**claim_id:** `HID-M34-A06-EXEMPLO-007`
**Tipo:** evidência insuficiente
**Onde:** Aula 06 · Exemplo trabalhado, passo 4
**Está escrito:** "o furo seguinte deve seguir a direção em que a clorita fica mais intensa e mais rica em Mg."
**Problema:** a intensidade da cloritização como vetor para a zona de alimentação está bem estabelecida. O **sentido** do gradiente Fe/Mg da clorita não tem regra geral que eu tenha conseguido confirmar. Em alguns distritos o núcleo do conduto tem clorita ferrosa, em outros magnesiana. Não se inventou uma direção.
**Correção proposta:** manter a intensidade como vetor e dizer que a razão Fe/Mg da clorita varia de forma sistemática, mas que o sentido do gradiente muda de depósito para depósito e precisa ser calibrado no distrito.
**Fonte:** Galley 1993/2007 (condutos com núcleo clorítico e halo sericítico); estudos de vetorização no Cinturão Pirítico Ibérico (*Solid Earth* 12:1931, 2021), consultados 2026-09-29  ·  **Nível:** revisada por pares
**Confiança:** não verificado (o sentido do gradiente); afirmação retirada
**Também aparece em:** Aula 02 ("composição pode servir de vetor", sem sentido, fica como está).

### 🔵 18. Seridó/Brejuí: skarn de W sem fonte primária

**claim_id:** `HID-M34-A04-SERIDO-004`
**Tipo:** evidência insuficiente → confirmado
**Onde:** Aula 04 · parágrafo "Exemplo brasileiro clássico de skarn de W"; metadados
**Está escrito:** "[...] com minas como Brejuí, em que a scheelita ocorre em skarns em rochas cálcio-silicáticas e mármores do Grupo Seridó (informação a ser conferida na auditoria; ver claim de risco moderado)."
**Problema:** a informação estava sem fonte, e o aviso interno à auditoria estava no texto do aluno. Conferido: a maioria das centenas de ocorrências de scheelita da província está em níveis cálcio-silicáticos no contato entre mármores e gnaisses da **Formação Jucurutu** (Grupo Seridó), perto de plútons graníticos brasilianos. Brejuí, em Currais Novos, é um skarn de **W-Mo** desenvolvido em mármores dessa formação.
**Correção proposta:** reescrever com a Formação Jucurutu, os plútons brasilianos e Brejuí como skarn de W-Mo; citar Souza Neto et al. (2008); remover o aviso.
**Fonte:** Souza Neto et al. 2008, *Miner. Deposita* 43:185-205; Mindat (Brejuí W-Mo skarn deposit), consultado 2026-09-29  ·  **Nível:** revisada por pares / base de referência
**Confiança:** confirmado
**Também aparece em:** Aula 04 (recap, compatível).

### 🔵 19. VHMS brasileiros (Palmeirópolis, Aripuanã) sem fonte

**claim_id:** `HID-M34-A06-VHMS-BRASIL-004`
**Tipo:** evidência insuficiente → confirmado
**Onde:** Aula 06 · final da seção VHMS; metadados
**Está escrito:** "No Brasil, ocorrem VHMS em terrenos proterozoicos, como o Zn-Cu de Palmeirópolis (Tocantins) e o distrito de Aripuanã (Mato Grosso), citados na literatura brasileira (a conferir em auditoria)."
**Problema:** a informação estava sem fonte, com o aviso interno visível. Conferido: Palmeirópolis é um VMS de **Zn-Pb-Cu** em metavulcânicas ácidas e básicas **mesoproterozoicas** (~1,3 Ga) em fácies anfibolito. Aripuanã é um VMS **paleoproterozoico** (1,76–1,75 Ga) de **Zn-Pb-Ag (Au-Cu)**, formado numa caldeira submarina de vulcânicas félsicas.
**Correção proposta:** reescrever com os metais e as idades corretos e com as fontes; remover o aviso.
**Fonte:** Oliveira, Torresi & Rossi 2022, *Applied Earth Science* 131(2); Biondi, Santos & Cury 2013, *Econ. Geol.* 108:781-811 (resumos, consultados 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** —

### 🔵 20. Crixás/Serra Grande sem fonte (claim novo, desmembrado do `HID-M34-A08-BRASIL-006`)

**claim_id:** `HID-M34-A08-CRIXAS-010`
**Tipo:** evidência insuficiente → confirmado
**Onde:** Aula 08 · "Crixás (GO)"; metadados
**Está escrito:** "**Crixás (GO)**, no greenstone belt homônimo, com ouro em zonas de cisalhamento (Serra Grande) (informação a conferir na auditoria)."
**Problema:** a informação estava sem fonte, com o aviso interno visível. Conferido: Crixás é depósito de ouro **orogênico**, lavrado pela Mineração Serra Grande (AngloGold Ashanti). Os corpos são controlados por falhas de empurrão de ângulo baixo a moderado e ficam em unidades hospedeiras com estilos de alteração distintos.
**Correção proposta:** reescrever com o controle por falhas de empurrão e zonas de cisalhamento e citar Ulrich et al. (2021); remover o aviso.
**Fonte:** Ulrich et al. 2021, *Minerals* 11:1050 (consultado 2026-09-29)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 08 (recap, compatível), Aula 10 (compatível).

### 🔵 21. Avisos "a conferir na auditoria" no texto do aluno

**claim_id:** `HID-M34-MOD-PENDENCIAS-REDACAO-001`
**Tipo:** evidência insuficiente (marcas de redação)
**Onde:** Aula 04 (Seridó), Aula 05 (Fontes, Juliani), Aula 06 (VHMS brasileiros), Aula 07 (Morro Agudo/Vazante; frase "valores que devem ser conferidos na fonte primária antes de citar", em Carajás), Aula 08 (Crixás; Fontes, Lobato), Aula 09 (Mara Rosa; Fontes, "fonte primária a definir")
**Problema:** o redator deixou no corpo e nas Fontes avisos dirigidos à auditoria. Para o aluno, isso anuncia que a informação não foi checada. Todos os pontos foram conferidos (achados 4–6, 16, 18–20), e os avisos saíram. Em Carajás (Salobo, Sossego, Cristalino, Igarapé Bahia/Alemão como IOCG, com eventos neoarqueanos e paleoproterozoicos em Sossego segundo Moreto et al., 2015), o texto não cita nenhuma idade e está correto. Só a frase de aviso foi retirada.
**Correção proposta:** retirar os avisos; atualizar o campo `source` dos metadados que diziam "a conferir".
**Fonte:** ver achados citados  ·  **Nível:** —
**Confiança:** confirmado
**Também aparece em:** metadados das Aulas 03, 04, 05, 06, 07, 08, 09 e 10.

### 🟠 22. Arquitetura do pórfiro dada pelos halos concêntricos de Lowell & Guilbert (1970), em contradição com o Módulo 22

**claim_id:** `HID-M34-A03-ZONAMENTO-002` (cobre também o parágrafo correspondente de `HID-M34-A02-ZONAMENTO-006`)
**Tipo:** inconsistência interna (entre módulos) / desatualização
**Onde:** Aula 03 · "O que é um depósito do tipo pórfiro" (lista da arquitetura) e Recap; Aula 02 · "O zonamento como resultado de perda de acidez e calor"
**Está escrito:** "A arquitetura vertical resumida (Lowell & Guilbert, 1970; Sillitoe, 2010; Seedorff et al., 2005): Núcleo [...] potássica; Halo sericítico sobreposto ou envolvente; Franja propilítica externa [...]; Lithocap [...] no topo".
**Problema:** a auditoria do Módulo 22 (achado `GEOMOD3D-M22-A04-ZONEAMENTOPORFIRO-005`) já registrou que a sequência núcleo potássico → fílica → propilítica em anéis concêntricos é o modelo **histórico** de Lowell & Guilbert (1970). Sillitoe (2010) descreve a arquitetura como sobretudo **vertical**: de baixo para cima, sódico-cálcica, potássica, clorita-sericita, sericítica e argílica avançada, com a propilítica **distal e em níveis profundos**. O Módulo 34 atribuía a lista concêntrica também a Sillitoe (2010), o que contradiz o Módulo 22. Na Aula 02, a menção a Lowell & Guilbert como "modelo clássico" é correta, mas faltava a ressalva.
**Correção proposta:** na Aula 03, apresentar Lowell & Guilbert como o modelo clássico e a pilha vertical de Sillitoe (2010) como a arquitetura vigente, com a propilítica distal e profunda; ajustar o recap. Na Aula 02, acrescentar uma frase com a pilha vertical, remetendo à Aula 03.
**Fonte:** Sillitoe 2010, *Econ. Geol.* 105:3-41; Lowell & Guilbert 1970, *Econ. Geol.* 65:373-408; auditoria do Módulo 22 (2026)  ·  **Nível:** revisada por pares
**Confiança:** confirmado
**Também aparece em:** Aula 02; Módulo 22 (a04), já correto e compatível, não alterado.

---

## Verificado e correto

| claim_id | Alegação | Fonte | Confiança |
|---|---|---|---|
| `HID-M34-A01-FONTES-001` | Cinco reservatórios de água; a fonte condiciona salinidade, ligantes e redox | Robb 2005; Pirajno 2009; Hedenquist & Lowenstern 1994, *Nature* 370:519-527 | confirmado |
| `HID-M34-A01-ISOTOPOS-002` | Reta meteórica δD = 8δ¹⁸O + 10 (Craig 1961, *Science* 133:1702-1703); campos magmático e metamórfico (Taylor 1974, *Econ. Geol.* 69:843-883); isótopos restringem, não provam | Craig 1961; Taylor 1974 | confirmado |
| `HID-M34-A01-LIGANTES-003` | Cloreto para Cu-Ag-Zn-Pb-Fe; Au(HS)₂⁻ em fluido de baixa salinidade e pH quase neutro | Seward & Barnes 1997 | confirmado |
| `HID-M34-A01-GATILHOS-004` | Quatro gatilhos; ponto crítico da água ~374 °C, ~22 MPa | Robb 2005; valor termodinâmico padrão (373,9 °C; 22,06 MPa) | confirmado |
| `HID-M34-A01-HIDROLISE-005` | Hidrólise e razão cátion/H⁺ organizam a alteração (feldspato → sericita → caulinita/pirofilita) | Hemley & Jones 1964, *Econ. Geol.* 59:538-569 (resumo conferido); Reed 1997 | confirmado |
| `HID-M34-A01-CLASSIFICACAO-006` | Classificação calor × fluido é didática; orogênico e IOCG com fonte debatida | Pirajno 2009; Goldfarb & Groves 2015; Barton 2014 | confirmado |
| `HID-M34-A01-EXEMPLO-007` | Exemplo hipotético; lógica de ebulição e mistura coerente | — | confirmado |
| `HID-M34-A02-PRINCIPIO-001` | Assembleia função de T e acidez (a_K⁺/a_H⁺) | Meyer & Hemley 1967; Hemley & Jones 1964 | confirmado |
| `HID-M34-A02-ALCALINA-002` | Sódica e potássica de alta T; potássica no núcleo dos pórfiros | Seedorff et al. 2005; Sillitoe 2010 | confirmado |
| `HID-M34-A02-HIDROLITICA-003` | Sericítica (qz-ser-py); argílica intermediária × avançada | Sillitoe 2010; Corbett & Leach 1998 | confirmado |
| `HID-M34-A02-PROPILITICA-004` | Propilítica distal e pouco diagnóstica | Lowell & Guilbert 1970; Sillitoe 2010 | confirmado |
| `HID-M34-A02-CLORITICA-CARBONATICA-005` | Cloritização em condutos de VHMS; carbonatização depende do CO₂ | Franklin et al. 2005; Groves et al. 1998 | confirmado |
| `HID-M34-A02-EXEMPLO-007` | Seção hipotética interpretada como pórfiro com *lithocap* | — | confirmado |
| `HID-M34-A03-VEIOS-003` | Veios A, B, D de El Salvador | Gustafson & Hunt 1975, *Econ. Geol.* 70:857-912 | confirmado |
| `HID-M34-A03-FLUIDOS-004` | Fluido magmático → vapor + salmoura; condensado ácido forma o *lithocap* | Hedenquist & Lowenstern 1994; Sillitoe 2010 | confirmado |
| `HID-M34-A03-TECTONICA-005` | Arcos convergentes; precursores de Richards 2003 (*Econ. Geol.* 98:1515-1533); Sr/Y debatido | Richards 2003; Cooke, Hollings & Walshe 2005, *Econ. Geol.* 100:801-818 | confirmado |
| `HID-M34-A03-VARIANTES-006` | Oxidado, reduzido (Rowins 2000, *Geology* 28:491-494), alcalino; Cadia (NSW, Austrália), Galore Creek (Colúmbia Britânica, Canadá) | Rowins 2000; Holliday & Cooke 2007 (Exploration 07:791-809, conferido) | confirmado |
| `HID-M34-A03-EXEMPLO-007` | Exemplo hipotético de pórfiro oxidado | — | confirmado |
| `HID-M34-A04-SKARN-001` | Skarn como rocha; exo × endoskarn | Meinert 1992; Meinert et al. 2005 | confirmado |
| `HID-M34-A04-PROGRADO-RETROGRADO-002` | Progrado anidro → retrógrado hidratado com minério | Meinert et al. 2005 | confirmado |
| `HID-M34-A04-CLASSES-003` | Classes por metal como tendências redox | Meinert 1992; Meinert et al. 2005 | confirmado |
| `HID-M34-A04-IRGS-005` | IRGS do Yukon-Alasca (Fort Knox), série da ilmenita, Au-Bi-Te-As-W, baixo sulfeto, fluido rico em CO₂ | Thompson et al. 1999; Lang & Baker 2001; Hart 2007 (GAC SP5:95-112, conferido) | confirmado |
| `HID-M34-A04-EXEMPLO-007` | Exemplo hipotético de skarn de W | — | confirmado |
| `HID-M34-A05-EBULICAO-003` | Ebulição, perda de H₂S/CO₂, pH sobe; texturas crustiformes, calcita lamelar, adulária | White & Hedenquist 1990; Simmons et al. 2005 | confirmado |
| `HID-M34-A05-CONTINUUM-004` | Pórfiro-HS-LS/IS como partes de um sistema | Sillitoe 2010; Sillitoe & Hedenquist 2003 | confirmado |
| `HID-M34-A05-EXEMPLO-007` | Exemplo hipotético de HS e LS no mesmo distrito | — | confirmado |
| `HID-M34-A06-ARQUITETURA-002` | Monte, *stockwork* Cu-rico, pé de parede clorítico-sericítico, exalito | Franklin et al. 2005; Spry, Peter & Slack 2000 | confirmado |
| `HID-M34-A06-DEBATE-006` | SEDEX com componente de substituição; Broken Hill debatido | Leach et al. 2005, 2010 | em disputa (já tratado como debate) |
| `HID-M34-A07-MVT-001` | MVT: Zn-Pb epigenético em carbonato, salmoura de baixa T, dolomita em sela | Leach et al. 2005, 2010 | confirmado |
| `HID-M34-A07-MVT-AMBIENTE-002` | Bacias de antepaís; fluxo gravitacional | Leach et al. 2005 | confirmado |
| `HID-M34-A07-MVT-GATILHO-003` | Mistura × redução de sulfato | Leach et al. 2005 | confirmado |
| `HID-M34-A07-IOCG-DEFINICAO-005` | IOCG: óxido de Fe pobre em Ti, Cu-Au, ETR-P-F, alteração Na-Ca → K | Hitzman et al. 1992; Williams et al. 2005; Groves et al. 2010 | confirmado |
| `HID-M34-A07-IOCG-FLUIDO-006` | Fonte do fluido debatida; B em turmalina de Carajás indica evaporito marinho | Xavier et al. 2008, *Geology* 36:743-746; Barton 2014 | em disputa (já tratado como debate) |
| `HID-M34-A07-CARAJAS-007` | Salobo, Sossego, Cristalino, Igarapé Bahia/Alemão; eventos neoarqueanos e paleoproterozoicos em Sossego | Moreto et al. 2015, *Econ. Geol.* 110:809-835 | confirmado (sem idade no texto) |
| `HID-M34-A07-EXEMPLO-008` | Exemplo hipotético IOCG × MVT | — | confirmado |
| `HID-M34-A08-ORO-DEFINICAO-001` | Orogênico em cinturões metamórficos, sin-deformacional | Groves et al. 1998 | confirmado |
| `HID-M34-A08-FLUIDO-003` | Fluido aquo-carbônico, baixa salinidade, Au(HS)₂⁻ | Groves et al. 1998; Goldfarb & Groves 2015 | confirmado |
| `HID-M34-A08-FONTE-004` | Fonte do fluido orogênico debatida | Goldfarb & Groves 2015, *Lithos* 233:2-26 | em disputa (já tratado como debate) |
| `HID-M34-A08-TEMPO-005` | Picos no Neoarqueano, Paleoproterozoico e Fanerozoico | Goldfarb, Groves & Gardoll 2001, *Ore Geol. Rev.* 18:1-75 | confirmado |
| `HID-M34-A08-CARLIN-007` | Carlin: ouro invisível em pirita arsenical, descarbonatação, jasperoide | Cline et al. 2005 | confirmado |
| `HID-M34-A08-CARLIN-ORIGEM-008` | Origem magmático-hidrotermal proposta (Muntean et al. 2011, *Nat. Geosci.* 4:122-127) | Muntean et al. 2011 | em disputa (já tratado como debate) |
| `HID-M34-A08-EXEMPLO-009` | Exemplo hipotético orogênico × Carlin | — | confirmado |
| `HID-M34-A09-REESCRITA-001` | Metamorfismo aproximadamente isoquímico preserva a química anômala | Bonnet & Corriveau 2007 (GAC SP5:1035-1049, conferido) | confirmado |
| `HID-M34-A09-TRADUCAO-002` | Argílica/sericítica → qz-cianita; clorítica → cordierita-antofilita | Bonnet & Corriveau 2007; Spry et al. 2000 | confirmado |
| `HID-M34-A09-ALUMINOSILICATOS-003` | Aluminossilicatos também em metassedimentos; distinção geoquímica | Bonnet & Corriveau 2007 | confirmado |
| `HID-M34-A09-HERDADO-IMPOSTO-004` | Sulfetos dúcteis remobilizados; pirita e arsenopirita resistem | literatura de metamorfismo de minério | confirmado |
| `HID-M34-A10-SISTEMA-MINERAL-001` | Fonte, via, armadilha, deposição | Wyborn, Heinrich & Jaques 1994 (AusIMM, 109-115, conferido); McCuaig & Hronsky 2014 | confirmado |
| `HID-M34-A10-SWIR-002` | SWIR e composição de mica branca/clorita como vetores | Thompson, Hauff & Robitaille 1999 (SEG Newsletter 39, conferido); Halley, Dilles & Tosdal 2015 (SEG Newsletter 100, conferido) | confirmado |
| `HID-M34-A10-PATHFINDERS-003` | *Pathfinders* por tipo; regolito desloca anomalias | síntese das Aulas 03–08 | confirmado |
| `HID-M34-A10-GEOFISICA-004` | Magnetometria, IP, radiometria, gravimetria, EM por propriedade física | literatura geral de geofísica de exploração (Módulo 19) | confirmado |
| `HID-M34-A10-TERRENOS-ANTIGOS-006` | Preservação, química anômala, herdado × imposto, controle estrutural | Bonnet & Corriveau 2007; Groves et al. 1998 | confirmado |
| `HID-M34-A10-EXEMPLO-007` | Exemplo hipotético de greenstone com regolito | — | confirmado |

**Nota sobre a paginação de referências não rebuscadas.** Foram conferidas por busca as referências dos pontos de risco e as que sustentam correções. As demais (Robb 2005; Pirajno 2009; Seward & Barnes 1997; Reed 1997; Meyer & Hemley 1967; Lowell & Guilbert 1970; Seedorff et al. 2005; Meinert 1992/2005; Thompson et al. 1999; Lang & Baker 2001; Ishihara 1977; Simmons et al. 2005; White & Hedenquist 1990; Galley et al. 2007; Goodfellow & Lydon 2007; Leach et al. 2005/2010; Spry et al. 2000; Hitzman et al. 1992; Williams et al. 2005; Groves et al. 2010; Barton 2014; Cline et al. 2005; McCuaig & Hronsky 2014; Hannington et al. 2005) são as de referência padrão da área, com volume e paginação compatíveis com a literatura. Nenhuma delas sustenta um número ensinado como constante.

## Observações não factuais

- A Aula 06 acumula dois tipos de depósito e duas tabelas-resumo. Carga e extensão ficam para a revisão didática.
- A frase "com relação temporal e espacial a magmatismo eocênico" (Aula 08) e a data "~1,87 Ga" (Aula 04, nova) são as únicas idades numéricas que entram no módulo. Não devem virar cobrança de memorização.

---

## Correções aplicadas

**Aplicadas em:** 2026-09-29

| # | claim_id | Severidade | Desfecho | Arquivos alterados |
|---|---|---|---|---|
| 1 | `HID-M34-A02-ZONAMENTO-006` | 🔴 | Corrigido | aula-02 |
| 2 | `HID-M34-A05-TECTONICA-005` | 🔴 | Corrigido | aula-05 |
| 3 | `HID-M34-A10-ANALOGOS-005` | 🔴 | Corrigido | aula-10 |
| 4 | `HID-M34-A05-TAPAJOS-006` | 🔴 | Corrigido | aula-05 |
| 5 | `HID-M34-A08-BRASIL-006` | 🔴 | Corrigido | aula-08 |
| 6 | `HID-M34-A09-MARAROSA-005` | 🟠 | Corrigido com ressalva (filiação de Posse dada como aberta) | aula-09, aula-10 |
| 7 | `HID-M34-A06-SEDEX-005` | 🟠 | Corrigido | aula-06 |
| 8 | `HID-M34-A06-VHMS-MOTOR-001` | 🟠 | Corrigido | aula-06, aula-10 |
| 9 | `HID-M34-A08-CONTINUUM-002` | 🟠 | Corrigido | aula-08 |
| 10 | `HID-M34-A05-TRES-TIPOS-002` | 🟠 | Corrigido | aula-05 |
| 11 | `HID-M34-A04-ALTAFLORESTA-006` | 🟠 | Corrigido | aula-04 |
| 12 | `HID-M34-A03-DEFINICAO-001` | 🟠 | Corrigido | aula-03 |
| 13 | `HID-M34-A06-CLASSIFICACAO-VHMS-003` | 🟠 | Corrigido | aula-06 |
| 14 | `HID-M34-A05-DEFINICAO-001` | 🟠 | Corrigido | aula-05 |
| 15 | `HID-M34-A09-EXEMPLO-006` | 🟠 | Corrigido | aula-09 |
| 16 | `HID-M34-A07-MVT-BRASIL-004` | 🟡 | Corrigido (nome antigo "Grupo Bambuí" mantido como referência histórica) | aula-07 |
| 17 | `HID-M34-A06-EXEMPLO-007` | 🔵 | Corrigido com ressalva (sentido do gradiente Fe/Mg retirado) | aula-06 |
| 18 | `HID-M34-A04-SERIDO-004` | 🔵 | Corrigido (confirmado com fonte) | aula-04 |
| 19 | `HID-M34-A06-VHMS-BRASIL-004` | 🔵 | Corrigido (confirmado com fonte) | aula-06 |
| 20 | `HID-M34-A08-CRIXAS-010` | 🔵 | Corrigido (confirmado com fonte; claim novo na aula) | aula-08 |
| 21 | `HID-M34-MOD-PENDENCIAS-REDACAO-001` | 🔵 | Corrigido (avisos retirados) | aula-03 a aula-10 (metadados), aula-04, -05, -06, -07, -08, -09 (texto/Fontes) |
| 22 | `HID-M34-A03-ZONAMENTO-002` | 🟠 | Corrigido | aula-03, aula-02 |

**Propagação:** nenhuma externa. O módulo não tem questionário, baralho nem glossário (a auditoria correu antes deles), e não há card no Anki a corrigir. Busca no curso por Morro Agudo, Vazante, Crixás, Chapada, Mara Rosa, Palmeirópolis, Aripuanã, Seridó/Brejuí, Tapajós, telescopagem e *black smoker* fora do módulo 34: ver `cross_module_note` no estado.

**Pendências:** nenhuma.

## Restrições para o questionário e os flashcards

1. **Telescopagem:** a alteração de temperatura **mais baixa** (sericítica, argílica avançada) se superpõe à de temperatura **mais alta** (potássica), e nunca o contrário.
2. **Zonamento tectônico dos epitermais:** **HS e IS** em arcos andesítico-dacíticos neutros a levemente extensionais, com os pórfiros; **LS** em riftes com vulcanismo bimodal. Não cobrar "compressão favorece HS".
3. **LS × IS:** LS tem pirita-arsenopirita-pirrotita, esfalerita **rica** em Fe e metais-base subordinados. IS tem tetraedrita-tenantita, esfalerita **pobre** em Fe e Ag-Pb-Zn.
4. **Epitermal:** termo de Lindgren; faixa moderna até ~1,5 km e ~150–300 °C, sempre como valores aproximados.
5. **Black smokers:** Galápagos 1977 (fontes mornas, Corliss et al. 1979) ≠ *black smokers* de 1979 na Dorsal do Pacífico Leste (Spiess et al. 1980). Não cobrar datas exatas como memorização.
6. **SEDEX:** salmoura oxidada (tipo McArthur) **ou** reduzida (tipo Selwyn). Não cobrar "o fluido SEDEX é oxidado" como regra.
7. **VHMS:** cinco tipos litoestratigráficos de Franklin et al. (2005). A intensidade da cloritização é vetor. **Não** cobrar o sentido do gradiente Fe/Mg da clorita.
8. **Orogênico:** continuum de sub-xisto-verde a granulito (~2–20 km), maioria em xisto-verde.
9. **Islândia não é arco.** Análogos LS: Zona Vulcânica de Taupo (Broadlands-Ohaaki) e Filipinas.
10. **Pórfiros:** ~3/4 do Cu e ~1/2 do Mo do mundo (Sillitoe 2010), como ordem de grandeza.
11. **Serrinha (Alta Floresta):** relacionado a intrusão, de estilo próximo ao pórfiro, em monzogranito cálcio-alcalino tipo I. **Não** é exemplo de IRGS reduzido em sentido estrito.
12. **Morro Agudo:** Grupo Vazante (não Bambuí); MVT segundo os estudos recentes, já classificado como SEDEX e tipo irlandês. **Vazante:** willemita hipogênica controlada por zona de cisalhamento.
13. **Mara Rosa:** Chapada = pórfiro Cu-Au metamorfisado (cianita = halo argílico metamorfisado) com evento de cisalhamento sobreposto. A filiação de Posse é **aberta** e não deve ser cobrada como pórfiro.
14. **Quadrilátero Ferrífero:** três estilos de Lobato et al. (2001); Cuiabá = substituição de formação ferrífera. Não cobrar Morro Velho como minério em formação ferrífera.
15. Debates abertos, sem vencedor: fonte do fluido orogênico e IOCG, origem de Carlin, classificação SEDEX e IRGS.
16. Não cobrar idades numéricas dos depósitos brasileiros nem números de recurso/reserva.
17. **Arquitetura do pórfiro:** sobretudo vertical (sódico-cálcica → potássica → clorita-sericita → sericítica → argílica avançada), com a propilítica distal e profunda. Os halos concêntricos em planta de Lowell & Guilbert (1970) são o modelo **histórico** (coerente com o Módulo 22).
