# Scénáře infografických snímků — 2. lekce

## Principy digitalizace

Sada pro témata 2.1–2.5 z výukového textu *Základy informatiky*. Každý scénář je připraven jako samostatné zadání pro grafika, prezentační nástroj i generátor obrazu. Všechny texty určené přímo na snímek jsou uvedeny v přesném znění.

## Společný vizuální rámec série

- Formát 16:9, ideálně 1600 × 900 px; bílé až velmi světle šedé pozadí a bezpečný okraj minimálně 40 px.
- Profesionální akademicko-technologický vzhled pro studenty střední školy. Bez infantilních ikon, kreslených maskotů, neonových sci-fi rozhraní, falešných ovládacích panelů a dekorativního zahlcení.
- Výrazná tmavě modrá horní lišta; velké bílé bezpatkové písmo s českou diakritikou. Nadpis přibližně 44–54 px, podnadpis 25–30 px, běžný text nejméně 22–24 px.
- Barevná logika: tmavá námořnická modř pro strukturu a pojmy, střední modř pro data, tyrkysová pro tok signálu nebo převod, oranžová pro aktivní měření či zaokrouhlení, červená pouze pro chybu, ztrátu nebo varování.
- Barva nesmí být jediným nositelem významu. Analogový průběh zobrazovat spojitou čarou, digitální hodnoty body, sloupci nebo diskrétními bloky; fyzický signál plnou linkou a abstraktní data geometrickým kódem.
- Jeden dominantní vysvětlující mechanismus na snímek, zpravidla přes 50 % plochy. Maximálně pět vedlejších informačních bloků. Šipky používat jen pro skutečný směr přeměny, toku nebo závislosti.
- Pro generátory, které nezvládají přesnou českou sazbu, vytvořit obraz bez textu se zachovanými prázdnými plochami a uvedené texty následně vysázet v prezentačním editoru. Nevkládat pseudo-text ani náhodné značky.

---

# Snímek 2.1 — Informace potřebuje fyzickou reprezentaci

## Výukový záměr

Student má pochopit, že informace je interpretovaný význam, zatímco signál je měřitelný fyzický stav, který tento význam nese. Tentýž obsah může během ukládání, přenosu a zobrazení několikrát změnit fyzickou podobu, aniž by se změnil jeho zamýšlený význam.

**Hlavní otázka:** Jak může stejná zpráva projít pamětí, rádiem, optickým vláknem a displejem?

**Nosná teze:** Informace necestuje bez nosiče; systém jí v každé části cesty přiřadí konkrétní fyzickou reprezentaci a pravidlo interpretace.

## Přesné texty na snímku

**Název:** STEJNÝ VÝZNAM, JINÁ FYZICKÁ STOPA

**Podnázev:** Informace je význam. Signál je měřitelný stav, který tento význam právě nese.

**Středová zpráva:** `AHOJ`

**Pět stanic přenosu:**

1. **PAMĚŤ TELEFONU** — „elektrický náboj v paměťových buňkách“
2. **RÁDIOVÝ PŘENOS** — „změny elektromagnetické vlny“
3. **OPTICKÁ SÍŤ** — „časovaný sled světelných impulsů“
4. **PAMĚŤ PŘÍJEMCE** — „nově vytvořené fyzické stavy“
5. **DISPLEJ** — „světlo pixelů čitelné člověkem“

**Centrální rozlišení:**

- **INFORMACE** — „dohodnutý význam zprávy AHOJ“
- **SIGNÁL** — „fyzická veličina měnící se podle pravidla“
- **INTERPRETACE** — „pravidlo, které ze stavů znovu vytvoří data a význam“

**Blok DIGITÁLNÍ ≠ NEFYZICKÉ:** „Také logická 0 a 1 jsou v zařízení realizovány rozsahy napětí, světlem, nábojem nebo magnetizací.“

**Blok POZOR:** „Kabelem necestují malé jedničky a nuly. Přenáší se fyzický signál, který přijímač interpretuje jako digitální data.“

## Obrazová koncepce a kompozice

Dominantou je široký **technický průřez cestou jediné zprávy** od odesílatele k příjemci. Na levém okraji drží člověk telefon se zprávou `AHOJ`; na pravém okraji se stejný text rozsvítí na displeji druhého telefonu. Mezi nimi vede jedna souvislá tyrkysová trasa, která pětkrát mění svou fyzickou podobu. Nemá vypadat jako datový kabel plný nul a jedniček, ale jako řada skutečných převodů.

