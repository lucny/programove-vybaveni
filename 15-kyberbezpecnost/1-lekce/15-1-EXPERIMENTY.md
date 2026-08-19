<!--
author: Marek Lučný
title: Kyberprostor, hrozby a řízení bezpečnosti – praktická laboratoř
language: cs
mode: Textbook
comment: Šest bezpečně vedených experimentů k první lekci okruhu Kyberbezpečnost.
-->

# Praktická laboratoř: Kyberprostor, hrozby a řízení bezpečnosti

V této laboratoři si ověříte, že kybernetická bezpečnost nezačíná nákupem programu, ale porozuměním tomu, **co chráníme, před čím to chráníme a jak poznáme přiměřené opatření**. Šest experimentů propojuje aktiva, hrozby, zranitelnosti, rizika a CIA triádu s konkrétními situacemi.

> **🛡️ Bezpečnostní pravidlo laboratoře**
>
> Pracujte pouze s vlastními testovacími daty, fiktivními scénáři, veřejnými ukázkami nebo materiálem poskytnutým učitelem. Nevkládejte hesla, tokeny, neveřejné osobní údaje ani adresy cizích účtů. Nezkoušejte se připojovat k cizím zařízením, skenovat je nebo ověřovat jejich zranitelnosti. Narazíte-li na cizí účet, zařízení či citlivý údaj, experiment ukončete a informujte učitele.

## Jak pracovat

U každého experimentu nejprve napište krátkou **předpověď**. Během práce oddělujte pozorování od vysvětlení: údaj na obrazovce je důkaz, zatímco jeho propojení s pojmem z lekce je interpretace. Na závěr uveďte také omezení použitého nástroje nebo postupu.

```text
Předpověď:
Pozorování nebo důkaz:
Vysvětlení odborným pojmem:
Omezení výsledku:
Navržené opatření:
```

| Experiment | Hlavní pojem | Prostředí | Orientační čas |
|---|---|---|---:|
| 1.1 Modelování hrozeb | aktivum, hrozba, zranitelnost, riziko | papír nebo textový editor | 30 min |
| 1.2 Záznam zranitelnosti | CVE, CVSS, aktualizace | NVD NIST | 30 min |
| 1.3 Veřejně viditelná infrastruktura | kyberprostor, expozice, oprávnění | Shodan / učitelská ukázka | 25 min |
| 1.4 Reakce na únik dat | důvěrnost, incident, nápravná opatření | Have I Been Pwned / ukázka | 25 min |
| 1.5 Mapa zachycených hrozeb | měření, vzorek dat, interpretace | Radware Live Threat Map | 25 min |
| 1.6 Řízený výpadek připojení | dostupnost, odolnost, obnova | vlastní testovací zařízení | 30 min |

## Experiment 1.1: Od aktiva k opatření

**Cíl:** Sestavit jednoduchý model hrozeb a určit, kterému riziku je rozumné věnovat pozornost nejdříve.

**Nástroj:** Papír a psací potřeby, tabulkový procesor nebo běžný textový editor. Není potřeba žádný bezpečnostní software; modelování hrozeb je především metoda strukturovaného přemýšlení.

**Úkoly:**

1. Pro zadaný fiktivní systém určete nejméně tři důležitá aktiva.
2. Ke každému aktivu sestavte úplný řetězec `hrozba → zranitelnost → následek` a určete dotčené části CIA triády.
3. Ohodnoťte pravděpodobnost a dopad, seřaďte rizika a navrhněte preventivní i obnovovací opatření.

**Výstupy:** Vyplněná tabulka nejméně tří rizik, pořadí jejich priorit a odstavec zdůvodňující, proč má být nejvýznamnější riziko řešeno jako první.

<details>

<summary>**🧠 Rozbalit článek k tématu: Jak funguje modelování hrozeb**</summary>

**Bezpečnost nezačíná seznamem útoků**

Představte si školní fotografický kroužek. Členové mají společný cloudový prostor, notebook s rozpracovanými fotografiemi a veřejný web. Každá z těchto věcí má jinou hodnotu a jinak se chrání. Fotografie mohou být nenahraditelné, přihlašovací účet otevírá cestu k dalším datům a veřejný web musí být dostupný návštěvníkům.

To, co má hodnotu, označujeme jako **aktivum**. **Hrozba** je možná příčina škody, například krádež notebooku, chyba uživatele, malware nebo výpadek služby. **Zranitelnost** je slabé místo, které může hrozba využít: chybějící záloha, snadno uhodnutelné heslo nebo neaktualizovaný program. **Riziko** spojuje pravděpodobnost takové události se závažností jejích následků.

Jedna hrozba může ohrozit několik vlastností CIA triády. Krádež nezamčeného notebooku může porušit důvěrnost fotografií, umožnit jejich změnu a současně způsobit jejich nedostupnost. Dobré opatření proto reaguje na konkrétní cestu ke škodě, nikoli jen na obecný strach z „hackera“.

