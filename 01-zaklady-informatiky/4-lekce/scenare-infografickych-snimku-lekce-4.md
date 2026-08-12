# Scénáře infografických snímků — 4. lekce

## Přenos dat

Sada pro témata 4.1–4.6 z výukového textu *Základy informatiky*. Každý scénář je samostatné zadání pro grafika, prezentační nástroj i generátor obrazu. Všechny texty určené přímo na snímek jsou uvedeny v přesném znění; delší formulace lze při generování obrazu vysázet dodatečně v prezentačním editoru.

## Společný vizuální rámec série

- Formát 16:9, ideálně 1600 × 900 px; bílé až velmi světle šedé pozadí, bezpečný okraj minimálně 40 px.
- Profesionální akademicko-technologický styl pro studenty střední školy. Bez infantilních ikon, náhodných nul a jedniček, neonového sci-fi rozhraní, falešných ovládacích panelů a dekorativního zahlcení.
- Tmavě modrá horní lišta, velké bílé bezpatkové písmo s českou diakritikou. Nadpis přibližně 44–54 px, podnadpis 25–30 px, běžný text nejméně 22–24 px.
- Paleta navazuje na předchozí lekce: námořnická modř pro strukturu, střední modř pro data, tyrkysová pro správný tok signálu, oranžová pro aktivní změnu nebo čekání, červená pouze pro rušení, chybu či ztrátu.
- Logická data, fyzický signál a řídicí zpětnou vazbu odlišovat nejen barvou, ale také tvarem: datové bloky, spojité průběhy a přerušované řídicí šipky. Šipky používat pouze pro skutečný směr přenosu, potvrzení nebo závislosti.
- Jeden dominantní vysvětlující mechanismus na snímek, maximálně pět vedlejších obsahových bloků. V časových diagramech musí být pořadí událostí jednoznačné; u signálů nesmějí dekorativní křivky předstírat konkrétní technický standard.
- Číselné hodnoty, jednotky a bitové zápisy sázet neproporcionálním písmem. Důsledně rozlišovat `bit/s`, `Bd`, `ms`, `b` a `B`.
- Pokud obrazový generátor nezvládá přesnou českou sazbu, vytvořit vizuál s rezervovanými plochami a text doplnit až v editoru. Nevkládat pseudo-text, falešná loga ani vodoznaky.

---

# Snímek 4.1 — Obecný model datové komunikace

## Výukový záměr

Student má pochopit komunikaci jako řetězec převodů mezi zdrojem a příjemcem. Má odlišit obsah sdělení od jeho dočasné fyzické reprezentace, rozpoznat místo působení šumu a chápat zpětnou vazbu jako samostatnou řídicí cestu, nikoli jako součást původní zprávy.

**Hlavní otázka:** Co všechno se musí stát, aby druhý člověk při videohovoru uslyšel naši větu?

**Nosná teze:** Přenášený význam zůstává zachován jen tehdy, když na sebe správně navazují kódování, fyzický přenos, příjem a interpretace.

## Přesné texty na snímku

**Název:** OD MYŠLENKY K PŘIJATÉ ZPRÁVĚ

**Podnázev:** Komunikace je řetězec převodů; šum působí na signál, zpětná vazba řídí spolehlivost.

**Hlavní komunikační cesta:**

1. **ZDROJ** — „mluvčí vytvoří sdělení“
2. **KÓDOVÁNÍ** — „zvuk se změní na digitální reprezentaci“
3. **VYSÍLAČ** — „zařízení vytvoří signál vhodný pro médium“
4. **KANÁL** — „signál prochází fyzickým prostředím“
5. **PŘIJÍMAČ** — „zařízení rozpozná přijaté symboly“
6. **DEKÓDOVÁNÍ** — „z dat znovu vznikne zvuk“
7. **PŘÍJEMCE** — „posluchač interpretuje význam“

**Vstup do kanálu:** **ŠUM A RUŠENÍ** — „mohou změnit nebo znejasnit přijatý signál“

**Zpětná cesta:** **POTVRZENÍ / POŽADAVEK NA OPAKOVÁNÍ** — „příjemce dává systému informaci o výsledku přenosu“

**Dvě vrstvy:**

- **OBSAH:** „věta „Přijdu v pět““
- **REPREZENTACE:** „zvuk → vzorky → pakety → rádiový, elektrický nebo optický signál“

**Blok POZOR:** „Potvrzení neznamená, že člověk sdělení pochopil. Potvrzuje pouze stav přenosu podle pravidel daného systému.“

## Obrazová koncepce a kompozice

Dominantou je **průhledný řez videohovorem mezi dvěma místnostmi**. Na levém okraji vysloví mluvčí větu „Přijdu v pět“, na pravém okraji ji druhý člověk uslyší. Mezi nimi probíhá jediná horizontální komunikační dráha tvořená sedmi funkčně odlišnými stanicemi. Stanice nemají být stejné kartičky: zdroj je realistický člověk, kódování detail zvukové vlny přecházející do vzorků, vysílač rádiový modul, kanál řez několika fyzickými úseky, přijímač rekonstrukce symbolů a dekódování převod zpět na zvukovou vlnu.

