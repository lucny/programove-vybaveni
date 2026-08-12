# Scénáře infografických snímků — 3. lekce

## Kódování v informatice

Sada pro témata 3.1–3.7 z výukového textu *Základy informatiky*. Každý scénář je samostatné zadání pro grafika, prezentační nástroj i generátor obrazu. Všechny texty určené přímo na snímek jsou uvedeny v přesném znění; delší formulace lze při generování obrazu vysázet dodatečně v prezentačním editoru.

## Společný vizuální rámec série

- Formát 16:9, ideálně 1600 × 900 px; bílé až velmi světle šedé pozadí, bezpečný okraj minimálně 40 px.
- Profesionální akademicko-technologický styl pro studenty střední školy. Bez infantilních ikon, náhodných nul a jedniček, neonového sci-fi rozhraní a dekorativního zahlcení.
- Tmavě modrá horní lišta, velké bílé bezpatkové písmo s českou diakritikou. Nadpis přibližně 44–54 px, podnadpis 25–30 px, běžný text nejméně 22–24 px.
- Paleta navazuje na předchozí lekce: námořnická modř pro strukturu, střední modř pro data, tyrkysová pro převod a tok, oranžová pro aktivní pravidlo či rozhodnutí, červená pouze pro chybu nebo varování.
- Barevný význam vždy podpořit tvarem, typem čáry, šrafou nebo symbolem. Jeden dominantní vysvětlující mechanismus na snímek, maximálně pět vedlejších obsahových bloků.
- Číselné zápisy sázet neproporcionálním písmem. Důsledně zachovat dolní indexy soustav, mezery ve skupinách bitů, velikost písmen v hexadecimálním zápisu a přesnou podobu kódových bodů a bajtů.
- Pokud obrazový generátor nezvládá přesnou českou sazbu či matematické výrazy, vytvořit vizuál s rezervovanými plochami a text doplnit až v editoru. Nevkládat pseudo-text.

---

# Snímek 3.1 — Binární a další číselné soustavy

## Výukový záměr

Student má pochopit poziční soustavu jako obecný princip: číslice sama nestačí, její hodnotu určuje pozice a základ soustavy. Dvojkový zápis není „řeč elektronu“, ale lidská interpretace spolehlivě rozlišitelných stavů. Hexadecimální a osmičkový zápis představují kratší pohled na tutéž bitovou hodnotu.

**Hlavní otázka:** Jak může tatáž hodnota vypadat jako `56`, `111000`, `70` i `38`?

**Nosná teze:** Číselná soustava mění zápis, nikoli hodnotu; každá pozice násobí číslici mocninou základu.

## Přesné texty na snímku

**Název:** STEJNÁ HODNOTA, JINÝ ZÁPIS

**Podnázev:** Hodnotu číslice určuje její pozice a základ soustavy.

**Středová rovnost:** `56₁₀ = 111000₂ = 70₈ = 38₁₆`

**Poziční rozklad:** `11010110₂ = 1×128 + 1×64 + 0×32 + 1×16 + 0×8 + 1×4 + 1×2 + 0×1 = 214₁₀`

**Čtyři soustavy:**

- **BINÁRNÍ — základ 2:** „číslice 0–1 • váhy 1, 2, 4, 8…“
- **OSMIČKOVÁ — základ 8:** „číslice 0–7 • jedna číslice = 3 bity“
- **DESÍTKOVÁ — základ 10:** „číslice 0–9 • váhy 1, 10, 100…“
- **HEXADECIMÁLNÍ — základ 16:** „číslice 0–9 a A–F • jedna číslice = 4 bity“

**Přímé seskupení:** `1101 0110₂ = D6₁₆`

**Praktické použití HEX:** „barvy CSS • adresy paměti • MAC adresy • surové bajty“

**Blok POZOR:** „Nula a jednička jsou dohodnuté logické významy fyzických stavů. Obvod neobsahuje malé napsané číslice.“

## Obrazová koncepce a kompozice

Dominantou je **poziční váhový stroj**. Osm svislých vah nebo transparentních buněk nese zleva váhy `128, 64, 32, 16, 8, 4, 2, 1`. Nad každou je bit zápisu `11010110₂`; aktivní jedničky spouštějí modrý dílek odpovídající hmotnosti, nuly nechávají pozici prázdnou. Dílky se na pravé straně sečtou do jediného výsledku `214₁₀`. Diagram tak ukáže, že význam bitu vzniká jeho pozicí, ne samotným symbolem.

Pod hlavním mechanismem je jedna hodnota `56` zobrazena jako čtyřstranný technický objekt. Každá strana nese jiný zápis: `56₁₀`, `111000₂`, `70₈`, `38₁₆`. Objekt se nemění, mění se pouze čtecí stupnice. Vpravo je zvětšený detail bitového pásu `1101 0110`, kolem něhož se uzavřou dvě přesné svorky po čtyřech bitech; nad nimi se objeví `D` a `6`.

