# Scénáře infografických snímků — 6. lekce

## Práce s informacemi

Sada pro témata 6.1–6.6 z výukového textu *Základy informatiky*. Každý scénář je samostatné zadání pro grafika, prezentační nástroj i generátor obrazu. Všechny texty určené přímo na snímek jsou uvedeny v přesném znění; delší formulace lze při generování obrazu vysázet dodatečně v prezentačním editoru.

## Společný vizuální rámec série

- Formát 16:9, ideálně 1600 × 900 px; bílé až velmi světle šedé pozadí, bezpečný okraj minimálně 40 px.
- Profesionální akademicko-technologický styl pro studenty střední školy. Bez infantilních detektivů, kreslených žárovek, kýčovitých mozkových motivů, falešných pečetí „ověřeno“, neonového sci-fi rozhraní a dekorativního zahlcení.
- Tmavě modrá horní lišta, velké bílé bezpatkové písmo s českou diakritikou. Nadpis přibližně 44–54 px, podnadpis 25–30 px, běžný text nejméně 22–24 px.
- Paleta navazuje na předchozí lekce: námořnická modř pro strukturu, střední modř pro informaci, tyrkysová pro ověřený vztah a návaznost, oranžová pro otázku či rozhodnutí, červená pouze pro riziko, neověřený skok nebo citlivá data.
- Zdroj, tvrzení, důkaz a závěr odlišovat nejen barvou, ale i tvarem: dokument, výroková karta, datový vzorek a výsledná syntéza. Šipky používat jen pro skutečný původ, převzetí, transformaci nebo ověření.
- Jeden dominantní vysvětlující mechanismus na snímek, maximálně pět vedlejších obsahových bloků. Každý snímek musí ukázat rozhodovací nebo ověřovací proces, nikoli pouze seznam doporučení.
- Reálné stránky, platformy a vyhledávače zobrazovat pouze jako neutrální rozhraní bez log a ochranných známek. Nepoužívat vymyšlené studie, statistiky, citace ani univerzální bodové skóre důvěryhodnosti.
- Pokud obrazový generátor nezvládá přesnou českou sazbu, bibliografický zápis nebo symboly, vytvořit vizuál s rezervovanými plochami a text doplnit až v editoru. Nevkládat pseudo-text, falešná loga ani vodoznaky.

---

# Snímek 6.1 — Od problému k informační potřebě

## Výukový záměr

Student má pochopit, že kvalitní vyhledávání nezačíná zadáním slov do vyhledávače, ale formulací problému, otázky a potřebného důkazu. Má umět rozložit široké téma na konkrétní dílčí otázky a podle cíle zvolit vhodný typ zdroje. Má také vědět, že plynulá odpověď AI nemůže napravit vágní nebo špatně položenou otázku.

**Hlavní otázka:** Jak proměnit neurčité téma v otázku, na kterou lze získat použitelnou odpověď?

**Nosná teze:** Nejprve určujeme, co potřebujeme rozhodnout a jaký důkaz by odpověď podpořil; teprve potom hledáme.

## Přesné texty na snímku

**Název:** NEZAČÍNEJ VYHLEDÁVAČEM

**Podnázev:** Dobré hledání začíná otázkou a představou, jak bude vypadat dostatečný důkaz.

**Hlavní navigační tok:**

- **1 PROBLÉM** — „Co potřebuji pochopit nebo rozhodnout?“
- **2 OTÁZKA** — „Jaké konkrétní tvrzení má odpověď obsahovat?“
- **3 DŮKAZ** — „Co by odpověď skutečně podpořilo?“
- **4 TYP ZDROJE** — „Kde takový důkaz pravděpodobně vzniká?“
- **5 DOTAZ** — „Jaké pojmy, kontext a omezení použiji?“

**Rozpad širokého tématu `IPv6`:**

- „Proč bylo IPv6 navrženo?“ → **historický a technický kontext**
- „Jak se zapisuje adresa?“ → **specifikace nebo kvalitní výklad**
- „Jak probíhá zavádění vedle IPv4?“ → **aktuální dokumentace a případové studie**

**Vzorec dobrého dotazu:** `hlavní pojem + kontext + omezení`

**Příklad:** `generativní AI + střední škola + ochrana osobních údajů + doporučení`

**Blok DŮKAZ PODLE ÚČELU:** „Přesné znění hledáme v původním dokumentu, princip v kvalitním výkladu a aktuální cenu v současném zdroji.“

**Blok POZOR:** „Plynulá odpověď na vágní otázku může znít přesvědčivě, ale stále řešit jiný problém.“

## Obrazová koncepce a kompozice

Dominantou je **navigační trychtýř kombinovaný s plánovacím stolem**. Vlevo přichází široký, mlhavý oblak s kartou `Zjisti něco o IPv6`. Trychtýř jej nepřevádí přímo na výsledky, ale postupně do pěti ostře vymezených stanic: problém, otázka, důkaz, typ zdroje a dotaz. Každá stanice fyzicky zužuje prostor možností a zpřesňuje tvar výstupní karty. Poslední karta obsahuje konkrétní dotaz, vedle něhož jsou tři prázdné „zásuvky“ pro různé typy zdrojů.