Nad hlavní cestou vede tenká námořnicky modrá **významová nit** s textem věty. Pod ní se reprezentace viditelně mění: akustický tlak, číselné bloky, paket, fyzický průběh, znovu data a zvuk. Nit nemá naznačovat, že stejný fyzický předmět putuje celou trasou; v převodnících se vždy znovu vytváří jiná reprezentace.

Ve středu snímku je kanál zvětšený jako transparentní tunel. Z horního okraje do něj vstupuje rušivý červenooranžový průběh a mírně deformuje signál. Přijímač na konci tunelu porovnává přijaté stavy s rozhodovacími oblastmi. Ze stanice příjemce se spodním obloukem vrací přerušovaná řídicí cesta s potvrzením; při chybě se cesta změní na požadavek opakování. Datová cesta a zpětná vazba se nesmějí slít do jedné obousměrné šipky.

V dolním pásu je stručné srovnání „OBSAH / REPREZENTACE“ a malý blok „POZOR“. Celý panel má fungovat jako anatomie jediné komunikace, nikoli jako obecná síťová mapa.

## Vizuální metafora

Komunikace je **štafetový překlad mezi několika přesně navazujícími pracovišti**. Každé pracoviště předává dál nově vytvořenou reprezentaci téhož zamýšleného sdělení. Metafora má limit: význam věty není fyzický předmět a na technické úrovni nelze potvrdit lidské porozumění.

## Produkční prompt

> Vytvoř profesionální český výukový infografický snímek 16:9, 1600 × 900 px, na bílém až velmi světle šedém pozadí. Nahoře tmavě modrá lišta s názvem „OD MYŠLENKY K PŘIJATÉ ZPRÁVĚ“ a podnázev „Komunikace je řetězec převodů; šum působí na signál, zpětná vazba řídí spolehlivost.“ Dominantní průhledný řez videohovorem mezi dvěma lidmi. Jedna hlavní cesta zleva doprava má sedm přesně označených stanic: „1 ZDROJ“, „2 KÓDOVÁNÍ“, „3 VYSÍLAČ“, „4 KANÁL“, „5 PŘIJÍMAČ“, „6 DEKÓDOVÁNÍ“, „7 PŘÍJEMCE“ a uvedené krátké popisky. Nad cestou drž významovou nit s větou „Přijdu v pět“, zatímco fyzická reprezentace se mění ze zvuku na vzorky, pakety, rádiový, elektrický či optický signál a zpět. Do kanálu shora vstupuje „ŠUM A RUŠENÍ“. Spodní přerušovaná řídicí cesta vede zprava doleva jako „POTVRZENÍ / POŽADAVEK NA OPAKOVÁNÍ“. Přidej srovnání „OBSAH / REPREZENTACE“ a malý blok „POZOR“. Modro-tyrkysová technická estetika, jemné realistické řezy zařízení, velké české písmo, přesné směry šipek a dostatek volného prostoru. Bez putujících písmen v kabelu, bez jediné obousměrné šipky pro data i potvrzení, bez pseudo-textu, falešných log a technicky nesmyslných detailů.

## Kontrolní bod

Hlavní data musejí proudit od zdroje k příjemci, zatímco potvrzení nebo žádost o opakování se vrací opačným směrem. Šum musí působit na fyzický kanál, ne přímo na významovou větu.

---

# Snímek 4.2 — Jak data fyzicky cestují

## Výukový záměr

Student má pochopit, že jediný logický přenos může postupně využít několik fyzických médií a v každém z nich jiný fyzikální jev. Má rozlišit protokol od média a chápat volbu přenosové cesty jako kompromis mezi dosahem, kapacitou, odolností, mobilitou, cenou a bezpečností.

**Hlavní otázka:** Jak se fotografie z telefonu promění na rádiovou vlnu, elektrický signál a světelné impulzy, aniž by přestala být stejnými daty?

**Nosná teze:** Protokol určuje logická pravidla komunikace; médium určuje fyzickou podobu signálu na konkrétním úseku.

## Přesné texty na snímku

**Název:** JEDNA FOTOGRAFIE, TŘI FYZICKÉ SVĚTY

**Podnázev:** Logická data pokračují; na každém úseku se nově vytvoří signál vhodný pro dané médium.

**Trasa fotografie:**

1. **WI‑FI — ELEKTROMAGNETICKÁ VLNA** — „mobilita • sdílené prostředí • vliv překážek a rušení“
2. **METALICKÉ VEDENÍ — ELEKTRICKÝ SIGNÁL** — „vedená cesta • útlum • citlivost na elektromagnetické rušení“
3. **OPTICKÉ VLÁKNO — SVĚTELNÉ IMPULZY** — „vysoká kapacita • dlouhé vzdálenosti • odolnost vůči elektromagnetickému rušení“

