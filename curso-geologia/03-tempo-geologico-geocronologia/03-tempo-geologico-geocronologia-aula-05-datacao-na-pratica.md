# Aula 05: Datação radiométrica na prática — o que se data e o que dá errado

**ID:** geologia-m03-a05
**Módulo:** [[03-tempo-geologico-geocronologia-modulo|Módulo 03 — Tempo geológico e geocronologia]]
**Duração estimada:** ~30 min
**Nível:** iniciante (contrato `iniciante-absoluto-v1`)
**Objetivo:** saber o que pode e o que não pode ser datado, escolher o método adequado e reconhecer as armadilhas que produzem idades erradas.

## Antes de começar, você precisa saber

- O que é **meia-vida**, **razão pai/filho** e **sistema fechado** — [[03-tempo-geologico-geocronologia-aula-04-meia-vida|aula 04]].
- Que uma idade data o **fechamento do relógio**, não necessariamente a formação — mesma aula.
- Como montar a **ordem relativa** dos eventos de uma seção — [[03-tempo-geologico-geocronologia-aula-01-datacao-relativa|aula 01]]. É com ela que se confere o resultado do laboratório.
- Os **três tipos de rocha** pela origem — [[00-partida-do-zero-aula-02-tres-tipos-de-rocha|módulo 00, aula 02]].

## Vocabulário desta aula

| Palavra | O que quer dizer |
|---|---|
| **Zircão** | Mineral pequeno e resistentíssimo, o preferido para datar rochas antigas. |
| **Temperatura de fechamento** | Temperatura abaixo da qual um mineral passa a reter o isótopo-filho. |
| **Rezeramento** | Perda do filho acumulado por aquecimento, que faz o relógio recomeçar do zero. |
| **Grão herdado** | Cristal mais antigo que a rocha que o contém, incorporado durante a formação dela. |
| **Balizamento** | Cercar a idade de uma camada entre um limite superior e um inferior. |
| **Camada de cinza** | Nível de cinza vulcânica depositado numa sequência sedimentar; datável. |
| **Meteorito** | Fragmento de rocha vindo do espaço, sobrevivente da formação do Sistema Solar. |

## Conteúdo

### A regra que quase ninguém espera: rocha sedimentar não se data

Comece pelo caso mais importante e mais contraintuitivo.

Suponha que você queira datar um arenito. Você o manda ao laboratório, e o resultado volta: 1,8 bilhão de anos.

**Esse número quase certamente não é a idade do arenito.**

A razão é o próprio significado da aula 04: a datação mede quando o relógio **fechou** dentro de um cristal. E os grãos de um arenito são cristais que se formaram numa **outra rocha**, muito antes — foram arrancados dela, transportados por rios, e só depois depositados ali.

O relógio de cada grão fechou lá atrás, na rocha-mãe. Datar o arenito é datar **a rocha de onde vieram os grãos**, não o momento em que eles se acumularam na praia.

> [!warning] Consequência prática enorme **A datação radiométrica direta funciona bem em rochas ígneas e metamórficas — e mal, ou não funciona, em sedimentares.** E são justamente as sedimentares que guardam os fósseis e a história da vida. O registro que mais queremos datar é o que menos se deixa datar diretamente.

O que se faz então?

**Balizamento.** Em vez de datar a camada, datam-se as rochas ígneas que se relacionam com ela, e usa-se a datação **relativa** da aula 01 para cercar o resultado:

- Um dique que **corta** a camada dá uma **idade mínima**: a camada é mais velha que ele.
- Um derrame de lava **sob** a camada dá uma **idade máxima**: a camada é mais nova que ele.
- Uma **camada de cinza vulcânica** dentro da sequência é o caso ideal: a cinza caiu do céu e se depositou junto com o sedimento, então datá-la data **a própria camada**.

Repare no que aconteceu: **a datação absoluta não substituiu a relativa. Ela depende dela.** Sem a ordem de campo, os números do laboratório não se encaixam em lugar nenhum. As duas trabalham juntas, e é essa combinação que produz a escala de tempo geológico da aula 06.

### Os relógios usuais, e para que cada um serve

| Sistema | Meia-vida | O que se data com ele | Cuidado principal |
|---|---|---|---|
| **U–Pb** (em zircão) | ~700 Ma e ~4,5 Ga | rochas ígneas antigas; o padrão-ouro | grãos herdados |
| **K–Ar** e **Ar–Ar** | ~1,25 Ga | rochas vulcânicas, micas | argônio é gás: escapa fácil |
| **Rb–Sr** | ~49 Ga | rochas ígneas e metamórficas antigas | rezeramento por metamorfismo |
| **C-14** | ~5,7 mil anos | matéria orgânica recente; arqueologia | **não serve para rochas** |