Modelování hrozeb se používá při návrhu aplikací, sítí i pracovních postupů. Tým si nakreslí, z jakých částí se systém skládá, kudy proudí data, kdo k nim přistupuje a kde se mění úroveň důvěry. Následně hledá realistické způsoby, jak by mohlo dojít ke ztrátě důvěrnosti, narušení integrity nebo omezení dostupnosti. Výsledkem není seznam všech myslitelných katastrof, ale podklad pro rozhodnutí, do kterých opatření investovat čas a peníze.

Papír nebo tabulkový procesor je pro první model vhodnější než složitý specializovaný nástroj. Student se soustředí na význam položek, vazby mezi nimi a kvalitu argumentu. V profesionálním prostředí se stejné principy rozšiřují o diagramy toku dat, katalogy typických hrozeb, vlastníky rizik a pravidelné přehodnocování. Model totiž stárne spolu se systémem: přibývají služby, mění se uživatelé a objevují se nové zranitelnosti.

Číselné skóre v této úloze slouží pouze k porovnání rizik uvnitř jednoho scénáře. Není to objektivní předpověď budoucnosti. Dva týmy mohou stejnému riziku přidělit jiné hodnoty, pokud pracují s jinými informacemi. Důležitější než samotné číslo je proto písemné zdůvodnění a možnost odhad později opravit.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup**</summary>

**Postup**

1. Zvolte **fiktivní scénář**: fotografický kroužek, školní knihovna, malý e-shop nebo studentský projekt. Nepopisujte skutečné neveřejné zabezpečení školy.
2. Určete nejméně tři aktiva. Zahrňte alespoň jedno datové aktivum, jeden účet nebo službu a jednu věc související s provozem či reputací.
3. U každého aktiva napište, zda by jeho poškození zasáhlo hlavně **důvěrnost**, **integritu**, **dostupnost**, nebo více vlastností současně.
4. Doplňte jednu konkrétní hrozbu a jednu zranitelnost. Formulujte celý řetězec, například: „ztráta notebooku → disk bez ochrany → přístup k fotografiím“.
5. Ohodnoťte pravděpodobnost i dopad číslem 1 až 3. Orientační prioritu vypočítejte jako `pravděpodobnost × dopad`. Číslo není přesná vědecká hodnota; slouží k porovnání položek ve stejném modelu.
6. Navrhněte preventivní opatření a jeden krok obnovy. U ztráty zařízení může jít například o ochranu přístupu, šifrování úložiště a ověřenou zálohu.
7. Seřaďte rizika podle priority. U prvního vysvětlete, proč zvolené opatření snižuje pravděpodobnost, dopad, nebo obojí.

| Aktivum | Hrozba | Zranitelnost | CIA | Pravděpodobnost | Dopad | Opatření |
|---|---|---|---|---:|---:|---|
| fotografie projektu | ztráta zařízení | jediná kopie dat | D, I, A | 2 | 3 | pravidelná ověřená záloha |

**Ověření a odevzdání**

Zkontrolujte, že jste nezaměnili hrozbu se zranitelností. „Slabé heslo“ je zranitelnost; hrozbou může být útočník, který zkouší získat účet. Odevzdejte tabulku a krátké zdůvodnění nejvyšší priority. Připojte jednu větu o omezení: například že bodové hodnocení vychází z odhadu a při nových informacích se může změnit.

</details>

## Experiment 1.2: Jak číst záznam o zranitelnosti

**Cíl:** Naučit se vyhledat a kriticky přečíst veřejný záznam CVE bez pokusu zranitelnost zneužít.