V levém dolním rohu může být realistický makrořez digitálním vstupem se dvěma bezpečně oddělenými pásmy napětí označenými „logický stav 0“ a „logický stav 1“. Neuvádět konkrétní napětí, protože závisí na použité technologii. V pravém dolním rohu je stručná mapa praktických použití hexadecimálního zápisu.

## Vizuální metafora

Číselná soustava je **jiná stupnice na stejném měřidle**. Podobně jako lze tutéž délku vyjádřit v metrech nebo centimetrech, lze tutéž celočíselnou hodnotu zapsat různými soustavami. Metafora má limit: změna jednotky a změna základu nejsou matematicky totožné operace; společná je pouze neměnnost popisované hodnoty.

## Produkční prompt

> Vytvoř profesionální český výukový infografický snímek 16:9, 1600 × 900 px, na bílém až velmi světle šedém pozadí. Tmavě modrá horní lišta s přesným názvem „STEJNÁ HODNOTA, JINÝ ZÁPIS“ a podnázev „Hodnotu číslice určuje její pozice a základ soustavy.“ Dominantní poziční váhový stroj přes 55 % plochy: osm zarovnaných buněk s váhami `128, 64, 32, 16, 8, 4, 2, 1` a nad nimi přesný bitový zápis `11010110₂`. Jedničky aktivují odpovídající váhové díly, nuly zůstávají prázdné; výsledný součet je `214₁₀`. Uveď celý rozklad `1×128 + 1×64 + 0×32 + 1×16 + 0×8 + 1×4 + 1×2 + 0×1 = 214₁₀`. Dole ukaž jeden neměnný objekt se čtyřmi zápisy `56₁₀ = 111000₂ = 70₈ = 38₁₆`. Vpravo detail seskupení `1101 0110₂ = D6₁₆`, přesně čtyři bity na jednu hexadecimální číslici. Přidej stručné popisy soustav se základy 2, 8, 10 a 16, praktické použití HEX a malý fyzický detail dvou logických stavů bez konkrétních napěťových hodnot. Čistá modro-tyrkysová technická estetika, oranžová jen pro aktivní váhu, velké monospace zápisy, přesné dolní indexy. Bez náhodného binárního pozadí, pseudo-textu, tvrzení, že elektronika „myslí v nulách a jedničkách“, nebo matematicky chybných seskupení.

## Kontrolní bod

Všechny čtyři zápisy hodnoty 56 musejí být správné. U rozkladu `11010110₂` musí být aktivní přesně váhy 128, 64, 16, 4 a 2 a výsledkem 214.

---

# Snímek 3.2 — Převody mezi číselnými soustavami

## Výukový záměr

Student má rozlišit tři různé převodní strategie: váhový rozklad při převodu do desítkové soustavy, opakované dělení se zbytky při převodu z desítkové soustavy a přímé seskupování bitů při převodu mezi binární, osmičkovou a hexadecimální soustavou. Nemá zaměňovat pořadí zbytků ani seskupovat bity zleva.

**Hlavní otázka:** Kterou převodní cestu zvolit a odkud číst výsledek?

**Nosná teze:** Převod zachovává hodnotu; mění pouze pravidlo, podle něhož zápis čteme nebo sestavujeme.

## Přesné texty na snímku

**Název:** TŘI CESTY KE STEJNÉ HODNOTĚ

**Podnázev:** Váhy, zbytky nebo skupiny bitů — metoda závisí na směru převodu.

**Cesta A — BIN → DEC:**

`101101₂`

`32 + 8 + 4 + 1 = 45₁₀`

„Sečti váhy pozic, na kterých je 1.“

**Cesta B — DEC → BIN:**

`56 : 2 → zbytky 0, 0, 0, 1, 1, 1`

„Zbytky čti zdola nahoru.“

`56₁₀ = 111000₂`

**Cesta C — BIN ↔ HEX:**

`0011 1000₂ = 38₁₆`

„Seskupuj zprava po čtyřech bitech.“

**Prefixy v kódu:** `0b1010 = 10₁₀` • `0x1A = 26₁₀`

**Praktický detail RGB:** `#FF8000 → R 255 • G 128 • B 0`

**Blok POZOR:** „Při dělení zapisujeme zbytky shora dolů, ale výsledný binární zápis čteme v opačném pořadí.“

## Obrazová koncepce a kompozice

Dominantou je **převodní dílna se třemi různými nástroji**, nikoli tři stejné kartičky. Vlevo nahoře jsou binární pozice zavěšené nad váhovou miskou: jedničky shodí hodnoty 32, 8, 4 a 1 do součtu 45. Vlevo dole je svislá dělicí šachta pro číslo 56; každé patro dělí dvěma a odkládá zbytek na pravou hranu. Výrazná tyrkysová šipka se po posledním dělení obrátí vzhůru a přečte zbytky `111000`.

Pravou polovinu zabírá rychlá „hexadecimální spojka“. Binární pás se zarovná zprava, případně doplní nulami vlevo, a přesná mechanická čelist jej rozřeže na čtveřice `0011 | 1000`. Každá čtveřice se přímo překlopí na číslici `3 | 8`. Pod spojkou je praktický řez barvou CSS `#FF8000`: tři hexadecimální dvojice vstupují do tří kanálů RGB a vytvářejí oranžový barevný vzorek.