**O zircão merece destaque**, porque é a estrela da geocronologia. É um mineral minúsculo, comum em rochas ígneas, e tem três virtudes raras reunidas:

1. Quando cristaliza, **aceita urânio** na sua estrutura e **rejeita chumbo**. Ou seja, nasce com o relógio praticamente zerado: quase todo o chumbo que houver dentro dele foi produzido ali mesmo, por decaimento.
2. É **extraordinariamente duro e quimicamente resistente**. Sobrevive a erosão, transporte, soterramento e até a episódios de metamorfismo.
3. Tem **temperatura de fechamento alta** — segura o chumbo mesmo bastante quente.

Os cristais mais antigos já encontrados na Terra são zircões, e é por essa resistência que eles sobreviveram enquanto as rochas que os continham foram destruídas.

### As quatro coisas que dão errado

Uma idade radiométrica pode estar errada, e um bom geólogo sabe **de que jeito** ela costuma errar.

**1. Perda de filho — a rocha parece mais jovem.** Se o isótopo-filho vazou, a razão pai/filho parece menos avançada do que é, e a idade sai baixa. O caso clássico é o **argônio**: ele é um **gás nobre**, não se liga a nada e escapa com facilidade quando o mineral é aquecido. Um metamorfismo posterior pode expulsar quase todo o argônio acumulado — e aí o relógio K–Ar **rezera**. A idade obtida passa a ser a do metamorfismo, não a da formação.

**Nem sempre isso é um defeito.** Se você quer justamente datar o metamorfismo, essa é a informação desejada. O que é erro é **não saber qual dos dois você mediu.**

**2. Filho em excesso — a rocha parece mais velha.** Se o mineral já continha algum filho ao se formar, ou se filho entrou depois vindo de fora, a contagem infla e a idade sai alta. A correção rigorosa desse problema exige o método da **isócrona**, que dispensa supor a quantidade inicial de filho. Ele envolve gráficos e álgebra, e está deferido ao **módulo 09**.

**3. Grão herdado — data-se a rocha errada.** Um magma pode engolir zircões da rocha encaixante e carregá-los para dentro da rocha nova. Aquele grão é mais velho que a rocha em que está. Datá-lo dá a idade da rocha-avó. Solução prática: datar **muitos** grãos. Um conjunto coerente de idades iguais indica a rocha; grãos isolados e muito mais velhos denunciam herança — e, de quebra, informam sobre o que havia antes ali.

**4. Alteração e contaminação.** Rocha intemperizada troca elementos com a água que a percorre. Amostra alterada produz idade sem significado. Por isso se coleta material fresco e se separam minerais individuais, em vez de moer a rocha inteira.

> [!tip] Como o geólogo se protege **Concordância.** Datam-se vários minerais da mesma rocha, e de preferência por mais de um sistema isotópico. Se U–Pb e Ar–Ar dão o mesmo número, a chance de as duas contas terem errado do mesmo jeito é remota. E o resultado sempre é conferido contra a **ordem de campo** da aula 01: uma idade que contraria a superposição está errada, ou está datando outra coisa.

### Como se datou a Terra

Fecha bem o assunto, porque reúne tudo.

Nos anos 1950, ninguém tinha conseguido datar a Terra. E o motivo era o problema desta aula levado ao extremo: **não existe rocha terrestre da época da formação do planeta.** A tectônica de placas do módulo 02 reciclou tudo. Datar qualquer rocha terrestre dá a idade de um evento posterior — nunca do começo.

Clair Patterson contornou isso mudando de objeto. Se a Terra se formou junto com o resto do Sistema Solar, a partir do mesmo material e ao mesmo tempo, então **corpos que não foram reprocessados** guardam a idade original. Meteoritos são esses corpos.

Datando meteoritos por urânio–chumbo, Patterson chegou, em **1956**, a cerca de **4,55 bilhões de anos** — e o valor sobreviveu a setenta anos de refinamento, hoje em torno de **4,54 Ga**.

Note o raciocínio, que é o mais bonito da geocronologia: **para descobrir a idade da Terra, foi preciso parar de datar a Terra.**

> [!note] Uma questão que segue aberta Qual é a **rocha mais antiga** preservada na Terra é assunto ainda discutido — candidatos diferentes dependem de qual método e qual critério se aceitam. Este curso registra a disputa como aberta (regra LC-08) e a retoma no módulo 25.

## Exemplo trabalhado