V řezu telefonu zobrazit nábojové stavy paměťových buněk; ve vzduchu prostorovou rádiovou vlnu; v řezu optickým vláknem světelné impulzy; v přijímači nově vytvořené elektrické stavy; na displeji mřížku svítících pixelů. Nad všemi stanicemi se v průsvitné námořnicky modré linii drží neměnná významová vrstva `AHOJ`. Pod ní se fyzická vrstva proměňuje. V každém rozhraní je malý převodník s dvojicí sloves „zakóduje / interpretuje“.

Uprostřed kompozice vytvořit svislý zvětšený detail jedné stanice: nahoře abstraktní datový symbol, uprostřed pravidlo kódování a dole tolerované rozsahy fyzické hodnoty pro logické stavy. Dvě oddělená pásma označit `0` a `1`; mezi nimi nechat neutrální přechodovou oblast. Detail má ukázat, proč malé fyzické odchylky nemusí změnit přečtený logický stav.

Spodní pás tvoří tři nepravidelně široké bloky „INFORMACE / SIGNÁL / INTERPRETACE“. Blok „DIGITÁLNÍ ≠ NEFYZICKÉ“ je napojen přímo na zvětšený řez, zatímco oranžově orámované „POZOR“ uzavírá cestu vpravo dole.

## Vizuální metafora

Zpráva je **štafeta, která na jednotlivých úsecích mění dopravní prostředek**, nikoli předmět putující beze změny. Metaforu vyjádřit technicky: spojitá významová vrstva zůstává, fyzický nosič se v převodnících obnovuje. Nezobrazovat putující balíček písmen, který by naznačoval, že tatáž fyzická věc prochází celou trasou.

## Produkční prompt

> Vytvoř profesionální český výukový infografický snímek 16:9, 1600 × 900 px, na bílém až velmi světle šedém pozadí. Nahoře tmavě modrá lišta s velkým bílým názvem „STEJNÝ VÝZNAM, JINÁ FYZICKÁ STOPA“. Podnázev: „Informace je význam. Signál je měřitelný stav, který tento význam právě nese.“ Dominantní široký technický průřez ukazuje cestu jediné zprávy `AHOJ` mezi dvěma telefony. Jedna tyrkysová trasa prochází pěti stanicemi, ale v každé se zobrazí jinou skutečnou fyzickou reprezentací: „1 PAMĚŤ TELEFONU — elektrický náboj v paměťových buňkách“, „2 RÁDIOVÝ PŘENOS — změny elektromagnetické vlny“, „3 OPTICKÁ SÍŤ — časovaný sled světelných impulsů“, „4 PAMĚŤ PŘÍJEMCE — nově vytvořené fyzické stavy“, „5 DISPLEJ — světlo pixelů čitelné člověkem“. Nad trasou udržuj průsvitnou významovou vrstvu `AHOJ`, zatímco fyzický nosič se mění. V rozhraních ukaž převod „zakóduje / interpretuje“. Uprostřed přidej zvětšený detail fyzické veličiny se dvěma tolerovanými pásmy označenými `0` a `1`, aby bylo patrné, že digitální stav je interpretací rozsahu reálných hodnot. Dole tři krátké bloky „INFORMACE“, „SIGNÁL“ a „INTERPRETACE“ s dodanými texty, blok „DIGITÁLNÍ ≠ NEFYZICKÉ“ a malé oranžové „POZOR“. Čistá modro-tyrkysová technická estetika, jemné 3D řezy, velké české písmo, přesné šipky a dostatek volného prostoru. Bez putujících nul a jedniček v kabelu, bez dětské poštovní ilustrace, falešných log, pseudo-textu a technicky nemožných detailů.

## Kontrolní bod

I bez čtení delších textů musí být patrné, že na každém úseku vzniká jiný fyzický signál, zatímco význam zprávy zůstává zachován pouze díky společným pravidlům kódování a interpretace.

---

# Snímek 2.2 — Analogový a digitální svět

## Výukový záměr

Student má rozlišit spojitou analogovou reprezentaci od diskrétní digitální reprezentace a pochopit, proč digitální kopie může být bitově shodná, ačkoli samotný převod zvuku na čísla pracuje s konečným počtem měření a hodnot. Snímek nemá stavět analog a digitál do jednoduchého souboje „špatné versus dobré“.