Směr čtení je u každé metody fyzicky jiný: váhy vedou k součtu, dělicí šachta vede dolů a výsledek zpět nahoru, seskupování postupuje od pravého okraje. Právě tyto směry mají tvořit hlavní paměťovou oporu snímku.

## Vizuální metafora

Převod je **volba správného nástroje v dílně**. Hodnota je obrobek, který zůstává stejný, zatímco nástroj mění jeho zápis. Metafora nesmí vyvolat dojem, že existuje jediný univerzální mechanický postup nebo že převodem dochází k zaokrouhlení celého čísla.

## Produkční prompt

> Navrhni profesionální český výukový snímek 16:9, 1600 × 900 px, bílé pozadí, tmavě modrá horní lišta. Přesný název „TŘI CESTY KE STEJNÉ HODNOTĚ“, podnázev „Váhy, zbytky nebo skupiny bitů — metoda závisí na směru převodu.“ Dominantní technická převodní dílna se třemi odlišnými mechanismy. První: `101101₂` nad pozičními váhami `32, 16, 8, 4, 2, 1`, sečtou se pouze `32 + 8 + 4 + 1 = 45₁₀`. Druhý: svislá šachta opakovaného dělení čísla 56 dvěma, zbytky shora dolů `0, 0, 0, 1, 1, 1`, výrazná šipka zpět zdola nahoru a výsledek `56₁₀ = 111000₂`. Třetí: binární pás zarovnaný zprava do čtveřic `0011 1000₂`, přímý převod na `38₁₆`. Přidej `0b1010 = 10₁₀`, `0x1A = 26₁₀` a praktický RGB detail `#FF8000 → R 255 • G 128 • B 0`. Barevně a tvarem odliš vstup, pravidlo a výsledek. Velké české písmo, monospace čísla, přesné směry šipek. Bez kalkulačky jako hlavní ilustrace, bez čtení zbytků shora dolů, bez seskupování bitů od levého okraje a bez pseudo-textu.

## Kontrolní bod

Dělicí šachta musí dát šest zbytků v pořadí zápisu `0, 0, 0, 1, 1, 1` a výsledek se musí číst zdola nahoru jako `111000₂`. U hexadecimálního převodu se skupiny tvoří zprava.

---

# Snímek 3.3 — Kódování, komprese, šifrování a hashování

## Výukový záměr

Student má bezpečně rozlišit čtyři operace podle jejich cíle, podmínek zpětného získání dat a typického použití. Snímek má odstranit časté omyly „Base64 šifruje“, „ZIP chrání obsah“ a „hash lze dešifrovat“.

**Hlavní otázka:** Co se s daty skutečně děje — mění se zápis, velikost, čitelnost, nebo vzniká otisk?

**Nosná teze:** Podobně vypadající změna dat může mít zcela jiný účel; operaci určujeme podle její funkce, ne podle nesrozumitelnosti výstupu.

## Přesné texty na snímku

**Název:** KÓDOVÁNÍ NENÍ ŠIFROVÁNÍ

**Podnázev:** Čtyři operace mění data, ale každá řeší jiný problém.

**Čtyři funkční větve:**

- **KÓDOVÁNÍ — jiný zápis:** „Známé pravidlo převádí mezi reprezentacemi.“ • „Příklad: UTF-8, Base64“
- **KOMPRESE — menší objem:** „Odstraňuje nebo omezuje redundanci.“ • „Příklad: ZIP, JPEG“
- **ŠIFROVÁNÍ — utajený obsah:** „Bez správného klíče nemá být obsah srozumitelný.“ • „Příklad: šifrované spojení“
- **HASHOVÁNÍ — kontrolní otisk:** „Z dat vznikne krátký výstup; běžně se neobrací zpět.“ • „Příklad: kontrola integrity“

**Společná pipeline:** „text → UTF-8 → komprese → šifrování → hash šifrovaných dat“

**Otázky pro rozlišení:** „Lze převést zpět? • Je potřeba klíč? • Má být výstup menší? • Porovnáváme otisk?“

**Tři časté omyly:** „Base64 není šifrování. • ZIP není automaticky bezpečný. • Hash není zašifrovaný text.“

## Obrazová koncepce a kompozice

Dominantou je **laboratorní rozcestník jednoho stejného souboru**. Vstupní skleněný datový válec s čitelným textem se rozdělí do čtyř různě fungujících zařízení:

- kodér zachová objem podobného řádu a změní sadu symbolů; vstupní a výstupní konektor mají obousměrnou šipku bez klíče,
- kompresor složí opakující se struktury do menšího balíku; u bezeztrátového příkladu je cesta vratná, ale snímek netvrdí, že každá komprese je bezeztrátová,
- šifrovací komora vytvoří neprůhledný datový blok a zpětná cesta prochází fyzickým symbolem klíče,
- hashovací lis vytvoří krátký otisk pevné délky; šipka vede pouze ven a dva podobné vstupy mají výrazně jiné otisky.

