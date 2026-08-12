# Základy informatiky

## Modernizovaný výukový text pro studenty informačních technologií

> Informatika nezačíná u počítače. Začíná u otázky, jak lze skutečnost popsat pomocí dat, jak z dat získat informaci, jak ji reprezentovat, přenést, zmenšit, ověřit a nakonec využít k rozhodování.

Tento text navazuje na původní výukový materiál **Základy informatiky** a zachovává jeho hlavní tematickou osu: informatiku, data a signál, digitalizaci, číselné soustavy, kódování, reprezentaci čísel, přenos dat a kompresi. Původní výklad je však přeorganizován do šesti ucelených lekcí a na řadě míst technicky zpřesněn. Doplněna je také samostatná lekce o práci s informacemi, která propojuje technickou stránku informatiky s informační gramotností, ověřováním zdrojů a odpovědným používáním generativní AI.

Text je psán tak, aby mohl sloužit nejen jako studijní materiál, ale také jako podklad pro mluvený výklad, krátké podcastové pořady nebo komentované prezentace. Jednotlivé podkapitoly proto nevytvářejí jen seznam definic; snaží se vysvětlovat souvislosti, používat konkrétní příklady a ukazovat, proč jsou dané principy důležité v běžné počítačové praxi.

---

# 1. Informatika a informační technologie

## 1.1 Co vlastně zkoumá informatika?

Když se řekne informatika, mnoho lidí si představí počítače, programování nebo práci v kancelářských aplikacích. To je ale podobné, jako kdybychom fyziku definovali jako „práci s dalekohledem a voltmetrem“. Počítač je pro informatiku mimořádně důležitý nástroj, není však jejím jediným předmětem.

Informatika zkoumá, **jak lze informace reprezentovat, zpracovávat a předávat pomocí přesně definovaných postupů**. Zajímá ji například, jak popsat problém tak, aby jej bylo možné řešit algoritmem, jak efektivně ukládat data, jak navrhovat programové a informační systémy, jak mezi sebou propojit počítače nebo jak automaticky hledat vzory v rozsáhlých datových souborech.

Základní myšlenku si můžeme představit jako řetězec:

**problém → data → model → algoritmus → výpočet → informace → rozhodnutí nebo akce**

Představme si například chytrou budovu. Senzory měří teplotu, koncentraci oxidu uhličitého a obsazenost místností. Samotná čísla jsou jen data. Program je musí správně vyhodnotit, porovnat s pravidly a rozhodnout, zda zapnout ventilaci nebo topení. Informatika zde není jen „počítač v rozvaděči“. Je to způsob reprezentace měření, algoritmus rozhodování, software, komunikační síť, databáze historických hodnot i způsob, jak výsledky zobrazit správci budovy.

Moderní informatika proto zahrnuje mnoho oblastí. Patří sem algoritmy a programování, databáze, počítačové sítě, operační systémy, umělá inteligence, kybernetická bezpečnost, počítačová grafika, modelování a simulace, robotika, práce s velkými daty nebo návrh rozhraní mezi člověkem a počítačem.

Důležitý je také rozdíl mezi **informatikou** a **informačními technologiemi**. Informatika je vědní a technická disciplína zabývající se principy výpočtu a práce s informacemi. Informační technologie jsou konkrétní prostředky, které tyto principy realizují: počítače, sítě, servery, programy, databáze, cloudové služby a další technické systémy.

Tento rozdíl je praktický. Programátor, správce sítě nebo datový analytik používá informační technologie, ale zároveň uplatňuje informatické principy. Stejně tak člověk, který navrhuje nový algoritmus komprese obrazu, řeší informatický problém ještě předtím, než rozhodne, na jakém konkrétním počítači bude algoritmus běžet.

**Příklad z praxe.** Navigace v telefonu přijme data o poloze, digitální mapu a aktuální dopravní situaci. Algoritmus hledá vhodnou trasu a aplikace ji zobrazí uživateli. Jeden zdánlivě jednoduchý pokyn „naviguj mě domů“ tak propojuje data, algoritmy, databáze, sítě, uživatelské rozhraní i fyzický hardware.

---

## 1.2 Data, informace a znalost

Pojmy **data** a **informace** se v běžné řeči často zaměňují, v informatice je však užitečné je rozlišovat.

Data jsou zaznamenané hodnoty nebo symboly, se kterými můžeme dále pracovat. Mohou vzniknout měřením reality, ručním zadáním, výpočtem, simulací nebo automatickým generováním. Datem může být číslo `21,4`, fotografie, GPS souřadnice, řetězec znaků, zvukový záznam, výsledek experimentu nebo třeba seznam kliknutí na webové stránce.

Samotné datum nemusí mít pro příjemce jasný význam. Hodnota `21,4` může znamenat teplotu, délku, cenu, napětí nebo něco úplně jiného. Aby se z ní stala použitelná informace, potřebujeme **kontext**.

Například:

**21,4 + „teplota ve třídě ve °C“ → informace „ve třídě je 21,4 °C“**

Pokud navíc víme, že běžná požadovaná teplota je kolem 20 až 22 °C, můžeme z informace odvodit poznatek: „teplota je v očekávaném rozsahu a topení není třeba zesilovat.“

Vztah lze proto zjednodušeně vyjádřit:

**data → kontext → informace → interpretace a zkušenost → znalost → rozhodnutí**

Není to absolutní filozofická definice, ale pro výuku informatiky je velmi užitečná. Ukazuje, že význam není uložen pouze v samotných bitech. Stejný řetězec bitů může být v jednom programu interpretován jako číslo, v jiném jako znak nebo část obrázku.

Důležitou roli hrají také **metadata**, tedy „data o datech“. U fotografie mohou metadata obsahovat datum vytvoření, rozměry, použitý fotoaparát nebo někdy i GPS polohu. U dokumentu mohou popisovat autora, datum poslední úpravy nebo jazyk. Metadata často rozhodují o tom, zda dokážeme data správně interpretovat a dohledat.

Tento rozdíl je zásadní také pro databáze a informační systémy. Databáze může obsahovat tisíce řádků naměřených hodnot. Teprve jejich výběrem, porovnáním a interpretací může vzniknout informace, například že se spotřeba energie v budově za poslední měsíc zvýšila o deset procent.

Informace navíc není automaticky pravdivá jen proto, že vznikla z dat. Data mohou být neúplná, chybně změřená, zastaralá nebo účelově vybraná. Informatika se proto nezabývá jen ukládáním hodnot, ale také jejich kvalitou, původem, strukturou a způsobem zpracování.

**Příklad z praxe.** Měří-li školní meteostanice každou minutu teplotu, získává množství dat. Zpráva „nejvyšší dnešní teplota byla 29,8 °C“ je informace vytvořená výběrem a zpracováním těchto dat. Závěr „dnešek byl mimořádně teplý“ už vyžaduje další kontext, například dlouhodobé klimatické údaje.

---

## 1.3 Informační technologie jako systém

Pojem **informační a komunikační technologie**, zkráceně ICT, se tradičně používá pro technické a programové prostředky, které umožňují informace vytvářet, zpracovávat, ukládat a přenášet. Dnes je užitečné chápat je ještě šířeji jako celý ekosystém.

Do tohoto systému patří především **hardware**: počítače, telefony, servery, senzory, síťové prvky nebo úložná zařízení. Druhou vrstvu tvoří **software**: operační systémy, aplikace, databázové systémy, webové služby a programové knihovny. Třetí vrstvu představují **data**, bez nichž by mnoho dnešních služeb nemělo co zpracovávat. Další vrstvu tvoří **komunikační sítě** a internet, které propojují jednotlivá zařízení a služby.

Moderní informační systém ale nekončí u techniky. Patří do něj také uživatelé, organizační pravidla a procesy. Školní informační systém například není jen databáze na serveru. Zahrnuje účty učitelů a studentů, pravidla přístupu, způsob zadávání známek, zálohování, ochranu osobních údajů, aktualizace, školení uživatelů a postup při výpadku.

Tato širší perspektiva pomáhá pochopit, proč mohou informační systémy selhat, i když je jejich hardware v pořádku. Chyba může být v programu, síti, datech, oprávněních, organizaci práce nebo lidském rozhodnutí.

Cloudové služby tento princip ještě zvýrazňují. Uživatel nemusí vědět, na kterém fyzickém serveru se jeho dokument právě nachází. Stále však existuje reálná infrastruktura datových center, úložišť a sítí, kterou provozuje konkrétní organizace. Slovo „cloud“ tedy neznamená, že data přestala být fyzicky uložena. Znamená především jiný způsob poskytování výpočetních zdrojů a služeb.

Stejně tak není vhodné chápat software jako nehmotnou „magii“. Program je přesně strukturovaná informace, která je uložena na fyzickém médiu, načítána do paměti a vykonávána procesorem. Databáze, dokument, fotografie i program jsou různé typy dat, které počítač interpretuje podle příslušných pravidel.