**Hlavní otázka:** Kde se při digitálním záznamu ztrácí spojitost a kde lze naopak kopírovat bez další ztráty?

**Nosná teze:** Digitalizace vytváří konečný číselný model spojitého jevu; jakmile jsou data správně přečtena, lze tento model kopírovat bitově přesně.

## Přesné texty na snímku

**Název:** JEDEN ZVUK, DVA ZPŮSOBY ZÁZNAMU

**Podnázev:** Analogová stopa sleduje průběh fyzicky. Digitální záznam jej popíše konečnou řadou čísel.

**Společný vstup:** „spojitá změna akustického tlaku“

**Horní větev — ANALOGOVÁ REPREZENTACE:**

- „spojitý elektrický průběh z mikrofonu“
- „tvar drážky nebo změna magnetizace“
- „každá další fyzická kopie může přidat šum a zkreslení“

**Dolní větev — DIGITÁLNÍ REPREZENTACE:**

- „vzorkování: kdy změříme“
- „kvantování: jakou hodnotu uložíme“
- „kódovaná posloupnost čísel“
- „správně přečtená data lze kopírovat bitově přesně“

**Výstup:** „nově vytvořený zvuk z reproduktoru“

**Blok KDE VZNIKÁ OMEZENÍ:** „Převod reality na konečný počet čísel závisí na vzorkovací frekvenci, bitové hloubce, filtrech a dalším zpracování.“

**Blok POZOR:** „Bitově přesná kopie není totéž co dokonale přesný model původního analogového jevu.“

## Obrazová koncepce a kompozice

Kompozice má podobu **dvojitého zvukového laboratorního stolu**. Vlevo je jediný realistický zdroj zvuku — například struna koncertního klavíru a zvětšený tlakový průběh ve vzduchu. Mikrofon vytvoří společný spojitý elektrický signál, který se potom rozdělí do dvou prostorově odlišných větví.

Horní analogová větev je plynulá: průběh se přímo otiskne do detailu gramofonové drážky nebo magnetické vrstvy pásku. Za ním následují tři fyzické kopie jako po sobě jdoucí průsvitné stopy. Každá kopie je mírně odlišná a obsahuje jemně narůstající šum; odchylku ukázat tenkým červeným obrysem vůči předchozí stopě.

Dolní digitální větev prochází A/D převodníkem. Spojitá čára se nejprve protne pravidelnými svislými okamžiky měření, potom se body zarovnají na diskrétní úrovně a nakonec se promění v čisté číselné bloky. Za nimi jsou tři identické kopie kontrolované shodou; místo dekorativních nul a jedniček použít malé uspořádané bloky a symbol kontroly shody. Obě větve se vpravo vracejí přes reprodukční zařízení k nově vytvořené akustické vlně.

Mezi větvemi ponechat jasnou srovnávací osu: nahoře „fyzická podobnost stopy“, dole „číselná shoda dat“. Uprostřed dolní větve zvýraznit dva odlišné okamžiky omezení: převod spojitého průběhu na vzorky a přiřazení vzorků k úrovním. Kopírování již uložených dat zobrazit bez postupné degradace.

Blok „KDE VZNIKÁ OMEZENÍ“ umístit přímo pod A/D převodník. „POZOR“ patří k identickým kopiím, aby opravoval častý omyl v místě, kde vzniká.

## Vizuální metafora

Analogová větev je **otisk**, který se při každém dalším fyzickém přetištění může mírně změnit. Digitální větev je **číselný předpis**, který lze opsat beze změny, pokud jsou symboly správně rozpoznány. Metafora nesmí tvrdit, že digitální záznam obsahuje nekonečně přesný obraz reality ani že analogová reprezentace je automaticky nekvalitní.

## Produkční prompt

