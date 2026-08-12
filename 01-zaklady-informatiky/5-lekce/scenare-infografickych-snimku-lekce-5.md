# Scénáře infografických snímků — 5. lekce

## Datová komprese

Sada pro témata 5.1–5.5 z výukového textu *Základy informatiky*. Každý scénář je samostatné zadání pro grafika, prezentační nástroj i generátor obrazu. Všechny texty určené přímo na snímek jsou uvedeny v přesném znění; delší formulace lze při generování obrazu vysázet dodatečně v prezentačním editoru.

## Společný vizuální rámec série

- Formát 16:9, ideálně 1600 × 900 px; bílé až velmi světle šedé pozadí, bezpečný okraj minimálně 40 px.
- Profesionální akademicko-technologický styl pro studenty střední školy. Bez infantilních ikon, nafukovacích kufrů, magického „smršťování“, náhodných nul a jedniček, neonového sci-fi rozhraní a dekorativního zahlcení.
- Tmavě modrá horní lišta, velké bílé bezpatkové písmo s českou diakritikou. Nadpis přibližně 44–54 px, podnadpis 25–30 px, běžný text nejméně 22–24 px.
- Paleta navazuje na předchozí lekce: námořnická modř pro strukturu, střední modř pro data, tyrkysová pro vratný převod a úsporu, oranžová pro rozhodnutí či odstraněnou redundanci, červená pouze pro nevratnou ztrátu, chybu nebo varování.
- Původní data, model či slovník a komprimovaný výstup odlišovat nejen barvou, ale i tvarem: plné datové bloky, obrysové odkazy a šrafované odstraněné detaily. Šipky používat jen pro skutečný směr kódování, dekódování nebo závislosti.
- Jeden dominantní vysvětlující mechanismus na snímek, maximálně pět vedlejších obsahových bloků. Každý snímek musí ukázat, odkud se úspora bere, jaká informace je nutná k obnově a kde leží hranice zjednodušení.
- Číselné příklady a bitové zápisy sázet neproporcionálním písmem. Důsledně rozlišovat velikost souboru, kompresní poměr, procentní úsporu a datový tok v `bit/s`.
- Pokud obrazový generátor nezvládá přesnou českou sazbu, vzorce nebo kódová slova, vytvořit vizuál s rezervovanými plochami a text doplnit až v editoru. Nevkládat pseudo-text, falešná loga, vodoznaky ani neexistující názvy formátů.

---

# Snímek 5.1 — Proč lze data komprimovat?

## Výukový záměr

Student má pochopit kompresi jako změnu reprezentace, která využívá opakování, nerovnoměrnou četnost a další předvídatelnou strukturu dat. Má rozlišit redundanci od informace potřebné k obnově a vědět, proč již účinně komprimovaná nebo téměř náhodná data obvykle další kompresí mnoho nezískají. Současně má oddělit kompresi od pouhého spojení souborů do archivu.

**Hlavní otázka:** Kde se v datech skrývá prostor, který lze nahradit kratším popisem?

**Nosná teze:** Komprese nevytváří menší kopii kouzlem; hledá pravidelnost, kterou lze popsat úsporněji než jednotlivé hodnoty.

## Přesné texty na snímku

**Název:** KDY LZE DATA POPSAT KRATŠE?

**Podnázev:** Úspora vzniká tam, kde opakování a předvídatelnost nahradíme pravidlem.

**Hlavní demonstrace:**

- `AAAAAAAAAAAA` — „12 samostatných symbolů“
- `12×A` — „hodnota + počet opakování“
- **STEJNÝ OBSAH, JINÁ REPREZENTACE**

**Tři zdroje úspory:**

- **OPAKOVÁNÍ** — „stejná hodnota nebo sekvence se vrací“
- **NEROVNOMĚRNÁ ČETNOST** — „některé symboly jsou mnohem pravděpodobnější“
- **PŘEDVÍDATELNOST** — „část dat lze popsat vztahem k okolí nebo minulosti“

**Srovnání datových krajin:**

- **PRAVIDELNÁ DATA** — „dlouhé vzory → velká šance na úsporu“
- **JIŽ KOMPRIMOVANÁ DATA** — „vzory už byly z velké části využity“
- **TÉMĚŘ NÁHODNÁ DATA** — „krátký obecný popis obvykle nenajdeme“