**Příklad z praxe.** Videokonference propojuje kameru a mikrofon, kodeky, operační systém, síťové protokoly, servery, autentizaci, šifrování a uživatelské rozhraní. Když „nejde videohovor“, příčina nemusí být jen v internetu. Může jít o zakázaný mikrofon, chybný ovladač, přetížené zařízení, síťový problém nebo chybu vzdálené služby.

---

## 1.4 Oblasti a aplikace informatiky

Informatika zasahuje prakticky do všech oblastí současného života. Není však nutné učit se její podobory jako izolovaný seznam. Smysluplnější je sledovat, **jaký typ problému jednotlivé oblasti řeší**.

Algoritmy a programování hledají přesné postupy, kterými lze problémy řešit. Databáze se soustředí na ukládání, vyhledávání a konzistentní správu dat. Počítačové sítě řeší komunikaci mezi zařízeními. Kybernetická bezpečnost chrání systémy, data a identity před zneužitím.

Umělá inteligence se snaží řešit úlohy, pro které není snadné napsat pevnou sadu jednoduchých pravidel. Patří sem například rozpoznávání obrazu, zpracování přirozeného jazyka, doporučovací systémy nebo generativní modely. Historické expertní systémy naproti tomu často pracovaly s explicitně vytvořenými pravidly a znalostní bází. Jsou zajímavým příkladem toho, jak se přístupy k AI v čase měnily.

Robotika propojuje software s fyzickým světem. Robot musí vnímat prostředí pomocí senzorů, vyhodnotit situaci a pomocí akčních členů provést činnost. Podobné principy dnes najdeme nejen v průmyslových robotech, ale také v dronech, autonomních vozidlech nebo automatizovaných skladech.

Počítačová simulace vytváří model určitého systému a umožňuje sledovat jeho chování bez nutnosti experimentovat přímo s realitou. Lze tak simulovat proudění vzduchu kolem letadla, šíření epidemie, pohyb planet nebo dopravu ve městě. Výsledek simulace je ale vždy závislý na kvalitě modelu a vstupních dat.

Počítačová grafika se zabývá vytvářením a zpracováním obrazových dat. Zahrnuje vše od jednoduchých ikon přes 3D hry až po vizualizaci lékařských dat. Human-computer interaction zkoumá, jak navrhovat systémy tak, aby s nimi člověk dokázal bezpečně a efektivně pracovat.

Dnešní informatika je také stále více propojena s dalšími obory. Bioinformatika zpracovává biologická data, geoinformatika pracuje s prostorovými informacemi, digitální humanitní vědy používají výpočetní metody při studiu kultury a historie. Hranice oboru nejsou ostré, protože práce s daty a algoritmy se stala univerzálním nástrojem vědy i průmyslu.

**Hlavní myšlenka této lekce:** informatika není nauka o konkrétním typu počítače. Je to disciplína, která zkoumá reprezentaci informace a výpočetní postupy, jimiž lze data transformovat na užitečné výsledky.

---

# 2. Principy digitalizace

## 2.1 Informace potřebuje fyzickou reprezentaci

Informace sama o sobě nemá elektrické napětí, barvu ani hmotnost. Aby ji bylo možné uložit, přenášet nebo automaticky zpracovávat, musí být nějakým způsobem fyzicky reprezentována. K tomu slouží **signál**.

Signálem může být změna elektrického napětí, světelný impuls, rádiová vlna, změna magnetizace nebo mechanický pohyb. V historii lidé používali také mnohem jednodušší signály: světlo majáku, vlajky, kouř nebo uzly na provázku. Princip je stále stejný — určitý fyzický stav dostane dohodnutý význam.

U zvuku je prvotním signálem změna tlaku vzduchu. Mikrofon ji převádí na elektrický signál. Ten může být dále zesílen, digitalizován, uložen do souboru a později znovu převeden na elektrické napětí pro reproduktor. Informace o původním zvuku během této cesty několikrát změní fyzickou podobu.

Je proto důležité rozlišovat **informaci** a **signál**. Informace je význam, který interpretujeme; signál je fyzický nositel tohoto významu. Stejná informace může být postupně reprezentována různými signály.

Například textová zpráva „Ahoj“ může být uložena jako elektrické náboje v paměti telefonu, při přenosu reprezentována rádiovým signálem, v optické síti světelnými impulzy a na displeji nakonec světlem vyzařovaným jednotlivými pixely.

Digitální technika přitom neznamená, že fyzický svět přestal být spojitý. I digitální zařízení pracují s reálnými elektrickými a elektromagnetickými jevy. Rozdíl je v tom, že systém určité rozsahy fyzických hodnot interpretuje jako **diskrétní logické stavy**, například 0 a 1. To poskytuje větší odolnost proti malým odchylkám a usnadňuje spolehlivé zpracování.

**Příklad z praxe.** Na ethernetovém kabelu „necestují jedničky a nuly“ jako malé předměty. Přenášejí se fyzické elektrické změny, které elektronika přijímače podle definovaných pravidel interpretuje jako digitální data.

---

## 2.2 Analogový a digitální svět

Analogový signál se mění spojitě. Teoreticky může v určitém rozsahu nabývat libovolné hodnoty. Typickým příkladem je průběh napětí z mikrofonu, který sleduje změny akustického tlaku.

Analogový záznam se snaží tuto spojitou změnu napodobit jinou fyzickou veličinou. U magnetofonového pásku odpovídá průběhu zvuku změna magnetizace materiálu. U gramofonové desky je zvuk zakódován do tvaru drážky.

Analogový systém má výhodu v přímém vztahu mezi reprezentací a původním jevem, ale zároveň je citlivý na šum a postupné zkreslení. Při každém dalším analogovém kopírování se do signálu mohou přidat nové odchylky.

Digitální reprezentace naproti tomu popisuje informaci pomocí diskrétních hodnot. U běžné výpočetní techniky jsou konečná data reprezentována binárně, tedy pomocí posloupností bitů.

To má zásadní důsledek: pokud se digitální data správně přečtou, lze je kopírovat **bitově přesně**. Kopie souboru tedy nemusí být horší než originál. To však neznamená, že celý proces digitalizace je bezeztrátový. Při převodu spojitého fyzikálního jevu na konečný počet čísel musíme zvolit, kdy měříme a s jakou přesností. Zde vznikají dvě klíčové operace: **vzorkování a kvantování**.

Analogový a digitální způsob reprezentace proto není jednoduchý souboj „horší versus lepší“. Digitální forma přináší obrovské výhody při ukládání, kopírování, zpracování a přenosu. Kvalita výsledku ale závisí na parametrech digitalizace a na dalším zpracování.

Velmi názorný je zvuk. Zvuková vlna v místnosti je spojitá. Mikrofon ji převede na spojité elektrické napětí. A/D převodník z něj v pravidelných okamžicích odebere vzorky a přiřadí jim číselné hodnoty. Čísla se uloží do paměti. Při přehrávání D/A převodník vytvoří z čísel nový elektrický průběh a reproduktor jej převede zpět na akustickou vlnu.

**Důležitá poznámka.** Pojem „digitální signál“ se používá v různých významech. V logickém modelu označuje diskrétní hodnoty, ale jejich fyzický přenos stále využívá spojité elektrické, optické nebo rádiové signály. Pro pochopení informatiky je proto dobré oddělit abstraktní data od jejich fyzické reprezentace.

---

## 2.3 Vzorkování: kdy změříme hodnotu?

Představme si analogovou zvukovou křivku jako plynule se měnící čáru. Počítač ji nemůže uložit jako nekonečné množství přesných hodnot. Musí ji převést na konečnou posloupnost čísel. Prvním krokem je **vzorkování**.

Vzorkování znamená, že v pravidelných časových okamžicích změříme okamžitou hodnotu signálu. Počet měření za sekundu se nazývá **vzorkovací frekvence** a udává se v hertzech.

Například vzorkovací frekvence 44,1 kHz znamená:

**44 100 vzorků za sekundu**

Tato hodnota se historicky používá u zvukového CD. Neříká nic o tom, jak přesně je každý vzorek uložen; pouze určuje, jak hustě v čase signál měříme.

Čím vyšší vzorkovací frekvence je, tím rychlejší změny signálu můžeme zachytit. Má to ale cenu: více vzorků znamená více dat.

Pro správné vzorkování je důležitá souvislost známá z Nyquistova-Shannonova teorému. Velmi zjednodušeně platí, že chceme-li věrně reprezentovat frekvenčně omezený signál, musí být vzorkovací frekvence vyšší než dvojnásobek jeho nejvyšší obsažené frekvence.