V pravé polovině se jeden pojem `IPv6` rozvětví do tří rozdílných misí. Každá má jinou ikonu cíle a jinou trasu: historický důvod míří ke kontextové časové ose, zápis adresy k technické specifikaci a nasazení vedle IPv4 k aktuální dokumentaci a případovým studiím. Nezobrazovat jeden univerzální „nejlepší zdroj“.

Dole probíhá tenká **kalibrační linka důkazu**. Na ní jsou tři úkoly — ověřit přesné znění, pochopit princip, zjistit aktuální hodnotu — a pod nimi odpovídající typ zdroje. Vedle je malý vstup do AI: stejný vágní oblak vstoupí do modelu a vyjde jako uhlazený odstavec, ale oranžový obrys upozorní, že nejasná otázka zůstala nejasná. AI zde není karikována jako lhář; problémem je nedostatečně specifikované zadání a chybějící důkazní kritérium.

## Vizuální metafora

Informační potřeba je **plán cesty před zadáním cíle do navigace**. Nestačí napsat název oblasti; musíme vědět, kam přesně míříme a podle čeho poznáme, že jsme dorazili. Limit metafory: při skutečném hledání se otázka může po prvních zjištěních oprávněně změnit a celý proces se může vracet o krok zpět.

## Produkční prompt

> Vytvoř profesionální český výukový infografický snímek 16:9, 1600 × 900 px, na bílém až velmi světle šedém pozadí. Nahoře tmavě modrá lišta s názvem „NEZAČÍNEJ VYHLEDÁVAČEM“ a podnázev „Dobré hledání začíná otázkou a představou, jak bude vypadat dostatečný důkaz.“ Dominantní navigační trychtýř s pěti jasnými stanicemi `1 PROBLÉM → 2 OTÁZKA → 3 DŮKAZ → 4 TYP ZDROJE → 5 DOTAZ`; zleva vstupuje mlhavá karta `Zjisti něco o IPv6`, vpravo vychází konkrétní vyhledávací zadání. Vedle rozvětvi pojem `IPv6` do tří rozdílných otázek: proč vzniklo, jak se zapisuje adresa, jak se zavádí vedle IPv4; každá vede k jinému typu zdroje. Dole ukaž vzorec `hlavní pojem + kontext + omezení` a příklad `generativní AI + střední škola + ochrana osobních údajů + doporučení`. Přidej blok „DŮKAZ PODLE ÚČELU“ a varování, že plynulá odpověď na vágní otázku může řešit jiný problém. Modro-tyrkysový technický styl, oranžová pro rozhodovací body, velké české písmo, dostatek volného prostoru. Bez log vyhledávačů, bez univerzálního zdroje pro všechny otázky, bez dojmu lineárního procesu bez možnosti návratu a bez pseudo-textu.

## Kontrolní bod

Pořadí musí být přesně `problém → otázka → potřebné důkazy → vhodný typ zdroje → konkrétní dotaz`. Snímek nesmí tvrdit, že formulace klíčových slov sama zaručí správnou odpověď nebo že jeden druh zdroje je nejlepší pro všechny informační potřeby.

---

# Snímek 6.2 — Typy zdrojů a původ informace

## Výukový záměr

Student má rozlišit primární, sekundární a terciární zdroj podle jejich vztahu ke vzniku informace, nikoli podle automatického žebříčku kvality. Má chápat provenanci jako dohledatelný původ a historii informace a rozpoznat, že mnoho článků může pouze přebírat jedno původní tvrzení. Má vědět, že metadata pomáhají s orientací, ale nejsou sama o sobě nezfalšovatelným důkazem.

**Hlavní otázka:** Kolik nezávislých zdrojů skutečně máme a odkud jejich tvrzení pochází?

**Nosná teze:** Počet nalezených stránek není počet nezávislých důkazů; rozhoduje původ, způsob převzetí a vazba na původní materiál.

## Přesné texty na snímku

**Název:** SLEDUJ PŮVOD, NE POČET KOPIÍ

**Podnázev:** Deset webů může opakovat jediné tvrzení z jednoho původního zdroje.

**Tři vrstvy zdrojů:**

- **PRIMÁRNÍ** — „původní studie, datová sada, specifikace, zákon nebo záznam“
- **SEKUNDÁRNÍ** — „vysvětluje, analyzuje nebo porovnává primární materiál“
- **TERCIÁRNÍ** — „shrnuje širší oblast a pomáhá s orientací“

**Provenanční stopa:** `vznik → autor / instituce → metoda → verze → převzetí → úpravy`

**Příklad jedné statistiky:**

- `1 tisková zpráva`
- `5 přebírajících článků`
- `1 původ tvrzení, nikoli 5 nezávislých studií`