**Blok ARCHIVACE ≠ KOMPRESE:** „Archiv spojí více položek do jednoho balíku. Komprese mění jejich reprezentaci s cílem zmenšit objem. Formát může dělat obojí.“

**Blok POZOR:** „Redundance není automaticky chyba nebo nepotřebný obsah. U bezeztrátové komprese musí spolu s pravidlem umožnit přesnou obnovu původních dat.“

## Obrazová koncepce a kompozice

Dominantou je **transparentní analyzátor datové krajiny**. Zleva do něj vstupuje dlouhý pás dat složený ze tří charakterově odlišných úseků: pravidelné pruhy a opakující se dlaždice, text s nerovnoměrnou četností znaků a vizuálně neuspořádaný šum. Skener nad pásem nehledá „prázdná místa“, ale zvýrazňuje opakované skupiny, četné symboly a předvídatelné pokračování. Z každého rozpoznaného vzoru vede čistá vodicí čára k jeho kratšímu modelu: počet opakování, krátké kódové slovo nebo odkaz na dřívější sekvenci.

Uprostřed je největší názorný příklad `AAAAAAAAAAAA → 12×A`. Po průchodu dekodérem se na pravé straně znovu rozvine přesně dvanáct písmen A. Nad oběma reprezentacemi vede tenká závorka „stejný obsah“; samotné bloky však mají rozdílnou fyzickou délku. Zobrazení nesmí tvrdit, že zápis `12×A` je konkrétní univerzální souborový formát — jde o princip kratšího popisu.

Spodní část tvoří tři nestejně široké „datové vzorky“ vložené do stejného kompresoru. Pravidelný vzorek se výrazně zkrátí, již komprimovaný vzorek jen minimálně a téměř náhodný vzorek se může kvůli hlavičce dokonce nepatrně zvětšit. Výsledky nejsou vyjádřeny vymyšlenými procenty, ale relativní délkou a slovním hodnocením. Malý boční řez zobrazí archivní krabici, která pojme tři soubory; vedle ní samostatný kompresní mechanismus. Tím se odstraní omyl, že „zabalit“ a „zmenšit“ je vždy stejná operace.

## Vizuální metafora

Komprese je **gramatika dat**: místo opakovaného opisování celého vzoru zapíšeme pravidlo a parametry, podle nichž lze vzor znovu vytvořit. Metafora má limit: reálný kompresor nemusí význam dat chápat a pravidlo i pomocná metadata samy zabírají místo.

## Produkční prompt

> Vytvoř profesionální český výukový infografický snímek 16:9, 1600 × 900 px, na bílém až velmi světle šedém pozadí. Nahoře tmavě modrá lišta s názvem „KDY LZE DATA POPSAT KRATŠE?“ a podnázev „Úspora vzniká tam, kde opakování a předvídatelnost nahradíme pravidlem.“ Dominantní transparentní analyzátor datové krajiny: vstupní pás obsahuje pravidelné opakování, nerovnoměrně četné znaky a téměř náhodný úsek. Skener zvýrazňuje skutečné vzory a převádí je na kratší modely. Uprostřed velký přesný příklad `AAAAAAAAAAAA → 12×A`, za dekodérem se obnoví přesně `AAAAAAAAAAAA`; označ „STEJNÝ OBSAH, JINÁ REPREZENTACE“. Přidej tři zdroje úspory „OPAKOVÁNÍ“, „NEROVNOMĚRNÁ ČETNOST“, „PŘEDVÍDATELNOST“. Dole srovnej „PRAVIDELNÁ DATA“, „JIŽ KOMPRIMOVANÁ DATA“ a „TÉMĚŘ NÁHODNÁ DATA“ bez vymyšlených procent. Vpravo malý řez „ARCHIVACE ≠ KOMPRESE“: archiv spojuje položky, komprese zmenšuje reprezentaci. Modro-tyrkysová technická estetika, oranžová pro odhalený vzor, velké české písmo a dostatek volného prostoru. Bez kouzelného lisu, bez tvrzení, že každý soubor se vždy zmenší, bez univerzálního formátu `12×A`, bez pseudo-textu a náhodného binárního pozadí.