Při 44,1 kHz je tak teoretická Nyquistova frekvence 22,05 kHz. Praktický systém navíc používá filtry, které mají zabránit tomu, aby se do převodníku dostaly příliš vysoké frekvence.

Když vzorkujeme příliš pomalu, vzniká **aliasing**. Rychlé změny jsou pak ve vzorcích interpretovány jako jiný, obvykle nižší průběh. Podobný jev známe z filmu: kolo automobilu se může zdánlivě otáčet dozadu, protože kamera pořizuje obrazy jen v určitých okamžicích.

Vzorkování tedy odpovídá na otázku:

**KDY měříme?**

Neměli bychom ho zaměňovat s kvantováním, které řeší jiný problém: **s jakou přesností naměřenou hodnotu uložíme**.

**Příklad z praxe.** Digitální teploměr nemusí měřit teplotu desetitisíckrát za sekundu, protože teplota místnosti se mění pomalu. Zvuk má mnohem rychlejší změny, proto vyžaduje podstatně vyšší vzorkovací frekvenci. Správný parametr tedy vždy závisí na povaze měřeného jevu.

---

## 2.4 Kvantování a bitová hloubka

Po vzorkování známe časové okamžiky, ve kterých chceme hodnotu uložit. Stále ale potřebujeme rozhodnout, **jak přesně** ji vyjádříme číslem. To řeší kvantování.

Při kvantování rozdělíme možný rozsah hodnot na konečný počet úrovní a každý vzorek přiřadíme k nejbližší z nich. Čím více úrovní máme k dispozici, tím jemnější rozdíly dokážeme reprezentovat.

Počet dostupných úrovní souvisí s **bitovou hloubkou**. Máme-li pro jeden vzorek `n` bitů, můžeme vytvořit `2^n` různých bitových kombinací.

Například:

- 2 bity → 4 hodnoty,
- 4 bity → 16 hodnot,
- 8 bitů → 256 hodnot,
- 16 bitů → 65 536 hodnot.

U lineárního PCM zvuku s bitovou hloubkou 16 bitů lze každý vzorek reprezentovat jednou z 65 536 možných číselných hodnot. To dovoluje mnohem jemnější odstupňování amplitudy než například osmibitový záznam.

Rozdíl mezi vzorkováním a kvantováním si můžeme představit pomocí měření výšky člověka. Vzorkování určuje, **kdy** člověka změříme — například jednou za měsíc. Kvantování určuje přesnost pravítka — zda zapisujeme výšku po metrech, centimetrech nebo milimetrech.

Kvantování přináší **kvantizační chybu**, protože původní analogová hodnota obvykle neleží přesně na některé z dostupných úrovní. Při dostatečné bitové hloubce je tato odchylka malá, při nízké bitové hloubce může být výrazná.

Důležité je uvědomit si, že vyšší bitová hloubka zvětšuje také množství dat. U nekomprimovaného digitálního zvuku lze základní datový tok vypočítat:

**vzorkovací frekvence × bitová hloubka × počet kanálů**

Pro stereofonní zvuk 44,1 kHz / 16 bit:

`44 100 × 16 × 2 = 1 411 200 bit/s`

tedy přibližně **1,411 Mbit/s**.

Tento jednoduchý výpočet propojuje digitalizaci s tématy, která přijdou později: přenosovou rychlostí a kompresí. Pokud chceme takový zvuk přenášet nebo ukládat úsporněji, můžeme použít kompresi.

---

## 2.5 Bit, byte a velikost digitálních dat

**Bit** je základní jednotka množství digitální informace. Název vznikl ze slov *binary digit*, tedy dvojková číslice. Bit může nabývat dvou stavů, které zapisujeme jako `0` a `1`.

Osm bitů tvoří **byte** neboli bajt. Jeden bajt tedy může mít `2^8 = 256` různých bitových kombinací.

Je důležité rozlišovat značky:

- `b` znamená bit,
- `B` znamená byte.

Rozdíl je praktický. Rychlost sítě se často udává v **Mbit/s**, zatímco velikost souboru v **MB**.

Pokud máme soubor o velikosti 100 MB a síť o nominální rychlosti 100 Mbit/s, neznamená to, že se soubor přenese za jednu sekundu. Jeden byte má osm bitů, takže 100 MB představuje přibližně 800 megabitů, navíc se při přenosu přidává režie protokolů a skutečná propustnost bývá nižší než jmenovitá.

U násobků bajtu je vhodné rozlišovat **desítkové a binární předpony**.

Desítkové jednotky podle SI používají násobky tisíce:

- 1 kB = 1 000 B,
- 1 MB = 1 000 000 B,
- 1 GB = 1 000 000 000 B.

Binární jednotky používají mocniny dvou:

- 1 KiB = 1 024 B,
- 1 MiB = 1 048 576 B,
- 1 GiB = 1 073 741 824 B.

V praxi se historicky často používalo označení KB nebo MB i pro binární hodnoty, což může způsobovat zmatek. Moderní technická terminologie proto rozlišuje kB/MB/GB a KiB/MiB/GiB.

Často se také setkáme s pojmem 32bitový nebo 64bitový procesor či operační systém. Toto číslo souvisí s architekturou procesoru, šířkou některých registrů, instrukcí a adresovacích mechanismů. Není přesné říci, že 64bitový procesor „vždy zpracuje přesně 64 bitů najednou“, protože moderní procesory jsou mnohem složitější. U klasického 32bitového adresního prostoru však často narazíme na hranici `2^32` adresovatelných bajtů, tedy přibližně 4 GiB.

**Hlavní myšlenka této lekce:** digitalizace převádí fyzikální jev na posloupnost diskrétních čísel. Vzorkování určuje, kdy měříme, kvantování s jakou přesností hodnotu uložíme a počet bitů určuje, kolik různých hodnot dokážeme reprezentovat.

---

# 3. Kódování v informatice

## 3.1 Binární a další číselné soustavy

Lidé běžně používají desítkovou soustavu, protože má deset číslic `0` až `9`. Počítače však uvnitř pracují především s dvojkovou reprezentací, v níž používáme jen dvě číslice: `0` a `1`.

Důvod není v tom, že by elektronické obvody znaly „čísla“ v lidském smyslu. Digitální elektronika je navržena tak, aby spolehlivě rozlišovala několik stavů, nejčastěji dva logické stavy. Ty pak interpretujeme jako nulu a jedničku.

Dvojková soustava je stejně jako desítková **poziční**. Hodnota číslice závisí na její pozici. V desítkové soustavě mají pozice váhy `10^0`, `10^1`, `10^2` a tak dále. V binární soustavě jsou to mocniny dvou.

Například binární číslo:

`11010110₂`

má hodnotu:

`1×2^7 + 1×2^6 + 0×2^5 + 1×2^4 + 0×2^3 + 1×2^2 + 1×2^1 + 0×2^0`

tedy:

`128 + 64 + 16 + 4 + 2 = 214`

Vedle binární soustavy se v informatice často používá **hexadecimální soustava** se základem 16. Má číslice `0–9` a písmena `A–F`, která představují hodnoty deset až patnáct.

Hexadecimální zápis je praktický, protože jedna hexadecimální číslice přesně odpovídá čtyřem bitům. Dlouhá binární čísla tak lze zapsat podstatně kratší a čitelnější podobou.

Například:

`1101 0110₂ = D6₁₆`

Hexadecimální hodnoty najdeme v programování, diagnostice, adresách paměti, zápisu barev v HTML a CSS, MAC adresách nebo při zobrazování surových bajtů.

Osmičková soustava se základem 8 má dnes menší význam, ale stále se s ní můžeme setkat například u některých zápisů přístupových práv v unixových systémech. Jedna oktalová číslice odpovídá třem bitům.

Číselná soustava nemění samotnou hodnotu čísla. Mění pouze způsob zápisu. Čísla `56₁₀`, `111000₂`, `70₈` a `38₁₆` představují stejnou matematickou hodnotu.

---

## 3.2 Převody mezi číselnými soustavami

Převody mezi soustavami nejsou samoúčelné počítání. Pomáhají pochopit, jak počítač interpretuje bitové vzory a proč se některé hodnoty v programování zapisují právě hexadecimálně.

Při převodu z binární soustavy do desítkové využíváme váhy jednotlivých pozic. U čísla `101101₂` si můžeme zapsat:

`32 16 8 4 2 1`

a pod ně:

`1 0 1 1 0 1`

Sečteme pouze hodnoty pozic s jedničkou:

`32 + 8 + 4 + 1 = 45`

tedy:

`101101₂ = 45₁₀`

Při převodu kladného celého desítkového čísla do binární soustavy můžeme opakovaně dělit dvěma a zapisovat zbytky. Zbytky potom čteme v opačném pořadí.

Například 56:

- 56 : 2 = 28, zbytek 0
- 28 : 2 = 14, zbytek 0
- 14 : 2 = 7, zbytek 0
- 7 : 2 = 3, zbytek 1
- 3 : 2 = 1, zbytek 1
- 1 : 2 = 0, zbytek 1