**Metadata, která hledáme:** „autor • datum • verze • vydavatel • metoda • aktualizace“

**Blok VHODNOST ≠ BLÍZKOST:** „Primární zdroj bývá nejblíže vzniku informace, ale kvalitní výklad může být vhodnější pro pochopení.“

**Blok POZOR:** „Metadata jsou stopa, ne razítko pravosti. Mohou chybět, být změněna nebo nepopisovat celý kontext.“

## Obrazová koncepce a kompozice

Dominantou je **provenanční rodokmen jedné informace**, který se čte zprava doleva. Na pravé straně je pět vizuálně různých webových karet se stejnou statistikou. Jejich tenké linky se postupně sbíhají: tři články přebírají jeden agregátor, dva odkazují přímo, ale všechny cesty nakonec vedou k jediné marketingové tiskové zprávě. Pod kořenem je výrazný štítek `1 původ tvrzení`. Struktura nesmí působit jako pět nezávislých potvrzení.

V levé třetině stojí **třípatrový řez knihovnou zdrojů**. Dole je primární materiál — datová tabulka, specifikace a původní záznam. Nad ním sekundární analýza s viditelnými odkazy dolů. Nahoře terciární přehled propojující více větví. Patra nejsou označena medailemi ani pořadím kvality; každé má jinou funkci a jinou vzdálenost od vzniku informace.

Uprostřed vede od původního dokumentu **časová provenanční stopa**: autor nebo instituce, metoda, datum, verze, pozdější převzetí a úprava. Jednotlivé uzly jsou zobrazeny jako dohledatelné záznamy, nikoli jako automatické potvrzení správnosti. Malá lupa nad metadaty ukazuje, co lze zjistit, zatímco otevřený zámek připomíná, že metadata lze měnit.

## Vizuální metafora

Původ informace je **rodokmen nebo tok vody k prameni**. Mnoho výtoků může být napájeno jediným potrubím; jejich počet proto neznamená více nezávislých pramenů. Limit metafory: nejstarší či původní zdroj nemusí být bezchybný a nezávislé zdroje mohou oprávněně pracovat se stejnými veřejnými daty.

## Produkční prompt

> Navrhni profesionální český infografický snímek 16:9, 1600 × 900 px, bílé pozadí a tmavě modrá horní lišta. Přesný název „SLEDUJ PŮVOD, NE POČET KOPIÍ“ a podnázev „Deset webů může opakovat jediné tvrzení z jednoho původního zdroje.“ Dominantní provenanční rodokmen: vpravo pět neutrálních webových karet se stejnou statistikou, jejich odkazy se sbíhají k jedné marketingové tiskové zprávě; výrazný závěr `1 původ tvrzení, nikoli 5 nezávislých studií`. Vlevo třípatrový řez zdroji „PRIMÁRNÍ“, „SEKUNDÁRNÍ“, „TERCIÁRNÍ“ s jejich přesnými funkcemi, bez medailí a bez žebříčku kvality. Uprostřed časová stopa `vznik → autor / instituce → metoda → verze → převzetí → úpravy`. Přidej metadata „autor • datum • verze • vydavatel • metoda • aktualizace“, blok „VHODNOST ≠ BLÍZKOST“ a upozornění, že metadata nejsou razítko pravosti. Modro-tyrkysová akademicko-technická estetika, oranžová pro přebírání, velká česká typografie. Bez skutečných log, bez tvrzení, že primární zdroj je automaticky nejlepší nebo pravdivý, bez počítání kopií jako nezávislých důkazů a bez pseudo-textu.

## Kontrolní bod

Všechny kopie ve scénáři musejí vést k jednomu původnímu zdroji a snímek je nesmí počítat jako nezávislá potvrzení. Primární, sekundární a terciární zdroj musejí být popsány podle funkce a vzdálenosti od vzniku informace, nikoli jako univerzální pořadí důvěryhodnosti.

---

# Snímek 6.3 — Jak poznat kvalitní informaci

## Výukový záměr

Student má hodnotit konkrétní informaci souběžně podle původu, důkazů, aktuálnosti, účelu, nezávislosti a relevance. Má pochopit, že profesionální vzhled, autor, doména nebo první místo ve vyhledávání nejsou samy o sobě důkazem správnosti. Nemá mechanicky sečíst „kladné znaky“, ale posoudit, zda zdroj skutečně podporuje dané tvrzení pro danou otázku.

**Hlavní otázka:** Jak posoudit informaci bez falešného univerzálního skóre důvěryhodnosti?

**Nosná teze:** Kvalita není jedna vlastnost zdroje; vzniká ze vztahu mezi tvrzením, důkazy, metodou, časem, účelem a konkrétní otázkou.

## Přesné texty na snímku

**Název:** DŮVĚRYHODNOST NENÍ JEDNO RAZÍTKO