**Převodní uzly:** „přijmout signál → obnovit data → vytvořit nový signál“

**Logická vrstva:** „fotografie rozdělená do paketů“

**Fyzická vrstva:** „rádiové pole • elektrické veličiny • světlo ve vlákně“

**Blok PROTOKOL ≠ MÉDIUM:** „IP může procházet přes Wi‑Fi, Ethernet, optiku i mobilní síť. Jedna technologie není navždy svázána s jedním nosičem.“

**Bezpečnostní blok:** „Kabel omezuje fyzický přístup, ale sám obsah nechrání. Důvěrnost řeší šifrování a další pravidla systému.“

## Obrazová koncepce a kompozice

Dominantou je **izometrický řez skutečnou cestou fotografie do cloudového datového centra**. Vlevo telefon odešle fotografii přes prostorový rádiový segment k přístupovému bodu. Odtud cesta pokračuje krátkým řezem kroucenou metalickou dvojlinkou do síťového uzlu a dále dlouhým optickým vláknem do datového centra v pravé části. Stejný malý modrý paketový identifikátor se objevuje nad každým úsekem v logické vrstvě, ale pod ním se fyzický signál mění.

Každý úsek je vykreslen jinou technikou: Wi‑Fi jako prostorové vlnoplochy procházející místností a částečně zeslabené zdí; metalika jako zvětšený řez párem vodičů s diferenciálním elektrickým průběhem; optika jako podélný 3D řez jádrem a pláštěm s vedeným světelným impulzem. Nezobrazovat světlo jako paprsek poskakující v ostrých cik-cak odrazech po celé délce; stačí názorné vedení energie v jádře bez předstírání přesného fyzikálního modelu.

V obou převodních uzlech je tříkrokový detail „přijmout → obnovit → vyslat“. Tím se odstraní omyl, že původní rádiová nebo elektrická vlna fyzicky pokračuje do dalšího média. Nad celou trasou probíhá tenká modrá logická vrstva paketů, pod ní tři fyzické řezy. V dolní části je nepravidelná trojice stručných profilů médií a blok „PROTOKOL ≠ MÉDIUM“.

Praktický bezpečnostní detail ukáže, že rádiové pole přesahuje stěnu místnosti, zatímco kabel vede konkrétní trasou; vedle obou však zůstává stejný symbol šifrovaného obsahu. Smyslem není označit některé médium za automaticky bezpečné.

## Vizuální metafora

Datová cesta připomíná **cestu jedné zásilky po silnici, železnici a moři**, avšak technicky přesnější je představa překladišť: na každém úseku vzniká nový fyzický nosič podle pravidel daného rozhraní. Limit metafory: paket není jedna neměnná krabice a na trase může být dělen, spojován nebo zpracován více vrstvami.

## Produkční prompt

> Vytvoř profesionální český infografický snímek 16:9, 1600 × 900 px, bílé až světle šedé pozadí, tmavě modrá horní lišta. Přesný název „JEDNA FOTOGRAFIE, TŘI FYZICKÉ SVĚTY“, podnázev „Logická data pokračují; na každém úseku se nově vytvoří signál vhodný pro dané médium.“ Dominantní izometrický technický řez cestou fotografie z telefonu do datového centra. Úsek 1 „WI‑FI — ELEKTROMAGNETICKÁ VLNA“ z telefonu k přístupovému bodu, prostorové vlnoplochy a překážka. Úsek 2 „METALICKÉ VEDENÍ — ELEKTRICKÝ SIGNÁL“, zvětšený řez kroucenou dvojlinkou a vedený elektrický průběh. Úsek 3 „OPTICKÉ VLÁKNO — SVĚTELNÉ IMPULZY“, podélný řez jádrem a pláštěm s vedeným světlem do datového centra. V převodních uzlech přesný postup „přijmout signál → obnovit data → vytvořit nový signál“. Nad fyzickými řezy společná logická vrstva „fotografie rozdělená do paketů“. Přidej stručné vlastnosti všech médií, blok „PROTOKOL ≠ MÉDIUM“ a bezpečnostní poznámku, že kabel sám obsah nešifruje. Modro-tyrkysová série, oranžová pouze pro aktivní převod, velké české písmo, přesné šipky a velkorysý bílý prostor. Bez putujících nul a jedniček, bez jediného nepřerušeného fyzického signálu přes všechna média, bez tvrzení, že Wi‑Fi nebo kabel je automaticky bezpečný, bez pseudo-textu a falešných log.

## Kontrolní bod

V každém převodním uzlu se musí fyzická reprezentace ukončit a z dat vzniknout nový signál pro další médium. Logická fotografie může pokračovat přes celou trasu, ale rádiová vlna nesmí přecházet přímo do vodiče ani optického vlákna.

---

# Snímek 4.3 — Rychlost, propustnost, baud, latence a jitter

## Výukový záměr