**Nástroj:** Webová databáze [National Vulnerability Database – NVD](https://nvd.nist.gov/vuln/search), kterou provozuje americký institut NIST. NVD doplňuje záznamy CVE o údaje potřebné pro vyhledávání, porovnávání a hodnocení zranitelností.

**Úkoly:**

1. Podle názvu a verze produktu vyhledejte jeden odpovídající záznam CVE.
2. Zjistěte dotčené verze, způsob možného zneužití, dopad, CVSS a doporučení primárního zdroje.
3. Rozlište technickou závažnost zranitelnosti od skutečného rizika pro modelovou organizaci.

**Výstupy:** Jednostránková karta zranitelnosti s odkazem na CVE, přesným rozsahem dotčených verzí, interpretací CVSS, dopadem na CIA triádu a doporučenou bezpečnou reakcí.

<details>

<summary>**🧠 Rozbalit článek k tématu: CVE, NVD a CVSS**</summary>

**Zranitelnost má přesnou identitu**

Výrok „program má bezpečnostní chybu“ je příliš neurčitý. Bezpečnostní komunita používá identifikátory **CVE**, aby bylo možné stejnou zranitelnost jednoznačně popsat v databázi, oznámení výrobce i aktualizačním nástroji. Záznam obvykle uvádí popis, dotčené verze, odkazy na zdroje a hodnocení závažnosti.

Skóre **CVSS** pomáhá popsat technickou závažnost za určitých předpokladů. Není to však automaticky hodnota rizika pro konkrétní školu nebo uživatele. Kritická chyba v produktu, který vůbec nepoužíváme, pro nás nepředstavuje stejné riziko jako méně závažná chyba v důležité veřejné službě. Pro rozhodnutí potřebujeme znát také aktivum, jeho vystavení, existující ochrany a možné následky.

Systém **CVE — Common Vulnerabilities and Exposures** přiděluje veřejně známé zranitelnosti jednoznačné identifikátory, například ve tvaru `CVE-rok-číslo`. Identifikátor funguje podobně jako katalogové číslo: různí výrobci, správci i bezpečnostní nástroje díky němu vědí, že mluví o stejné chybě. Samotný záznam CVE bývá stručný a odkazuje na další zdroje, zejména na oznámení výrobce.

**NVD — National Vulnerability Database** tato data přebírá a strukturuje. Umožňuje hledat podle produktu, verze, data, závažnosti a dalších vlastností. U záznamu lze najít popis, odkazy, konfigurace dotčených produktů a metriky CVSS. Databáze se používá při inventarizaci zranitelností, rozhodování o aktualizacích, správě rizik a automatizovaném porovnávání používaného softwaru s katalogem známých chyb.

**CVSS — Common Vulnerability Scoring System** popisuje technické vlastnosti zranitelnosti. Sleduje například, zda je dosažitelná po síti, zda vyžaduje oprávnění nebo zásah uživatele a jaký může mít dopad na důvěrnost, integritu a dostupnost. Základní skóre je užitečné pro třídění, ale nezná místní kontext. Neví, zda je služba veřejná, zda existují další ochranné vrstvy ani jak cenná data zpracovává.

Při práci s NVD je proto nutné ověřit přesnou verzi produktu a číst primární zdroj. Shoda názvu nestačí a starší záznam může být doplněn nebo přehodnocen. Analýza záznamu slouží k bezpečnému rozhodnutí o opravě; není návodem k útoku.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup v NVD**</summary>

**Postup**

1. Použijte název a verzi programu zadanou učitelem. Případně zjistěte verzi běžného programu na vlastním zařízení v nabídce „O aplikaci“. Nezveřejňujte celý inventář školních zařízení.
2. Otevřete vyhledávání NVD a zadejte název produktu spolu s verzí. Pokud je výsledků příliš mnoho, vyberte záznam určený učitelem.
3. Zapište identifikátor CVE, datum zveřejnění a stručný popis **vlastními slovy**.
4. Najděte údaj o dotčených verzích. Ověřte, zda záznam skutečně odpovídá zvolené verzi; shoda názvu produktu sama nestačí.
5. Poznamenejte uvedené skóre a slovní stupeň závažnosti. Vypište dvě podmínky útoku, které lze ze záznamu vyčíst, například zda vyžaduje síťový přístup nebo zásah uživatele.
6. Otevřete alespoň jeden odkaz na oznámení výrobce či jiný primární zdroj uvedený u záznamu. Zjistěte, zda doporučuje aktualizaci, změnu nastavení nebo jiné omezení.
7. Navrhněte bezpečnou reakci správce: ověřit skutečně používanou verzi, zálohovat důležitá data, otestovat opravu a řízeně ji nasadit.

> **Důležitá hranice:** Úloha končí analýzou veřejného záznamu. Nestahujte demonstrační exploit, neposílejte testovací požadavky cizím systémům a nezkoušejte ověřovat chybu útokem.

**Co má obsahovat karta zranitelnosti**

- identifikátor CVE a odkaz na záznam,
- dotčený produkt a rozsah verzí,
- stručný popis možného dopadu na CIA triádu,
- CVSS jako údaj o technické závažnosti,
- jeden důvod, proč se skutečné riziko může lišit,
- doporučené opatření doložené zdrojem.

**Ověření a odevzdání**

Odevzdejte kartu a odpovězte: „Proč vysoké CVSS samo o sobě nestačí k určení priority v naší organizaci?“ Kvalitní odpověď propojí technickou závažnost s hodnotou aktiva, skutečnou expozicí a možným dopadem.

</details>

## Experiment 1.3: Co prozradí veřejně viditelná infrastruktura

**Cíl:** Rozlišit fyzické zařízení, veřejnou expozici, zranitelnost a oprávnění k bezpečnostnímu testu.

**Nástroj:** Vyhledávač internetových služeb [Shodan](https://www.shodan.io/) v režimu veřejné ukázky, případně anonymizovaný snímek výsledku připravený učitelem. Shodan indexuje technické odpovědi veřejně dostupných síťových služeb; nepoužívá se zde k aktivnímu testování zařízení.

**Úkoly:**

1. V anonymizovaném záznamu rozpoznejte síťovou službu, port, čas pozorování, odhad produktu a přibližnou polohu.
2. Oddělte doložená fakta od domněnek a vysvětlete rozdíl mezi expozicí a zranitelností.
3. Navrhněte tři otázky a tři opatření, kterými by oprávněný správce omezil zbytečnou veřejnou dostupnost služby.

**Výstupy:** Anotovaný záznam bez identifikátorů cizího zařízení, tabulka `zjištění → možný význam → nejistota` a seznam obranných doporučení.

<details>

<summary>**🧠 Rozbalit článek k tématu: Shodan a internet věcí**</summary>

**Kyberprostor má fyzickou vrstvu**

Internet není nehmotný svět. Tvoří jej servery, routery, kamery, řídicí jednotky, datová centra, kabely a software, který všechny prvky propojuje. Některá zařízení při komunikaci zveřejňují technické informace označované jako **banner**: například použitý protokol, produkt nebo verzi služby. Vyhledávače internetových služeb tyto veřejně dostupné údaje indexují podobně, jako webový vyhledávač indexuje stránky.

Veřejná viditelnost však není totéž co zranitelnost. Záznam může být zastaralý, poloha jen přibližná a identifikace produktu chybná. A hlavně: to, že zařízení lze na internetu najít, nikomu nedává oprávnění se k němu přihlašovat, skenovat je nebo zkoušet hesla. Bezpečnostní test vyžaduje výslovný souhlas vlastníka a přesně vymezený rozsah.

Běžný webový vyhledávač zpracovává hlavně obsah stránek. **Shodan** se zaměřuje na služby, které odpovídají na síťových portech: webové servery, vzdálenou správu, databázové služby, průmyslová zařízení nebo prvky internetu věcí. Jeho servery v průběhu času oslovují veřejné adresy a ukládají části odpovědí. Výsledkem je index, v němž lze podle technických vlastností hledat podobně jako v katalogu.

Číslo **portu** pomáhá operačnímu systému doručit komunikaci správné službě. Port 443 se často používá pro HTTPS, ale samotné číslo nezaručuje, že na něm běží očekávaný nebo bezpečně nastavený program. **Banner** je část odpovědi služby, která může obsahovat název produktu, verzi, protokol nebo jiný identifikátor. Některé bannery jsou přesné, jiné záměrně obecné či zavádějící.

Shodan používají správci a bezpečnostní týmy k hledání vlastních nechtěně zveřejněných služeb, kontrole rozsahu organizace a výzkumu trendů internetu věcí. Stejná data však mohou být zneužita, a proto je zásadní právní i etická hranice. V této úloze se pouze interpretuje připravený záznam. Žádné spojení s nalezeným zařízením, pokus o přihlášení ani ověřování chyby není součástí experimentu.

Poloha ve výsledku bývá odvozena z databáze IP adres a může ukazovat sídlo poskytovatele místo skutečného zařízení. Čas záznamu zase říká, kdy byla služba pozorována, nikoli zda je dostupná právě nyní. Správný analytik proto u každého údaje uvádí jeho stáří, zdroj a míru jistoty.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup s ukázkou Shodanu**</summary>

**Postup**

1. Učitel poskytne snímek anonymizovaného záznamu, veřejnou demonstrační stránku nebo předem vybraný neproblematický příklad. Nevyhledávejte školu, domácí IP adresy, kamery ani konkrétní cizí organizaci.
2. V záznamu barevně označte čtyři druhy informace: síťovou službu, čas pozorování, odhadovaný produkt a přibližné umístění.
3. Ke každému údaji napište, co lze oprávněně tvrdit a co už by byla spekulace. Například banner může naznačovat produkt, ale sám nedokazuje použitelnou zranitelnost.
4. Určete možné aktivum a vysvětlete, kterou složku CIA triády by mohl incident ovlivnit. U veřejného informačního serveru bude často zásadní dostupnost a integrita obsahu.
5. Sepište tři otázky, které by měl položit oprávněný správce: „Musí být tato služba veřejná?“, „Je podporovaná a aktualizovaná?“ a „Je přístup omezen na nezbytné uživatele?“
6. Navrhněte přiměřená opatření bez zásahu do zařízení: omezení veřejné expozice, bezpečná konfigurace, aktualizace, vícefaktorové ověření, sledování událostí nebo segmentace sítě.

**Cvičení v přesné interpretaci**

Rozdělte následující výroky do dvou skupin:

- **Doloženo záznamem:** „V určitém čase odpovídala na daném portu služba s tímto bannerem.“
- **Není doloženo záznamem:** „Zařízení lze určitě napadnout“ nebo „majitel porušil zákon“.

Právě toto rozlišení je základem profesionální práce: technický údaj nejprve popíšeme a až potom, s dalšími důkazy a oprávněním, hodnotíme jeho význam.

**Ověření a odevzdání**

Odevzdejte anotovaný záznam, tři obranné otázky a jednu větu vysvětlující rozdíl mezi **expozicí** a **zranitelností**. Do práce nevkládejte úplnou IP adresu, přihlašovací údaje ani jiné identifikátory cizího zařízení.

</details>

## Experiment 1.4: Rozhodování po oznámení úniku dat

**Cíl:** Určit, co výsledek služby pro kontrolu úniků říká, co neříká a jak má vypadat přiměřená reakce.

**Nástroj:** Databáze známých úniků [Have I Been Pwned](https://haveibeenpwned.com/) v podobě veřejné demonstrační stránky nebo anonymizovaného snímku připraveného učitelem. Služba porovnává zadanou e-mailovou adresu s údaji evidovanými ve známých únicích; v tomto cvičení se nepoužívají cizí ani povinně osobní adresy.

**Úkoly:**

1. Z modelového výsledku určete postiženou službu, dobu úniku a druhy kompromitovaných údajů.
2. Rozlište, co výsledek dokládá, co z něj nelze zjistit a které další účty mohou být ohroženy znovupoužitým heslem.
3. Sestavte seřazený plán okamžité reakce a dlouhodobé prevence.

**Výstupy:** Tabulka `zjištění → možné riziko → reakce`, očíslovaný plán nejméně pěti kroků a dvě omezení interpretace výsledku.

<details>

<summary>**🧠 Rozbalit článek k tématu: Úniky dat a Have I Been Pwned**</summary>

**Únik u jedné služby může ovlivnit další účty**

Když služba utrpí únik dat, mohou se mimo její kontrolu dostat e-mailové adresy, uživatelská jména, heslové hashe nebo další osobní údaje. Narušena je především **důvěrnost**. Pokud člověk používá stejné heslo na více místech, útočníci mohou uniklé přihlašovací údaje automaticky zkoušet i u jiných služeb. Tento navazující útok se označuje jako credential stuffing.

Have I Been Pwned shromažďuje informace o známých únicích a umožňuje zjistit, zda se v nich objevila e-mailová adresa. Nalezený záznam neznamená, že je účet právě teď ovládán útočníkem. Naopak nenalezený záznam není důkazem absolutního bezpečí: služba zná jen zveřejněné a zpracované incidenty.

Projekt **Have I Been Pwned**, často zkracovaný jako HIBP, vytváří vyhledávatelný katalog veřejně známých úniků. Uživatel může zjistit, zda se určitá adresa objevila v evidovaném incidentu, a přečíst si, která služba byla zasažena a jaké typy údajů byly součástí úniku. Nástroj se používá při osobní digitální hygieně, při reakci na incident i v organizacích, které sledují ohrožení adres na vlastních doménách.

E-mailová adresa není tajné heslo, stále je však osobním a bezpečnostně významným údajem. Může propojit účty člověka napříč službami a pomoci útočníkovi vytvořit přesvědčivější phishing. Proto v učebně pracujeme s demonstračním záznamem. Pokud někdo dobrovolně kontroluje vlastní adresu, musí rozumět účelu služby a nikdy do ní nezadává své heslo.

Únik databáze ještě automaticky neznamená, že útočník získal heslo v čitelné podobě. Služby mají hesla ukládat jako odolné solené hashe, ale kvalita ochrany se liší a slabé heslo může být později uhádnuto. Uniknout mohou i telefonní čísla, adresy, data narození, bezpečnostní otázky nebo historie aktivit. Každý typ údajů vytváří jiný scénář dalšího zneužití.

Zvlášť nebezpečné je **znovupoužití hesla**. Automatizovaný credential stuffing zkouší uniklou kombinaci adresy a hesla u dalších služeb. Obrana proto nespočívá jen ve změně hesla u historicky napadeného webu. Je nutné najít všechny další účty se stejným heslem, použít unikátní přístupové údaje, zapnout MFA a zkontrolovat obnovovací adresy i aktivní relace.

HIBP je zdroj informace, nikoli důkaz úplného bezpečí. Neobsahuje každý incident, nemusí znát dosud nezveřejněný únik a neříká, kdo data použil. Výsledek je začátkem analýzy a reakce, ne jejím koncem.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup pro modelový únik**</summary>

**Postup s modelovým případem**

1. Použijte výhradně veřejnou demonstrační stránku, anonymizovaný snímek nebo fiktivní případ od učitele. Nezadávejte školní či cizí e-mail. Vlastní adresu použijte jen dobrovolně a podle pokynu učitele; heslo se do této služby nikdy nezadává.
2. Z výsledku vypište název postižené služby, přibližnou dobu incidentu a druhy kompromitovaných údajů.
3. Určete, co je doložené a co ne. Doložen může být výskyt adresy v konkrétním úniku; z výsledku obvykle nelze zjistit, kdo data použil nebo zda je současné heslo stále stejné.
4. Seřaďte reakci podle naléhavosti:
   - změnit heslo u postižené služby, pokud je účet stále aktivní,
   - změnit stejné či odvozené heslo všude, kde bylo znovu použito,
   - zapnout vícefaktorové ověření,
   - zkontrolovat historii přihlášení a obnovovací údaje,
   - počítat s cíleným phishingem využívajícím uniklé informace.
5. Ke každému kroku přiřaďte riziko, které snižuje. Unikátní heslo omezuje přenos škody mezi službami, MFA přidává další překážku a kontrola relací může odhalit cizí přístup.
6. Doplňte dlouhodobé opatření: správce hesel, upozornění na budoucí úniky a omezení množství údajů sdílených se službami.

**Modelová situace**

Fiktivní uživatel zjistil, že jeho adresa byla součástí staršího úniku e-shopu. Stejné heslo tehdy používal také u e-mailu, ale později ho v e-shopu změnil. Nejvyšší prioritu nemá další změna už nepoužívaného hesla v e-shopu, nýbrž ověření e-mailového účtu, odstranění znovupoužitého hesla a kontrola historie přihlášení. E-mail totiž často umožňuje obnovit přístup k ostatním službám.

**Ověření a odevzdání**

Odevzdejte tabulku `zjištění → možné riziko → reakce` a dvě omezení výsledku. V závěru vysvětlete rozdíl mezi zprávou „adresa byla v evidovaném úniku“ a tvrzením „útočník právě zná moje současné heslo“.

</details>

## Experiment 1.5: Jak číst živou mapu kybernetických hrozeb

**Cíl:** Pozorovat vizualizaci zachycených událostí a vyhnout se ukvapeným závěrům z atraktivní mapy.

**Nástroj:** Interaktivní webová vizualizace [Radware Live Threat Map](https://livethreatmap.radware.com/). Mapa používá anonymizované a vzorkované údaje z cloudových bezpečnostních služeb a globální sítě klamných systémů provozovatele. Rozlišuje například webové útočníky, DDoS zdroje, narušitele, skenery a anonymizační uzly.

**Úkoly:**

1. Prozkoumejte legendu a popis zdrojů dat a vlastními slovy vysvětlete dvě zobrazené kategorie aktivity.
2. Ve dvou časových intervalech zaznamenejte vybraný dynamický ukazatel a porovnejte změnu.
3. Rozdělte závěry na tvrzení, která mapa dokládá, a tvrzení, která z ní vyvodit nelze.

**Výstupy:** Časová tabulka pozorování, popis dvou kategorií událostí, seznam potřebných doplňujících dat a tři pravidla korektní interpretace vizualizace.

<details>

<summary>**🧠 Rozbalit článek k tématu: Jak fungují mapy kybernetických hrozeb**</summary>

**Mapa je vizualizace měření, nikoli úplný obraz internetu**

Pohyblivé čáry a barevné body vytvářejí dojem, že sledujeme každý probíhající útok. Ve skutečnosti mapa zobrazuje události zachycené konkrétními bezpečnostními technologiemi a podle pravidel jejich provozovatele. Záleží proto na rozmístění senzorů, počtu uživatelů produktu, klasifikaci událostí i způsobu převodu dat do obrazu.

Žebříček „nejvíce napadených zemí“ nemusí znamenat, že v dané zemi objektivně probíhá nejvyšší počet všech útoků. Může zde být více měřených zařízení nebo jiná struktura uživatelů. Animovaná čára také sama o sobě nedokazuje skutečný původ útočníka. IP adresa může patřit napadenému prostředníkovi, VPN nebo cloudové službě a určení původce útoku je samostatný analytický problém.

Živá mapa převádí proud technických záznamů do obrazu, kterému člověk rychle porozumí. Zdrojem mohou být cloudové ochranné služby, systémy detekce průniků, klamné servery nebo jiné bezpečnostní komponenty. Každá zachycená událost obsahuje čas, kategorii a určitou informaci o místě či síti. Server data agreguje a webová aplikace z nich vytváří body, čáry, počitadla a žebříčky.

Radware Live Threat Map vychází podle provozovatele z jeho cloudových systémů a z globální **deception network**. Klamný systém úmyslně napodobuje zajímavou službu, ale neobsahuje běžný provoz skutečných uživatelů. Když jej někdo skenuje nebo se k němu pokouší přistoupit, vzniká užitečný signál pro analýzu škodlivé aktivity. Data jsou před zveřejněním vzorkována a anonymizována, takže mapa ukazuje přehled, nikoli jednotlivé zákaznické incidenty.

Kategorie **Web Attackers** souvisí s podezřelou aktivitou namířenou proti webovým aplikacím. **DDoS Attackers** představují zdroje spojované s pokusy o zahlcení služby. **Intruders** označují aktivitu vyhodnocenou jako pokus o průnik, zatímco **Scanners** mapují systémy, které ve velkém hledají dostupné služby. **Anonymizers** upozorňují na infrastrukturu skrývající původ spojení; její použití samo o sobě ještě nedokazuje útok. Kategorie jsou klasifikací provozovatele, ne nezávislým soudem o úmyslu konkrétní osoby.

Taková vizualizace se používá především pro orientaci, komunikaci a sledování trendů. Dokáže názorně ukázat, že detekce probíhají nepřetržitě a ve velkém měřítku. Bezpečnostní operační centrum však pro skutečné rozhodování potřebuje mnohem podrobnější údaje: záznamy konkrétních zařízení, kontext uživatele, síťovou komunikaci, časovou osu a ověření více zdroji.

Je také nutné rozlišit **detekci, útok a incident**. Detekce znamená, že nástroj rozpoznal událost podle svých pravidel. Může jít o skutečný škodlivý soubor, zablokovaný pokus, opakovaný záznam nebo falešný poplach. Útok popisuje činnost protivníka a incident znamená skutečné či významně hrozící narušení bezpečnosti. Jedna animace na mapě sama neurčuje, do které kategorie situace patří.

Mapa je ovlivněna **výběrovým zkreslením**. Vidí hlavně prostředí, z nichž dostává telemetrii. Země s větším počtem senzorů může vykázat více detekcí, i kdyby skutečná míra hrozeb byla srovnatelná. Pro férové porovnání bychom potřebovali znát jmenovatel — například počet aktivních zařízení — a jednotnou metodiku měření.

Atraktivní vzhled je výhodou i rizikem. Pomáhá zaujmout, ale může vytvářet falešný pocit přesnosti. Úkolem analytika je proto vždy uvést čas, zdroj, definici ukazatele a hranici toho, co vizualizace skutečně dokládá.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup s živou mapou**</summary>

**Postup**

1. Před otevřením mapy napište předpověď: který typ údaje podle vás mapa skutečně měří a co z ní naopak nebude možné určit.
2. Otevřete Radware Live Threat Map. Zapište čas pozorování a zvolený statistický interval, například jednu hodinu; bez tohoto kontextu nelze dvě pozorování korektně porovnat.
3. V legendě najděte kategorie `Web Attackers`, `DDoS Attackers`, `Intruders`, `Scanners` a `Anonymizers`. Vyberte dvě a jejich význam vysvětlete vlastními slovy. Neodvozujte význam pouze z barvy nebo názvu.
4. Zvolte jednu kategorii a po dobu dvou minut každých třicet sekund zapište jeden dostupný dynamický ukazatel, například počet či pořadí zobrazené země. Nejde o soutěž, ale o sledování proměnlivosti.
5. Po pěti minutách pozorování zopakujte se stejnou kategorií a statistickým intervalem. Porovnejte záznamy a popište přesně, co se změnilo.
6. Vytvořte dva sloupce: „Mapa dokládá“ a „Mapa nedokládá“. Do prvního může patřit počet událostí zobrazených daným systémem v daném čase. Do druhého patří totožnost útočníka, úplný počet světových útoků nebo příčina rozdílu mezi zeměmi.
7. Navrhněte, jaká další data by byla potřeba pro spolehlivější srovnání: počet aktivních senzorů, velikost připojené populace, časové období a jednotná definice události.

**Ověření a odevzdání**

Odevzdejte malou tabulku pozorování a tři interpretační pravidla. Jedno pravidlo musí upozornit na **výběrové zkreslení**, druhé na rozdíl mezi detekcí a potvrzeným incidentem a třetí na obtížnost určování původce. Snímek mapy doplňte časem pořízení; bez něj je dynamický údaj obtížně ověřitelný.

</details>

## Experiment 1.6: Řízená simulace nedostupnosti

**Cíl:** Poznat závislost běžné práce na síti a navrhnout opatření pro zachování nebo rychlou obnovu dostupnosti.

**Nástroj:** Režim letadlo nebo dočasné vypnutí Wi-Fi na vlastním testovacím zařízení, čtyři předem vybrané bezpečné aplikace a laboratorní protokol. Režim letadlo řídí rádiová rozhraní zařízení; simulujeme jím následek výpadku připojení, nikoli skutečný DoS útok.

**Úkoly:**

1. Připravte čtyři úkoly závislé různou měrou na místních a cloudových datech a předpovězte jejich chování bez sítě.
2. Na omezenou dobu odpojte pouze vlastní testovací zařízení, proveďte úkoly a přesně zaznamenejte rozdíly.
3. Připojení obnovte, ověřte synchronizaci a navrhněte opatření pro zachování služby i obnovu provozu.

**Výstupy:** Úplný protokol `před výpadkem → offline → po obnově`, důkaz o výsledku jednoho úkolu a plán odolnosti nejméně se třemi zdůvodněnými opatřeními.

<details>

<summary>**🧠 Rozbalit článek k tématu: Dostupnost, offline režim a synchronizace**</summary>

**Dostupnost poznáme nejlépe ve chvíli, kdy chybí**

**Dostupnost** znamená, že oprávněný uživatel může použít systém a data tehdy, kdy je potřebuje. Omezit ji může útok DoS nebo DDoS, ale také porucha, chyba konfigurace, přerušený kabel, výpadek napájení či nezdařená aktualizace. Bezpečnostní incident proto nemusí být způsoben útočníkem.

V tomto experimentu žádný útok neprovádíme. Bezpečně simulujeme výpadek tím, že na omezenou dobu odpojíme **vlastní zařízení** od sítě. Cílem je zjistit, které činnosti závisejí na cloudu a které mají místní či offline variantu. Takový test pomáhá plánovat odolnost: lokální kopie důležitého dokumentu, ověřená záloha, alternativní komunikační cesta nebo přesný postup obnovy.

**Režim letadlo** je funkce operačního systému, která vypíná nebo omezuje bezdrátová rádiová rozhraní, například mobilní síť, Wi-Fi a někdy Bluetooth. V tomto cvičení poskytuje jednoduchý a vratný způsob, jak jednomu zařízení odebrat síťové spojení bez zásahu do routeru nebo práce ostatních. Nevyvolává přetížení serveru a nenapodobuje mechanismus útoku DoS; modeluje pouze stav, kdy klient službu nemůže dosáhnout.

Cloudová aplikace obvykle rozděluje práci mezi zařízení uživatele a vzdálené servery. Některá data drží jen na serveru, jiná ukládá také do **místní mezipaměti — cache**. Cache může urychlit načítání a umožnit omezenou práci offline, ale nemusí obsahovat úplná ani aktuální data. Aplikace proto musí uživateli jasně ukázat, co je dostupné a které změny ještě nebyly odeslány.

Po obnovení spojení nastupuje **synchronizace**. Aplikace porovná místní změny se stavem na serveru a pokusí se je sjednotit. Pokud stejný dokument mezitím změnil jiný uživatel nebo zařízení, může vzniknout konflikt. Spolehlivý systém konflikt rozpozná a nabídne bezpečné řešení; špatný postup může jednu verzi bez upozornění přepsat.

Synchronizace není automaticky záloha. Když uživatel omylem smaže soubor, změna se může rychle přenést na všechna zařízení. Záloha uchovává oddělenou obnovitelnou kopii nebo historii verzí. Pro dostupnost jsou důležité obě schopnosti: pokračovat alespoň omezeně během výpadku a následně obnovit správný stav.

Organizace zvyšují odolnost také redundancí připojení, náhradními servery, lokálními kopiemi kritických postupů a pravidelným testováním obnovy. Opatření má vycházet z toho, jak dlouhý výpadek je přijatelný a kolik dat lze ztratit. Bez praktického testu mohou i dobře znějící plány při skutečném incidentu selhat.

</details>

<details>

<summary>**🧭 Rozbalit podrobný praktický postup simulace**</summary>

**Příprava**

1. Pracujte na vlastním nebo učitelem určeném testovacím zařízení. Neodpojujte školní síť, router ani zařízení dalších uživatelů.
2. Uložte rozpracovanou práci a ukončete přenosy či videohovory. Experiment nesmí způsobit ztrátu dat ani narušit výuku ostatních.
3. Připravte čtyři bezpečné úkoly: otevření dokumentu, nahlédnutí do kalendáře, přehrání mediálního souboru a zapsání poznámky. U každého předem odhadněte, zda bez internetu uspěje.
4. U jednoho dokumentu zajistěte místní kopii a jiný ponechte pouze jako modelovou cloudovou položku bez citlivého obsahu.

**Postup**

1. Ověřte, že je zařízení připojeno, a proveďte všechny čtyři úkoly. Zapište výchozí stav.
2. Zapněte režim letadlo nebo vypněte Wi-Fi pouze na tomto zařízení. Ověřte ikonou sítě, že připojení skutečně není dostupné.
3. Zopakujte úkoly. U každého zaznamenejte: funguje plně, funguje omezeně, nebo nefunguje. Poznamenejte také chybové hlášení či nabídnutý offline režim.
4. Vytvořte novou testovací poznámku v aplikaci, která umí pracovat offline. Nepoužívejte skutečné osobní údaje.
5. Připojení obnovte. Sledujte, zda se aplikace sama synchronizuje a zda nevznikla konfliktní verze. Výsledek synchronizace není totéž co záloha; chybná změna se může synchronizovat také.
6. Ke každému neúspěšnému úkolu navrhněte jedno opatření: místní kopii, offline režim, náhradní spojení, zálohu nebo postup pro ruční obnovu.

**Vyhodnocení**

| Úkol | Předpověď | Stav online | Stav offline | Stav po obnově | Opatření |
|---|---|---|---|---|---|
| místní dokument | bude dostupný | funguje | funguje | beze změny | pravidelně aktualizovat kopii |

Samotné odpojení neodpovídá technickému průběhu DDoS útoku. Modeluje však jeho možný důsledek pro uživatele: služba není dosažitelná. Toto omezení výslovně uveďte, aby se simulace nezaměnila s reálným mechanismem útoku.

**Ověření a odevzdání**

Odevzdejte vyplněnou tabulku a krátký plán odolnosti se třemi opatřeními. U každého napište, zda pomáhá službu zachovat během výpadku, nebo až obnovit po jeho skončení. Nakonec potvrďte, že se testovací poznámka po návratu sítě synchronizovala očekávaným způsobem.

</details>

## Závěrečná reflexe

**Který závěr nejlépe odpovídá práci bezpečnostního analytika?**

<!-- data-randomize="true" -->
[( )] Jeden nástroj poskytne úplný a definitivní obraz rizika.
[(X)] Pozorování je nutné doložit, zasadit do kontextu a uvést jeho omezení.
[( )] Veřejně viditelné zařízení je automaticky dovoleno bezpečnostně testovat.
[( )] Nejvyšší technické skóre vždy určuje nejvyšší prioritu organizace.

Vyberte jeden experiment a jednou větou propojte jeho výsledek s řetězcem:

`aktivum → hrozba → zranitelnost → následek → riziko → opatření`