**Podnázev:** Ptej se, zda konkrétní zdroj podpírá konkrétní tvrzení pro tvůj účel.

**Šest diagnostických čoček:**

- **PŮVOD** — „Kdo informaci zveřejnil a má vztah k tématu?“
- **DŮKAZY** — „Na jakých datech, metodě nebo dokumentaci tvrzení stojí?“
- **AKTUÁLNOST** — „Je datum přiměřené rychlosti změn tématu?“
- **ÚČEL** — „Informovat, prodávat, přesvědčovat, bavit, nebo získat pozornost?“
- **NEZÁVISLOST** — „Je přiznán střet zájmů a existuje nezávislé potvrzení?“
- **RELEVANCE** — „Odpovídá zdroj stejné populaci, období a otázce?“

**Tři vrstvy sdělení:** `FAKT • INTERPRETACE • NEJISTOTA`

**Příklad relevance:** „Kvalitní studie o jiné skupině nebo jiném období nemusí odpovědět na naši otázku.“

**Blok NESTAČÍ SAMO O SOBĚ:** „profesionální vzhled • známá doména • uvedený autor • vysoké pořadí ve výsledcích“

**Blok POZOR:** „Checklist pomáhá klást otázky. Mechanické skóre však může zakrýt zásadní slabinu v metodě nebo relevanci.“

## Obrazová koncepce a kompozice

Dominantou je **diagnostická laboratoř jednoho konkrétního tvrzení**. Uprostřed leží karta s neutrálním výrokem `Nová metoda zlepší výsledek o X %`; hodnota X zůstává záměrně symbolická, aby se nevytvářela falešná studie. Kartu současně osvětluje šest fyzicky odlišných analytických čoček: identifikační štítek původu, průhled do dat a metody, časová osa, mapa motivace, síť vlastnických či finančních vazeb a překryv s cílovou populací. Každá čočka odhaluje jiný rozměr a žádná sama nerozsvítí zelenou pečeť „pravda“.

Vpravo je malá **kontrastní dvojice**. První zdroj vypadá profesionálně, ale po odklopení fasády chybí metoda a data. Druhý je vizuálně střídmý, ale má dohledatelného autora, popsaný postup, zdroje a omezení. Cílem není tvrdit, že nehezký web je důvěryhodný; snímek pouze oddělí vzhled od důkazní kvality.

Dole je horizontální karta relevance. Stejná studie se posune mezi poli `jiná populace`, `jiné období`, `jiný problém` a `naše otázka`. Překryv ukazuje, že obecně kvalitní výzkum může být pro konkrétní závěr nepoužitelný. Vedle jsou tři vrstvy sdělení — fakt, interpretace a nejistota — zobrazené odlišným tvarem, aby se při čtení neslily.

## Vizuální metafora

Hodnocení informace je **diagnostika systému více senzory**. Teploměr, rentgen a laboratorní test měří různé vlastnosti; jeden pěkný údaj nenahrazuje celý obraz. Limit metafory: výsledkem není objektivní číslo „důvěryhodnosti“, ale zdůvodněný úsudek závislý na otázce a dostupných důkazech.

## Produkční prompt

> Vytvoř profesionální český výukový snímek 16:9, 1600 × 900 px, bílé až velmi světle šedé pozadí, tmavě modrá horní lišta. Název „DŮVĚRYHODNOST NENÍ JEDNO RAZÍTKO“, podnázev „Ptej se, zda konkrétní zdroj podpírá konkrétní tvrzení pro tvůj účel.“ Dominantní diagnostická laboratoř: uprostřed neutrální karta tvrzení `Nová metoda zlepší výsledek o X %`, kolem ní šest odlišných čoček „PŮVOD“, „DŮKAZY“, „AKTUÁLNOST“, „ÚČEL“, „NEZÁVISLOST“, „RELEVANCE“. Každá čočka odhaluje jinou informaci; žádná sama nevytváří pečeť pravdy. Vpravo srovnej profesionálně vypadající zdroj bez metody a střídmý zdroj s dohledatelnými důkazy, bez skutečných značek. Dole ukaž překryv studie s naší populací, obdobím a otázkou a rozliš `FAKT • INTERPRETACE • NEJISTOTA`. Přidej blok „NESTAČÍ SAMO O SOBĚ“ a varování před mechanickým skóre. Modro-tyrkysová technická estetika, oranžová pro motivaci a rozhodování, velké české písmo. Bez univerzálního bodového hodnocení, bez falešné certifikační pečeti, bez dojmu, že známá doména nebo uvedený autor automaticky zaručuje správnost, bez pseudo-textu.

## Kontrolní bod

Snímek musí hodnotit vztah konkrétního tvrzení ke konkrétní otázce a nesmí vytvořit univerzální součet bodů. Aktuálnost musí být zobrazena relativně k tématu: starý historický pramen může být relevantní, zatímco stará cena nebo verze softwaru může být nepoužitelná.

---

# Snímek 6.4 — Ověřování a triangulace