Po přečtení zbytků zdola nahoru dostaneme:

`56₁₀ = 111000₂`

Převod mezi binární a hexadecimální soustavou je ještě jednodušší. Binární číslo rozdělíme zprava do čtveřic:

`0011 1000`

První čtveřice `0011` má hodnotu 3, druhá `1000` hodnotu 8:

`00111000₂ = 38₁₆`

Podobně při převodu do osmičkové soustavy seskupujeme bity po trojicích.

V programovacích jazycích se často používají prefixy, které základ soustavy jasně označí. Například v mnoha jazycích:

- `0b1010` znamená binární 10,
- `0x1A` znamená hexadecimální 26.

Konkrétní syntaxe závisí na jazyku, proto je vždy dobré ověřit jeho pravidla.

**Praktický význam.** Když v CSS uvidíme barvu `#FF8000`, můžeme dvojice `FF`, `80` a `00` chápat jako tři osmibitové hodnoty zapsané hexadecimálně: červenou, zelenou a modrou složku.

---

## 3.3 Kódování, komprese, šifrování a hashování

Pojem **kódování** znamená, že pomocí dohodnutého pravidla převádíme informaci z jedné reprezentace do jiné. Kód není nutně bezpečnostní mechanismus a nemusí data zmenšovat.

Morseova abeceda například převádí písmena na sekvence teček a čárek. ASCII přiřazuje znakům číselné hodnoty. Base64 převádí binární data na omezenou sadu textových znaků. Ve všech případech jde o změnu reprezentace podle známého pravidla.

Je důležité odlišit kódování od tří dalších operací.

**Komprese** mění reprezentaci tak, aby data zabírala méně místa. Cílem je úspora kapacity nebo přenosového času.

**Šifrování** mění data tak, aby jejich obsah bez příslušného klíče nebyl srozumitelný neoprávněnému příjemci. Cílem je důvěrnost, nikoli zmenšení dat.

**Hashování** vytváří z dat krátký otisk pevné nebo omezené délky. Kryptografický hash se používá například pro kontrolu integrity nebo při bezpečném ukládání odvozených hodnot hesel. Z hashe se běžně nemá dát rekonstruovat původní obsah.

Jeden soubor může postupně projít všemi operacemi. Text lze nejprve zakódovat do UTF-8, poté komprimovat, následně zašifrovat a nakonec z výsledku vypočítat hash pro kontrolu integrity.

Záměna těchto pojmů vede k častým chybám. Base64 například není šifrování, protože každý, kdo zná pravidlo, dokáže původní data přímo převést zpět. ZIP není automaticky bezpečný jen proto, že je komprimovaný. A hash není „zašifrovaný text“, protože běžný kryptografický hash není navržen pro zpětné dešifrování.

**Jednoduché rozlišení:**

- kódování — změna reprezentace,
- komprese — zmenšení objemu,
- šifrování — utajení obsahu,
- hashování — vytvoření kontrolního otisku.

Toto rozlišení se bude později hodit při práci se znakovými sadami, kompresí, kontrolními součty i kybernetickou bezpečností.

---

## 3.4 Čárové a QR kódy

Kódování nemusí být ukryté pouze uvnitř paměti počítače. Velmi názorným příkladem jsou čárové a QR kódy, které převádějí informace do grafické podoby čitelné strojem.

Jednorozměrný čárový kód pracuje s posloupností čar a mezer. Konkrétní význam závisí na použitém standardu. Maloobchodní kódy typu EAN obvykle neslouží jako kompletní databáze výrobku. Nesou identifikační číslo, které informační systém obchodu použije jako klíč k vyhledání názvu, ceny a dalších údajů.

To je důležitý informatický princip: **kód často nemusí obsahovat samotnou informaci, ale pouze identifikátor, pomocí kterého ji nalezneme jinde**.

QR kód je dvourozměrný maticový kód. Dokáže uložit více dat než běžný jednorozměrný kód a může obsahovat text, URL, kontaktní údaje nebo jiný strukturovaný obsah.

Na první pohled vypadá jako náhodná mozaika černých a bílých čtverců. Ve skutečnosti má přesně definovanou strukturu. Výrazné čtverce v rozích pomáhají čtečce určit orientaci. Další části slouží k synchronizaci, popisu formátu, maskování a opravě chyb. Teprve část modulů skutečně nese uživatelská data.

Proto není přesné říci, že „každý černý čtvereček je jednička a každý bílý nula“ v jednoduchém přímém významu. Grafický vzor je výsledkem několika kroků kódování a maskování.

Velkou výhodou QR kódu je **opravný kód**. Díky redundantním datům lze obsah často přečíst i tehdy, když je část kódu poškozena nebo zakryta. Používají se zde mechanismy založené na Reed-Solomonových kódech.

To vytváří pěkné propojení s pozdější kapitolou o přenosu dat: někdy nepřidáváme redundanci proto, že bychom chtěli plýtvat místem, ale proto, abychom dokázali některé chyby opravit.

**Bezpečnostní poznámka.** QR kód je jen způsob zápisu informace. Neříká nic o tom, zda je obsažený odkaz bezpečný. Před otevřením QR odkazu je proto vhodné zkontrolovat cílovou adresu stejně jako u odkazu v e-mailu.

---

## 3.5 ASCII, Unicode a UTF-8

Počítač neukládá písmeno `A`, `č` nebo `中` jako malý obrázek písmene. Textové znaky musí mít číselnou reprezentaci, na které se jednotlivé systémy shodnou.

Historicky velmi důležitý je standard **ASCII** — American Standard Code for Information Interchange. Původní ASCII je sedmibitový a obsahuje 128 kódových hodnot. Vedle písmen, číslic a interpunkce zahrnuje také řídicí znaky.

ASCII byl vytvořen hlavně pro anglické prostředí. Pro další jazyky proto vznikala různá osmibitová kódování, například Windows-1250 nebo ISO-8859-2 pro středoevropské jazyky. Neexistuje však jeden jediný univerzální standard s názvem „extended ASCII“. Tento termín se používá neformálně pro různé osmibitové tabulky, které si mezi sebou nemusí odpovídat.

To vedlo k dobře známým problémům: text vytvořený v jednom kódování mohl být v jiném systému zobrazen jako nesmyslné znaky.

Řešením se stal **Unicode**. Jeho cílem je přiřadit jednoznačný kódový bod znakům používaným v různých jazycích a systémech písma.

Například české malé `á` má kódový bod:

`U+00E1`

Unicode ale není totéž co způsob uložení znaků do bajtů. K tomu slouží konkrétní kódování, například **UTF-8**, UTF-16 nebo UTF-32.

UTF-8 je dnes mimořádně rozšířené. Je proměnné délky: různé znaky používají různý počet bajtů. Základní znaky ASCII používají v UTF-8 jeden bajt a jejich bajtové hodnoty odpovídají ASCII. Další znaky používají více bajtů.

Například znak `á` s kódovým bodem `U+00E1` se v UTF-8 uloží jako dva bajty:

`C3 A1`

To je zásadní rozdíl:

**Unicode říká, který znak máme na mysli. UTF-8 říká, jak tento znak uložíme jako bajty.**

Do textu patří také řídicí znaky. `LF` představuje line feed a v unixových systémech včetně dnešního macOS se používá jako konec řádku. Windows tradičně používá dvojici `CRLF`. Historické systémy Classic Mac OS používaly samotné `CR`.

V programovacích jazycích se setkáme s **escape sekvencemi**, například `\n` pro nový řádek nebo `\"` pro vložení uvozovky do řetězce. Nejde o nový znakový standard; je to způsob, jak určitým znakům v syntaxi programu přidělit speciální význam.

---

## 3.6 Jak počítač ukládá celá čísla

Celé číslo uložené v paměti je bitový vzor pevné délky. Význam tohoto vzoru závisí na tom, jaký datový typ používáme.

U **unsigned**, tedy neznaménkového osmibitového čísla, máme `2^8 = 256` možných kombinací. Ty mohou přímo reprezentovat hodnoty:

`0 až 255`

Například:

`00000000₂ = 0`

`11111111₂ = 255`

U znaménkových celých čísel potřebujeme reprezentovat i záporné hodnoty. Moderní počítače běžně používají **dvojkový doplněk**, anglicky *two's complement*.

U osmibitového signed integeru je typický rozsah:

`−128 až +127`

Kladná čísla vypadají stejně jako běžný binární zápis. Pro získání záporné reprezentace můžeme pro výukový příklad vzít kladnou hodnotu, invertovat bity a přičíst jedna.

Například `5`:

`00000101`

invertujeme:

`11111010`

přičteme 1:

`11111011`