**Situação:** uma sequência sedimentar com fósseis. Do topo para a base: folhelho, uma **camada de cinza vulcânica**, calcário. Um **dique** corta o folhelho e o calcário, mas não o solo atual. Datações: cinza = **310 Ma**; dique = **180 Ma**; grãos de zircão retirados do calcário = idades espalhadas entre **900 Ma e 2,1 Ga**.

**Interprete cada número.**

**A cinza: 310 Ma.** É o número mais valioso da seção. Cinza vulcânica cai do céu e se deposita junto com o sedimento — o relógio dela fechou no momento da deposição. Isso data **a própria sequência**: aquele ponto da coluna tem 310 Ma.

**O dique: 180 Ma.** O dique corta as camadas, então é mais novo que todas elas (relação de corte, aula 01). Coerente: 180 < 310. Ele data um evento posterior, não a sequência.
**Verificação:** se o dique tivesse dado 400 Ma, haveria contradição direta com a ordem de campo — e a ordem de campo ganharia. O número estaria errado, ou o dique carregaria material herdado.

**Os zircões do calcário: 900 Ma a 2,1 Ga.** Aqui está a armadilha. São idades **muito maiores** que a da cinça logo acima, e estão **espalhadas** em vez de agrupadas. Leitura correta: esses grãos são **detríticos** — vieram de rochas antigas erodidas em algum lugar e foram transportados até ali. Cada um data a **rocha-mãe** dele, não o calcário.
**Erro a evitar:** concluir "o calcário tem 2,1 Ga". Ele é mais **jovem** que 310 Ma por posição, e mais **velho** que o dique de 180 Ma.

**E o que os zircões detríticos valem, então?** Bastante, só que outra coisa: eles dizem que a área-fonte do sedimento continha rochas de 900 Ma a 2,1 Ga. E o grão **mais novo** de todos impõe um limite: a camada não pode ser mais velha que ele. Isso é procedência sedimentar — módulo 14.

**A lição:** o mesmo laboratório, a mesma técnica e três números, cada um datando um evento diferente. **O número não interpreta a si mesmo.** Quem interpreta é a geologia de campo.

## Erros comuns

- **Achar que se data uma rocha sedimentar mandando-a ao laboratório.** Data-se a fonte dos grãos.
- **Achar que a datação absoluta tornou a relativa obsoleta.** Ela **depende** da relativa para ter sentido.
- **Usar carbono-14 para rochas.** Ordem de grandeza incompatível.
- **Achar que uma idade discordante é sempre erro de laboratório.** Muitas vezes é uma idade **certa de outro evento**.
- **Achar que argônio escapando é falha do método.** É propriedade do material — argônio é gás nobre. O método é bom; a interpretação é que precisa saber disso.
- **Datar um grão só e concluir.** Datam-se muitos, e exige-se concordância.
- **Esquecer de perguntar "que evento zerou este relógio?"**

## O que não concluir

- **Que idades radiométricas são pouco confiáveis.** Quando o material é adequado e há concordância entre sistemas, estão entre as medidas mais robustas das ciências naturais. As armadilhas são conhecidas, nomeadas e contornáveis.
- **Que toda camada sedimentar pode ser balizada com precisão.** Muitas sequências não têm cinza nem intrusão útil, e a idade fica larga.
- **Que a idade da Terra é um número fechado sem incerteza.** ~4,54 Ga vem com margem, e depende de premissas sobre a formação do Sistema Solar (módulo 24).
- **Que a rocha mais antiga da Terra está definida.** Segue **em disputa** na literatura; retomada no módulo 25.
- **Que zircão resolve tudo.** Ele não ocorre em toda rocha — é raro em rochas pobres em sílica, como os basaltos.

## Recap relâmpago

- **Rocha sedimentar não se data diretamente:** os grãos são mais velhos que a rocha.
- Solução: **balizar** com diques, derrames e, idealmente, **camadas de cinza vulcânica** — estas datam a própria camada.
- **A datação absoluta depende da relativa.** As duas se conferem mutuamente.
- **Zircão** é o padrão-ouro: aceita urânio, rejeita chumbo, resiste a tudo, fecha a alta temperatura.
- **Quatro armadilhas:** perda de filho (parece mais jovem — argônio!), filho em excesso (parece mais velho), **grão herdado**, e alteração/contaminação.
- Rezeramento por metamorfismo não é defeito: **é a idade de outro evento**.
- Proteção: **muitos grãos, mais de um sistema, e concordância com o campo**.
- **Patterson, 1956:** datou a Terra em ~4,55 Ga **datando meteoritos**, porque não há rocha terrestre da origem. Valor atual ~**4,54 Ga**.
- Qual é a rocha mais antiga da Terra segue **em aberto**.