## Výukový záměr

Student má osvojit praktický postup laterálního čtení: opustit původní stránku, dohledat původ tvrzení, zkontrolovat kontext a hledat skutečně nezávislé potvrzení. Má umět odlišit další kopii od nového důkazu a zvolit ověřovací metodu podle typu média. Má také chápat, že intenzita ověřování má odpovídat závažnosti rozhodnutí.

**Hlavní otázka:** Jak ověřit důležité tvrzení, aniž bychom zůstali uvnitř stránky, která jej zveřejnila?

**Nosná teze:** Ověření vzniká propojením původu, kontextu a nezávislého důkazu, nikoli opakováním stejného tvrzení na více místech.

## Přesné texty na snímku

**Název:** OVĚŘUJ DO STRAN, NE JEN DOVNITŘ

**Podnázev:** Otevři další stopy: původ, kontext a nezávislé potvrzení.

**Vyšetřovací postup:**

- **1 TVRZENÍ** — „Co přesně se tvrdí?“
- **2 PŮVODNÍ ZDROJ** — „Kde informace vznikla?“
- **3 KONTEXT** — „Co bylo před výrokem, po něm a v metodice?“
- **4 NEZÁVISLÁ STOPA** — „Potvrzuje ji jiný autor, data nebo metoda?“
- **5 ZÁVĚR** — „Co víme, co nevíme a s jakou jistotou?“

**Nástroj podle typu tvrzení:**

- **FOTOGRAFIE** — „reverzní hledání a původní publikace“
- **STATISTIKA** — „původní tabulka, metodika a velikost vzorku“
- **CITÁT** — „celý rozhovor, záznam nebo přepis“
- **TECHNICKÁ VLASTNOST** — „dokumentace a nezávislé měření“

**Triangulace:** „Nezávislé úhly se protínají u stejného vysvětlení.“

**Blok SCREENSHOT NENÍ KONTEXT:** „Ukazuje určitý obraz, ale nemusí dokazovat místo, čas, autorství ani neupravenost.“

**Blok MÍRA KONTROLY:** „Recept na večeři a zdravotní, právní či bezpečnostní rozhodnutí nevyžadují stejnou úroveň ověření.“

## Obrazová koncepce a kompozice

Dominantou je **vyšetřovací stůl se třemi otevřenými směry**, nikoli stereotypní detektivní nástěnka. Uprostřed leží karta tvrzení a výřez obrazovky. Z nich vedou tři skutečné ověřovací trasy: tyrkysová zpět k původnímu zdroji, modrá do širšího kontextu a oranžová k nezávislému měření nebo datům. Trasy se na pravé straně setkají v průhledném trojúhelníku triangulace. Uvnitř průniku je pouze to, co všechny relevantní stopy skutečně podpírají; mimo průnik zůstávají neověřené části.

Horní část obsahuje pět očíslovaných karet postupu, ale nejsou spojeny jako nevratný pás. Mezi původem, kontextem a nezávislou stopou jsou obousměrné návraty, protože nové zjištění může změnit formulaci tvrzení. Závěr má tři oddělené přihrádky `potvrzeno`, `nejisté`, `vyvráceno / nepodloženo`; snímek nesmí tvrdit, že každé ověřování končí jednoduchým ano či ne.

Dole jsou čtyři malé realistické pracovní situace: fotografie s reverzním hledáním, statistika propojená s původní tabulkou, citát propojený s celým záznamem a technický parametr propojený s dokumentací a měřením. Vpravo je **stupnice závažnosti rozhodnutí**: běžná volba má krátkou kontrolní dráhu, zdravotní či bezpečnostní rozhodnutí delší a přísnější. Stupnice vyjadřuje přiměřenost, ne rezignaci na pravdivost u méně důležitých témat.

## Vizuální metafora

Triangulace je **určení polohy z několika nezávislých měření**. Jedna přímka určí směr, ale teprve průnik více úhlů zpřesní polohu. Limit metafory: několik zdrojů může sdílet stejnou chybu nebo záviset na témže původním materiálu, takže nezávislost je nutné ověřit.

## Produkční prompt

> Navrhni profesionální český infografický snímek 16:9, 1600 × 900 px, bílé pozadí a tmavě modrá horní lišta. Přesný název „OVĚŘUJ DO STRAN, NE JEN DOVNITŘ“ a podnázev „Otevři další stopy: původ, kontext a nezávislé potvrzení.“ Dominantní moderní vyšetřovací stůl: uprostřed karta tvrzení a screenshot, z nich vedou tři jasné ověřovací cesty k „PŮVODNÍMU ZDROJI“, „KONTEXTU“ a „NEZÁVISLÉ STOPĚ“. Cesty se protínají v průhledném trojúhelníku „TRIANGULACE“ a vedou k závěru rozdělenému na potvrzené, nejisté a nepodložené části. Nahoře očíslovaný postup `1 TVRZENÍ → 2 PŮVODNÍ ZDROJ → 3 KONTEXT → 4 NEZÁVISLÁ STOPA → 5 ZÁVĚR`, s možností návratu mezi kroky. Dole čtyři mini-scény: fotografie a reverzní hledání, statistika a původní tabulka, citát a celý záznam, technická vlastnost a dokumentace plus nezávislé měření. Přidej blok „SCREENSHOT NENÍ KONTEXT“ a stupnici míry kontroly podle závažnosti rozhodnutí. Modro-tyrkysová technická estetika, oranžová pro otevřenou otázku, červená jen pro nepodložený skok. Bez stereotypní lupy přes celý snímek, bez tvrzení, že dvě kopie jsou dvě potvrzení, bez automatického binárního verdiktu a bez pseudo-textu.