Tento bitový vzor reprezentuje v osmibitovém dvojkovém doplňku hodnotu `−5`.

Výhodou dvojkového doplňku je, že procesor může pro sčítání kladných a záporných čísel používat velmi podobné binární operace.

Pevná šířka datového typu znamená, že existuje omezený rozsah hodnot. Pokud výpočet hranici překročí, může dojít k **integer overflow**. Konkrétní chování závisí na programovacím jazyku a prostředí.

Je také dobré rozlišovat datový typ a jeho název v konkrétním jazyce. `int` nemusí mít ve všech jazycích a platformách totožnou velikost. Při programování proto není vhodné automaticky přenášet tabulku z jednoho jazyka do jiného.

**Hlavní myšlenka:** samotná posloupnost bitů nemá jediný vrozený význam. `11111111` může být neznaménkové číslo 255, znaménkové číslo −1, část barvy nebo osm bitů uvnitř instrukce. Význam určuje kontext a datový typ.

---

## 3.7 Čísla s plovoucí řádovou čárkou

Celá čísla lze v omezeném rozsahu reprezentovat přesně. U reálných čísel je situace složitější. Mezi čísly 0 a 1 existuje nekonečně mnoho hodnot, ale počítač má konečnou paměť.

Proto se desetinná čísla často ukládají jako **čísla s plovoucí řádovou čárkou**, anglicky *floating point*. Moderní systémy obvykle vycházejí ze standardu IEEE 754.

Zjednodušeně můžeme bitový zápis rozdělit na tři části:

**znaménko | exponent | significand**

Tradičně se poslední části často říká mantisa, i když standardní terminologie používá pojem *significand*.

Princip připomíná vědecký zápis čísla. Místo:

`123 000 000`

můžeme napsat:

`1,23 × 10^8`

Floating point používá obdobnou myšlenku, ale v binární soustavě.

Výhodou je obrovský rozsah hodnot. Nevýhodou je, že mnoho běžných desetinných čísel nemá v binární soustavě konečný přesný zápis.

Například desetinné `0,1` nelze v běžné binární plovoucí řádové reprezentaci uložit naprosto přesně. Program tedy pracuje s velmi blízkou aproximací.

Proto může v některých jazycích nastat výsledek podobný:

`0.1 + 0.2 = 0.30000000000000004`

Nejde o poruchu procesoru. Jde o důsledek omezené reprezentace.

Rozdíl mezi běžnými typy `float` a `double` souvisí především s počtem použitých bitů a tedy s rozsahem a přesností. Běžný IEEE 754 binary32 má 32 bitů, binary64 64 bitů.

Praktický důsledek je zásadní například ve financích. Chceme-li přesně počítat desetinné měnové částky, nemusí být binární floating point vhodnou volbou. Používají se například celočíselné částky v nejmenších měnových jednotkách nebo speciální desítkové datové typy.

**Hlavní myšlenka této lekce:** počítač neukládá „znaky“ nebo „čísla“ přímo. Ukládá bitové vzory, jejichž význam určují pravidla kódování a datové typy.

---

# 4. Přenos dat

## 4.1 Obecný model datové komunikace

Komunikace vzniká tehdy, když chce jeden systém předat informaci jinému. Nezáleží na tom, zda jde o rozhovor dvou lidí, rádiové vysílání nebo přenos souboru přes internet — vždy můžeme najít několik společných prvků.

Na začátku stojí **zdroj informace**. Ten vytvoří sdělení, které je potřeba převést do formy vhodné pro přenos. Následuje vysílač, komunikační kanál, přijímač a příjemce.

Zjednodušený model můžeme zapsat:

**zdroj → kódování → vysílač → kanál → přijímač → dekódování → příjemce**

Do kanálu může působit **šum a rušení**. To znamená, že přijatý signál nemusí být úplně stejný jako odeslaný.

V digitální komunikaci se proto používají mechanismy, které pomáhají chybu odhalit, někdy opravit, případně vyžádat opakovaný přenos.

Důležitá může být také **zpětná vazba**. Příjemce například potvrdí, že data dorazila. Pokud potvrzení nepřijde, odesílatel může přenos opakovat. Tuto myšlenku později využívají například spolehlivé transportní protokoly.

Model je užitečný i mimo počítačové sítě. Při videohovoru je zdrojem hlas mluvčího, mikrofon jej převede na elektrický signál, zařízení jej digitalizuje a zakóduje, síť přenese data a na druhé straně se celý postup obrátí.

Je však dobré oddělit **obsah sdělení** od **způsobu jeho přenosu**. Stejný text lze přenést optickým vláknem, Wi-Fi, mobilní sítí nebo uložit na USB disk. Informace zůstává logicky stejná, fyzická reprezentace se mění.

---

## 4.2 Jak data fyzicky cestují

Digitální data se mohou mezi zařízeními přenášet různými fyzickými médii. Každé médium využívá jiný fyzikální jev.

V metalických vodičích se informace reprezentuje pomocí změn elektrických veličin. V optickém vlákně se používá světlo. Bezdrátová komunikace využívá elektromagnetické vlny šířící se prostorem.

To však neznamená, že jedno médium odpovídá jednomu konkrétnímu protokolu. Ethernet lze provozovat nad různými typy kabeláže i optikou. Internetový protokol IP může být přenášen prostřednictvím Ethernetu, Wi-Fi, mobilních sítí a mnoha dalších technologií.

Každé médium má určité vlastnosti: dosažitelnou přenosovou rychlost, útlum, citlivost na rušení, cenu, maximální délku segmentu nebo nároky na instalaci.

Optické vlákno je výhodné pro vysoké rychlosti a dlouhé vzdálenosti. Není ovlivňováno elektromagnetickým rušením stejným způsobem jako metalické vedení a používá se v páteřních sítích i datových centrech.

Rádiový přenos nabízí mobilitu a snadné připojení, ale sdílí společné prostředí s dalšími zařízeními. Výkon může ovlivnit vzdálenost, překážky, rušení nebo počet současně komunikujících uživatelů.

Fyzický přenos má také praktické bezpečnostní důsledky. Bezdrátový signál se šíří mimo hranice místnosti, zatímco fyzický kabel je přístupný jen tam, kam je veden. Ani kabel ale není automaticky bezpečný; ochranu obsahu řeší například šifrování na vyšších vrstvách.

**Příklad z praxe.** Fotografie odeslaná do cloudu může nejprve projít jako rádiový signál Wi-Fi z telefonu do přístupového bodu, poté jako elektrický signál ethernetovou sítí a dále jako světelné impulzy v optické páteřní infrastruktuře. Logická data přitom zůstávají součástí jednoho komunikačního procesu.

---

## 4.3 Rychlost, propustnost, baud, latence a jitter

Výrok „mám rychlý internet“ je technicky neúplný. Rychlost připojení má několik různých vlastností.

**Bitová rychlost** vyjadřuje počet bitů přenesených za sekundu a zapisuje se například v Mbit/s nebo Gbit/s.

**Propustnost** je množství užitečných dat, které se skutečně podaří přenést za určitý čas. Bývá nižší než teoretická rychlost linky, protože část přenosu zabírají hlavičky protokolů, potvrzování, čekání, rušení nebo další režie.

**Latence** vyjadřuje zpoždění. Přenos může mít vysokou kapacitu a zároveň vysokou latenci. To je důležité například u satelitních spojů nebo komunikace se vzdáleným datovým centrem.

**Jitter** je kolísání zpoždění mezi jednotlivými částmi přenosu. Vadí zejména aplikacím pracujícím v reálném čase, například hovoru nebo online hře.

Samostatným pojmem je **baud**, značka Bd. Baud udává počet symbolů přenesených za sekundu. Symbol nemusí nést pouze jeden bit.

Pokud systém používá dva možné symboly, může jeden symbol reprezentovat jeden bit. V takovém případě může být číselně:

`1 000 Bd = 1 000 bit/s`

Pokud ale rozlišujeme čtyři možné symboly, jeden symbol může reprezentovat dva bity. Potom například:

`1 000 Bd = 2 000 bit/s`

V moderních komunikačních systémech se používají modulace s mnoha stavy, takže baud a bit/s nelze obecně zaměňovat.

**Příklad.** Stahování velkého souboru potřebuje vysokou propustnost. Videohovor potřebuje nejen dostatečnou propustnost, ale především nízkou latenci a malé kolísání. Online hra může přenášet relativně málo dat, přesto bude při vysoké latenci působit nepoužitelně.

Proto žádné jediné číslo nevystihuje kvalitu síťového spojení.

---

## 4.4 Kódování signálu a modulace

Aby bylo možné data fyzicky přenést, musí se bitové hodnoty převést na změny signálu. Existuje mnoho způsobů, jak to udělat.

