# Flashcards — Módulo 06: Elementos de geomecânica

**Módulo:** [[06-elementos-de-geomecanica-modulo|Módulo 06 — Elementos de geomecânica]]
**Total:** 56 cards — 38 Basic (frente/verso) + 18 Cloze (lacuna)
**Arquivos para importação no Anki:** `06-elementos-de-geomecanica-flashcards-basic.csv` · `06-elementos-de-geomecanica-flashcards-cloze.csv`

## Basic (frente → verso)

| # | Frente | Verso |
|---|---|---|
| 01 | O que mede o coeficiente de uniformidade Cu, e como se calcula? | A amplitude de tamanhos de grão de um solo — Cu = D60/D10. Cu alto indica solo bem graduado, Cu próximo de 1 indica solo uniforme (mal graduado). |
| 02 | Como se calcula o coeficiente de curvatura Cc de uma curva granulométrica? | Cc = (D30)² / (D10 · D60) — usado com Cu para verificar se a curva é contínua, sem faixa de tamanhos ausente. |
| 03 | Qual é a equação da linha A da carta de plasticidade de Casagrande, e o que ela separa? | IP = 0,73(LL − 20). Acima dela ficam as argilas (C), abaixo os siltes e solos orgânicos (M, O). |
| 04 | No SUCS, qual critério separa solo de granulação grossa de solo de granulação fina? | A peneira nº 200 (0,075 mm) — mais de 50% da massa retida indica solo grosso, mais de 50% passando indica solo fino. |
| 05 | No SUCS, o que distingue os sufixos L e H em solos finos? | O limite de liquidez — LL abaixo de 50% recebe L (baixa compressibilidade), LL acima de 50% recebe H (alta compressibilidade). |
| 06 | Por que existem dois sistemas de classificação, SUCS e AASHTO? | Nasceram para propósitos diferentes a partir dos mesmos dois ensaios — o SUCS para engenharia geotécnica geral, o AASHTO para pavimentação rodoviária. |
| 07 | Qual a diferença de base entre índice de vazios e porosidade? | O índice de vazios usa o volume de sólidos como base (e = Vv/Vs), a porosidade usa o volume total (n = Vv/V). Convertem-se por n = e/(1+e). |
| 08 | Por que a mecânica dos solos prefere o índice de vazios à porosidade? | Porque durante a compressão é o volume de sólidos que permanece constante, tornando e a base de referência estável para acompanhar a variação de volume. |
| 09 | Como se define o teor de umidade de um solo, e por que ele pode passar de 100%? | w = Mw/Ms, com base na massa **seca**, não na total. Passa de 100% quando há mais massa de água que de sólidos, como em argilas moles e turfas. |
| 10 | Qual a relação entre peso específico natural e peso específico seco? | γd = γ/(1+w) — divide-se pelo fator (1+w) para remover a água da base de peso, mantendo o mesmo volume total de referência. |
| 11 | Qual a diferença entre Gs e Dr? | Gs é a densidade relativa dos **grãos**, uma propriedade mineralógica (tipicamente 2,65–2,70). Dr é a densidade relativa (compacidade), um **estado** de empacotamento de solo granular, Dr = (emáx−e)/(emáx−emín). |
| 12 | Por que a curva de compactação de Proctor tem forma de sino? | Dois efeitos competem — até a umidade ótima a água lubrifica o rearranjo dos grãos e a densificação aumenta, e além dela o excesso de água ocupa espaço que seria de sólidos, reduzindo γd. |
| 13 | Comparado ao Proctor normal, o que o Proctor modificado produz? | Maior energia de compactação, deslocando a curva para densidade seca máxima **maior** e umidade ótima **menor**. As duas curvas não são comparáveis sem qualificar a energia. |
| 14 | Enuncie o princípio das tensões efetivas de Terzaghi, nas suas duas partes. | Primeira: σ' = σ − u. Segunda: todo efeito mensurável (resistência, compressão, distorção) decorre exclusivamente de mudanças na tensão efetiva, nunca da total isolada. |
| 15 | Por que a poropressão é chamada de tensão "neutra"? | Porque é isotrópica — atua igualmente em todas as direções e não transmite cisalhamento, sendo portanto neutra quanto à resistência ao cisalhamento. |
| 16 | Como a poropressão reduz a resistência sem remover peso do sistema? | Ela não altera a tensão total, muda a divisão do trabalho — a água pressurizada suporta uma fatia maior da carga e sobra menos para ser transmitida grão a grão, e só o contato grão a grão gera atrito. |
| 17 | Quando é válido calcular a tensão efetiva acumulando o peso específico submerso? | Apenas na condição hidrostática, **sem fluxo**. Havendo fluxo, u deixa de ser γw·zw e é obrigatório voltar à definição σ' = σ − u com a carga hidráulica real. |
| 18 | O que é a coesão aparente das areias úmidas, e por que "aparente"? | Ganho de resistência causado pela poropressão **negativa** (sucção capilar), que aumenta σ'. É aparente porque nenhuma cimentação foi criada — some ao secar ou ao saturar. |
| 19 | O que relaciona o coeficiente K0, e qual o erro mais comum ao aplicá-lo? | Relaciona tensões **efetivas**, K0 = σ'h/σ'v. O erro comum é aplicá-lo à tensão total — o correto é σ'h = K0·σ'v e depois σh = σ'h + u. |
| 20 | Como se estima K0 para um solo normalmente adensado? | Pela correlação de Jáky, K0 ≈ 1 − sen φ' (forma simplificada da expressão original do autor). Para φ' = 30°, K0 ≈ 0,5. |
| 21 | Por que solos sobreadensados podem ter K0 maior que 1? | Porque a descarga não devolve a tensão horizontal na mesma proporção em que devolve a vertical, e parte do empuxo horizontal fica retida no depósito. Corrige-se por K0,SA ≈ K0,NA·(OCR)^sen φ'. |
| 22 | Qual o gradiente hidráulico crítico e o que ocorre quando ele é atingido? | icr = γsub/γw = (Gs−1)/(1+e), próximo de 1 para valores típicos. Nele a tensão efetiva zera e o solo perde toda a resistência friccional — areia movediça ou levantamento de fundo. |
| 23 | Que dois resultados uma rede de fluxo fornece diretamente? | A vazão, Q = k·H·(Nf/Nd), e a poropressão em qualquer ponto, obtida contando as quedas de potencial até ele. |
| 24 | Em geotecnia, por que a percolação importa mais pela poropressão que pela vazão? | Porque é u que define σ' e, portanto, a estabilidade. A vazão é um problema de bombeamento, o gradiente é um problema de ruptura. |
| 25 | Como se calculam as condutividades equivalentes horizontal e vertical de um pacote estratificado? | Horizontal por média **aritmética** ponderada (dominada pela camada mais permeável), vertical por média **harmônica** (dominada pela menos permeável). |
| 26 | Qual a diferença entre heave e piping? | Heave é o levantamento em bloco quando σ' zera numa área ampla, governado por icr. Piping é erosão regressiva localizada, que inicia num ponto de saída e avança para montante, podendo começar bem abaixo de icr. |
| 27 | Qual é a defesa efetiva contra erosão regressiva (piping)? | Filtros graduados de proteção, que deixam a água sair retendo as partículas — controlar a saída, não apenas reduzir o fluxo. |
| 28 | Que ensaio de permeabilidade se usa para solos granulares, e qual para solos finos? | Permeâmetro de carga constante (ASTM D2434) para granulares, e de carga variável (ASTM D5084 e correlatos) para siltes e argilas, onde a vazão é pequena demais para o primeiro. |
| 29 | O que é uma unidade Lugeon? | A absorção de 1 litro por metro de furo por minuto sob pressão de 1 MPa, medida em trecho isolado por obturadores. Corresponde a condutividade da ordem de 10⁻⁷ m/s. |
| 30 | Por que a condutividade de campo costuma exceder a de laboratório em rocha? | Porque o fluxo do maciço é dominado pelas descontinuidades e segue a lei cúbica — uma única fratura aberta pode conduzir mais água que toda a matriz, que é o que o corpo de prova mede. |
| 31 | Por que argilas recalcam por anos e areias recalcam durante a construção? | Mesmo mecanismo, escalas de tempo diferentes — a velocidade do adensamento é controlada pela condutividade hidráulica, que difere em várias ordens de grandeza entre os dois materiais. |
| 32 | O que é a tensão de pré-adensamento, e o que ela separa na curva e–log σ'? | A maior tensão efetiva que o solo já suportou. Separa o trecho de recompressão (inclinação Cr, pouca deformação) da reta virgem (inclinação Cc, muita deformação). |
| 33 | Como se define o OCR, e o que distingue solo normalmente adensado de sobreadensado? | OCR = σ'p/σ'v0. OCR = 1 indica normalmente adensado (nunca suportou mais que hoje), OCR maior que 1 indica sobreadensado, por erosão, dessecação ou rebaixamento antigo do lençol. |
| 34 | Como se calcula o recalque primário quando a carga final cruza a tensão de pré-adensamento? | Em duas parcelas — ρ = (Cr·H/(1+e0))·log(σ'p/σ'v0) + (Cc·H/(1+e0))·log(σ'vf/σ'p), com logaritmo decimal. |
| 35 | O que é Hd na teoria do adensamento, e por que sua identificação é crítica? | É a maior distância que a água percorre até uma face drenante — H/2 com drenagem dupla, H com drenagem simples. Entra ao **quadrado** no fator tempo, de modo que confundir os dois casos altera o prazo por um fator 4. |
| 36 | Por que o módulo de deformabilidade de um maciço é menor que o da rocha intacta? | Porque as descontinuidades fecham e deslizam sob carga. Estima-se Em por RMR (Bieniawski 1978, Serafim & Pereira 1983) ou por GSI (Hoek & Diederichs 2006). |
| 37 | Quando a análise usa c' e φ', e quando usa su? | c' e φ' na condição **drenada** (excesso de poropressão dissipado, σ' conhecida). su na condição **não drenada** (Δu desconhecido, envoltória horizontal em tensões totais com φu = 0). |
| 38 | Por que o momento crítico é o curto prazo num aterro e o longo prazo num corte? | No aterro (carregamento) a poropressão positiva é máxima no fim da construção e depois dissipa, aumentando σ'. No corte (descarregamento) as poropressões negativas dão estabilidade temporária e se equilibram com o tempo, reduzindo σ'. |

## Cloze (lacuna)

| # | Texto com lacuna |
|---|---|
| 39 | O coeficiente de uniformidade é Cu = {{c1::D60/D10}} e o coeficiente de curvatura é Cc = {{c2::(D30)²/(D10·D60)}}. |
| 40 | A linha A da carta de plasticidade de Casagrande é dada por IP = {{c1::0,73(LL−20)}}. |
| 41 | No SUCS, a peneira que separa solos de granulação grossa dos de granulação fina é a nº {{c1::200}}, de abertura {{c2::0,075}} mm. |
| 42 | O índice de vazios e a porosidade convertem-se por n = {{c1::e/(1+e)}} e e = {{c2::n/(1−n)}}. |
| 43 | O teor de umidade w = Mw/Ms usa como base a massa {{c1::seca}}, e não a massa total. |
| 44 | A curva de compactação é limitada pela curva teórica de saturação γd,zav = {{c1::Gs·γw/(1+w·Gs)}}. |
| 45 | O princípio das tensões efetivas de Terzaghi estabelece que σ' = {{c1::σ − u}}. |
| 46 | Na franja capilar a poropressão é {{c1::negativa}}, o que {{c2::aumenta}} a tensão efetiva. |
| 47 | O coeficiente de empuxo em repouso é estimado, para solos normalmente adensados, por K0 ≈ {{c1::1 − sen φ'}}, correlação atribuída a {{c2::Jáky}}. |
| 48 | O gradiente hidráulico crítico é icr = γsub/γw = {{c1::(Gs−1)/(1+e)}}, próximo de {{c2::1}} para valores típicos. |
| 49 | A vazão obtida de uma rede de fluxo é Q = {{c1::k·H·(Nf/Nd)}}. |
| 50 | Num pacote estratificado, a condutividade equivalente horizontal é uma média {{c1::aritmética}} ponderada e a vertical é uma média {{c2::harmônica}}. |
| 51 | A força de percolação por unidade de volume é j = {{c1::i·γw}}, atuando na direção do fluxo. |
| 52 | Uma unidade Lugeon corresponde à absorção de 1 litro por metro de furo por minuto sob pressão de {{c1::1 MPa}}. |
| 53 | Na curva e–log σ', o trecho de recompressão tem inclinação {{c1::Cr}} e a reta virgem tem inclinação {{c2::Cc}}, separados pela tensão de {{c3::pré-adensamento}}. |
| 54 | O fator tempo do adensamento é Tv = {{c1::cv·t/Hd²}}, e para U = 90% vale Tv = {{c2::0,848}}. |
| 55 | Em tensões principais, o critério de Mohr-Coulomb escreve-se σ'1 = σ'3·Nφ + 2c'·√Nφ, com Nφ = {{c1::tan²(45°+φ'/2)}}. |
| 56 | A resistência que governa uma superfície de ruptura preexistente em argila é a resistência {{c1::residual}}, e não a de pico. |

## Registro
- 38 cards Basic + 18 cards Cloze = **56 cards**
- last_id: 56
- Cobertura: todos os quatro objetivos de aprendizagem do módulo (oa01–oa04) representados. Distribuição por objetivo: oa01 (cards 01–06, 39–41), oa02 (07–30, 42–52), oa03 (31–36, 53–54), oa04 (37–38, 55–56).