Student má rozlišit několik nezávislých vlastností spojení a vybrat metriku, která skutečně ovlivňuje danou aplikaci. Má pochopit, že bitová rychlost není totéž co užitečná propustnost, vysoká kapacita nezaručuje malou latenci a baud udává počet symbolů, nikoli obecně počet bitů.

**Hlavní otázka:** Proč může být spojení výborné pro stahování a současně nepříjemné pro videohovor nebo hru?

**Nosná teze:** Kvalitu spojení neurčuje jediné číslo; aplikace potřebují jinou kombinaci kapacity, zpoždění a stability.

## Přesné texty na snímku

**Název:** RYCHLÝ INTERNET NENÍ JEDNO ČÍSLO

**Podnázev:** Kapacita, užitečný tok, zpoždění a jeho kolísání měří odlišné vlastnosti spojení.

**Čtyři měřicí přístroje:**

- **BITOVÁ RYCHLOST** — „kolik bitů za sekundu linka přenáší • `bit/s`“
- **PROPUSTNOST** — „kolik užitečných dat skutečně dorazí za sekundu“
- **LATENCE** — „jak dlouho trvá cesta informace • `ms`“
- **JITTER** — „jak moc se zpoždění jednotlivých částí mění • `ms`“

**Kam mizí kapacita:** „hlavičky • potvrzování • čekání • sdílení média • opakované přenosy“

**Symbolová lupa:**

- „`1 000 Bd` = 1 000 symbolů/s“
- „2 rozlišitelné symboly → 1 bit na symbol → `1 000 bit/s`“
- „4 rozlišitelné symboly → 2 bity na symbol → `2 000 bit/s`“

**Aplikační profily:**

- **VELKÝ SOUBOR:** „hlavně vysoká propustnost“
- **VIDEOHOVOR:** „dostatečný tok + nízká latence + malý jitter“
- **ONLINE HRA:** „málo dat, ale velmi citlivá na latenci a jitter“

**Blok POZOR:** „Baud a bit/s jsou stejné jen tehdy, když jeden symbol skutečně nese právě jeden bit.“

## Obrazová koncepce a kompozice

Dominantou je **diagnostická zkušební dráha pro tři různé aplikace**. Přes střed vede široký průhledný datový tunel. Jeho šířka vyjadřuje dostupnou bitovou rychlost, skutečně projíždějící modré bloky užitečných dat propustnost, stopky mezi vstupem a výstupem latenci a nepravidelné rozestupy bloků jitter. Všechny čtyři vlastnosti jsou současně patrné na jednom fyzickém modelu, ale mají vlastní tvar a měřidlo.

Do stejného tunelu se postupně vloží tři „testovací náklady“. Velký soubor je souvislý náklad, kterému vadí úzký tunel, ale snese delší cestu. Videohovor je pravidelný sled zvukových a obrazových dílků; při nepravidelných rozestupech se v přijímacím časovém zásobníku objevují mezery. Online hra posílá malé řídicí impulzy, ale dlouhé stopky mezi akcí a odezvou způsobí viditelně opožděnou reakci. Nezobrazovat aplikace jako soutěž aut; má jít o technickou zkušebnu s časovou osou.

V levé dolní části je řez kapacitou: z celé šířky linky ukrojí část protokolové hlavičky, potvrzení a čekání, takže užitečný tok je užší. V pravé části je **symbolová lupa**: hodinový takt vytvoří přesně 1 000 symbolových intervalů za sekundu; pod jedním intervalem jsou dvě možné úrovně pro jeden bit a vedle čtyři stavy označené `00, 01, 10, 11` pro dva bity. Neodvozovat z toho univerzální rychlost reálné modulace, jde o názorný ideální příklad vztahu symbolů a bitů.

## Vizuální metafora

Spojení je **tunel s určitou šířkou, délkou a pravidelností průjezdu**. Šířka odpovídá kapacitě, doba průchodu latenci a kolísání rozestupů jitteru. Metafora má limit: datové sítě nejsou tekutina ani silnice a propustnost ovlivňují protokoly, sdílení i chybovost.

## Produkční prompt

> Navrhni profesionální český výukový snímek 16:9, 1600 × 900 px, na bílém pozadí s tmavě modrou horní lištou. Název „RYCHLÝ INTERNET NENÍ JEDNO ČÍSLO“, podnázev „Kapacita, užitečný tok, zpoždění a jeho kolísání měří odlišné vlastnosti spojení.“ Dominantní technická diagnostická dráha: šířka průhledného datového tunelu vyjadřuje „BITOVÁ RYCHLOST“, množství skutečně doručených modrých bloků „PROPUSTNOST“, stopky od vstupu k výstupu „LATENCE“ a nepravidelné rozestupy bloků „JITTER“. Na stejné dráze ukaž profily „VELKÝ SOUBOR“, „VIDEOHOVOR“ a „ONLINE HRA“ s uvedenými potřebami. Dole ukaž, jak hlavičky, potvrzování, čekání, sdílení média a opakování zmenšují užitečný tok. Vpravo přesná symbolová lupa: „1 000 Bd = 1 000 symbolů/s“, dva symboly znamenají v názorném příkladu jeden bit na symbol a čtyři symboly `00, 01, 10, 11` dva bity na symbol. Přidej blok „POZOR“ s větou, že baud a bit/s nejsou obecně totéž. Velké české písmo, přesné jednotky `bit/s`, `Bd`, `ms`, tvary a časové značky podporující význam barev. Bez jednoho univerzálního tachometru, bez záměny Mbit/s a MB/s, bez tvrzení, že vyšší propustnost automaticky snižuje latenci, bez pseudo-textu.