Pod rozcestníkem je jedna reálná pipeline, která ukazuje, že se operace mohou skládat. Hashovací větev se nesmí tvářit jako další krok nutný pro každé zpracování; je uvedena jako příklad kontroly konkrétního výsledku. Vpravo dole je diagnostický panel se čtyřmi otázkami, pomocí nichž student určí účel neznámé operace.

## Vizuální metafora

Operace jsou **čtyři různé stroje ve zpracovatelské lince**: přebalování, vakuování, trezor a otisk prstu. Metafora pomáhá odlišit cíle, ale není doslovná — zejména hash není biometrický údaj a komprese nemusí vždy zachovat všechen původní obsah.

## Produkční prompt

> Vytvoř sofistikovaný český výukový snímek 16:9, 1600 × 900 px, bílý podklad, tmavě modrá horní lišta s názvem „KÓDOVÁNÍ NENÍ ŠIFROVÁNÍ“. Podnázev „Čtyři operace mění data, ale každá řeší jiný problém.“ Dominantní laboratorní rozcestník jednoho stejného datového souboru do čtyř odlišných zařízení. „KÓDOVÁNÍ — jiný zápis“ s obousměrným převodem podle známého pravidla a příklady UTF-8, Base64. „KOMPRESE — menší objem“ se zmenšeným balíkem a příklady ZIP, JPEG. „ŠIFROVÁNÍ — utajený obsah“ s neprůhledným výstupem a zpětnou cestou pouze přes klíč. „HASHOVÁNÍ — kontrolní otisk“ s krátkým výstupem a jednosměrnou šipkou, příklad kontrola integrity. Dole přesná pipeline `text → UTF-8 → komprese → šifrování → hash šifrovaných dat`. Přidej diagnostické otázky a oranžovo-červený blok „Base64 není šifrování. • ZIP není automaticky bezpečný. • Hash není zašifrovaný text.“ Velké písmo, vysoká čitelnost, funkční rozdíly vyjádřené směrem šipek, velikostí a symbolem klíče, ne pouze barvou. Bez zámků u Base64, bez odemykání hashe, bez tvrzení, že komprese vždy zachovává data, bez pseudo-textu.

## Kontrolní bod

Z diagramu musí být patrné, že kódování je vratné podle známého pravidla, dešifrování vyžaduje klíč a kryptografický hash není navržen jako vratná reprezentace původního obsahu.

---

# Snímek 3.4 — Čárové a QR kódy

## Výukový záměr

Student má pochopit QR kód jako přesně strukturovaný maticový záznam, v němž část modulů slouží orientaci, synchronizaci, formátu a opravě chyb. Současně má odlišit identifikátor výrobku v čárovém kódu od databázového záznamu a kód od důvěryhodnosti jeho obsahu.

**Hlavní otázka:** Co všechno čtečka potřebuje, než z mozaiky získá skutečná data?

**Nosná teze:** Strojově čitelný kód není náhodný obraz ani automaticky databáze; nese data i strukturu potřebnou ke spolehlivému přečtení.

## Přesné texty na snímku

**Název:** UVNITŘ QR KÓDU

**Podnázev:** Ne každý modul nese obsah — část vzoru pomáhá kód najít, přečíst a opravit.

**Funkční vrstvy QR:**

- **ORIENTACE:** „výrazné poziční značky určují natočení“
- **SYNCHRONIZACE:** „pravidelný vzor pomáhá určit mřížku“
- **FORMÁT A MASKA:** „říkají, jak data správně interpretovat“
- **DATA:** „text, URL nebo strukturovaný obsah“
- **OPRAVA CHYB:** „redundance pomáhá obnovit část poškozeného kódu“

**Čárový kód v obchodě:** „EAN obvykle nese identifikátor → databáze dohledá název a cenu.“

**Blok REDUNDANCE:** „Nadbytečné údaje nejsou vždy plýtvání. Mohou umožnit opravu chyb.“

**Bezpečnostní blok:** „QR kód může obsahovat nebezpečný odkaz. Před otevřením zkontroluj cílovou adresu.“

**Blok POZOR:** „Černý modul není jednoduše vždy ‚1‘ s přímým významem. Výsledný vzor vzniká kódováním a maskováním.“

## Obrazová koncepce a kompozice

Dominantou je **precizní explodovaný řez skutečně působícím QR kódem**. Základní černobílá matice zůstává uprostřed a nad ní se v mírném izometrickém odsazení oddělí barevně i tvarem označené funkční vrstvy: tři poziční značky v rozích, časovací linie, pás formátových informací, oblast dat a šrafované oblasti redundantních opravných symbolů. Nepředstírat přesnou mapu konkrétního vygenerovaného QR obsahu, pokud není skutečně vypočtena; panel má být jasně označen jako funkční schéma.

Přes levou hranu snímku probíhá čtecí proces: kamera zachytí kód nakřivo, algoritmus podle tří rohů narovná perspektivu, obnoví mřížku, přečte funkční informace a teprve potom dekóduje obsah. Jeden roh kódu je realisticky poškozen; z poškození vedou šrafované vazby k opravným datům a následně k úspěšně obnovenému textu. Neuvádět univerzální procento opravitelného poškození, protože závisí na verzi, úrovni opravy a umístění vady.