Při přenosu v **základním pásmu** může systém přímo používat změny elektrického nebo optického signálu podle určitého linkového kódu. Není ale přesné představovat si jednoduché pravidlo „0 = žádné napětí, 1 = napětí“ jako obecný princip všech digitálních sítí. Moderní systémy používají složitější kódování, které pomáhá synchronizaci, omezuje určité nežádoucí vlastnosti signálu a lépe využívá přenosové médium.

Jinou možností je **modulace nosné vlny**. Informace se přenáší změnou některé vlastnosti nosného signálu.

Měnit lze například amplitudu, frekvenci nebo fázi. Moderní modulace často kombinují několik vlastností. Typickým příkladem je QAM, která reprezentuje více různých symbolů pomocí kombinace amplitudy a fáze.

Modulace proto není jednoduše „převod digitálního signálu na analogový“. Přesnější je říci, že informační symboly mění parametry fyzické nosné vlny tak, aby je přijímač dokázal rozlišit.

Slovo **modem** vzniklo historicky ze slov *modulator-demodulator*. U klasického telefonního připojení musel modem převést digitální data počítače na signál vhodný pro analogovou telefonní linku a na druhé straně jej znovu interpretovat.

Podobný princip ale v mnohem složitější podobě používají i moderní bezdrátové systémy. Wi-Fi nebo mobilní sítě dokážou během jediné symbolové doby reprezentovat více bitů, pokud jsou podmínky signálu dostatečně kvalitní.

To vysvětluje také vztah mezi kvalitou spojení a přenosovou rychlostí. Při silném rušení nemusí přijímač spolehlivě rozlišit jemné rozdíly mezi mnoha symboly. Systém proto může přejít na robustnější, ale méně datově účinný způsob modulace.

---

## 4.5 Jak poznáme, že se data poškodila?

Každý fyzický přenos může být ovlivněn chybou. V digitálním systému proto často přidáváme k užitečným datům **redundanci**, která pomáhá zjistit, zda přijatý obsah odpovídá odeslanému.

Jednoduchým mechanismem je **paritní bit**. U sudé parity nastavíme paritní bit tak, aby byl celkový počet jedniček sudý. Pokud se během přenosu změní jeden bit, parita přestane souhlasit.

Parita je jednoduchá, ale má omezené schopnosti. Nezachytí například každou kombinaci více chyb.

Další možností je **kontrolní součet**. Odesílatel vypočítá z dat krátkou hodnotu a přiloží ji k přenosu. Příjemce provede stejný výpočet a výsledky porovná. Pokud se liší, víme, že s vysokou pravděpodobností došlo ke změně.

Velmi důležitý je **CRC**, Cyclic Redundancy Check. Jde o matematicky definovaný mechanismus navržený pro účinnou detekci určitých typů přenosových chyb, zejména shluků chybných bitů. Používá se například v linkových a úložných technologiích.

CRC není totéž co kryptografický hash. Oba mechanismy sice vytvářejí krátkou hodnotu odvozenou z dat, ale mají jiný bezpečnostní účel. CRC je navržen především pro neúmyslné chyby přenosu, ne pro ochranu proti útočníkovi, který data záměrně mění.

Stejně důležité je rozlišit **detekci a opravu**. CRC samo běžně neříká, který konkrétní bit máme změnit. Umí velmi dobře zjistit, že data nejsou v pořádku. Co se stane dál, závisí na komunikačním systému.

---

## 4.6 Co s chybou uděláme: retransmise a FEC

Když systém zjistí, že se data poškodila, existují dvě základní strategie.

První je **opakovaný přenos**. Příjemce nebo komunikační protokol dá najevo, že určitá část dat chybí nebo je chybná, a odesílatel ji pošle znovu. Tyto principy se označují jako ARQ — Automatic Repeat reQuest.

Je to vhodné tam, kde lze čekat a kde máme zpětný komunikační kanál. Typickým příkladem je přenos souboru. Raději několik milisekund počkáme na opakování, než abychom přijali poškozený dokument.

Druhou možností je **FEC — Forward Error Correction**. Odesílatel přidá takovou redundanci, aby příjemce mohl některé chyby opravit bez nového přenosu.

To je výhodné například tam, kde by opakované odesílání bylo pomalé nebo nemožné. FEC se používá v bezdrátové komunikaci, satelitních přenosech, optických médiích nebo QR kódech.

Příkladem jsou Hammingovy kódy, Reed-Solomonovy kódy nebo moderní LDPC kódy. Není nutné znát jejich matematickou konstrukci, důležitý je princip:

**více redundantních dat → větší šance chybu odhalit nebo opravit**

To vytváří zajímavý kontrast s kompresí. Komprese se snaží nadbytečnost odstranit, zatímco opravné kódování část nadbytečnosti záměrně přidává. V reálném přenosovém systému se proto často nejprve data komprimují a teprve potom se přidá potřebná redundance pro spolehlivý přenos.

**Hlavní myšlenka této lekce:** kvalitu přenosu neurčuje jen počet bitů za sekundu. Důležitá je také fyzická reprezentace signálu, zpoždění, rušení a mechanismy, které chyby detekují a řeší.

---

# 5. Datová komprese

## 5.1 Proč lze data komprimovat?

Představme si text:

`AAAAAAAAAAAA`

Je zřejmé, že zapisovat dvanáctkrát písmeno A není jediný možný způsob reprezentace. Můžeme například zapsat:

`12×A`

a původní obsah dokážeme jednoznačně obnovit.

To je základní intuice datové komprese: mnoho dat obsahuje **redundanci**, tedy opakující se nebo předvídatelné struktury, které lze popsat úsporněji.

Komprese je změna reprezentace dat s cílem snížit jejich velikost. Menší soubor zabere méně místa na disku a lze jej rychleji přenést sítí.

Úspěšnost komprese silně závisí na typu dat. Textový dokument s opakujícími se slovy může být dobře komprimovatelný. Soubor, který už prošel účinnou kompresí, například JPEG fotografie nebo video, často dalším zabalením do ZIPu téměř nezmenšíme.

Z pohledu informační teorie souvisí možnost komprese s předvídatelností a entropií zdroje dat. Pro základní pochopení stačí jednoduchá myšlenka: jestliže se některé vzory vyskytují častěji než jiné, můžeme jim dát úspornější reprezentaci.

Komprese však není jeden univerzální algoritmus. Jiný typ redundance najdeme v textu, jiný v fotografii a jiný v časové posloupnosti videa. Proto existuje velké množství kompresních metod.

Důležité je také rozlišovat kompresi od archivace. Archivní formát může spojit více souborů do jednoho balíčku a současně je komprimovat, ale tyto dvě funkce nejsou totožné. Například formát TAR tradičně především sdružuje soubory; komprese se k němu často přidává pomocí dalšího algoritmu, například gzip.

---

## 5.2 Bezeztrátová a ztrátová komprese

Zásadní rozdělení komprese je na **bezeztrátovou** a **ztrátovou**.

Bezeztrátová komprese musí umožnit po dekompresi získat **bitově přesně původní data**. Je nezbytná u programů, databází, textových dokumentů, zdrojových kódů nebo výsledků měření, kde může být významný každý bit.

Typickými příklady jsou ZIP, 7z, PNG nebo FLAC.

Ztrátová komprese část informace úmyslně odstraní. Po dekompresi už nedostaneme původní data přesně zpět. Proč bychom něco takového chtěli?

Protože u některých typů dat lze odstranit nebo zjednodušit části, které jsou pro člověka méně významné, a získat výrazně menší soubor.

U fotografie může být cílem odstranit jemné detaily, které lidský zrak téměř nepostřehne. U zvuku lze využít vlastností lidského sluchu. U videa navíc můžeme využít podobnosti sousedních snímků.

Ztrátová komprese proto není totéž co náhodné poškození. Algoritmus se snaží ztrátu řídit tak, aby byl subjektivní dopad co nejmenší vzhledem k dosažené úspoře.

Typické příklady:

- JPEG — fotografie,
- MP3, AAC, Opus — zvuk,
- H.264/AVC, H.265/HEVC, VP9, AV1 — video.

Některé formáty mohou podporovat více režimů. WebP a AVIF například mohou pracovat i se ztrátovou i bezeztrátovou kompresí.

Volba mezi oběma typy proto závisí na účelu. Zdrojový kód programu nesmíme „trochu zjednodušit“. U fotografie pro web může být malá ztráta detailu rozumnou cenou za výrazně menší datový objem.

**Praktická otázka zní:** Co si můžeme dovolit zahodit — a co musí být obnoveno přesně?

---

## 5.3 Kompresní poměr, úspora a kvalita

Úspěšnost komprese můžeme vyjádřit několika způsoby.

Pokud měl původní soubor 10 MB a po kompresi má 2 MB, pak je **kompresní poměr**:

`10 : 2 = 5 : 1`

Soubor je tedy pětkrát menší.