## Kontrolní bod

Nezávislé potvrzení musí být založeno na jiném autorovi, datech nebo metodě, ne pouze na přebraném článku. Screenshot nesmí být zobrazen jako důkaz původu či autenticity a závěr musí umožnit přiznat nejistotu.

---

# Snímek 6.5 — Jak z informací vytvořit vlastní poznatek

## Výukový záměr

Student má pochopit syntézu jako transformaci ověřených informací do vlastní struktury, nikoli jako kopírování vět ze zdrojů. Má umět volit mezi tabulkou, časovou osou, diagramem a grafem podle typu vztahu. Musí rozlišovat fakt, interpretaci, odhad a názor a přenášet do výstupu i nejistotu a omezení původních dat.

**Hlavní otázka:** Co se musí stát mezi nalezením zdrojů a vznikem vlastního poznatku?

**Nosná teze:** Poznatek vzniká výběrem, porovnáním a strukturováním vztahů — se zachovaným původem, nejistotou a mezemi důkazů.

## Přesné texty na snímku

**Název:** ZDROJE NEJSOU HOTOVÝ POZNATEK

**Podnázev:** Vlastní porozumění vzniká transformací, porovnáním a přiznáním nejistoty.

**Transformační tok:**

- **1 VYBER** — „Co přímo odpovídá na otázku?“
- **2 ROZTŘIĎ** — „Fakt, interpretace, odhad, nebo názor?“
- **3 POROVNEJ** — „Použij stejná kritéria pro všechny varianty.“
- **4 ZOBRAZ VZTAH** — „Tabulka, časová osa, procesní diagram nebo graf.“
- **5 FORMULUJ ZÁVĚR** — „Co z důkazů plyne a kde zůstává nejistota?“

**Čtyři typy výroků:**

- **FAKT** — „ověřitelné tvrzení“
- **INTERPRETACE** — „vysvětlení významu“
- **ODHAD** — „aproximace z neúplných dat“
- **NÁZOR** — „hodnotící stanovisko“

**Volba struktury:**

- „varianty podle stejných kritérií“ → **TABULKA**
- „vývoj v čase“ → **ČASOVÁ OSA**
- „kroky a závislosti“ → **DIAGRAM**
- „číselný vztah“ → **GRAF**

**Blok GRAF MŮŽE ZKRESLIT:** „Oříznutá osa zvětší malý rozdíl; procento bez základu a průměr bez rozptylu skrývají kontext.“

**Blok POZOR:** „Přibližný údaj nepřepisuj jako přesné číslo a neshodu zdrojů neskrývej průměrem bez vysvětlení.“

## Obrazová koncepce a kompozice

Dominantou je **transparentní transformační dílna**, do níž zleva vstupují výřezy ze tří odlišných zdrojů. Každý úryvek má viditelný štítek původu a symbol míry nejistoty. První stanice odstraní části nerelevantní pro položenou otázku, ale nezahazuje odkazy na zdroj. Druhá roztřídí tvrzení do čtyř tvarově odlišných zásobníků: fakt jako pevná karta, interpretace jako propojení, odhad jako přerušovaný obrys a názor jako řečová karta.

Uprostřed je **volič reprezentace** se čtyřmi výstupy. Stejná sada informací se nesmí mechanicky zobrazit všemi způsoby; výhybka ukazuje, že srovnání variant vede do tabulky, časový vývoj do osy, proces do diagramu a číselný vztah do grafu. Vybraný příklad — porovnání dvou technologií — prochází tabulkou se stejnými kritérii a následně se z ní vytváří stručný závěr s přiznaným omezením.

Pravá část ukazuje výsledný **model poznatku**: centrální teze je spojena s podpůrnými důkazy, protidůkazem a kartou nejistoty. Nejde o hromadu citátů. Každá vazba zůstává dohledatelná zpět ke zdroji. Dole je dvojice stejně datově založených grafů; jeden používá celou osu, druhý oříznutou osu a vizuálně dramatizuje malý rozdíl. Vedle jsou karty `62 % z čeho?` a `průměr bez rozptylu`, které upozorní na chybějící kontext bez vymyšlených datových závěrů.

## Vizuální metafora