## Kontrolní bod

Příklad musí umožnit přesně obnovit dvanáct písmen A. Snímek nesmí zaměnit redundanci za bezvýznamná data ani tvrdit, že komprese zaručeně zmenší libovolný vstup; archivace a komprese musejí být zobrazeny jako dvě odlišné funkce.

---

# Snímek 5.2 — Bezeztrátová a ztrátová komprese

## Výukový záměr

Student má rozhodnout, kdy je nutná bitově přesná obnova a kdy lze přijmout řízenou změnu vnímaného výsledku. Má chápat, že ztrátová komprese není náhodné poškození, ale optimalizace podle modelu vnímání nebo důležitosti informace. Musí také vědět, že jednou odstraněné detaily nelze dekompresí věrně získat zpět.

**Hlavní otázka:** Co se po dekompresi musí vrátit přesně a co může být účelně zjednodušeno?

**Nosná teze:** Typ komprese neurčuje přípona ani velikost úspory, ale požadavek na shodu obnovených dat s originálem.

## Přesné texty na snímku

**Název:** CO SMÍ KOMPRESE ZAHODIT?

**Podnázev:** Bezeztrátová cesta obnoví každý bit; ztrátová zachová účel za cenu řízené změny.

**Větev A — BEZEZTRÁTOVÁ:**

- „originál → komprese → dekomprese → bitově shodný originál“
- **KONTROLA:** `původní bity = obnovené bity`
- **KDY JE NUTNÁ:** „program • zdrojový kód • databáze • text • měření“
- **PŘÍKLADY:** „ZIP • 7z • PNG • FLAC“

**Větev B — ZTRÁTOVÁ:**

- „originál → model důležitosti → odstranění detailu → podobný výsledek“
- **KONTROLA:** `obnovená data ≠ původní data`
- **KDY DÁVÁ SMYSL:** „fotografie • zvuk • video“
- **PŘÍKLADY:** „JPEG • MP3 • AAC • Opus • H.264 • AV1“

**Rozhodovací otázka:** „Je chyba jediného bitu nepřijatelná, nebo hodnotíme vnímanou kvalitu a účel?“

**Blok ŘÍZENÁ ZTRÁTA:** „Algoritmus se snaží omezit méně významné detaily. Výsledek ale není původní soubor a ztracené informace nelze dekompresí vrátit.“

**Blok POZOR:** „Ztrátový soubor nelze opakovaným ukládáním ‚vyléčit‘. Další ztrátová komprese může přidat nové artefakty.“

## Obrazová koncepce a kompozice

Dominantou je **rozcestí jednoho datového objektu do dvou fyzicky odlišných laboratoří**. Vlevo vstupuje společný transparentní blok s viditelnou jemnou strukturou. Horní bezeztrátová větev jej rozebere na vzory a krátké popisy, ale v dekodéru všechny části znovu poskládá. Před originálem a obnoveným blokem jsou dvě stejné bitové mřížky; srovnávací světelná brána je překryje a ukáže přesnou shodu.

Dolní ztrátová větev pracuje s fotografickým výřezem, zvukovým spektrem a dvojicí sousedních videosnímků. „Model důležitosti“ průsvitně označí jemné textury, maskované zvukové složky a časově podobné oblasti, které může algoritmus popsat hruběji nebo nepřenášet samostatně. Na výstupu je vizuálně podobná scéna, ale při lupě jsou patrné zjednodušené detaily. Odstraněné části odcházejí pouze jednosměrnou červenooranžovou cestou; žádná šipka je nesmí při dekompresi vracet.

Mezi větvemi je výrazná **rozhodovací výhybka podle účelu**. Na přesnou větev míří zdrojový kód, databázová tabulka a měřicí záznam. Na ztrátovou větev míří fotografie pro web, hudební stream a video. Smyslem není říci, že každý obraz nebo zvuk má být ztrátový — například PNG a FLAC dokazují opačnou možnost. V dolním pásu proto stojí krátká otázka, zda je prioritou bitová shoda, nebo přijatelná vnímaná kvalita při menší velikosti.

## Vizuální metafora