> Navrhni sofistikovaný český výukový snímek 16:9, 1600 × 900 px, s bílým pozadím a tmavě modrou horní lištou. Přesný název: „JEDEN ZVUK, DVA ZPŮSOBY ZÁZNAMU“. Podnázev: „Analogová stopa sleduje průběh fyzicky. Digitální záznam jej popíše konečnou řadou čísel.“ Dominantou je dvojitý zvukový laboratorní stůl. Vlevo realistická struna klavíru vytváří „spojitou změnu akustického tlaku“, mikrofon ji převede na spojitý elektrický průběh a cesta se rozdělí. Horní větev „ANALOGOVÁ REPREZENTACE“ ukazuje plynulý průběh, fyzický otisk do drážky nebo magnetické vrstvy a tři po sobě jdoucí kopie s jemně narůstající odchylkou a šumem. Dolní větev „DIGITÁLNÍ REPREZENTACE“ ukazuje A/D převod: „vzorkování: kdy změříme“, „kvantování: jakou hodnotu uložíme“, „kódovaná posloupnost čísel“ a tři vizuálně identické, kontrolované kopie s textem „správně přečtená data lze kopírovat bitově přesně“. Obě větve končí reproduktorem a „nově vytvořeným zvukem z reproduktoru“. Jasně odliš spojitou křivku, body vzorků, diskrétní úrovně a bloky dat také tvarem, nejen barvou. Přidej blok „KDE VZNIKÁ OMEZENÍ“ s dodaným textem a oranžový blok „POZOR“. Čistá vědecko-technická estetika, jemná polorealistická zařízení, velké české písmo, minimum křížení a dostatek bílého prostoru. Bez nostalgického kýče, bez tvrzení, že digitál je vždy lepší, bez dekorativních nul a jedniček, pseudo-textu a falešných log.

## Kontrolní bod

Snímek musí jednoznačně oddělit dvě situace: ztráta či omezení může vzniknout při digitalizaci a zpracování, zatímco další správná digitální kopie již uložených dat nemusí být horší než předchozí.

---

# Snímek 2.3 — Vzorkování: kdy změříme hodnotu?

## Výukový záměr

Student má pochopit vzorkování jako pravidelné měření v čase, nikoli jako určení přesnosti uložené hodnoty. Musí rozpoznat, že příliš řídké vzorkování může rychlý průběh zaměnit za jiný pomalejší průběh — aliasing — a že potřebná frekvence závisí na rychlosti změn sledovaného jevu.

**Hlavní otázka:** Jak může správně změřená řada bodů popsat úplně jiný pohyb nebo zvuk?

**Nosná teze:** Vzorky ukazují jen stav v určitých okamžicích; bez dostatečně hustého měření mezi nimi může zůstat skrytý rychlejší průběh.

## Přesné texty na snímku

**Název:** KDY JE MĚŘENÍ PŘÍLIŠ ŘÍDKÉ?

**Podnázev:** Vzorkovací frekvence určuje počet měření za sekundu — nikoli přesnost každé hodnoty.

**Centrální experiment:** „Stejné otáčející se kolo, dvě frekvence snímání“

**Horní časová osa — HUSTÉ VZORKOVÁNÍ:** „Pořadí poloh zachová skutečný směr a rychlost pohybu.“

**Dolní časová osa — ŘÍDKÉ VZORKOVÁNÍ:** „Vzorky připomínají pomalé otáčení opačným směrem.“

**Definice:** „Vzorkovací frekvence `fₛ` = počet vzorků za sekundu; jednotka hertz (Hz).“

**Zjednodušené pravidlo:** „Pro frekvenčně omezený signál: `fₛ > 2 × fₘₐₓ`“

**Příklad AUDIO:** „44,1 kHz = 44 100 vzorků/s; teoretická Nyquistova frekvence 22,05 kHz.“

**Srovnání TEMPO JEVU:** „Teplota místnosti se mění pomalu. Zvuk se mění rychle. Potřebná hustota měření proto není stejná.“

**Blok POZOR — ALIASING:** „Příliš pomalé vzorkování nevytvoří jen méně detailů. Může vytvořit věrohodně vypadající, ale nesprávný nižší průběh.“

**Rozlišení pojmů:** „VZORKOVÁNÍ = KDY měříme • KVANTOVÁNÍ = S JAKOU PŘESNOSTÍ hodnotu uložíme“

## Obrazová koncepce a kompozice

Dominantou je **stroboskopický experiment s jediným kolem** v bočním pohledu. Kolo má jeden výrazný oranžový referenční bod na obvodu a jemnou šipku skutečného směru otáčení. Z jedné fyzické situace vedou dvě paralelní časové osy složené z přesně zarovnaných snímků.