Syntéza je **stavba modelu z označených součástí**, nikoli rozmixování zdrojů do beztvaré směsi. Každý díl má původ, funkci a toleranci; výsledek musí ukázat i nejisté spoje. Limit metafory: lidská interpretace není mechanická a volba struktury sama o sobě nezaručí správný závěr.

## Produkční prompt

> Vytvoř profesionální český výukový snímek 16:9, 1600 × 900 px, bílé až světle šedé pozadí, tmavě modrá horní lišta. Název „ZDROJE NEJSOU HOTOVÝ POZNATEK“, podnázev „Vlastní porozumění vzniká transformací, porovnáním a přiznáním nejistoty.“ Dominantní transparentní transformační dílna: zleva vstupují označené výřezy ze tří zdrojů, postupují přes pět stanic `1 VYBER → 2 ROZTŘIĎ → 3 POROVNEJ → 4 ZOBRAZ VZTAH → 5 FORMULUJ ZÁVĚR`. Ve druhé stanici přesně rozliš čtyři tvary `FAKT`, `INTERPRETACE`, `ODHAD`, `NÁZOR`. Uprostřed volič struktury: varianty podle kritérií → tabulka, vývoj v čase → časová osa, kroky a závislosti → diagram, číselný vztah → graf. Vpravo výsledný model poznatku s centrální tezí, podpůrnými důkazy, protidůkazem, nejistotou a dohledatelnými vazbami ke zdrojům. Dole srovnej graf s plnou a oříznutou osou a přidej upozornění `62 % z čeho?` a `průměr bez rozptylu`. Modro-tyrkysový technický styl, oranžová pro interpretaci, přerušovaný obrys pro nejistotu, velké české písmo. Bez hromady kopírovaných citátů, bez ztráty vazby na původ, bez tvrzení, že graf či tabulka automaticky dokazují závěr, bez pseudo-textu.

## Kontrolní bod

Fakt, interpretace, odhad a názor musejí být jasně odlišeny. Výsledný závěr musí zůstat dohledatelný ke zdrojům a zachovat jejich nejistotu; grafický příklad nesmí použít vymyšlená čísla k tvrzení o reálném jevu.

---

# Snímek 6.6 — Citace, licence a odpovědné využívání AI

## Výukový záměr

Student má rozlišit citaci od licence: citace dokládá původ tvrzení či převzatého obsahu, zatímco licence určuje dovolené způsoby užití díla. Má vědět, že parafráze stále vyžaduje uvedení zdroje a že veřejná dostupnost obrázku neznamená volné použití. U generativní AI má chápat model jako pomocný nástroj, nikoli jako původní faktický zdroj, a chránit osobní, neveřejná a citlivá data.

**Hlavní otázka:** Co musíme zkontrolovat, než cizí obsah nebo výstup AI použijeme ve vlastní práci?

**Nosná teze:** Odpovědné použití spojuje dohledatelný původ, oprávnění k použití, ověření faktů a ochranu dat.

## Přesné texty na snímku

**Název:** PŮVOD, OPRÁVNĚNÍ, OVĚŘENÍ, DATA

**Podnázev:** Citace říká odkud; licence říká co smíš; ověření říká čemu můžeš věřit.

**Čtyři publikační brány:**

- **1 PŮVOD** — „Kdo je autor a kde vzniklo tvrzení nebo dílo?“
- **2 CITACE** — „Dokáže čtenář dohledat použitý zdroj?“
- **3 LICENCE** — „Je dovoleno dílo použít, upravit a zveřejnit daným způsobem?“
- **4 OVĚŘENÍ A DATA** — „Jsou fakta ověřena a nevkládám citlivý obsah?“

**Citace:**

- **PŘÍMÁ CITACE** — „doslovný text označ a uveď zdroj“
- **PARAFRÁZE** — „vlastní formulace, ale převzatá myšlenka stále potřebuje zdroj“

**Licence:** „Zaznamenej autora • název • zdroj • konkrétní licenci.“

**AI může pomoci:** „brainstorming • vysvětlení • dotazy • struktura • varianty“

**AI odpověď není sama o sobě zdroj.**

**Nevkládej bez oprávnění:** „hesla • osobní údaje • neveřejné dokumenty • citlivá data“

**Blok POZOR:** „Veřejně dostupné ≠ volně použitelné. Uvedení autora samo nenahrazuje oprávnění dané licencí.“

## Obrazová koncepce a kompozice

Dominantou je **publikační kontrolní brána**, kterou prochází připravovaný školní dokument. Zleva přicházejí tři druhy materiálu: převzaté tvrzení, fotografie a odstavec navržený AI. Každý dostává samostatný průvodní štítek, takže se jejich povinnosti neslijí.