Bezeztrátová komprese je **skládací technický výkres**, který po rozložení obsahuje všechny původní čáry. Ztrátová komprese je **řízená generalizace mapy**: pro dané měřítko odstraní jemnosti, ale zachová hlavní orientaci. Limit metafory: algoritmus neví univerzálně, co je pro konkrétního člověka důležité, a různé režimy mohou vytvářet odlišné artefakty.

## Produkční prompt

> Navrhni profesionální český výukový snímek 16:9, 1600 × 900 px, bílé pozadí a tmavě modrá horní lišta. Přesný název „CO SMÍ KOMPRESE ZAHODIT?“ a podnázev „Bezeztrátová cesta obnoví každý bit; ztrátová zachová účel za cenu řízené změny.“ Dominantní rozcestí jednoho datového objektu do dvou laboratoří. Horní tyrkysová větev „BEZEZTRÁTOVÁ“: `originál → komprese → dekomprese → bitově shodný originál`, dvě stejné bitové mřížky a kontrola `původní bity = obnovené bity`; příklady ZIP, 7z, PNG, FLAC a použití program, zdrojový kód, databáze, text, měření. Dolní oranžová větev „ZTRÁTOVÁ“: `originál → model důležitosti → odstranění detailu → podobný výsledek`, lupa ukazuje zjednodušenou texturu, přitom `obnovená data ≠ původní data`; příklady JPEG, MP3, AAC, Opus, H.264, AV1 a použití fotografie, zvuk, video. Odstraněné detaily vedou pouze ven, nikdy zpět. Uprostřed otázka „Je chyba jediného bitu nepřijatelná, nebo hodnotíme vnímanou kvalitu a účel?“ Přidej bloky „ŘÍZENÁ ZTRÁTA“ a „POZOR“. Modro-tyrkysová série, červená jen pro nevratně odstraněnou informaci, velké české písmo. Bez dojmu, že ztrátová komprese je náhodné poškození, bez navracení zahozených detailů, bez tvrzení, že obraz a zvuk se vždy komprimují ztrátově, bez pseudo-textu.

## Kontrolní bod

Bezeztrátová větev musí končit bitově shodnými daty. Ztrátová větev musí zřetelně ukázat nevratné odstranění či zjednodušení části informace a nesmí slibovat přesnou obnovu ani označovat každou změnu za lidsky nepostřehnutelnou.

---

# Snímek 5.3 — Kompresní poměr, úspora a kvalita

## Výukový záměr

Student má správně vypočítat kompresní poměr a procentní úsporu a současně chápat, že samotná velikost nepopisuje kvalitu ani výpočetní náklady. U ztrátové komprese má číst nastavení jako kompromis mezi objemem, kvalitou, rychlostí, kompatibilitou a datovým tokem. Nemá automaticky srovnávat dva kodeky jen podle stejného bitrate.

**Hlavní otázka:** Jak vyjádřit úsporu a proč nejmenší soubor nemusí být nejlepší výsledek?

**Nosná teze:** Poměr a procenta měří velikost; vhodnost komprese určuje až účel, kvalita a náklady zpracování.

## Přesné texty na snímku

**Název:** MENŠÍ SOUBOR MÁ SVOU CENU

**Podnázev:** Velikost lze spočítat přesně; kvalitu a vhodnost musíme posoudit v kontextu.

**Výpočetní stanice:**

- **PŮVODNÍ VELIKOST:** `10 MB`
- **KOMPRIMOVANÁ VELIKOST:** `2 MB`
- **KOMPRESNÍ POMĚR:** `10 : 2 = 5 : 1`
- **VÝSLEDNÁ VELIKOST:** `2 / 10 = 20 % původní`
- **ÚSPORA:** `(1 − 2/10) × 100 % = 80 %`

**Pět regulačních os:**

- **VELIKOST** — „kolik místa a přenosu výsledek potřebuje“
- **KVALITA** — „kolik relevantních detailů zůstane“
- **RYCHLOST** — „jak dlouho trvá kódování a dekódování“
- **NÁROKY** — „procesor, paměť a energie“
- **KOMPATIBILITA** — „zda výsledek přehraje cílové zařízení“

**Bitrate:** „Počet bitů za sekundu zvuku nebo videa ovlivňuje velikost, ale sám nezaručuje stejnou kvalitu.“