Procentuální úsporu můžeme vypočítat:

`(1 − komprimovaná velikost / původní velikost) × 100 %`

V našem příkladu:

`(1 − 2/10) × 100 % = 80 %`

U bezeztrátové komprese nás zajímá především velikost, rychlost komprese a dekomprese nebo nároky na paměť. Kvalita výsledku se nezhoršuje, protože po dekompresi musí být data přesná.

U ztrátové komprese je situace složitější. Menší soubor obvykle znamená větší ztrátu informace. Musíme proto hledat kompromis mezi velikostí, kvalitou, výpočetní náročností, kompatibilitou a požadovaným datovým tokem.

U zvuku a videa se často používá **bitrate**, tedy počet bitů za sekundu. Vyšší bitrate obvykle dává kodeku více prostoru pro zachování detailů, ale výsledný soubor je větší.

Nelze ale jednoduše říci, že dva soubory se stejným bitrate mají stejnou kvalitu. Záleží na kodeku, nastavení, obsahu, počtu průchodů a dalších parametrech.

Stejně tak není vhodné posuzovat kompresi pouze podle procent. U velmi malého textového souboru nemusí silný algoritmus přinést výhodu, protože vlastní hlavičky komprimovaného formátu zaberou nezanedbatelné místo.

**Příklad z praxe.** Fotografie s jednolitým pozadím a velkými opakujícími se plochami může být komprimovatelná jinak než fotografie hustého listí, vlasů nebo zrnitých detailů. Komprese vždy závisí na struktuře vstupních dat.

---

## 5.4 RLE, Huffman a slovníkové algoritmy

Několik klasických algoritmů dokáže velmi názorně ukázat, odkud se úspora dat bere.

### RLE — Run-Length Encoding

RLE využívá opakování stejných hodnot za sebou.

Například:

`AAAAAAABBBCC`

můžeme zapsat přibližně jako:

`7A3B2C`

U dlouhých jednobarevných úseků obrazu nebo jednoduchých dat může být RLE velmi účinné. U náhodného textu by však mohlo být dokonce větší než původní data.

### Huffmanovo kódování

Huffmanovo kódování využívá četnost symbolů. Často se vyskytující symboly dostanou **kratší kódová slova**, méně časté delší.

Nejde tedy o to, že by nejčastější znak „dostal nejnižší binární číslo“. Podstatná je délka kódu a vlastnost, že jednotlivá kódová slova lze jednoznačně rozlišit.

Pokud se v textu písmeno A objevuje mnohem častěji než znak Z, dává smysl reprezentovat A kratším bitovým vzorem.

### Slovníkové metody

Algoritmy rodiny Lempel-Ziv hledají opakující se sekvence a nahrazují je odkazy na již známé části nebo položky slovníku.

LZW je známý slovníkový algoritmus, který se historicky používá například v GIF a některých variantách TIFF.

Dnešní kompresní formáty často kombinují více principů. Samotné RLE, Huffman nebo LZW jsou proto ideální hlavně pro pochopení základních myšlenek, nikoli jako úplný popis moderních kodeků.

Zajímavé je, že komprese využívá statistickou strukturu dat. Čím přesněji algoritmus dokáže předvídat pravděpodobné vzory, tím méně bitů může být v průměru potřeba k jejich reprezentaci.

---

## 5.5 Komprese v obrazu, zvuku, videu a archivech

V praxi se často zaměňují tři pojmy: **formát souboru, kontejner a kodek**.

Kodek je algoritmus nebo jeho implementace určená pro kódování a dekódování dat. Kontejner je struktura, která může uvnitř spojovat různé datové proudy a metadata.

Například soubor MP4 může obsahovat video kódované H.264, zvuk kódovaný AAC, titulky a metadata.

MP4 je tedy kontejner, zatímco H.264 a AAC jsou kodeky nebo formáty kódování příslušných proudů.

U obrázků se setkáme například s PNG, JPEG, WebP nebo AVIF. PNG používá bezeztrátovou kompresi a dobře se hodí pro grafiku s ostrými hranami. JPEG je ztrátový formát tradičně vhodný pro fotografie. WebP a AVIF mohou podle režimu pracovat ztrátově i bezeztrátově.

U zvuku patří mezi důležité příklady bezeztrátový FLAC a ztrátové MP3, AAC či Opus. Opus je navržen tak, aby byl použitelný jak pro řeč, tak pro hudbu a interaktivní komunikaci.

U videa se dnes často používají H.264/AVC, H.265/HEVC, VP9 nebo AV1. Video komprese využívá nejen redundanci uvnitř jednoho snímku, ale také podobnost mezi snímky v čase.

Archivní nástroje jako ZIP nebo 7z se používají pro obecná data, kde je nutná bezeztrátová obnova.

Při volbě formátu proto nestačí znát pouze příponu souboru. Je třeba přemýšlet o účelu, kompatibilitě, velikosti, kvalitě, rychlosti zpracování a podpoře v cílovém prostředí.

**Hlavní myšlenka této lekce:** komprese není magické zmenšení. Využívá strukturu a redundanci dat. Bezeztrátová komprese musí původní data obnovit přesně; ztrátová komprese získává větší úsporu výměnou za řízenou ztrátu informace.

---

# 6. Práce s informacemi

## 6.1 Od problému k informační potřebě

Vyhledávání informací často selhává ještě předtím, než člověk otevře vyhledávač. Problémem není nedostatek výsledků, ale nepřesně formulovaná otázka.

Představme si úkol: „Zjisti něco o IPv6.“ Takové zadání je příliš široké. Potřebujeme vědět, co skutečně hledáme.

Můžeme otázku zpřesnit: Proč bylo IPv6 navrženo? Jak velký je jeho adresní prostor? Jak se zapisuje IPv6 adresa? Jak se IPv6 zavádí vedle IPv4?

Každá otázka vyžaduje jiné informace a někdy také jiné zdroje.

Prvním krokem informační práce je tedy formulace **informační potřeby**:

**problém → otázka → potřebné důkazy → vhodný typ zdroje**

Pokud potřebujeme zjistit přesné znění technického standardu, má smysl hledat původní specifikaci. Pokud potřebujeme princip pochopit, může být vhodnější kvalitní výukový materiál. Pokud zjišťujeme aktuální cenu, potřebujeme současný zdroj, nikoli deset let starý článek.

Dobrý dotaz často obsahuje hlavní pojem, kontext a omezení. Místo „AI ve škole“ můžeme hledat „generativní AI střední škola ochrana osobních údajů doporučení“.

Je také užitečné předem rozhodnout, **co bude považováno za dostatečný důkaz**. Jediný anonymní příspěvek na diskusním fóru může být zajímavá zkušenost, ale nestačí k potvrzení obecného technického nebo zdravotního tvrzení.

Tato dovednost je důležitá i při práci s AI. Jazykový model dokáže formulovat odpověď i na velmi vágní otázku. Plynulost však může zakrýt skutečnost, že otázka nebyla dostatečně přesná. Kvalitní práce proto začíná rozmyslem ještě před promptem.

---

## 6.2 Typy zdrojů a původ informace

Ne všechny zdroje mají stejnou funkci. Užitečné je rozlišovat **primární, sekundární a terciární zdroje**, i když hranice nemusí být vždy ostrá.

Primární zdroj je nejblíže původnímu vzniku informace. U technického standardu to může být samotná specifikace RFC. U vědeckého výsledku původní studie. U zákona oficiální znění. U statistiky původní datová sada nebo zpráva instituce, která data shromáždila.

Sekundární zdroj primární materiál vysvětluje, analyzuje nebo porovnává. Může být velmi kvalitní a pro studenta často srozumitelnější než původní dokument.

Terciární zdroje shrnují širší oblast, například encyklopedie, učebnice nebo přehledové portály.

Primární zdroj není automaticky „nejlepší pro každou situaci“. Technická norma může být přesná, ale pro začátečníka obtížně čitelná. Kvalitní výklad může být pro pochopení vhodnější. Když ale potřebujeme ověřit konkrétní tvrzení, je cenné vědět, odkud pochází.

S tím souvisí **provenance**, tedy původ a historie informace. U datové sady chceme vědět, kdo ji vytvořil, jakou metodou, kdy byla aktualizována a zda byla později upravována.

Metadata mohou při hodnocení zdroje výrazně pomoci. U dokumentu nás zajímá autor, datum, verze nebo vydavatel. U fotografie můžeme zkoumat čas a místo vzniku, ale metadata sama o sobě nejsou nezfalšovatelným důkazem.

Na internetu je běžné, že desítky webů přebírají stejné tvrzení z jediného původního zdroje. Počet nalezených kopií proto není totéž co počet nezávislých potvrzení.

**Příklad.** Pokud pět článků opakuje statistiku „90 % uživatelů…“ a všechny odkazují na stejnou marketingovou tiskovou zprávu, stále máme jeden původní zdroj, nikoli pět nezávislých studií.