Ve spodním pásu je menší kontrast s EAN: paprsek přečte čáry, získá identifikační číslo a síťová šipka vede do databáze obchodu, odkud se vrátí název a cena. Vpravo dole je realistický náhled domény před otevřením QR odkazu.

## Vizuální metafora

QR kód je **mapa s orientačními body, souřadnicovou sítí, nákladem a záchrannou rezervou**. Metafora vysvětluje funkční rozdělení, ale nesmí naznačit, že jsou všechny oblasti u každého QR kódu rozmístěny do jednoduchých souvislých barevných bloků.

## Produkční prompt

> Vytvoř profesionální český výukový snímek 16:9, 1600 × 900 px, na bílém pozadí s tmavě modrou horní lištou. Název „UVNITŘ QR KÓDU“, podnázev „Ne každý modul nese obsah — část vzoru pomáhá kód najít, přečíst a opravit.“ Dominantní explodovaný funkční řez QR kódem označený jako schéma. Zřetelně rozliš „ORIENTACE“, „SYNCHRONIZACE“, „FORMÁT A MASKA“, „DATA“ a „OPRAVA CHYB“ tvarem, šrafou a střídmou barvou. Vlevo ukaž skutečný čtecí proces: šikmý záběr kamerou → nalezení tří pozičních značek → narovnání perspektivy a mřížky → přečtení formátu → dekódování dat. Část kódu je poškozená a opravená díky redundanci, bez tvrzení o univerzálním procentu obnovy. Dole kontrast `EAN identifikátor → databáze obchodu → název a cena`. Přidej bezpečnostní kontrolu cílové adresy a varování, že černý modul není vždy prostá jednička s přímým významem. Akademicko-technická estetika, přesná mřížka, velké české písmo. Bez log komerčních skenerů, bez falešného QR kódu, který má údajně vést na skutečný web, bez pseudo-textu a bez barevné mapy vydávané za přesný standardizovaný layout každého QR.

## Kontrolní bod

Tři poziční značky musejí být v odpovídajících třech rozích, čtecí proces musí nejprve určit geometrii a teprve potom obsah a poškození nesmí zakrýt tvrzení, že opravitelnost má vždy pevné procento.

---

# Snímek 3.5 — ASCII, Unicode a UTF-8

## Výukový záměr

Student má odlišit znak, kódový bod a konkrétní bajtovou reprezentaci. Má pochopit, že Unicode určuje identitu znaku, zatímco UTF-8 určuje způsob jeho uložení, a že stejné bajty dekódované nesprávným kódováním mohou vytvořit poškozený text.

**Hlavní otázka:** Jak se znak `á` promění na bajty `C3 A1` a znovu na správný obrazovkový znak?

**Nosná teze:** Znak není bajt; mezi významem znaku, jeho kódovým bodem, uložením a vykreslením existují odlišné vrstvy.

## Přesné texty na snímku

**Název:** ZNAK NENÍ BAJT

**Podnázev:** Unicode určuje znak. UTF-8 určuje, jak jej uložit do bajtů.

**Hlavní tok:**

1. **ZNAK:** `á`
2. **KÓDOVÝ BOD UNICODE:** `U+00E1`
3. **KÓDOVÁNÍ UTF-8:** `C3 A1`
4. **DEKÓDOVÁNÍ:** `C3 A1 → U+00E1`
5. **VYKRESLENÍ FONTEM:** `á`

**Kompatibilita ASCII:** „ASCII má 128 kódových hodnot. Základní znaky ASCII používají v UTF-8 jeden bajt.“

**Srovnání délky:** `A → U+0041 → 41` • `á → U+00E1 → C3 A1`

**Blok CHYBNÉ KÓDOVÁNÍ:** „Správné bajty + nesprávný dekodér = nesmyslné znaky.“

**Konec řádku:** „Unix a dnešní macOS: LF • Windows: CRLF • historický Classic Mac OS: CR“

**Escape sekvence:** „`\n` je zápis se zvláštním významem v syntaxi programu, ne nový znakový standard.“

**Blok POZOR:** „‚Extended ASCII‘ není jeden univerzální standard. Různé osmibitové tabulky se mohou lišit.“

## Obrazová koncepce a kompozice

Dominantou je **průhledný datový tunel pro jediný znak `á`**. Vlevo stojí znak jako abstraktní typografický objekt, ne jako obrázek uložený v paměti. První kontrolní brána mu přiřadí identitu `U+00E1`. Druhá brána označená UTF-8 jej zabalí do dvou osmibitových kontejnerů `C3` a `A1`. Na pravé straně proběhne opačný proces: dekodér obnoví kódový bod a font vytvoří konkrétní glyf na obrazovce.

Pod hlavním tunelem vede paralelní tenká trasa znaku `A`: `A → U+0041 → 41`. Její jediný bajt vizuálně vysvětluje kompatibilitu UTF-8 s ASCII bez dojmu, že všechny znaky zabírají stejně místa. Uprostřed dole se tok rozdvojí: správný dekodér vrací `á`, nesprávně zvolená osmibitová tabulka vytvoří typickou poškozenou dvojici znaků. Chybný výstup není třeba konkretizovat, pokud by generátor mohl vytvořit další nesmyslný text; stačí jasný rozpad a značka „chybné dekódování“.