## Kontrolní bod

Čtyři metriky musejí být z diagramu rozlišitelné i bez barvy. Symbolová lupa musí ukazovat, že baud počítá symboly a počet bitů na symbol závisí na počtu spolehlivě rozlišitelných stavů.

---

# Snímek 4.4 — Kódování signálu a modulace

## Výukový záměr

Student má pochopit, že bity se nepřenášejí přímo: vysílač je mapuje na fyzicky rozlišitelné symboly a přijímač provádí opačné rozhodnutí. Má rozlišit linkové kódování v základním pásmu od modulace nosné a chápat, proč kvalitnější spojení umožní rozlišovat více stavů a přenést více bitů na symbol.

**Hlavní otázka:** Jak se abstraktní skupina bitů promění v měřitelnou změnu signálu?

**Nosná teze:** Symbol je dohodnutý fyzický stav nebo změna; více stavů přenese více bitů, ale vyžaduje přesnější rozlišení v přítomnosti šumu.

## Přesné texty na snímku

**Název:** BITY MUSÍ DOSTAT FYZICKÝ TVAR

**Podnázev:** Vysílač mapuje data na symboly signálu; přijímač je v šumu znovu rozlišuje.

**Vstup:** `00 • 01 • 10 • 11`

**Dvě převodní cesty:**

- **ZÁKLADNÍ PÁSMO — LINKOVÝ KÓD:** „data řídí změny elektrického nebo optického průběhu podle pravidla“
- **MODULACE NOSNÉ:** „symbol mění amplitudu, frekvenci, fázi nebo jejich kombinaci“

**Tři vlastnosti nosné:**

- **AMPLITUDA** — „velikost kmitu“
- **FREKVENCE** — „rychlost kmitání“
- **FÁZE** — „poloha v periodě“

**Konstelační mapa:** „jeden bod = jeden rozlišitelný symbol“

**Dvě podmínky:**

- **ČISTÝ SIGNÁL:** „body jsou oddělené → lze použít více symbolů → více bitů na symbol“
- **RUŠENÍ:** „body se rozmazávají → hrozí záměna → robustnější režim používá méně stavů“

**Blok POZOR:** „Modulace není pouhé „digitální → analogové“. Informační symboly mění parametry fyzického signálu podle dohodnutého pravidla.“

## Obrazová koncepce a kompozice

Dominantou je **překladový stůl mezi bitovými skupinami a fyzickým signálovým prostorem**. Z levého vstupu přicházejí čtyři skupiny `00, 01, 10, 11`. Uprostřed se cesta rozděluje: horní větev ukazuje jednoduchý názorný linkový kód jako posloupnost přesně časovaných změn úrovně v základním pásmu; dolní větev vede k nosné vlně, jejíž amplituda, frekvence nebo fáze se mění podle symbolu. Průběhy mají být označené jako funkční schéma, nikoli konkrétní Ethernet či Wi‑Fi standard.

Pravou polovinu zabírá **konstelační observatoř**. Ve středu souřadnicového pole jsou nejprve čtyři jasně oddělené body označené bitovými dvojicemi. Přes ně se posune průsvitná vrstva šumu: z bodů vzniknou malé mraky. Tenké rozhodovací hranice ukazují, kdy přijímač bod přiřadí nesprávnému symbolu. Nad mapou je posuvný technický přepínač „kvalita spojení“: při dobrých podmínkách se mapa rozvine na více hustších bodů, při rušení se vrátí k menšímu počtu vzdálenějších bodů. Neuvádět konkrétní standard ani tvrdit, že systém vždy adaptaci používá.

Mezi bitovým vstupem a signálovým výstupem je jasně vidět dvojice zařízení „MAPOVÁNÍ / ROZHODOVÁNÍ“. Vysílač přiřadí bitové skupině symbol; přijímač pouze odhaduje nejbližší platný symbol z měření zatíženého šumem. V dolním pásu je trojice drobných průběhů amplitudy, frekvence a fáze a blok „POZOR“.

## Vizuální metafora

Modulace je **abeceda napsaná polohami v signálovém prostoru**. Více znaků abecedy unese více informace, ale v mlze se podobné znaky snadněji spletou. Metafora má limit: reálný přijímač nečte body očima a moderní systémy používají kódování, filtry a časovou synchronizaci, které zde nejsou zobrazeny.