**Dva různé vstupy:**

- **HLADKÁ PLOCHA:** „méně jemné struktury“
- **LISTÍ A VLASY:** „mnoho hran a nepředvídatelných detailů“

**Blok POZOR:** „Stejný bitrate ≠ stejná kvalita. Rozhoduje kodek, nastavení, obsah i způsob kódování.“

**Malý soubor:** „U velmi malých dat mohou hlavičky a slovník převážit nad dosaženou úsporou.“

## Obrazová koncepce a kompozice

Dominantou je **technická vyvažovací konzola se dvěma propojenými částmi**. Levá třetina funguje jako přesná měřicí stanice: průhledný datový hranol `10 MB` vstoupí do kompresoru a vyjde jako hranol `2 MB`. Pod ním se ve třech samostatných řádcích odvodí poměr `5 : 1`, výsledná velikost `20 %` a úspora `80 %`. Čísla jsou velká, zarovnaná a barevně i tvarem odlišují původní objem, zbylý objem a odstraněnou část. Procento úspory se nesmí vizuálně zaměnit s poměrem 5 : 1.

Pravou polovinu zabírá **pětiosá ovládací plocha kompromisu**, nikoli jediný posuvník „kvalita“. Posun směrem k menší velikosti u ztrátového média může snížit zachované detaily nebo zvýšit výpočetní náročnost; výsledná volba zároveň musí projít bránou kompatibility cílového zařízení. Tři profily použití — webová fotografie, archivní předloha a živý videohovor — nastaví konzolu odlišně. Neuvádět univerzální „správné“ hodnoty bitrate.

Pod konzolou jsou dva stejně velké fotografické výřezy: hladké studiové pozadí a husté listí s vlasy. Projdou stejným názorným režimem, ale ve druhém výřezu lupa ukáže více obtížně popsatelných hran a textur. Tím snímek vysvětlí, že výsledek závisí na obsahu. V rohu je drobný řez velmi malým souborem, u něhož pevná hlavička zabere významnou část výstupu.

## Vizuální metafora

Volba komprese je **nastavení technického mixážního pultu**, nikoli tlačítko „více je lépe“. Každý účel potřebuje jinou rovnováhu velikosti, detailu, výpočetních nároků a kompatibility. Limit metafory: jednotlivé parametry nejsou nezávislé lineární posuvníky a kvalitu nelze vždy spolehlivě vyjádřit jedním číslem.

## Produkční prompt

> Vytvoř profesionální český infografický snímek 16:9, 1600 × 900 px, bílé až světle šedé pozadí, tmavě modrá horní lišta. Název „MENŠÍ SOUBOR MÁ SVOU CENU“, podnázev „Velikost lze spočítat přesně; kvalitu a vhodnost musíme posoudit v kontextu.“ Vlevo dominantní přesná měřicí stanice: datový hranol `10 MB` se zmenší na `2 MB`; pod ním tři jasně oddělené výpočty `10 : 2 = 5 : 1`, `2 / 10 = 20 % původní` a `(1 − 2/10) × 100 % = 80 %`. Vpravo sofistikovaná pětiosá konzola „VELIKOST“, „KVALITA“, „RYCHLOST“, „NÁROKY“, „KOMPATIBILITA“ se třemi rozdílnými profily použití: webová fotografie, archivní předloha, živý videohovor. Dole srovnej hladkou plochu s výřezem listí a vlasů; ukaž, že složitost obsahu mění komprimovatelnost. Přidej přesný text „Stejný bitrate ≠ stejná kvalita“ a malý detail, že hlavička může u velmi malého souboru převážit nad úsporou. Čistá modro-tyrkysová série, oranžová pro kompromis, velké monospace vzorce. Bez záměny poměru a procent, bez univerzálních hodnot bitrate, bez tvrzení, že nejmenší soubor je automaticky nejlepší, bez pseudo-textu.

## Kontrolní bod

Pro vstup `10 MB` a výstup `2 MB` musí být kompresní poměr přesně `5 : 1`, výsledná velikost `20 %` původní a úspora `80 %`. Snímek nesmí z bitrate odvozovat kvalitu bez ohledu na kodek, nastavení a obsah.