Pravý dolní roh obsahuje úzkou časovou osu konce řádku LF/CRLF a malý výřez zdrojového kódu s `\n`. Tyto prvky zůstávají vedlejší a nesmějí konkurovat hlavnímu rozlišení Unicode/UTF-8/font.

## Vizuální metafora

Unicode je **adresa položky v katalogu**, UTF-8 je **způsob zabalení této adresy do bajtových balíčků** a font je **výrobní šablona výsledného tvaru**. Metafora má limit: Unicode není jedna fyzická kniha znaků a glyf se může lišit podle fontu, aniž by se změnil kódový bod.

## Produkční prompt

> Vytvoř přesný český výukový snímek 16:9, 1600 × 900 px, světlé pozadí a tmavě modrá horní lišta s názvem „ZNAK NENÍ BAJT“. Podnázev „Unicode určuje znak. UTF-8 určuje, jak jej uložit do bajtů.“ Dominantní průhledný datový tunel: `ZNAK á → KÓDOVÝ BOD UNICODE U+00E1 → KÓDOVÁNÍ UTF-8 C3 A1 → DEKÓDOVÁNÍ C3 A1 → U+00E1 → VYKRESLENÍ FONTEM á`. Přesně odděl identitu znaku, bajty a výsledný glyf. Pod hlavní osou kratší srovnání `A → U+0041 → 41` a `á → U+00E1 → C3 A1`, aby bylo zřejmé, že UTF-8 má proměnnou délku a ASCII znaky používají jeden bajt. Přidej rozvětvení „Správné bajty + nesprávný dekodér = nesmyslné znaky“, blok o 128 hodnotách ASCII, stručný pás `Unix a dnešní macOS: LF • Windows: CRLF • historický Classic Mac OS: CR` a detail `\n` jako escape sekvence, nikoli nový standard. Varování: „‚Extended ASCII‘ není jeden univerzální standard.“ Velké monospace kódy, přesná velikost písmen a mezery. Bez mapy vlajek, bez tvrzení, že Unicode je font, bez ukládání znaku jako obrázku, bez pseudo-textu a zkomolené diakritiky.

## Kontrolní bod

Tok musí obsahovat přesnou dvojici `U+00E1` a `C3 A1`. Unicode, UTF-8 a font musejí být tři odlišné vrstvy; nesmí se tvrdit, že znak `á` má vždy dva bajty ve všech kódováních.

---

# Snímek 3.6 — Jak počítač ukládá celá čísla

## Výukový záměr

Student má pochopit, že bitový vzor pevné délky získává význam až spolu s datovým typem. Na osmibitovém příkladu má rozlišit unsigned a signed rozsah, princip dvojkového doplňku a přetečení přes hranici reprezentovatelného rozsahu.

**Hlavní otázka:** Jak může bitový vzor `11111111` znamenat 255 i −1?

**Nosná teze:** Bity samy nenesou znaménko ani datový typ; pravidlo interpretace určuje hodnotu a pevná šířka omezuje rozsah.

## Přesné texty na snímku

**Název:** BITY NEMAJÍ VROZENÝ VÝZNAM

**Podnázev:** Stejných osm bitů lze číst různě podle datového typu.

**Středový bitový vzor:** `11111111`

**Dvě interpretace:**

- **8bit unsigned:** `11111111₂ = 255` • rozsah `0 až 255`
- **8bit signed, dvojkový doplněk:** `11111111₂ = −1` • rozsah `−128 až +127`

**Vznik −5:**

`+5 = 00000101`

`invertuj bity → 11111010`

`přičti 1 → 11111011 = −5`

**Počet kombinací:** „8 bitů → `2⁸ = 256` bitových vzorů“

**Přetečení:** `127 + 1 → 10000000₂ → −128` „v osmibitovém dvojkovém doplňku“

**Blok KONTEXT:** „`11111111` může být také část barvy, instrukce nebo jiných dat.“

**Blok POZOR:** „Konkrétní chování overflow závisí na jazyku a prostředí. `int` nemá všude stejnou šířku.“

## Obrazová koncepce a kompozice

Dominantou je **osmibitový kruhový číselník se dvěma vyměnitelnými stupnicemi**. Uvnitř rotuje jediný prstenec 256 bitových stavů; vnější modrá stupnice jej čte jako unsigned od 0 do 255, vnitřní tyrkysová stupnice jako signed od 0 do 127 a dále od −128 do −1. Bitový stav `11111111` je zvýrazněn a dvě čisté vodicí čáry ukazují na 255 a −1. Diagram tím zabrání dojmu, že se bity při změně datového typu přepisují.