## Produkční prompt

> Vytvoř sofistikovaný český výukový snímek 16:9, 1600 × 900 px, bílé pozadí, tmavě modrá horní lišta s názvem „BITY MUSÍ DOSTAT FYZICKÝ TVAR“. Podnázev „Vysílač mapuje data na symboly signálu; přijímač je v šumu znovu rozlišuje.“ Dominantní překladový stůl: bitové skupiny `00 • 01 • 10 • 11` vstupují do dvou názorných cest. Horní „ZÁKLADNÍ PÁSMO — LINKOVÝ KÓD“ ukazuje přesně časované změny elektrického nebo optického průběhu. Dolní „MODULACE NOSNÉ“ ukazuje, že symbol mění amplitudu, frekvenci, fázi nebo jejich kombinaci. Vpravo velká konstelační mapa se čtyřmi body `00, 01, 10, 11`, rozhodovacími oblastmi a druhou vrstvou, v níž šum mění body na mraky a hrozí záměna. Ukaž kontrast „ČISTÝ SIGNÁL — více rozlišitelných symbolů“ versus „RUŠENÍ — méně, ale vzdálenějších a robustnějších symbolů“. Mezi vstupem a výstupem označ „MAPOVÁNÍ“ a opačné „ROZHODOVÁNÍ“. Dole tři krátké průběhy „AMPLITUDA“, „FREKVENCE“, „FÁZE“ a blok „POZOR“. Čistá modro-tyrkysová vědecká estetika, oranžová pro aktivní parametr, červená pouze pro chybnou rozhodovací oblast, velké české písmo. Bez pravidla „0 = žádné napětí, 1 = napětí“ vydávaného za obecný princip, bez tvrzení, že modulace je jen převod digitálního na analogové, bez falešných Wi‑Fi log, pseudo-textu a náhodných vln.

## Kontrolní bod

Bitové skupiny musejí být mapovány na symboly a teprve ty na fyzický průběh. Při šumu se musí zhoršovat rozlišitelnost bodů; snímek nesmí tvrdit, že více stavů je vždy výhodnější bez ohledu na kvalitu spojení.

---

# Snímek 4.5 — Jak poznáme, že se data poškodila?

## Výukový záměr

Student má pochopit detekci chyb jako porovnání redundance vytvořené odesílatelem s hodnotou znovu vypočtenou příjemcem. Má rozlišit paritu, kontrolní součet a CRC podle jejich schopností a chápat, že zjištění nesouladu obvykle samo neurčí, který bit opravit. Současně nesmí zaměnit CRC za kryptografickou ochranu.

**Hlavní otázka:** Jak může přijímač odhalit změnu, když původní data nemá vedle sebe pro přímé porovnání?

**Nosná teze:** Odesílatel přidá krátký kontrolní údaj; příjemce jej z dat vypočítá znovu a nesoulad odhalí poškození.

## Přesné texty na snímku

**Název:** DATOVÁ DETEKTIVKA: SEDÍ KONTROLNÍ STOPA?

**Podnázev:** Redundance umožní odhalit změnu, i když příjemce nezná původní obsah.

**Společný postup:**

1. **ODESÍLATEL VYPOČÍTÁ KONTROLU**
2. **DATA + KONTROLNÍ ÚDAJ PROJDOU KANÁLEM**
3. **PŘÍJEMCE VÝPOČET ZOPAKUJE**
4. **SHODA = PŘIJATO • NESHODA = CHYBA**

**Paritní experiment:**

- „sudá parita: `1011001 | P=0` → celkem 4 jedničky“
- „změna jednoho bitu → lichý počet → chyba odhalena“
- „dvě změny mohou sudou paritu zachovat“

**Tři nástroje:**

- **PARITA** — „velmi jednoduchá • zachytí každou jednotlivou bitovou chybu • ne všechny vícenásobné chyby“
- **KONTROLNÍ SOUČET** — „krátká hodnota vypočtená z bloků dat • schopnosti závisejí na použitém pravidle“
- **CRC** — „matematicky navržené pro účinnou detekci typických přenosových chyb a shluků chyb“

**Blok DETEKCE ≠ OPRAVA:** „Neshoda říká, že data nejsou v pořádku. Sama obvykle neukáže, který konkrétní bit změnit.“

**Bezpečnostní blok:** „CRC chrání proti náhodným chybám přenosu, ne proti útočníkovi, který data i kontrolu záměrně přepočítá.“

## Obrazová koncepce a kompozice

Dominantou je **forenzní kontrolní brána rozdělená na odesílací a přijímací laboratoř**. Vlevo vstoupí modrý datový blok do výpočtového razidla a získá malou kontrolní stopu. Uprostřed prochází dvojice „data + stopa“ kanálem, kde červený výboj změní jeden datový bit, nikoli kontrolní údaj. Vpravo přijímač provede ze skutečně přijatých dat tentýž výpočet a položí novou stopu přes přiloženou. Dokonalé překrytí vede zelenomodrou cestou „SHODA“, nesoulad červenooranžovou cestou „CHYBA“.