---

# Snímek 5.4 — RLE, Huffman a slovníkové algoritmy

## Výukový záměr

Student má rozlišit tři základní zdroje úspory: délku souvislého běhu, nerovnoměrnou četnost symbolů a opakování celých sekvencí. Má pochopit, proč se každý princip hodí na jinou strukturu dat a proč může režie nebo nevhodný vstup výsledek zvětšit. Snímek nemá předstírat, že jednoduché školní příklady úplně popisují moderní kompresní formáty.

**Hlavní otázka:** Jak tři různé algoritmy objeví tři různé druhy pravidelnosti?

**Nosná teze:** RLE počítá běhy, Huffman zkracuje časté symboly a slovníková metoda odkazuje na dříve známé sekvence.

## Přesné texty na snímku

**Název:** TŘI ZPŮSOBY, JAK NAJÍT VZOR

**Podnázev:** Stejná data nelze vždy zmenšit stejným trikem.

**Stanice 1 — RLE: POČÍTEJ BĚHY**

- `AAAAAAABBBCC → 7A3B2C`
- „Úspora vzniká v dlouhých souvislých opakováních.“
- **SLABINA:** `ABCDE → 1A1B1C1D1E` — „krátké běhy mohou data zvětšit“

**Stanice 2 — HUFFMAN: ZKRACUJ ČASTÉ**

- **ČETNOST:** `A×6 • B×2 • C×1`
- **KÓDY:** `A = 0 • B = 10 • C = 11`
- „Častý symbol dostane kratší kódové slovo.“
- **PODMÍNKA:** „kódy musejí být jednoznačně rozlišitelné“

**Stanice 3 — SLOVNÍK: ODKAZUJ NA SEKVENCI**

- `DATA DATA SÍŤ | DATA DATA SÍŤ`
- **SLOVNÍK `[1]`:** `DATA DATA SÍŤ`
- **VÝSTUP:** `[1] [1]`
- „Opakovanou skupinu nahradí odkaz na známý vzor.“

**Společný blok REŽIE:** „Počty, strom, slovník a další metadata také zabírají místo. Krátký školní zápis není úplný souborový formát.“

**Blok PRAXE:** „Moderní kompresní systémy často kombinují modelování, odkazy, transformace a entropické kódování.“

## Obrazová koncepce a kompozice

Dominantou je **mechanická laboratoř se třemi fyzicky rozdílnými pracovními stanicemi**, kterými neprochází tentýž příklad, ale každý dostane vstup odpovídající svému principu. Stanice RLE má optickou bránu, která změří délku souvislého barevného pásu a připevní k hodnotě počitadlo. Vedle správného dlouhého běhu je úzký odpadní test s pěti různými znaky; každý vyžaduje vlastní počet, takže výstup roste.

Huffmanova stanice připomíná **vyvažovací strom četností**. Devět symbolů `AAAAAABBC` se seskupí podle počtů `6, 2, 1`. Výrazné větve vedou k prefixovým kódům `A = 0`, `B = 10`, `C = 11`; délka cesty, nikoli číselná hodnota kódu, vyjadřuje cenu symbolu. Strom musí být zobrazen jako názorný platný příklad pro toto rozdělení, ne jako univerzální kód. Vedle je malý dekodér, který čte bity zleva a vždy dojde k právě jednomu listu.

Slovníková stanice má průhlednou paměťovou polici. První výskyt sekvence `DATA DATA SÍŤ` vytvoří položku `[1]`; druhý výskyt se fyzicky nahradí krátkým odkazem. Tenké vodicí čáry ukazují, že dekodér musí znát stejný slovník nebo pravidlo jeho vytvoření. Pod všemi stroji probíhá společný oranžový pás „režie“, do něhož se ukládají počty, popis stromu či slovník. Díky tomu se úspora netváří jako bezplatná.

## Vizuální metafora

Tři algoritmy jsou **tři typy zkratek v zápisníku**: počet stejných položek, kratší značka pro časté slovo a odkaz „viz dříve“ na celou frázi. Metafora má limit: konkrétní formát musí zkratky jednoznačně zakódovat v bitech a přenést vše potřebné k dekódování.