Na levé straně je svislý mikroskopický postup tvorby `−5`: osm mechanických přepínačů nejprve ukazuje `00000101`, potom se všechny překlopí a nakonec binární sčítačka přidá jedna. Na pravé straně se detail kruhu přiblíží k hranici 127: přidání jedné posune ukazatel na další bitový stav `10000000`, který signed stupnice čte jako −128. Přechod je označen jako model osmibitového dvojkového doplňku, nikoli univerzální chování každého programu.

Ve spodním pásu je jedna průhledná „typová čočka“ nad vzorem `11111111`: při průchodu čočkou unsigned se zobrazí číslo, při signed jiná hodnota a při RGB malý barevný kanál. Metafora typové čočky doplňuje, ale neopakuje hlavní kruhový model.

## Vizuální metafora

Datový typ je **stupnice nasazená na stejný číselník**. Bitový prstenec je fyzicky stejný, ale popisky stupnice určují interpretaci. Kruhový tvar přesně ukazuje modulární aritmetiku pevné šířky, ale varování musí přiznat, že reakci programu na overflow určuje jazyk a běhové prostředí.

## Produkční prompt

> Navrhni profesionální český infografický snímek 16:9, 1600 × 900 px, bílé pozadí, tmavě modrá horní lišta s názvem „BITY NEMAJÍ VROZENÝ VÝZNAM“. Podnázev „Stejných osm bitů lze číst různě podle datového typu.“ Dominantní osmibitový kruhový číselník s jedním prstencem 256 bitových stavů a dvěma přesnými stupnicemi. Zvýrazni `11111111`; unsigned stupnice jej čte jako `255` s rozsahem `0 až 255`, signed stupnice v dvojkovém doplňku jako `−1` s rozsahem `−128 až +127`. Vlevo přesný tříkrokový vznik `−5`: `+5 = 00000101`, `invertuj bity → 11111010`, `přičti 1 → 11111011 = −5`. Vpravo zvětšený přechod `127 + 1 → 10000000₂ → −128` výslovně označený „v osmibitovém dvojkovém doplňku“. Přidej `8 bitů → 2⁸ = 256 bitových vzorů`, typovou čočku ukazující další možný kontext a varování o jazyku, prostředí a šířce typu `int`. Přesné bity, monospace písmo, šipky pouze pro skutečné operace. Bez samostatného znaménkového bitu vydávaného za dvojkový doplněk, bez rozsahu −127 až +127, bez tvrzení, že každý overflow se vždy přetočí, a bez pseudo-textu.

## Kontrolní bod

Rozsahy musí být přesně `0 až 255` a `−128 až +127`. Transformace `00000101 → 11111010 → 11111011` musí zůstat osmibitová a přetečení musí být označeno jako konkrétní osmibitový model, ne obecná záruka jazyka.

---

# Snímek 3.7 — Čísla s plovoucí řádovou čárkou

## Výukový záměr

Student má pochopit floating point jako konečnou síť reprezentovatelných hodnot s velkým rozsahem, ale omezenou přesností. Má rozlišit znaménko, exponent a significand, pochopit binární aproximaci desetinného čísla `0,1` a znát praktický důvod, proč se pro přesné peněžní výpočty používají jiné reprezentace.

**Hlavní otázka:** Proč může počítač spočítat `0.1 + 0.2` jako hodnotu nepatrně odlišnou od `0.3`?

**Nosná teze:** Floating point neukládá všechna reálná čísla; ukládá nejbližší bod konečné binární sítě a mezery mezi body se mění s měřítkem.

## Přesné texty na snímku

**Název:** MEZI ČÍSLY JSOU MEZERY

**Podnázev:** Floating point nabízí velký rozsah, ale jen konečnou síť reprezentovatelných hodnot.

**Anatomie zápisu:** **ZNAMÉNKO | EXPONENT | SIGNIFICAND**

**Význam částí:**

- **ZNAMÉNKO:** „kladná nebo záporná hodnota“
- **EXPONENT:** „měřítko — posouvá rozsah“
- **SIGNIFICAND:** „významné číslice — určuje přesnost“

**Příklad aproximace:** „`0,1₁₀` nemá v běžném binárním floating pointu konečný přesný zápis.“

**Možný výsledek:** `0.1 + 0.2 → 0.30000000000000004`

**Dvě velikosti:** „binary32: 32 bitů • binary64: 64 bitů“

**Praktický důsledek:** „Pro přesné měnové částky použij například celé nejmenší jednotky nebo vhodný desítkový typ.“

**Blok POROVNÁVÁNÍ:** „U přibližných výpočtů často neporovnáváme na přesnou rovnost, ale s přiměřenou tolerancí.“

**Blok POZOR:** „Dlouhý desetinný výsledek není porucha procesoru. Je to viditelný důsledek konečné binární reprezentace.“

## Obrazová koncepce a kompozice

Dominantou je **několikanásobná lupa nad číselnou osou**. První široká osa ukazuje obrovský rozsah od velmi malých k velmi velkým hodnotám. Druhá lupa přiblíží okolí nuly, kde jsou reprezentovatelné body husté. Třetí lupa se posune k větší absolutní hodnotě, kde jsou při stejné bitové přesnosti mezery mezi sousedními body větší. Nezobrazovat body v lineárním měřítku tak, aby působily rovnoměrně po celé ose.