## Próxima aula

[[03-tempo-geologico-geocronologia-aula-06-escala-do-tempo-e-gssp|Aula 06 — A escala do tempo geológico e o que é um GSSP]]

## Anterior

[[03-tempo-geologico-geocronologia-aula-04-meia-vida|Aula 04 — Meia-vida: o relógio que não se pode adiantar]]

## Fontes

- C. Patterson, "Age of meteorites and the Earth", 1956.
- Prática padrão de geocronologia U–Pb em zircão; conceito de temperatura de fechamento.
- Achado M01-F02 (rocha mais antiga da Terra): retomado aqui como questão aberta, conforme registrado em `_contexto.md`.

<!--
nivel: iniciante-absoluto-v1
palavras_corpo: ~1600

mapa_objetivo_secao:
  OA-05: "A regra que quase ninguém espera" + "Os relógios usuais" + "As quatro coisas que dão errado" + "Como se datou a Terra" + "Exemplo trabalhado"

alegacoes_auditaveis:
  - claim_id: GEO-M03-A05-SEDIMENTAR-001
    claim: "Rochas sedimentares clásticas não podem ser datadas diretamente por métodos radiométricos, porque os grãos registram a idade da rocha-fonte."
    risk: interpretacao
    source: "princípio geocronológico consolidado"
  - claim_id: GEO-M03-A05-CINZA-002
    claim: "Camadas de cinza vulcânica intercaladas em sequências sedimentares permitem datar a própria deposição."
    risk: interpretacao
    source: "prática padrão de cronoestratigrafia; base da calibração da escala ICS"
  - claim_id: GEO-M03-A05-ZIRCAO-003
    claim: "O zircão incorpora urânio e exclui chumbo ao cristalizar, é quimicamente resistente e tem temperatura de fechamento alta, o que o torna o mineral de referência para U-Pb."
    risk: fato
    source: "mineralogia e geocronologia U-Pb consolidadas"
  - claim_id: GEO-M03-A05-ARGONIO-004
    claim: "O argônio é um gás nobre e escapa com facilidade sob aquecimento, o que pode rezerar o relógio K-Ar e fazer a rocha parecer mais jovem."
    risk: interpretacao
    source: "geocronologia K-Ar/Ar-Ar; comportamento consolidado"
  - claim_id: GEO-M03-A05-HERANCA-005
    claim: "Zircões herdados da rocha encaixante podem produzir idades mais antigas que a da rocha hospedeira, detectáveis pela dispersão entre muitos grãos."
    risk: interpretacao
    source: "prática de datação de populações de zircão"
  - claim_id: GEO-M03-A05-PATTERSON-1956-006
    claim: "Clair Patterson determinou em 1956 a idade da Terra em cerca de 4,55 bilhões de anos, datando meteoritos por urânio-chumbo, porque não existe rocha terrestre preservada da formação do planeta."
    risk: data
    source: "Patterson 1956. Conteúdo deferido do M01 para o M03, conforme deferred_content. A matemática da isócrona permanece deferida ao M09"
  - claim_id: GEO-M03-A05-IDADE-TERRA-ATUAL-007
    claim: "O valor atualmente aceito para a idade da Terra é de cerca de 4,54 bilhões de anos, com incerteza associada."
    risk: numero
    source: "valor consolidado; ordem de grandeza conforme LC-05"
  - claim_id: GEO-M03-A05-ROCHA-MAIS-ANTIGA-008
    claim: "Qual é a rocha mais antiga preservada na Terra permanece em disputa na literatura."
    risk: controverso
    source: "achado M01-F02 (Acasta vs. Nuvvuagittuq); declarado como questão aberta conforme LC-08; retomar no M25"
  - claim_id: GEO-M03-A05-CONCORDANCIA-009
    claim: "A confiabilidade de uma idade radiométrica apoia-se na concordância entre múltiplos grãos, múltiplos sistemas isotópicos e a ordem estabelecida por datação relativa."
    risk: interpretacao
    source: "prática geocronológica padrão"

nota_repartida: >-
  Aula nova da repartida de 2026-08-16. Corresponde ao terço final da antiga aula 02
  (decaimento-radioativo-e-datacao-radiometrica). Recebe o conteúdo deferido do M01
  sobre a datação da Terra por Patterson, em versão narrativa: a matemática da
  isócrona segue deferida ao M09. Retoma o achado M01-F02 como questão aberta,
  conforme previsto em `_contexto.md`.
-->