## Produkční prompt

> Navrhni profesionální český výukový snímek 16:9, 1600 × 900 px, bílé pozadí, tmavě modrá horní lišta s názvem „TŘI ZPŮSOBY, JAK NAJÍT VZOR“. Podnázev „Stejná data nelze vždy zmenšit stejným trikem.“ Dominantní mechanická laboratoř tří odlišných stanic. První „RLE — POČÍTEJ BĚHY“ přesně ukáže `AAAAAAABBBCC → 7A3B2C` a varovný případ `ABCDE → 1A1B1C1D1E`. Druhá „HUFFMAN — ZKRACUJ ČASTÉ“ ukáže vstup `AAAAAABBC`, četnosti `A×6 • B×2 • C×1` a jednoduchý platný prefixový strom s kódy `A = 0 • B = 10 • C = 11`; zdůrazni, že rozhoduje délka kódu a jednoznačná rozlišitelnost. Třetí „SLOVNÍK — ODKAZUJ NA SEKVENCI“ ukáže `DATA DATA SÍŤ | DATA DATA SÍŤ`, položku slovníku `[1] = DATA DATA SÍŤ` a názorný výstup `[1] [1]`. Pod všemi stanicemi společný pás „REŽIE“ pro počty, strom, slovník a metadata. Přidej blok, že moderní systémy často kombinují více principů. Modro-tyrkysová technická estetika, oranžová pro pravidlo a metadata, velké monospace příklady. Bez tvrzení, že uvedené zápisy jsou úplné souborové formáty, bez pravidla „nejčastější znak dostane nejnižší binární číslo“, bez nejednoznačných kódových slov a bez pseudo-textu.

## Kontrolní bod

RLE musí počítat pouze souvislé běhy. Huffmanův příklad musí mít jednoznačně dekódovatelná prefixová kódová slova a kratší kód pro nejčastější A. Slovníkový odkaz musí mířit na celou známou sekvenci; u všech tří principů musí být přiznána režie.

---

# Snímek 5.5 — Komprese v obrazu, zvuku, videu a archivech

## Výukový záměr

Student má odlišit kodek, kontejner a archiv a vybírat technologii podle typu redundance a cílového použití. Má na konkrétním souboru MP4 pochopit, že kontejner může spojovat několik proudů kódovaných různými kodeky. Současně má vědět, že přípona sama neříká vše o kvalitě, režimu komprese ani vnitřním obsahu.

**Hlavní otázka:** Co přesně se skrývá za příponou souboru a který nástroj skutečně data komprimuje?

**Nosná teze:** Kodek kóduje datový proud, kontejner proudy organizuje a archiv sdružuje obecné soubory; vhodná volba závisí na účelu.

## Přesné texty na snímku

**Název:** PŘÍPONA NENÍ CELÝ PŘÍBĚH

**Podnázev:** Kodek zpracuje proud, kontejner jej uspořádá a archiv uchová obecná data.

**Anatomie souboru `video.mp4`:**

- **KONTEJNER MP4** — „časování • propojení proudů • metadata“
- **VIDEO** — „kódováno například H.264“
- **ZVUK** — „kódován například AAC“
- **TITULKY** — „samostatná textová stopa“
- **METADATA** — „název, délka a technické údaje“

**Tři pojmy:**

- **KODEK** — „postup nebo implementace pro kódování a dekódování konkrétního média“
- **KONTEJNER** — „struktura, která spojuje proudy a metadata do jednoho souboru“
- **ARCHIV** — „balík obecných souborů s bezeztrátovou obnovou; komprese může být součástí“

**Mapa podle dat:**

- **OBRAZ:** „PNG — ostrá grafika, bezeztrátově • JPEG — fotografie, ztrátově • WebP/AVIF — více režimů“
- **ZVUK:** „FLAC — bezeztrátově • MP3/AAC/Opus — ztrátově“
- **VIDEO:** „H.264/H.265/VP9/AV1 — využití prostoru i podobnosti v čase“
- **OBECNÉ SOUBORY:** „ZIP/7z — přesná obnova“

**Rozhodovací filtr:** „účel • kompatibilita • velikost • kvalita • rychlost zpracování • podpora cílového prostředí“