V centru je desetinné `0,1` jako oranžový cíl mezi dvěma sousedními modrými body. Převodník jej musí přiřadit k bližšímu reprezentovatelnému bodu; velmi tenká úsečka označuje „chybu zaokrouhlení“. Dva takto aproximované vstupy `0.1` a `0.2` vstoupí do sčítačky a lupa nad výsledkem ukáže, že získaný bod neleží nutně přesně na matematickém `0.3`.

Nahoře pod titulkem je jeden čistý 32bitový pás rozdělený do tří nestejně velkých polí „znaménko | exponent | significand“. Snímek nemusí uvádět přesné počty bitů jednotlivých polí, pokud by to odvádělo od obecného principu; pokud je uvede, musejí odpovídat konkrétnímu formátu binary32. Vpravo dole je praktická pokladní účtenka: částka v korunách se převede na celé haléře nebo do desítkového typu. Vlevo dole je srovnání binary32 a binary64 jako dvou sítí, přičemž binary64 má obecně větší přesnost a rozsah, nikoli „dvojnásobně správné“ výsledky.

## Vizuální metafora

Floating point je **síť kotevních bodů na číselné ose**. Skutečná hodnota se musí přichytit k nejbližšímu dostupnému bodu; exponent mění měřítko sítě a significand určuje její jemnost. Metafora má limit: skutečné formáty IEEE 754 zahrnují i zvláštní hodnoty a pravidla, která tento úvodní panel záměrně nezobrazuje.

## Produkční prompt

> Vytvoř precizní český výukový snímek 16:9, 1600 × 900 px, na bílém pozadí, s tmavě modrou horní lištou. Název „MEZI ČÍSLY JSOU MEZERY“, podnázev „Floating point nabízí velký rozsah, ale jen konečnou síť reprezentovatelných hodnot.“ Dominantní několikanásobná lupa nad číselnou osou: široký rozsah, husté body u malých hodnot a větší mezery při větším měřítku. Oranžový cíl `0,1₁₀` leží mezi dvěma sousedními reprezentovatelnými body a je přiřazen k bližšímu; tenká úsečka označuje chybu zaokrouhlení. Ukaž, jak aproximace `0.1` a `0.2` vstoupí do sčítačky a mohou dát zobrazený výsledek `0.30000000000000004`, který leží nepatrně vedle matematického `0.3`. Nahoře technický bitový pás `ZNAMÉNKO | EXPONENT | SIGNIFICAND` s krátkými významy jednotlivých částí. Přidej `binary32: 32 bitů • binary64: 64 bitů`, blok o porovnání s tolerancí a praktický příklad měny uložené v celých nejmenších jednotkách nebo vhodném desítkovém typu. Varování vysvětluje, že nejde o poruchu procesoru. Čistá vědecká estetika, výrazné zvětšovací rámečky, velké písmo. Bez běžné rovnoměrné pravítkové stupnice vydávané za floating point, bez tvrzení, že všechny desetinné hodnoty jsou nepřesné, bez záměny exponentu a significandu a bez pseudo-textu.

## Kontrolní bod

Musí být zřejmé, že `0,1` je aproximováno nejbližším dostupným bodem a že hustota bodů není po celé číselné ose konstantní. Snímek nesmí tvrdit, že každý jazyk vždy vypíše uvedený dlouhý výsledek stejným způsobem.

---

# Poznámka k návaznosti série

Sedm snímků zachovává vizuální podpis předchozích lekcí, ale každý používá jiný vysvětlující mechanismus:

| Téma | Hlavní forma | Praktická situace | Co má student z obrazu vyčíst |
| --- | --- | --- | --- |
| 3.1 Číselné soustavy | poziční váhový stroj | hexadecimální zápis technických dat | základ mění zápis, nikoli hodnotu |
| 3.2 Převody | dílna se třemi nástroji | RGB barva `#FF8000` | metoda závisí na směru převodu |
| 3.3 Čtyři datové operace | laboratorní rozcestník | postupné zpracování souboru | účel operace je důležitější než vzhled výstupu |
| 3.4 Čárové a QR kódy | explodovaný funkční řez | sken produktu a QR odkazu | kód obsahuje data, čtecí strukturu i redundanci |
| 3.5 ASCII, Unicode, UTF-8 | datový tunel znaku | uložení českého `á` | znak, kódový bod, bajty a glyf nejsou totéž |
| 3.6 Celá čísla | dvojitá stupnice na bitovém kruhu | osmibitové signed/unsigned hodnoty | význam bitů určuje typ a šířka omezuje rozsah |
| 3.7 Floating point | mapa kotevních bodů s lupou | desetinný výpočet a měna | velký rozsah je vykoupen konečnou přesností |

Kapitola postupuje od zápisu celočíselné hodnoty přes obecné formy kódování až k tomu, jak datové typy interpretují bitové vzory. Při generování je nutné zvlášť kontrolovat aritmetiku převodů, přesnou podobu Unicode a UTF-8 zápisů, rozsahy osmibitových typů a vizuálně pravdivé znázornění nerovnoměrné přesnosti floating pointu.