Pod hlavní bránou je mechanický **paritní stůl** se sedmi datovými destičkami `1011001` a jednou destičkou `P=0`. Čtyři jedničky udrží váhu v sudé poloze. Jediný překlopený bit váhu vychýlí; vedle je stručný detail dvou překlopení, která rovnováhu obnoví, přestože data jsou chybná. Paritní metafora musí přesně odpovídat počtu jedniček.

V pravé dolní části jsou tři různě robustní nástroje: jednoduchá paritní váha, součtové razidlo a CRC převodovka s polynomickým symbolem bez zbytečného matematického rozvoje. CRC nemá být zobrazeno jako zámek nebo štít proti hackerovi. Blok „DETEKCE ≠ OPRAVA“ je připojen přímo k chybové větvi, která končí otazníkem nad polohou chyby, nikoli automatickou opravou bitu.

## Vizuální metafora

Kontrolní údaj je **pečeť vytvořená z obsahu zásilky**. Příjemce nevěří jen vzhledu pečeti; z doručeného obsahu vytvoří novou a obě porovná. Metafora má limit: běžné CRC není tajná ani nepadělatelná bezpečnostní pečeť a útočník může kontrolní hodnotu záměrně přepočítat.

## Produkční prompt

> Vytvoř profesionální český výukový infografický snímek 16:9, 1600 × 900 px, bílé až světle šedé pozadí a tmavě modrá horní lišta. Název „DATOVÁ DETEKTIVKA: SEDÍ KONTROLNÍ STOPA?“, podnázev „Redundance umožní odhalit změnu, i když příjemce nezná původní obsah.“ Dominantní forenzní kontrolní brána ve čtyřech krocích: „1 ODESÍLATEL VYPOČÍTÁ KONTROLU“, „2 DATA + KONTROLNÍ ÚDAJ PROJDOU KANÁLEM“, „3 PŘÍJEMCE VÝPOČET ZOPAKUJE“, „4 SHODA = PŘIJATO • NESHODA = CHYBA“. V kanálu změň jediný bit a vpravo vizuálně porovnej původní přiloženou kontrolu s nově vypočtenou hodnotou. Dole přesný paritní experiment `1011001 | P=0`: čtyři jedničky znamenají sudou paritu, změna jednoho bitu chybu odhalí, dvě změny ji mohou skrýt. Přidej tři odlišné nástroje „PARITA“, „KONTROLNÍ SOUČET“, „CRC“ s dodanými texty. Výrazně ukaž „DETEKCE ≠ OPRAVA“ a bezpečnostní poznámku, že CRC není kryptografická ochrana proti záměrné změně. Velké české písmo, monospace bitové zápisy, jasné porovnání hodnot, červená pouze pro skutečný nesoulad. Bez zámku u CRC, bez automatického ukázání polohy chyby, bez tvrzení, že parita zachytí všechny chyby, bez pseudo-textu a falešných rovnic.

## Kontrolní bod

Zápis `1011001` musí obsahovat přesně čtyři jedničky a sudý paritní bit musí být `0`. Snímek musí ukázat, že shoda kontrolních hodnot je test integrity proti náhodným chybám, nikoli důkaz pravosti nebo automatická lokalizace chyby.

---

# Snímek 4.6 — Co s chybou uděláme: retransmise a FEC

## Výukový záměr

Student má rozlišit dvě strategie reakce na chybu: ARQ využívá zpětnou vazbu a opakovaný přenos, zatímco FEC předem přidává opravnou redundanci, aby přijímač zvládl některé chyby bez čekání. Má umět zvolit strategii podle dostupnosti zpětného kanálu, ceny zpoždění a množství přidaných dat.

**Hlavní otázka:** Kdy je lepší poškozená data poslat znovu a kdy přidat „opravnou rezervu“ předem?

**Nosná teze:** ARQ platí časem a zpětnou komunikací; FEC platí předem větším objemem dat. Ani jedna strategie není univerzálně nejlepší.

## Přesné texty na snímku

**Název:** OPAKOVAT, NEBO OPRAVIT ZA JÍZDY?

**Podnázev:** Dvě strategie spolehlivosti směňují čas, kapacitu a množství přidané redundance.

**Levá větev — ARQ: OPAKOVANÝ PŘENOS**

1. „odeslat blok“
2. „chyba nebo ztráta“
3. „nepřijde potvrzení / přijde požadavek“
4. „odeslat blok znovu“

„Potřebuje zpětnou cestu a čas na další pokus.“

„Vhodné: soubor, webová data, situace, kde musí být výsledek přesný a lze čekat.“

**Pravá větev — FEC: DOPŘEDNÁ OPRAVA CHYB**

1. „přidat opravná data“
2. „odeslat větší kódovaný blok“
3. „část se poškodí“
4. „příjemce opraví chybu v mezích kódu“