Horní osa snímá často: oranžový bod postupuje mezi snímky po malých krocích a po spojení vznikne správný směr. Dolní osa snímá řídce: bod se mezi snímky posune téměř o celou otáčku, ale z viditelných poloh lze chybně odvodit malý krok opačně. Skutečný pohyb zobrazit plnou tyrkysovou kruhovou šipkou, zdánlivý alias přerušovanou červenooranžovou šipkou. Tím je fyzický mechanismus aliasingu patrný bez matematického výkladu.

V pravé třetině navázat zvětšovací „časovou lupu“: spojitá sinusová křivka a stejné body vzorků dovolují více různých průběhů, z nichž jeden je skutečný a druhý alias. Zde umístit zjednodušené pravidlo `fₛ > 2 × fₘₐₓ` a malou ikonickou clonu filtru před převodníkem. Filtr nepopsat jako všemocnou opravu; vizuálně pouze omezuje příliš vysoké frekvence ještě před vzorkováním.

Ve spodním levém rohu je věcný srovnávací detail: teploměr se třemi měřeními za delší dobu versus zvuková vlna s velmi hustými značkami. Uprostřed spodního pásu blok s příkladem 44,1 kHz. Vpravo dole výrazně oddělit dvojici „KDY / S JAKOU PŘESNOSTÍ“, aby se vzorkování nezaměnilo s kvantováním.

## Vizuální metafora

Vzorkování je **stroboskopická brána do času**: vidíme pouze okamžiky, kdy se clona otevře. Metafora přesně vysvětluje aliasing, ale má limit — u zvuku nejde o skutečné fotografické snímky; společným principem je periodické odečítání hodnoty.

## Produkční prompt

> Vytvoř profesionální český infografický snímek 16:9, 1600 × 900 px, na bílém pozadí. Nahoře tmavě modrá lišta s názvem „KDY JE MĚŘENÍ PŘÍLIŠ ŘÍDKÉ?“ a podnázev „Vzorkovací frekvence určuje počet měření za sekundu — nikoli přesnost každé hodnoty.“ Dominantní stroboskopický experiment: jedno technicky realistické otáčející se kolo s oranžovým referenčním bodem a dvě paralelní časové osy. Horní „HUSTÉ VZORKOVÁNÍ“ ukazuje mnoho poloh a správný směr pohybu; dolní „ŘÍDKÉ VZORKOVÁNÍ“ ukazuje málo poloh a věrohodný zdánlivý pohyb opačným směrem. Skutečný směr vyznač plnou tyrkysovou šipkou, alias přerušovanou červenooranžovou šipkou. Vpravo přidej časovou lupu se spojitou křivkou, vzorkovacími body a dvěma možnými průběhy přes stejné body. Uveď „Vzorkovací frekvence fₛ = počet vzorků za sekundu; jednotka hertz (Hz).“ a „Pro frekvenčně omezený signál: fₛ > 2 × fₘₐₓ“. Přidej jednoduchý filtr před vzorkováním. Dole malé srovnání pomalu se měnící teploty a rychle se měnícího zvuku, blok „44,1 kHz = 44 100 vzorků/s; teoretická Nyquistova frekvence 22,05 kHz“, oranžové „POZOR — ALIASING“ a jasné rozlišení „VZORKOVÁNÍ = KDY měříme • KVANTOVÁNÍ = S JAKOU PŘESNOSTÍ hodnotu uložíme“. Velké české písmo, přesná časová návaznost, střízlivá vědecká estetika, dostatek volného prostoru. Bez komiksového auta, dekorativních šipek, pseudo-textu nebo nepřesně umístěných vzorků.

## Kontrolní bod

Z dolní časové osy musí být skutečně možné odvodit zdánlivý opačný směr; nejde jen o obecnou ikonu chyby. Současně musí být vzorkovací frekvence popsána jako hustota měření v čase, ne jako počet hodnot amplitudy.

---

# Snímek 2.4 — Kvantování a bitová hloubka

## Výukový záměr

Student má pochopit, že kvantování přiřazuje naměřenou hodnotu k jedné z konečného počtu úrovní. Bitová hloubka určuje počet dostupných úrovní, ovlivňuje velikost kvantizační chyby a současně zvětšuje množství dat na vzorek.

**Hlavní otázka:** Co přesně získáme — a za co zaplatíme — přidáním bitů každému vzorku?

**Nosná teze:** Více bitů znamená více rozlišitelných hodnot a obvykle menší zaokrouhlení, ale také více dat; nezvyšuje však hustotu měření v čase.

## Přesné texty na snímku