---

## 6.3 Jak poznat kvalitní informaci

Důvěryhodnost zdroje nelze spolehlivě určit podle jediné vlastnosti. Profesionální vzhled stránky, doména nebo vysoké umístění ve vyhledávači nejsou samy o sobě důkazem správnosti.

Při hodnocení informace je vhodné položit několik otázek.

**Kdo tvrzení zveřejnil?** Je autor dohledatelný? Má k tématu relevantní zkušenost nebo odborné zázemí?

**Na čem tvrzení stojí?** Odkazuje na data, dokumentaci, experiment nebo jiný ověřitelný zdroj?

**Kdy informace vznikla?** U historického faktu může být starší článek v pořádku. U ceny, bezpečnostní zranitelnosti nebo aktuální verze softwaru může být zastaralý během několika měsíců.

**Jaký je účel zdroje?** Chce především informovat, prodávat, přesvědčovat, získávat pozornost nebo pobavit?

**Je přiznán střet zájmů?** Recenze produktu od jeho výrobce může obsahovat pravdivé údaje, ale není nezávislá.

**Je tvrzení v souladu s dalšími nezávislými zdroji?** Jedna izolovaná informace vyžaduje větší opatrnost než tvrzení potvrzené různými metodami a institucemi.

Kvalitní zdroj také obvykle dokáže rozlišit fakta, interpretace a nejistotu. Odborný text nemusí předstírat absolutní jistotu tam, kde data umožňují jen odhad.

Důležitá je i **relevance**. Velmi kvalitní studie může být pro naši otázku nepoužitelná, pokud zkoumá jinou populaci, jiné období nebo jiný problém.

Proto je lepší nepoužívat mechanický checklist „zdroj má autora = je důvěryhodný“. Hodnocení je vždy kombinací původu, důkazů, metodiky, aktuálnosti a vztahu ke konkrétní otázce.

---

## 6.4 Ověřování a triangulace

Když narazíme na důležité tvrzení, neměli bychom zůstat jen uvnitř jediné stránky. Užitečná strategie se označuje jako **lateral reading** — místo dlouhého studování zdroje samotného otevřeme další karty a zjišťujeme, co o něm říkají nezávislé informace.

Praktický postup může vypadat takto:

**tvrzení → původní zdroj → kontext → nezávislé potvrzení → závěr**

Nejprve se pokusíme dohledat, odkud informace skutečně pochází. Potom ověříme, zda je citována správně a zda nebyla vytržena z kontextu.

Dále hledáme nezávislý zdroj. Nejde o dvě stránky, které jedna od druhé kopírují, ale o potvrzení založené na jiných datech nebo jiném autorovi.

Tento princip se někdy označuje jako **triangulace** — problém posuzujeme z několika nezávislých úhlů.

U fotografie může být vhodné reverzní vyhledávání obrazu. U statistik dohledání původní tabulky. U technické vlastnosti výrobku dokumentace výrobce a nezávislé měření. U citátu původní rozhovor nebo záznam.

Zvláštní pozornost vyžadují snímky obrazovky. Screenshot zachycuje určitý obraz, ale sám o sobě nemusí dokazovat, kdy a kde vznikl ani zda nebyl upraven.

Podobně musíme přemýšlet o videu a syntetickém obsahu. Samotný fakt, že něco vypadá realisticky, není důkazem autenticity.

Ověřování neznamená nekonečnou nedůvěru ke všemu. Znamená přizpůsobit míru kontroly závažnosti rozhodnutí. Jinou úroveň ověření potřebujeme pro výběr receptu na večeři a jinou pro zdravotní, právní nebo bezpečnostní rozhodnutí.

---

## 6.5 Jak z informací vytvořit vlastní poznatek

Najít zdroj je jen začátek. Skutečná informační práce spočívá v tom, že dokážeme informace vybrat, porovnat, uspořádat a převést do vlastního pochopení.

První krok je oddělit podstatné informace od detailů. U technického článku se můžeme ptát: Jaký problém řeší? Jaký princip používá? Jaké má omezení? Kde se používá?

Druhým krokem je porovnání. Dvě technologie můžeme převést do tabulky podle stejných kritérií. Časový vývoj lze zapsat do osy. Proces lze znázornit diagramem.

Takové transformace nejsou jen „hezčí zápis“. Nutí nás odhalit vztahy mezi informacemi.

Dále bychom měli rozlišovat:

- **fakt** — ověřitelné tvrzení,
- **interpretaci** — vysvětlení významu,
- **odhad** — aproximaci založenou na neúplných datech,
- **názor** — hodnotící stanovisko.

Kvalitní výstup také přiznává nejistotu. Pokud zdroj uvádí přibližnou hodnotu, neměli bychom ji přepsat jako absolutně přesné číslo.

Zvlášť důležité je to při práci s grafy a statistikami. Průměr může skrýt velké rozdíly uvnitř skupiny. Procento bez informace o velikosti vzorku může být zavádějící. Graf s oříznutou osou může vizuálně zvětšit malý rozdíl.

Výsledkem informační práce proto není „co nejvíce zkopírovaných faktů“. Cílem je vytvořit strukturovaný, ověřitelný a srozumitelný poznatek, ze kterého lze odpovědně rozhodovat.

---

## 6.6 Citace, licence a odpovědné využívání AI

Použití cizí informace neznamená automaticky, že ji můžeme převzít bez uvedení původu. **Citace** umožňuje čtenáři dohledat zdroj a odlišit vlastní práci od převzatých myšlenek.

Při přímém citování přebíráme část textu doslova a jasně ji označíme. Při parafrázi myšlenku vyjadřujeme vlastními slovy, ale zdroj stále uvádíme.

Vedle citací je třeba rozlišovat **licenci**. To, že je obrázek volně dostupný na webu, neznamená, že jej můžeme libovolně používat. Licence určuje, co je dovoleno: například zda je možné dílo upravovat, používat komerčně nebo zda musíme uvést autora.

Licence Creative Commons nabízejí různé kombinace podmínek. Při použití média je proto dobré zaznamenat autora, název, zdroj a konkrétní licenci už ve chvíli, kdy materiál stahujeme.

Novým informačním prostředníkem je generativní AI. Jazykový model může velmi dobře pomáhat s brainstormingem, vysvětlováním, formulací vyhledávacích dotazů, strukturou textu nebo porovnáním variant.

Je však nutné držet jednoduché pravidlo:

**AI odpověď není sama o sobě zdroj.**

Model může vytvořit nesprávný údaj, smyšlenou citaci nebo zastaralou informaci. Pokud potřebujeme fakt použít ve výukovém textu, seminární práci nebo rozhodnutí, musíme dohledat skutečný zdroj.

Stejně důležitá je ochrana dat. Do veřejných AI služeb bychom neměli bez jasného oprávnění vkládat hesla, osobní údaje, neveřejné školní dokumenty nebo jiná citlivá data.

AI je nejpřínosnější tehdy, když ji používáme jako nástroj pro práci s informacemi, nikoli jako anonymní autoritu. Člověk stále rozhoduje, jaké zdroje přijme, jak tvrzení ověří a jakým způsobem výsledek použije.

**Hlavní myšlenka této lekce:** informační gramotnost není schopnost něco rychle vyhledat. Je to schopnost přesně formulovat otázku, najít vhodné zdroje, posoudit jejich kvalitu, ověřit tvrzení, vytvořit vlastní poznatek a transparentně uvést původ použitých informací.

---

# Závěrečné propojení kurzu

Celý kurz lze chápat jako jednu cestu informace.

Nejprve si v informatice ujasníme, že data získávají význam teprve v kontextu. Potom sledujeme, jak lze fyzikální jevy digitalizovat a převést na bitové reprezentace. V části o kódování zjišťujeme, jak stejné bity získávají konkrétní význam jako čísla, znaky nebo jiné datové struktury.

Následně přenášíme data mezi zařízeními. Musíme řešit fyzický signál, přenosovou rychlost, zpoždění a chyby. Když jsou data příliš objemná, používáme kompresi, která odstraňuje nebo reorganizuje redundanci.

Na konci se vracíme k původnímu smyslu celé informatiky: k člověku, který potřebuje z dat získat použitelnou informaci. Musí ji najít, pochopit, ověřit a použít.

Celou cestu lze shrnout:

**realita → signál → digitalizace → bity → kódování → přenos a uložení → zpracování → informace → poznatek → rozhodnutí**

Právě toto propojení dává jednotlivým technickým pojmům smysl. Bit, Unicode, CRC nebo Huffmanovo kódování nejsou izolované definice. Jsou to různé odpovědi na jedinou velkou informatickou otázku: **jak spolehlivě reprezentovat, zpracovat a předat význam pomocí výpočetního systému.**