„Nepotřebuje nový přenos pro každou opravitelnou chybu.“

„Vhodné: satelitní a bezdrátový přenos, optická média, QR kódy, živé vysílání.“

**Rozhodovací otázky:** „Je zpětný kanál? • Kolik stojí čekání? • Kolik redundance si můžeme dovolit? • Jaké chyby očekáváme?“

**Společná pipeline:** „komprese → přidání opravné redundance → přenos → oprava → dekomprese“

**Blok POZOR:** „FEC opraví jen chyby v mezích konkrétního kódu. Silnější ochrana obvykle znamená více přenášených dat.“

## Obrazová koncepce a kompozice

Dominantou je **rozdělený závod se stejným poškozeným datovým blokem**, ale obě poloviny mají odlišnou geometrii. Levá ARQ větev je časový ping-pong mezi odesílatelem a příjemcem. První blok letí doprava, v kanálu se poškodí, zpět se vrací přerušovaná žádost nebo nastane vypršení časovače a teprve druhý blok dorazí správně. Časová osa se viditelně prodlouží o celou cestu tam a zpět. Potvrzení a opakovaný datový blok musí mít opačné směry a odlišné tvary.

Pravá FEC větev je **řez ochranným kódem**. Původní modré datové díly se před přenosem doplní tyrkysovými redundantními díly a vytvoří větší geometrickou mřížku. Několik dílů se v kanálu poškodí; přijímač využije vztahy v mřížce a doplní je bez návratu k odesílateli. Hranice schopnosti je znázorněna druhým, silněji poškozeným blokem, u něhož oprava skončí symbolem „mimo možnosti kódu“. Neuvádět konkrétní počet opravitelných bitů bez určení kódu.

Uprostřed mezi větvemi je asymetrická rozhodovací váha. Na jedné misce jsou stopky a symbol zpětného kanálu, na druhé dodatečné datové bloky. Čtyři rozhodovací otázky vedou ke dvěma větvím; nejde o tvrzení, že jedna vždy vítězí. Ve spodním pásu probíhá důležitá pipeline: fotografie se nejprve komprimuje, potom se přidá opravná redundance, následuje přenos, oprava a teprve potom dekomprese. Komprese a FEC musejí mít opačné účinky na redundanci a správné pořadí.

Malý přesah obou větví může naznačit, že reálné systémy strategie kombinují: FEC opraví běžné chyby a neopravitelný blok si systém vyžádá znovu. Tento hybrid je vedlejší detail, nikoli třetí hlavní mechanismus.

## Vizuální metafora

ARQ je **návrat pro novou kopii**, FEC je **opravná sada přibalená před cestou**. První šetří přidaná data, dokud chyba nenastane; druhá spotřebuje kapacitu předem, aby se nemusela vracet. Limit metafory: opravná data nejsou univerzální náhradní díly, ale matematicky provázaná redundance konkrétního kódu.

## Produkční prompt

> Vytvoř profesionální český výukový snímek 16:9, 1600 × 900 px, na bílém pozadí s tmavě modrou horní lištou. Přesný název „OPAKOVAT, NEBO OPRAVIT ZA JÍZDY?“, podnázev „Dvě strategie spolehlivosti směňují čas, kapacitu a množství přidané redundance.“ Dominantní asymetrické rozdělení na dvě strategie. Vlevo „ARQ: OPAKOVANÝ PŘENOS“ jako přesný časový diagram odesílatel–příjemce: odeslat blok → chyba nebo ztráta → nepřijde potvrzení nebo přijde požadavek → blok se odešle znovu; jasně ukaž prodloužení o cestu tam a zpět. Vpravo „FEC: DOPŘEDNÁ OPRAVA CHYB“ jako zvětšený kódovaný blok: k modrým datům se předem přidají tyrkysová opravná data, část se poškodí a příjemce ji v mezích kódu obnoví bez zpětné cesty. Přidej druhý silněji poškozený blok označený „mimo možnosti kódu“. Uprostřed rozhodovací otázky „Je zpětný kanál? • Kolik stojí čekání? • Kolik redundance si můžeme dovolit? • Jaké chyby očekáváme?“ Dole přesná pipeline „komprese → přidání opravné redundance → přenos → oprava → dekomprese“ a malý hybridní detail „FEC + opakování“. Velké české písmo, jasné směry šipek, data a řídicí zprávy odlišit tvarem i barvou. Bez tvrzení, že FEC opraví libovolnou chybu, bez opakování bez zpětné cesty nebo časovače, bez opačného pořadí komprese a opravného kódování, bez pseudo-textu a falešných log.

## Kontrolní bod

ARQ musí obsahovat návratovou informaci nebo časový limit a následný nový přenos. FEC musí přidat redundanci předem a opravit pouze chyby v mezích kódu. Spodní pipeline musí být v pořadí komprese → FEC → přenos → oprava → dekomprese.