**Název:** VÍCE BITŮ, JEMNĚJŠÍ MĚŘÍTKO

**Podnázev:** Kvantování přiřadí každý vzorek k nejbližší dostupné úrovni.

**Hlavní vztah:** „`n` bitů na vzorek → `2ⁿ` možných hodnot“

**Srovnání vlevo — 2 BITY:** „4 úrovně • velké kroky • větší kvantizační odchylka“

**Srovnání vpravo — 4 BITY:** „16 úrovní • jemnější kroky • menší odchylka“

**Popisek procesu:** „naměřená hodnota → nejbližší úroveň → uložené číslo“

**Definice chyby:** „KVANTIZAČNÍ CHYBA = rozdíl mezi původní hodnotou vzorku a přiřazenou úrovní“

**Stupnice:** „2 bity = 4 • 4 bity = 16 • 8 bitů = 256 • 16 bitů = 65 536 hodnot“

**Blok DATA ROSTOU:** „nekomprimovaný tok = vzorkovací frekvence × bitová hloubka × počet kanálů“

**Praktický výpočet:** „44 100 × 16 × 2 = 1 411 200 bit/s ≈ 1,411 Mbit/s“

**Blok POZOR:** „Bitová hloubka určuje počet úrovní amplitudy. Vzorkovací frekvence určuje počet měření v čase.“

## Obrazová koncepce a kompozice

Dominantou je **prostorový řez jedním analogovým průběhem nad dvěma různě jemnými měřicími schodišti**. Spojitá křivka je v obou polovinách stejná a vzorky leží ve stejných časových okamžicích. Liší se pouze svislá stupnice hodnot.

V levé části mají dva bity čtyři masivní 3D úrovně. Z každého oranžového bodu na původní křivce vede krátká svislá linka k nejbližší modré úrovni. Délka linky je kvantizační chyba. V pravé části mají čtyři bity šestnáct tenkých úrovní; stejné vzorky se posunou o kratší vzdálenost. Vizuální srovnání musí používat stejné měřítko os i stejné okamžiky, jinak by bylo zavádějící.

U jednoho vybraného vzorku vytvořit zvětšený průhledný řez: původní hodnota, dvě sousední úrovně, zvolená nejbližší úroveň a uložené číslo. Tenká oboustranná úsečka přesně označí kvantizační chybu. Nezobrazovat chybu jako poruchu přístroje; jde o systematický důsledek konečné sady hodnot.

Pod diagramem je úzká exponenciální stupnice `2, 4, 8, 16 bitů`, jejíž počet úrovní roste rychleji než počet bitů. Nevykreslovat všech 65 536 čar; použít zvětšující se hustotu a uvést přesná čísla. Vpravo dole navazuje jednoduchá „datová váha“: zvýšení bitů na vzorek zvětší objem dat. Vedle ní je praktický výpočet stereofonního PCM 44,1 kHz / 16 bit.

## Vizuální metafora

Bitová hloubka je **jemnost svislého měřítka**, po jehož příčkách musí každý vzorek přistát. Hrubé schody vytvářejí větší odchylky, jemné schody menší. Metafora se vztahuje k lineárnímu kvantování; nesmí naznačit, že každý zvukový kodek nebo převodník používá vždy stejnoměrné lineární úrovně.

## Produkční prompt

> Vytvoř precizní český výukový snímek 16:9, 1600 × 900 px, na bílém až světle šedém pozadí. Nahoře tmavě modrá lišta s názvem „VÍCE BITŮ, JEMNĚJŠÍ MĚŘÍTKO“ a podnázev „Kvantování přiřadí každý vzorek k nejbližší dostupné úrovni.“ Dominantní prostorový technický řez porovnává tentýž spojitý průběh a stejné časové okamžiky nad dvěma svislými schodišti. Vlevo „2 BITY — 4 úrovně • velké kroky • větší kvantizační odchylka“, vpravo „4 BITY — 16 úrovní • jemnější kroky • menší odchylka“. Oranžové body leží na původní křivce; krátké svislé linky vedou k nejbližší modré úrovni a jejich délka představuje kvantizační chybu. U jednoho vzorku vytvoř lupu s popisky „původní hodnota“, „nejbližší úroveň“, „uložené číslo“ a „kvantizační chyba“. Přesný hlavní vztah: „n bitů na vzorek → 2ⁿ možných hodnot“. Dole stupnice „2 bity = 4 • 4 bity = 16 • 8 bitů = 256 • 16 bitů = 65 536 hodnot“, blok „DATA ROSTOU — nekomprimovaný tok = vzorkovací frekvence × bitová hloubka × počet kanálů“ a výpočet „44 100 × 16 × 2 = 1 411 200 bit/s ≈ 1,411 Mbit/s“. Přidej malé oranžové „POZOR“ s rozlišením bitové hloubky a vzorkovací frekvence. Velké písmo, shodné osy obou srovnání, čistá modro-tyrkysová paleta, oranžová jen pro měřený bod a odchylku. Bez pixel-artové estetiky, bez záměny času a amplitudy, bez pseudo-textu, falešných log nebo matematických nesmyslů.