**Blok POZOR:** „MP4 není jeden kodek. Stejný kontejner může nést různé kombinace proudů a přípona sama nezaručuje jejich přehratelnost.“

## Obrazová koncepce a kompozice

Dominantou je **explodovaný technický řez kontejnerem MP4**. Vpravo uprostřed se vznáší průhledná schránka `video.mp4`; z ní jsou vysunuté samostatné časově zarovnané vrstvy: filmový pás „VIDEO — H.264“, zvuková stopa „ZVUK — AAC“, textová stopa „TITULKY“ a tenká metadata. Společná časová osa prochází vrstvami a kontejner je synchronizuje. H.264 a AAC musejí být zobrazeny jako příklady obsahu, nikoli povinná definice každého MP4.

Vlevo jsou tři odlišné přístroje. **Kodek** přijímá jediný mediální proud a vytváří či čte jeho komprimovanou reprezentaci. **Kontejner** proudy nezobrazuje jako znovu komprimované jedním univerzálním algoritmem, ale skládá je s časováním a metadaty. **Archiv** přijímá několik obecných souborů — dokument, tabulku, program a fotografii — a vydává balík, z něhož se položky obnoví přesně. Přístroje mají jiné konektory a nesmějí být tři stejné kartičky.

Spodní pás je **mapa redundance podle média**. U obrazu se zvýrazní ostré hrany versus fotografická textura; u zvuku opakování a omezení vnímání; u videa prostorová struktura jednoho snímku a šipka k podobnosti mezi sousedními snímky; u archivů přesné opakující se bajtové sekvence bez dovolování ztráty. Nad mapou vede rozhodovací filtr se šesti otázkami. Cílem není vytvořit žebříček „nejlepších“ formátů, ale ukázat, proč se volba řídí účelem a prostředím.

## Vizuální metafora

Kontejner je **časově řízené pouzdro několika stop**, kodek je **překladač konkrétního proudu** a archiv je **evidovaný balík samostatných zásilek**. Metafora má limit: konkrétní specifikace určují, které kombinace jsou dovoleny, a praktická přehratelnost závisí na podpoře použitých kodeků i kontejneru.

## Produkční prompt

> Vytvoř sofistikovaný český výukový infografický snímek 16:9, 1600 × 900 px, bílé až velmi světle šedé pozadí a tmavě modrá horní lišta. Název „PŘÍPONA NENÍ CELÝ PŘÍBĚH“, podnázev „Kodek zpracuje proud, kontejner jej uspořádá a archiv uchová obecná data.“ Dominantní explodovaný technický řez souborem `video.mp4`: průhledný „KONTEJNER MP4“ synchronizuje samostatné vrstvy „VIDEO — například H.264“, „ZVUK — například AAC“, „TITULKY“ a „METADATA“ na společné časové ose. Vlevo tři funkčně odlišné přístroje „KODEK“, „KONTEJNER“, „ARCHIV“ s přesnými krátkými definicemi. Dole mapa podle typu dat: „OBRAZ — PNG, JPEG, WebP/AVIF“, „ZVUK — FLAC, MP3/AAC/Opus“, „VIDEO — H.264/H.265/VP9/AV1“, „OBECNÉ SOUBORY — ZIP/7z“; u videa ukaž prostorovou i časovou podobnost. Přidej rozhodovací filtr „účel • kompatibilita • velikost • kvalita • rychlost zpracování • podpora cílového prostředí“ a blok „MP4 není jeden kodek“. Modro-tyrkysová akademicko-technologická estetika, velké české písmo, přesné zarovnání stop a dostatek volného prostoru. Bez falešných log, bez tvrzení, že každý MP4 obsahuje právě H.264 a AAC, bez záměny ZIPu za ztrátovou multimediální kompresi, bez žebříčku univerzálně nejlepšího formátu a bez pseudo-textu.

## Kontrolní bod

MP4 musí být zobrazen jako kontejner, zatímco H.264 a AAC jako příklady kódování samostatných proudů. Video musí využívat podobnost v prostoru i čase; archiv ZIP/7z musí umožnit přesnou obnovu obecných dat. Přípona nesmí být prezentována jako úplná informace o vnitřním kodeku nebo kompatibilitě.