První komora dohledá původ a připojí zdroj. Druhá rozliší přímou citaci od parafráze: doslovný úsek zůstane v uvozovkách, parafráze se vizuálně přestaví do nové formulace, ale obě cesty nesou odkaz ke zdroji. Třetí komora je **licenční zámek** nad fotografií. Čtyři políčka `autor`, `název`, `zdroj`, `konkrétní licence` jsou uložena spolu s médiem už při získání; brána posuzuje zamýšlené použití a nesmí tvrdit, že samotná citace nahrazuje licenci.

Čtvrtá komora zpracuje AI výstup. Model je zobrazen jako pracovní asistent, který pomáhá s návrhem struktury a dotazů. Faktická tvrzení z jeho výstupu odcházejí boční cestou k reálným zdrojům a teprve po ověření se vracejí do dokumentu. Smyšlená citace nebo nedohledatelný údaj zůstane před bránou. Současně je před vstupem do AI **datový filtr**: běžné téma projde, zatímco heslo, osobní údaj, neveřejný dokument a citlivá data se zastaví v červeně orámované bezpečné zóně.

Na pravé straně je hotový dokument se třemi viditelnými vrstvami: vlastní text, odkazy na zdroje a přehled licencí použitých médií. AI není uvedena jako anonymní autorita; způsob přiznání jejího použití se může řídit konkrétními pravidly školy nebo zadání, což lze uvést drobným blokem `Řiď se pravidly instituce a úkolu`.

## Vizuální metafora

Publikování je **výstupní kontrola výrobku**. Původ materiálu, oprávnění, ověřené parametry a bezpečnost dat se kontrolují odděleně, protože splnění jedné podmínky nenahrazuje ostatní. Limit metafory: konkrétní citační norma, licenční podmínky a pravidla přiznání AI se liší podle školy, vydavatele, země a způsobu použití.

## Produkční prompt

> Navrhni profesionální český výukový infografický snímek 16:9, 1600 × 900 px, bílé pozadí a tmavě modrá horní lišta. Přesný název „PŮVOD, OPRÁVNĚNÍ, OVĚŘENÍ, DATA“ a podnázev „Citace říká odkud; licence říká co smíš; ověření říká čemu můžeš věřit.“ Dominantní publikační kontrolní brána: zleva vstupují převzaté tvrzení, fotografie a odstavec navržený AI. Projdou čtyřmi oddělenými branami `1 PŮVOD`, `2 CITACE`, `3 LICENCE`, `4 OVĚŘENÍ A DATA`. U citace rozděl dvě cesty: „PŘÍMÁ CITACE“ jako doslovný označený text se zdrojem a „PARAFRÁZE“ jako vlastní formulace, která stále nese zdroj. U licence ukaž záznam `autor • název • zdroj • konkrétní licence` a blok „Veřejně dostupné ≠ volně použitelné“. AI zobraz jako pracovní nástroj pro brainstorming, vysvětlení, dotazy, strukturu a varianty; faktická tvrzení vedou k reálným zdrojům a zpět až po ověření. Velký přesný text „AI ODPOVĚĎ NENÍ SAMA O SOBĚ ZDROJ.“ Před AI datový filtr zastaví `hesla • osobní údaje • neveřejné dokumenty • citlivá data`. Vpravo hotový dokument s dohledatelnými zdroji a licencemi. Modro-tyrkysová akademická estetika, oranžová pro kontrolní rozhodnutí, červená pouze pro citlivá data a nedohledatelný údaj, velké české písmo. Bez konkrétní univerzální citační normy, bez tvrzení, že uvedení autora automaticky dovoluje použití, bez smyšlených citací, bez log AI služeb a bez pseudo-textu.

## Kontrolní bod

Citace a licence musejí být zobrazeny jako dvě odlišné povinnosti. Parafráze musí zůstat propojena se zdrojem, veřejná dostupnost nesmí znamenat volné užití a žádné faktické tvrzení vytvořené AI nesmí projít do výsledku bez dohledání skutečného zdroje. Citlivá data musejí být zastavena před vstupem do veřejné AI služby.

---

## Kontinuita a rytmus celé 6. lekce

Šest snímků tvoří jednu cestu, ale neopakuje jednotnou šablonu:

1. **6.1** zužuje neurčité téma na informační potřebu pomocí navigačního trychtýře.
2. **6.2** sleduje informaci proti směru šíření až k původu pomocí rodokmenu zdrojů.
3. **6.3** zkoumá jedno tvrzení několika diagnostickými čočkami bez falešného skóre.
4. **6.4** otevírá více nezávislých ověřovacích cest a skládá je triangulací.
5. **6.5** převádí ověřené vstupy do strukturovaného vlastního poznatku.
6. **6.6** kontroluje původ, oprávnění, fakta a ochranu dat před zveřejněním.

Při generování celé sady zachovat společnou horní lištu, typografii a barevnou logiku, ale nestavět všech šest snímků jako stejné karty v mřížce. Vizuální návaznost má vzniknout opakováním tvarů `zdroj → tvrzení → důkaz → závěr`, zatímco prostorová kompozice se mění podle výukového mechanismu.