## Kontrolní bod

Obě poloviny musí mít totožné časové vzorky a rozsah amplitudy. Jedinou měněnou veličinou je počet kvantizačních úrovní; ze snímku musí být vidět jak zmenšení odchylky, tak růst dat na vzorek.

---

# Snímek 2.5 — Bit, byte a velikost digitálních dat

## Výukový záměr

Student má bezpečně rozlišit bit od bytu, rychlost přenosu od velikosti souboru a desítkové jednotky od binárních. Na jediném praktickém výpočtu má pochopit, proč soubor 100 MB nelze ideálně přenést linkou 100 Mbit/s za jednu sekundu a proč bude reálný čas ještě delší.

**Hlavní otázka:** Proč stejné číslo „100“ u souboru a sítě neznamená přenos za jednu sekundu?

**Nosná teze:** Velikost a rychlost lze porovnat až po převodu na stejné jednotky; značka `b` nebo `B` mění hodnotu osmkrát.

## Přesné texty na snímku

**Název:** PROČ 100 MB NENÍ 100 Mbit

**Podnázev:** Soubor měříme v bytech, síť často v bitech za sekundu. Nejdřív sjednoť jednotky.

**Hlavní výpočet:**

1. „100 MB × 8 = 800 Mbit“
2. „800 Mbit ÷ 100 Mbit/s = 8 s ideálně“
3. „reálně déle: režie protokolů + nižší skutečná propustnost“

**Základní převod:** „1 B = 8 b“

**Rozlišení značek:**

- **b = bit** — „jedna dvojková číslice: 0 nebo 1“
- **B = byte** — „osm bitů; 256 možných kombinací“

**Dvě stupnice jednotek:**

- **DESÍTKOVÉ:** „1 kB = 1 000 B • 1 MB = 1 000 000 B • 1 GB = 1 000 000 000 B“
- **BINÁRNÍ:** „1 KiB = 1 024 B • 1 MiB = 1 048 576 B • 1 GiB = 1 073 741 824 B“

**Detail 32/64 BITŮ:** „Označení architektury souvisí s registry, instrukcemi a adresováním. Neznamená, že procesor vždy zpracuje přesně tolik bitů najednou.“

**Blok POZOR:** „Velké `B` není typografický detail. Záměna 100 MB a 100 Mbit znamená osminásobný rozdíl ještě před započtením režie.“

## Obrazová koncepce a kompozice

Dominantou je **měřicí a přenosová brána** mezi souborem a sítí. Vlevo stojí čistý 3D datový kontejner označený `100 MB`; jeho průhledný řez ukazuje, že každý byte se skládá z osmi bitových pozic. Kontejner projde převodní bránou `× 8` a napravo se rozvine do dlouhého pásu `800 Mbit`, který vstupuje do síťového kanálu s nominální rychlostí `100 Mbit/s`.

Pod kanálem je přesná časová osa s osmi stejně dlouhými sekundovými úseky. Na konci osmého úseku stojí značka „ideální minimum“. Za ní pokračuje kratší šrafovaný úsek „režie a nižší skutečná propustnost“, jehož délku neurčovat konkrétním číslem. Tok tak vysvětluje jednotky i podíl velikost/rychlost, ne pouze hotový výsledek.

V levém dolním rohu je makrodetail jednoho bytu: osm fyzicky oddělených pozic s ukázkovou bitovou kombinací, vedle jasné `1 B = 8 b`. V pravé horní části jsou dvě nesouměrné kalibrační stupnice od stejného počátku: desítková po násobcích 1000 a binární po násobcích 1024. Mají odlišné tvary značek, aby rozdíl nebyl založen jen na barvě.

Detail „32/64 BITŮ“ pojmout jako malou lupu do procesoru: registr, adresování a instrukce jsou tři různé vazby z jediného označení. Nezobrazovat obecné tvrzení „64 bitů = dvakrát rychlejší“. Varování je napojené přímo na velká písmena `b/B` v hlavním výpočtu.

## Vizuální metafora

Soubor je **objem nákladu** a přenosová rychlost **průtok kanálu**. Čas vznikne jako podíl objemu a průtoku až po převodu na shodné jednotky. Metafora nesmí sugerovat pevný reálný čas přenosu: skutečný průtok ovlivňuje režie, síťové podmínky a další části cesty.

## Produkční prompt

> Vytvoř profesionální český infografický snímek 16:9, 1600 × 900 px, na bílém pozadí. Nahoře výrazná tmavě modrá lišta s názvem „PROČ 100 MB NENÍ 100 Mbit“ a podnázev „Soubor měříme v bytech, síť často v bitech za sekundu. Nejdřív sjednoť jednotky.“ Dominantní měřicí a přenosová brána: vlevo čistý 3D datový kontejner `100 MB` s řezem do bytů, uprostřed brána `× 8`, napravo dlouhý pás `800 Mbit` vstupující do síťového kanálu `100 Mbit/s`. Pod kanálem přesná osa osmi sekund s výpočtem „100 MB × 8 = 800 Mbit“, „800 Mbit ÷ 100 Mbit/s = 8 s ideálně“ a za osmou sekundou šrafovaný neurčitý úsek „reálně déle: režie protokolů + nižší skutečná propustnost“. Vlevo dole makrodetail „1 B = 8 b“ a přesné rozlišení „b = bit — jedna dvojková číslice: 0 nebo 1“ a „B = byte — osm bitů; 256 možných kombinací“. Vpravo nahoře dvě kalibrační stupnice: „DESÍTKOVÉ — 1 kB = 1 000 B • 1 MB = 1 000 000 B • 1 GB = 1 000 000 000 B“ a „BINÁRNÍ — 1 KiB = 1 024 B • 1 MiB = 1 048 576 B • 1 GiB = 1 073 741 824 B“. Přidej malou lupu „32/64 BITŮ“ s vazbou na registry, instrukce a adresování a oranžový blok „POZOR“. Velké české písmo, důsledně správná velikost písmen ve značkách, technická modro-tyrkysová estetika, oranžová pro převod a šrafování pro režii. Bez dětského vláčku z bitů, bez tvrzení o přesném reálném čase, bez záměny MB a MiB, pseudo-textu nebo falešných log.

## Kontrolní bod

Časová osa musí mít přesně osm ideálních sekund a teprve poté neurčitý úsek režie. Všechny výskyty `b`, `B`, `MB`, `Mbit/s`, `KiB`, `MiB` a `GiB` musejí zachovat správnou velikost písmen.

---

# Poznámka k návaznosti série

Pět snímků zachovává vizuální podpis 1. lekce, ale každý používá jiný vysvětlující mechanismus:

| Téma | Hlavní forma | Praktická situace | Co má student z obrazu vyčíst |
| --- | --- | --- | --- |
| 2.1 Informace a signál | technický průřez proměnami nosiče | zpráva mezi dvěma telefony | význam se zachovává, fyzická reprezentace se mění |
| 2.2 Analogový a digitální svět | dvě větve jednoho zvukového experimentu | záznam a kopírování zvuku | omezení digitalizace není totéž co degradace další kopie |
| 2.3 Vzorkování | stroboskopický časový experiment | zdánlivě obrácený pohyb kola | příliš řídké měření může vytvořit jiný průběh |
| 2.4 Kvantování | společný průběh nad dvěma měřicími schodišti | PCM zvuk se dvěma bitovými hloubkami | více úrovní zmenšuje odchylku, ale zvětšuje data |
| 2.5 Bit, byte a velikost dat | přenosová brána s přesnou časovou osou | přenos souboru 100 MB | velikost a rychlost lze porovnat až ve stejných jednotkách |

Série postupuje od obecného vztahu informace a fyzického nosiče přes vlastní digitalizaci až k praktickému množství dat. Při generování je vhodné zvlášť kontrolovat směry převodů, polohy vzorků, shodné osy při srovnávání kvantování a přesnou velikost písmen v jednotkách.
