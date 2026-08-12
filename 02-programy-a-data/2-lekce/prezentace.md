## Snímek 2.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Software jako vrstvený systém**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 2.1 Software jako vrstvený systém

Počítačový program nekomunikuje s hardwarem vždy přímo. Mezi aplikací a fyzickými zařízeními stojí několik softwarových vrstev.

Zjednodušený pohled může vypadat takto:

**uživatel → aplikace → operační systém → ovladače → hardware**

Ve skutečnosti je struktura ještě bohatší. Aplikace využívají knihovny a API, operační systém spravuje procesy a paměť, firmware inicializuje zařízení a hardware vykonává fyzické operace.

Toto vrstvení má velkou výhodu: programátor textového editoru nemusí vědět, jak přesně konkrétní model SSD zapisuje buňky flash paměti. Požádá operační systém, aby uložil soubor, a nižší vrstvy se postarají o detaily.

Stejná aplikace pak může fungovat s mnoha typy disků, tiskáren nebo síťových karet.

Software tradičně rozdělujeme na **systémový a aplikační**.

Systémový software vytváří prostředí, ve kterém může počítač fungovat a spouštět další programy. Patří sem především operační systémy, ovladače, firmware a mnoho systémových utilit.

Aplikační software řeší konkrétní úlohy uživatele: psaní textu, úpravu obrazu, komunikaci, programování, účetnictví nebo třeba 3D modelování.

Hranice ale není absolutní. Webový prohlížeč je z pohledu uživatele aplikace, ale v moderním systému se může stát téměř platformou pro další webové aplikace. Databázový systém může být samostatná aplikace i infrastrukturní služba pro desítky dalších programů.

Důležitější než memorovat hranici je chápat roli jednotlivé vrstvy.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Operační systém: správce zdrojů a prostředník**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 2.2 Operační systém: správce zdrojů a prostředník

Operační systém je základní software, který spravuje hardwarové zdroje a poskytuje služby aplikacím.

Jeho nejdůležitější částí je **jádro**, anglicky *kernel*. Jádro řeší například:

- plánování běhu procesů,
- správu operační paměti,
- komunikaci se zařízeními,
- práci se souborovými systémy,
- ochranu a izolaci procesů,
- část síťové komunikace.

Když spustíme program, operační systém vytvoří proces, přidělí mu paměť a procesorový čas a zpřístupní mu definované systémové služby.

Aplikace běžně nemá právo libovolně zapisovat do fyzické paměti jiného procesu nebo ovládat diskový řadič. K citlivým operacím přistupuje přes rozhraní operačního systému.

Tato rozhraní jsou jedním z významů pojmu **API — Application Programming Interface**. API je obecně definované rozhraní, pomocí kterého jedna softwarová část využívá služby jiné.

Uživatel s operačním systémem komunikuje prostřednictvím **uživatelského rozhraní**.

Grafické rozhraní, GUI, používá okna, ikony, nabídky a další grafické prvky. Příkazové rozhraní, CLI, používá textové příkazy.

Není správné chápat CLI jako něco „zastaralého“. V současných systémech je příkazová řádka zásadní pro automatizaci, správu serverů, vývoj software a DevOps. GUI je pohodlné pro interaktivní práci, CLI je často efektivnější pro opakovatelné a skriptovatelné operace.

Operační systémy existují pro různé kategorie zařízení: osobní počítače, servery, telefony, síťová zařízení, automobily nebo vestavěné systémy.

Zvláštní skupinou jsou **real-time operating systems — RTOS**. Jejich podstatou není prostě „rychlejší reakce v mikrosekundách“. Důležitá je **časová předvídatelnost**. U kritické operace potřebujeme vědět, že bude dokončena v definovaném časovém limitu.

V řízení motoru, průmyslové automatizaci nebo avionice může být zmeškání časového limitu závažnější než to, že průměrný výkon systému je vysoký.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Ovladače, firmware, BIOS a UEFI**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 2.3 Ovladače, firmware, BIOS a UEFI

Operační systém nemůže znát elektrické a protokolové detaily každého zařízení. Proto využívá **ovladače zařízení**, device drivers.

Ovladač je software, který umožňuje operačnímu systému komunikovat s konkrétní třídou nebo modelem hardwaru. Může například převádět obecné požadavky operačního systému na příkazy, kterým rozumí grafická karta, tiskárna nebo síťový adaptér.

Moderní systémy obsahují mnoho běžných ovladačů přímo a další mohou získat prostřednictvím aktualizačního systému nebo instalace výrobce.

Mechanismy typu Plug and Play pomáhají nové zařízení identifikovat, přiřadit mu prostředky a zvolit vhodný ovladač.

Vedle ovladače existuje **firmware**. To je software uložený přímo v zařízení nebo jeho nevolatilní paměti. Řídí základní chování daného hardwaru.

Firmware má například:

- SSD,
- router,
- fotoaparát,
- tiskárna,
- základní deska,
- mikrokontrolér v IoT zařízení.

Firmware lze často aktualizovat. Taková aktualizace může přidat funkce nebo opravit bezpečnostní chybu, ale neúspěšný update firmwaru může zařízení také vyřadit z provozu.

U osobních počítačů se historicky používá pojem **BIOS**. Moderní stroje většinou používají **UEFI**, které nahradilo mnoho omezení tradičního PC BIOSu. UEFI inicializuje hardware, umožňuje konfiguraci platformy a předává řízení zaváděcímu mechanismu operačního systému.

Je užitečné rozlišit tři role:

- firmware běží v zařízení a zná jeho hardware,
- ovladač propojuje zařízení s operačním systémem,
- operační systém zpřístupňuje služby aplikacím.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Utility: malé nástroje s velkým významem**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 2.4 Utility: malé nástroje s velkým významem

**Utility** jsou pomocné programy zaměřené na správu, diagnostiku, údržbu nebo konverzi dat.

Řada utilit je součástí operačního systému:

- správce procesů,
- monitor výkonu,
- nástroje pro disky,
- síťové diagnostické příkazy,
- zálohovací nástroje,
- správci souborů.

Jiné instalujeme samostatně, například archivační programy, analyzátory diskového prostoru nebo specializované diagnostické nástroje.

Historicky se utility často chápaly jako „malé servisní programy“. Dnešní hranice je méně ostrá. Například nástroj pro správu kontejnerů nebo komplexní zálohovací systém může být velmi rozsáhlý, přesto plní infrastrukturní či servisní roli.

Některé staré rady je vhodné přehodnotit. Například agresivní „čištění registru“ ve Windows není běžnou doporučenou údržbou moderního systému. Neověřené čističe mohou způsobit více problémů než užitku.

Podobně **defragmentace** má jiný význam podle typu úložiště. U klasických rotačních disků HDD může snížení fragmentace někdy pomoci. U SSD se tradiční defragmentace běžně neprovádí stejným způsobem; operační systém používá jiné mechanismy, například TRIM a optimalizaci vhodnou pro flash úložiště.

Dobrý správce systému proto nepouští „optimalizační“ nástroj jen proto, že slibuje zrychlení. Nejprve musí rozumět, jaký problém řeší a zda je pro daný typ systému skutečně vhodný.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Aplikační software a jeho ekosystém**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 2.5 Aplikační software a jeho ekosystém

Aplikační software je určen pro konkrétní potřeby uživatele nebo organizace.

Mezi běžné skupiny patří:

**Kancelářské aplikace** — textové procesory, tabulkové procesory, prezentace, poznámkové aplikace a nástroje týmové spolupráce.

**Grafické a DTP programy** — rastrové a vektorové editory, sazba publikací, CAD, 3D modelování nebo digitální malba.

**Multimediální software** — přehrávání, střih a zpracování obrazu, zvuku a videa.

**Komunikační aplikace** — prohlížeče, e-mailové klienty, messengery, videokonference nebo nástroje vzdálené správy.

**Informační a podnikové systémy** — ERP, CRM, školní informační systémy, účetní software, logistické systémy nebo systémy pro správu dokumentů.

**Vývojové nástroje** — editory, IDE, překladače, interpretery, debugger, verzovací nástroje a systémy pro sestavení aplikace.

Dnes je navíc běžné, že aplikační software není instalován pouze lokálně. Může běžet jako webová aplikace, cloudová služba, mobilní aplikace nebo kombinace klientské a serverové části.

Stejná služba může mít:

- webové rozhraní,
- desktopového klienta,
- mobilní aplikaci,
- API,
- serverový backend.

Pojem „aplikace“ tedy označuje především funkční celek pro uživatele, nikoli jediný spustitelný soubor.

---**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 2.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Platforma, kompatibilita a verze software**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 2.6 Platforma, kompatibilita a verze software

Program je navržen pro určité prostředí. Může záviset na operačním systému, procesorové architektuře, knihovnách, grafickém API nebo konkrétní verzi runtime.

Pojem **platforma** proto může znamenat více věcí. V běžné řeči mluvíme o Windows, macOS nebo Linuxu. Při vývoji ale může být podstatná kombinace:

`Windows + x86-64`

nebo:

`Linux + ARM64`

Program zkompilovaný pro x86-64 procesor nemusí přímo běžet na ARM64, i když používáme podobný operační systém. Řešením může být jiná sestavená verze, překlad za běhu, emulace nebo kompatibilní vrstva.

**Multiplatformní software** je dostupný pro více prostředí. To ale neznamená, že uvnitř používá všude totožný binární soubor. Vývojář může vytvářet samostatné sestavení pro jednotlivé platformy.

Kompatibilita se týká i verzí. Novější aplikace může vyžadovat nové systémové API a na starém operačním systému se nespustí. Naopak velmi stará aplikace může očekávat komponenty, které už moderní systém nepodporuje.

Software proto používá **verze**. Čísla jako `1.4.2` mohou vyjadřovat vývojovou řadu, ale neexistuje jeden univerzální význam čísel pro všechny produkty.

V mnoha vývojářských projektech se používá **Semantic Versioning**, například:

`MAJOR.MINOR.PATCH`

kde zvýšení major verze může signalizovat nekompatibilní změny, minor nové kompatibilní funkce a patch opravy. Platí to ale jen tam, kde se projekt k tomuto pravidlu skutečně hlásí.

Pojmy:

- **update** — aktualizace,
- **upgrade** — přechod na významně novější verzi nebo vyšší edici,
- **patch** — cílená oprava,
- **downgrade** — návrat k nižší verzi,

jsou užitečné, ale jejich přesné obchodní použití se může mezi výrobci lišit.

**Hlavní myšlenka druhé lekce:** software tvoří vrstvy. Operační systém spravuje zdroje, ovladače propojují OS s hardwarem, firmware řídí zařízení a aplikace využívají tyto vrstvy k řešení konkrétních úloh.

---

# 3. Softwarové licence

## 3.1 Software jako autorské dílo a licence jako oprávnění

Když si koupíme židli, stává se konkrétní fyzická židle naším majetkem a můžeme ji například prodat dál. U software je situace odlišná. Běžně nekupujeme autorská práva k programu. Získáváme **oprávnění používat software za určitých podmínek**.

Tyto podmínky stanovuje licence.

Počítačový program je autorské dílo a jeho autor nebo jiný nositel práv rozhoduje o tom, kdo jej smí rozmnožovat, měnit, distribuovat nebo používat určitým způsobem. Konkrétní práva a omezení závisejí na licenci a právním řádu.

Je proto příliš zjednodušující říci, že „licence je vždy nepřenosná“ nebo že uživatel „nikdy nesmí program upravit“. Některé licence přenos umožňují, jiné omezují. Některé licence výslovně dovolují modifikaci a další distribuci.

U proprietárního software se uživatel často setká s **EULA — End User License Agreement**. Ta může určit například:

- počet zařízení,
- povolené způsoby použití,
- možnosti přenosu licence,
- podmínky aktualizací,
- omezení reverzního inženýrství,
- pravidla pro firemní nebo školní nasazení.

U cloudových služeb se navíc kombinují licenční podmínky s podmínkami poskytování služby a zásadami ochrany osobních údajů.

Z praktického hlediska je důležité rozlišovat:

**vlastnictví kopie nebo zařízení**

a

**autorská a licenční práva k programu**.

To, že máme instalační soubor na disku, neznamená, že jej smíme neomezeně kopírovat a distribuovat.

---

## 3.2 Proprietární software, předplatné, freeware a freemium

**Proprietární software** je software, jehož autor nebo vlastník si ponechává rozhodující kontrolu nad distribucí a modifikací. Zdrojový kód obvykle není veřejně dostupný za podmínek umožňujících volné úpravy.

Proprietární neznamená automaticky „placený“. Program může být zdarma a přitom mít uzavřený zdrojový kód a velmi omezenou licenci.

To je případ řady programů označovaných jako **freeware**. Uživatel je může bezplatně používat, ale nemá automaticky právo získat zdrojový kód, program upravovat nebo dále šířit libovolným způsobem.

**Trial** neboli zkušební verze umožňuje produkt vyzkoušet, často po omezenou dobu nebo s omezenými funkcemi.

**Freemium** poskytuje základní funkce zdarma a pokročilé funkce, větší kapacitu nebo odstranění omezení nabízí za úplatu.

Historický pojem **shareware** označoval software, který bylo možné volně získat a vyzkoušet, ale další dlouhodobé nebo plné používání bylo spojeno s registrací či platbou. Tento distribuční model stále existuje, i když dnes se častěji používají pojmy trial nebo freemium.

Velká změna nastala s **předplatným**. Uživatel neplatí jednorázově za konkrétní vydání, ale periodicky za právo používat software nebo službu. To může zahrnovat průběžné aktualizace, cloudové funkce a podporu.

Předplatné mění také dlouhodobé náklady a závislost na poskytovateli. Když přestane předplatné platit, může uživatel přijít k části funkcí, přestože jeho vlastní dokumenty zůstávají.

Při výběru software proto není nejdůležitější otázka „je zdarma?“, ale:

- jaká práva licence poskytuje,
- jaké má omezení,
- jaké jsou dlouhodobé náklady,
- zda lze data exportovat,
- jak dlouho bude produkt podporován.

---

## 3.3 Svobodný software a open source

Pojmy **free software** a **open source** se často překrývají, ale vznikly z částečně odlišných tradic.

Hnutí svobodného software zdůrazňuje svobody uživatele — program používat, studovat, upravovat a sdílet za podmínek licence.

Open source zdůrazňuje dostupnost zdrojového kódu a licenční podmínky, které dovolují jeho používání, modifikaci a další distribuci.

Důležité je, že **open source neznamená „bez autorských práv“**. Právě licence určuje, co je možné dělat.

Stejně tak open source neznamená, že musí být produkt zdarma. Firma může prodávat open-source software, podporu, hostovanou službu nebo jiné související služby.

Historicky významný je projekt GNU spojený s Richardem Stallmanem a Free Software Foundation. Samostatně vzniklo linuxové jádro, které začal v roce 1991 vyvíjet Linus Torvalds. Kombinace linuxového jádra s nástroji a knihovnami z GNU a dalších projektů tvoří základ mnoha linuxových distribucí.

Open-source model dnes nepředstavuje pouze dobrovolnické projekty. Na mnoha zásadních projektech pracují placení vývojáři velkých firem, nadací, univerzit i nezávislí přispěvatelé.

Internetová infrastruktura, cloud, mobilní systémy a vývojářské nástroje jsou na open-source software velmi silně závislé.

---

## 3.4 Permisivní a copyleftové licence

Open-source licence nejsou všechny stejné.

Velmi užitečné je rozdělení na **permisivní** a **copyleftové** licence.

Permisivní licence, například MIT nebo BSD, obvykle dovolují velmi široké použití, úpravy a další distribuci, pokud jsou dodrženy relativně jednoduché podmínky, například zachování copyrightového oznámení.

Apache License 2.0 je také permisivní, ale obsahuje podrobnější ustanovení například k patentovým právům.

Copyleftové licence, jako GNU GPL, dovolují program používat, studovat, měnit a distribuovat, ale při distribuci odvozeného díla mohou vyžadovat zachování stejných svobod a zpřístupnění odpovídajícího zdrojového kódu podle podmínek licence.

Není tedy přesné tvrdit:

> „Každý open-source program musí být po úpravě vždy znovu distribuován jako open source.“

To závisí na konkrétní licenci a způsobu použití.

Stejně tak GPL neznamená, že každá firma, která software interně upraví, musí automaticky zveřejnit své interní úpravy celému světu. Povinnosti se vážou na podmínky licence a zejména na způsoby distribuce.

Licence se mohou lišit také v otázkách patentů, propojení s jiným kódem, síťového poskytování služby nebo používání ochranných známek.

Proto nestačí pouze vědět, že projekt „je na GitHubu“. Veřejně dostupný zdrojový kód ještě automaticky neznamená open-source licenci.

Pokud repozitář nemá jasnou licenci, nelze předpokládat, že si jeho kód smíme libovolně převzít do vlastního projektu.

---

## 3.5 Public domain, source-available a Creative Commons

**Public domain** označuje díla, ke kterým se neuplatňují majetková autorská práva způsobem typickým pro běžně chráněné dílo, například proto, že práva zanikla nebo protože právní systém umožňuje určité vzdání se práv.

Situace se liší podle jurisdikce, takže není vždy přesné tvrdit, že autor „jednoduše zruší všechna autorská práva“. Proto se v softwarovém světě používají nástroje jako CC0 nebo Unlicense, které se snaží umožnit co nejvolnější použití.

Vedle open source existuje **source-available software**. Zdrojový kód je veřejně čitelný, ale licence může zakazovat některé způsoby použití, například komerční poskytování služby. To nemusí splňovat definici open source.

Tento rozdíl je dnes důležitý, protože některé firmy publikují kód, ale zároveň si licencí chrání svůj obchodní model.

Samostatnou skupinu tvoří licence **Creative Commons**. Ty jsou velmi vhodné pro fotografie, texty, prezentace, videa nebo výukové materiály.

Pro software se obvykle doporučují specializované softwarové licence, nikoli běžné licence CC, protože software řeší specifické otázky zdrojového kódu, binární distribuce nebo patentů.

Student tak může potkat například:

- MIT u knihovny,
- GPL u programu,
- Apache-2.0 u vývojářského projektu,
- CC BY u fotografie nebo výukového textu.

Znalost licence je praktická součást digitální gramotnosti. Nejde jen o to „něco stáhnout“, ale vědět, zda a jak to můžeme použít ve vlastním projektu.

---

## 3.6 Licence ve škole, firmě a vlastním projektu

Licenční problém se často projeví až ve chvíli, kdy software používá více lidí nebo když vzniká vlastní projekt.

Škola může potřebovat licenci pro desítky nebo stovky zařízení či uživatelů. Výrobce může nabízet vzdělávací, objemové nebo institucionální licence.

Dnešní licencování je často založené spíše na uživatelských účtech než na fyzickém počtu počítačů. Jedna osoba může mít oprávnění používat aplikaci na několika zařízeních, zatímco organizace spravuje licence centrálně.

U cloudových služeb je běžný model „za uživatele a měsíc“. To je odlišné od historické multilicence na určitý počet instalací.

Při vlastním vývoji musíme kontrolovat licence použitých knihoven. To, že je knihovna technicky zdarma ke stažení, neznamená, že ji můžeme za jakýchkoli podmínek vložit do uzavřeného komerčního produktu.

Profesionální projekty proto vedou evidenci závislostí a licencí. Větší firmy používají nástroje pro **Software Composition Analysis**, které pomáhají sledovat nejen bezpečnostní zranitelnosti, ale i licenční povinnosti.

Důležité je oddělit licenční otázku od bezpečnosti. Open-source software není automaticky bezpečnější ani nebezpečnější než proprietární. Bezpečnost závisí na kvalitě vývoje, procesu aktualizací, auditu, reakci na zranitelnosti a konkrétním nasazení.

**Hlavní myšlenka třetí lekce:** cena software, dostupnost zdrojového kódu a licenční práva jsou tři různé věci. Licence určuje, co uživatel, škola nebo vývojář smí s programem dělat.

---

# 4. Emulace a virtualizace

## 4.1 Problém kompatibility: když program a počítač „mluví jiným jazykem“

Starý program vytvořený pro MS-DOS očekává jiné prostředí než moderní aplikace pro Windows 11. Hra pro původní konzoli PlayStation očekává konkrétní procesor, grafický hardware a systémové služby. Program zkompilovaný pro x86-64 může očekávat instrukce, které ARM procesor přímo nemá.

Vzniká **problém kompatibility**.

Jednou možností je program přepsat nebo znovu zkompilovat pro novou platformu. To ale nemusí být možné — zdrojový kód může chybět, projekt už není udržován nebo je původní hardware příliš specifický.

Proto vznikly techniky, které vytvářejí programu prostředí podobné tomu původnímu.

Je však důležité rozlišovat několik pojmů:

- emulace,
- virtualizace,
- kompatibilní vrstva,
- kontejnerizace.

Všechny mohou umožnit běh software mimo jeho původní prostředí, ale dělají to jiným způsobem.

---

## 4.2 Emulace: napodobení jiné platformy

**Emulátor** napodobuje chování jiného systému nebo jeho části.

Pokud hostitelský procesor nerozumí instrukcím cílového procesoru, emulátor je může interpretovat nebo dynamicky překládat do instrukcí, které hostitelský procesor vykonat umí.

Tím lze například na PC napodobit starou herní konzoli nebo historický počítač.

Emulátor musí často napodobit nejen CPU, ale i další komponenty:

- grafiku,
- zvukový čip,
- časovače,
- řadiče,
- paměťovou mapu,
- vstupní zařízení.

Čím přesnější má emulace být, tím složitější úloha to je.

Příkladem je DOSBox, který vytváří prostředí vhodné pro mnoho starších DOSových aplikací a her.

Velmi důležitá oprava běžného zjednodušení: **Wine není klasický emulátor Windows**. Samotný název historicky zdůrazňuje „Wine Is Not an Emulator“. Wine implementuje kompatibilní vrstvu, která převádí volání Windows API na odpovídající mechanismy hostitelského systému.

Podobně Rosetta 2 na Macích s Apple Silicon dynamicky překládá instrukce aplikací vytvořených pro x86-64 do prostředí ARM64. Jde o překladovou kompatibilní technologii, nikoli o kompletní emulaci celého PC.

Emulace může být výpočetně náročnější než nativní běh, protože mezi program a hardware vkládá další překladovou vrstvu. Moderní procesory však mají dostatečný výkon pro mnoho praktických emulačních úloh.

Emulace má také velký význam pro **digitální archivaci**. Pokud za dvacet let nebude existovat původní konzole nebo počítač, může být emulace jedinou cestou, jak zachovat původní software funkční.

---

## 4.3 Virtualizace a virtuální stroj

**Virtualizace** vytváří abstraktní verzi výpočetních zdrojů. Nejznámějším příkladem je virtuální stroj.

Fyzický počítač se označuje jako **hostitel**. Na něm běží virtualizační vrstva, která vytváří jeden nebo více virtuálních počítačů — **guestů**.

Každý virtuální stroj může mít virtuální:

- procesory,
- operační paměť,
- disk,
- síťový adaptér,
- další zařízení.

Uvnitř virtuálního stroje lze nainstalovat samostatný operační systém.

Moderní hardware podporuje virtualizaci přímo pomocí instrukčních rozšíření procesoru. Díky tomu nemusí hypervisor kompletně emulovat stejnou architekturu a výkon může být velmi blízký nativnímu.

Software řídící virtuální stroje se označuje jako **hypervisor**.

Často se rozlišují:

**Type 1 — bare-metal hypervisor**  
Běží přímo na hardwaru nebo tvoří základ serverové virtualizační platformy.

**Type 2 — hosted hypervisor**  
Běží jako aplikace nad běžným hostitelským operačním systémem.

Toto dělení je didakticky užitečné, i když moderní platformy někdy používají složitější hybridní architektury.

Virtuální stroje umožňují, aby jeden fyzický server provozoval mnoho izolovaných systémů. To zásadně změnilo datová centra: místo deseti slabě využitých fyzických serverů může jeden výkonný stroj provozovat deset virtuálních serverů.

---

## 4.4 Snapshoty, obrazy a virtuální sítě

Virtualizace není užitečná jen proto, že „máme další počítač v okně“. Její skutečná síla spočívá ve snadné manipulaci s celým softwarovým prostředím.

Virtuální disk je obvykle uložen jako soubor nebo sada souborů. Virtuální stroj lze proto:

- kopírovat,
- klonovat,
- přesunout na jiný server,
- zálohovat,
- obnovit.

Mnoho platforem podporuje **snapshot** — záznam stavu virtuálního stroje v určitém okamžiku. Před experimentem můžeme vytvořit snapshot, provést změnu a v případě problému se vrátit.

Snapshot ale není automaticky plnohodnotná dlouhodobá záloha. Může být závislý na původním virtuálním disku a jeho dlouhodobé hromadění může mít výkonnostní i provozní důsledky.

Virtuální stroje lze také připojit do **virtuálních sítí**. Mohou komunikovat mezi sebou, používat NAT, být oddělené od fyzické sítě nebo naopak vystupovat jako běžná zařízení v lokální síti.

To je výborné pro výuku. V jednom notebooku lze vytvořit virtuální server, klienta a směrovač a simulovat celou malou síť bez dalšího fyzického hardwaru.

Bezpečnostní izolace ale není absolutní. Zranitelnost hypervisoru nebo chybná konfigurace mohou izolaci narušit. Virtuální stroj proto není magická „bezpečnostní krabice“, do které lze bez rizika pustit cokoli.

---

## 4.5 Kontejnery nejsou malé virtuální stroje

Kontejnery jsou dnes zásadní technologie, ale často se vysvětlují nepřesně jako „lehké virtuální stroje“.

Virtuální stroj běžně obsahuje vlastní operační systém a vlastní kernel. Kontejner naproti tomu typicky **sdílí jádro hostitelského systému** a izoluje procesy, souborový systém, síťové prostředí a další zdroje pomocí mechanismů operačního systému.

To má velkou výhodu: kontejner může startovat rychle a má menší režii než plný virtuální stroj.

Typické schéma:

**virtuální stroj:**  
hardware → hypervisor → guest OS → aplikace

**kontejner:**  
hardware → host OS → container runtime → izolované aplikace

Docker popularizoval jednoduchou práci s kontejnerovými obrazy a reprodukovatelnými prostředími. Ve velkých systémech se kontejnery často orchestrují pomocí nástrojů, jako je Kubernetes.

Kontejnerový obraz může přesně popsat prostředí aplikace: konkrétní verzi runtime, knihovny a další závislosti. Vývojář tak snižuje problém „u mě to funguje, na serveru ne“.

Je také důležité nezaměňovat kontejnery s Python `venv`. Virtuální prostředí Pythonu izoluje především balíčky a interpreterové závislosti uvnitř jednoho operačního systému. Není to hardwarová virtualizace ani plnohodnotný kontejner.

Stejně tak VPN není „síťová virtualizace“ ve stejném smyslu jako virtuální switch nebo software-defined networking, i když používá virtuální síťová rozhraní a logické tunely.

Přesná terminologie pomáhá pochopit, co jednotlivá technologie skutečně izoluje.

---

## 4.6 Kdy použít emulaci, virtuální stroj nebo kontejner?

Každá technologie řeší jiný problém.

**Emulaci** volíme, když potřebujeme napodobit jinou architekturu nebo historický systém.

**Virtuální stroj** je vhodný, když potřebujeme celý samostatný operační systém, silnější izolaci, vlastní kernel nebo odlišnou systémovou konfiguraci.

**Kontejner** je výhodný, když chceme rychle izolovat a distribuovat aplikaci se závislostmi a přitom sdílet jádro hostitele.

**Kompatibilní vrstva** je užitečná, když lze volání programu převést na služby jiného operačního systému bez emulace celého stroje.

Příklady:

- stará konzolová hra → emulátor,
- test Windows Serveru na linuxovém serveru → virtuální stroj,
- webová aplikace s Node.js a databází → kontejnery,
- některá Windows aplikace na Linuxu → kompatibilní vrstva Wine.

V reálných systémech se techniky mohou kombinovat. Cloudový server může být virtuální stroj, na kterém běží Linux a uvnitř něj několik kontejnerů.

**Hlavní myšlenka čtvrté lekce:** emulace napodobuje jiné prostředí, virtualizace abstrahuje výpočetní zdroje a kontejnery izolují aplikace nad společným jádrem. Podobně vypadající výsledek může vzniknout z technicky velmi odlišného principu.

---

# 5. Cloudové služby

## 5.1 Cloud není místo v nebi, ale provozní model

Slovo **cloud** se někdy používá tak široce, že ztrácí význam. „Mám to v cloudu“ může znamenat dokument v OneDrive, databázi na serveru, webovou aplikaci nebo tisíc virtuálních strojů v datovém centru.

Cloud computing je vhodné chápat jako model, ve kterém jsou výpočetní, úložné nebo aplikační zdroje poskytovány jako síťová služba, často s možností pružně měnit kapacitu a automatizovat správu.

Cloud stále používá fyzický hardware. Data leží na skutečných discích a výpočty provádějí skutečné procesory v datových centrech.

„Cloud“ tedy neznamená nehmotnost, ale **oddělení uživatele od konkrétního fyzického serveru**.

Uživatel si může objednat virtuální server bez toho, aby věděl, ve kterém konkrétním racku běží. Může zvětšit úložiště přes API, aniž by technik fyzicky instaloval nový disk do jeho kanceláře.

Typickými vlastnostmi cloudu jsou:

- samoobslužné poskytování zdrojů,
- přístup přes síť,
- sdílení infrastruktury,
- pružná škálovatelnost,
- měření využití.

Cloud není synonymum internetu. Internet je globální komunikační infrastruktura. Cloudová služba je konkrétní způsob, jak nad sítí poskytovat výpočetní zdroje.

---

## 5.2 Public, private a hybrid cloud

Podle toho, komu infrastruktura slouží a jak je provozována, rozlišujeme několik modelů nasazení.

**Public cloud** nabízí prostředky více zákazníkům prostřednictvím poskytovatele. Příklady velkých platforem jsou AWS, Microsoft Azure nebo Google Cloud.

Jednotliví zákazníci mohou sdílet fyzickou infrastrukturu, ale jejich logické prostředí je oddělené virtualizací a dalšími bezpečnostními mechanismy.

**Private cloud** je cloudová infrastruktura určená jedné organizaci. Může běžet ve vlastním datovém centru nebo být provozována externím partnerem. Podstatná je vyhrazenost a způsob správy, nikoli prostě to, že „server stojí ve firmě“.

**Hybrid cloud** propojuje privátní a veřejné prostředí tak, aby organizace mohla rozdělit pracovní zátěže podle požadavků.

Například citlivou databázi může držet v privátním prostředí a výpočetně náročné anonymizované úlohy dočasně spouštět ve veřejném cloudu.

Vedle toho existují i **multi-cloud** strategie, kdy organizace používá více poskytovatelů.

Důvodem může být odolnost, dostupnost konkrétních služeb nebo snaha omezit vendor lock-in. Multi-cloud ale zároveň zvyšuje složitost správy.

---

## 5.3 SaaS, PaaS a IaaS: kdo se stará o kterou vrstvu

Klasické cloudové modely se liší podle toho, jak velkou část technologického „stohu“ spravuje poskytovatel.

### IaaS — Infrastructure as a Service

Poskytovatel dodá například virtuální stroje, sítě a úložiště. Zákazník se stará o operační systém, aktualizace, aplikace a data.

Je to podobné, jako kdybychom si pronajali vybavenou serverovnu, ale operační systémy a programy spravovali sami.

### PaaS — Platform as a Service

Poskytovatel spravuje větší část platformy. Vývojář nahraje aplikaci nebo kód a nemusí řešit některé detaily operačního systému, runtime nebo škálování.

PaaS urychluje vývoj, ale přináší silnější vazbu na konkrétní platformu.

### SaaS — Software as a Service

Uživatel používá hotovou aplikaci jako službu. Poskytovatel spravuje infrastrukturu, platformu i samotný software.

Příkladem mohou být webové kancelářské nástroje, CRM, e-mail nebo školní aplikace.

Uživatel se stále stará například o:

- své účty,
- správná oprávnění,
- kvalitu a citlivost ukládaných dat,
- konfiguraci funkcí služby.

Tím se dostáváme k principu **shared responsibility** — sdílené odpovědnosti.

Cloudový poskytovatel může zabezpečit datové centrum, ale zákazník stále může zveřejnit databázi chybným nastavením. SaaS může být technicky dobře chráněný, ale uživatel může podlehnout phishingu.

Čím více vrstev přenecháme poskytovateli, tím méně spravujeme sami, ale tím více jsme závislí na jeho službě a pravidlech.

---

## 5.4 Cloudové úložiště, synchronizace a záloha nejsou totéž

Toto je jedna z nejdůležitějších praktických věcí v celé kapitole.

**Cloudové úložiště** znamená, že data ukládáme na vzdálenou infrastrukturu.

**Synchronizace** znamená, že systém udržuje určité soubory nebo změny mezi zařízeními ve shodě.

**Záloha** je kopie určená k obnově po ztrátě nebo poškození.

Tyto tři funkce se mohou překrývat, ale nejsou totožné.

Představme si synchronizovanou složku. Omylem smažeme dokument. Synchronizační klient si řekne: „uživatel odstranil soubor“ a tuto změnu může rychle rozšířit na další zařízení.

To je správné chování synchronizace, ale z pohledu zálohy jsme právě přišli o kopie.

Mnohé cloudové služby mají koš nebo historii verzí, což poskytuje určitou ochranu. Není ale bezpečné automaticky předpokládat, že každá synchronizace je plnohodnotná zálohovací strategie.

Stejně tak **RAID není záloha**. RAID může zvýšit dostupnost při poruše jednoho disku, ale nechrání automaticky proti:

- omylu uživatele,
- ransomwaru,
- poškození souboru,
- smazání,
- požáru,
- krádeži celého zařízení.

Dobrá správa dat proto kombinuje více mechanismů podle toho, před jakou událostí chceme chránit.

---

## 5.5 Výhody cloudu: škálování, dostupnost a automatizace

Cloud přináší výhody hlavně tehdy, když využíváme jeho provozní model, nikoli jen „cizí disk“.

**Škálovatelnost** umožňuje zvětšovat a zmenšovat kapacitu podle potřeby. Web s malou návštěvností může používat několik málo prostředků a při náhlém nárůstu je automaticky rozšířit.

**Elasticita** zdůrazňuje schopnost kapacitu dynamicky přidělovat a zase uvolňovat.

**Automatizace** je další velká výhoda. Infrastrukturu lze spravovat pomocí API a konfiguračního kódu. Desítky serverů mohou vzniknout automaticky během několika minut.

**Geografická distribuce** umožňuje provozovat služby v několika regionech a přiblížit data uživatelům.

**Managed services** přenášejí část provozní práce na poskytovatele. Organizace nemusí sama spravovat databázový cluster nebo aktualizovat každý server.

Cloud ale není automaticky levnější. Při dlouhodobém stabilním zatížení může vlastní infrastruktura vycházet ekonomicky lépe. Cloud přináší flexibilitu, ale účtování za procesor, přenosy, úložiště a spravované služby může být složité.

Vznikla proto oblast **FinOps**, která se zabývá řízením a optimalizací nákladů cloudových služeb.

---

## 5.6 Rizika cloudu: závislost, data a právní prostředí

Přesun služby do cloudu neodstraňuje rizika. Mění jejich charakter.

Prvním je **vendor lock-in** — závislost na konkrétním poskytovateli. Čím více používáme jeho specifické databáze, API a služby, tím obtížnější může být migrace.

Dalším problémem je **dostupnost**. Velký poskytovatel může mít velmi kvalitní infrastrukturu, ale výpadky stále existují. Kritická služba musí mít návrh odolnosti, nikoli pouze důvěru ve značku poskytovatele.

Zásadní je **ochrana dat**:

- kde jsou data uložena,
- kdo k nim má přístup,
- jak jsou šifrována,
- jak dlouho se uchovávají,
- jak je lze exportovat a odstranit.

Organizace musí zohledňovat také právní a smluvní podmínky, zejména u osobních nebo citlivých dat.

Bezpečnost cloudu proto není tvrzení „data jsou v cloudu bezpečnější“. Mohou být chráněna profesionálními týmy a redundantní infrastrukturou, ale špatná konfigurace účtů a oprávnění může způsobit závažný únik.

**Hlavní myšlenka páté lekce:** cloud přesouvá část technické správy k poskytovateli a umožňuje pružně poskytovat zdroje jako službu. Zároveň vytváří nové závislosti, náklady a odpovědnosti za data a konfiguraci.

---

# 6. Správa programů a dat

## 6.1 Instalace programu: od jednoho setup.exe k balíčkovým systémům

Instalace programu znamená připravit software tak, aby mohl v daném systému správně fungovat.

Historický model osobního počítače byl jednoduchý: uživatel vložil CD, spustil `setup.exe`, prošel instalačním průvodcem a program nakopíroval soubory do několika adresářů.

Dnes existuje více způsobů distribuce.

Ve Windows se používají například instalační balíčky MSI, spustitelné instalátory nebo Microsoft Store. V macOS aplikace často přicházejí jako balíčky a obrazy DMG. Linuxové distribuce používají balíčkové systémy, například DEB nebo RPM, ale uživatel s nimi typicky nepracuje ručně — používá správce balíčků.

Například:

`apt install ...`

nebo:

`dnf install ...`

Správce balíčků řeší:

- zdroj balíčku,
- verze,
- závislosti,
- aktualizace,
- odinstalaci.

Podobný princip používají programovací jazyky:

- `pip` pro Python,
- `npm` pro JavaScript,
- Cargo pro Rust.

Moderní distribuce přes **app store** přidává digitální podpisy, automatické aktualizace, centrální správu oprávnění a někdy sandboxing.

Ve firmách a školách se instalace často automatizuje prostřednictvím centrální správy zařízení. Správce může aplikaci nasadit stovkám počítačů bez ručního klikání.

Správná instalace tedy dnes není jen „zkopírování souborů“. Jde o řízení celého životního cyklu aplikace a jejích závislostí.

---

## 6.2 Bezpečná instalace a původ software

Instalátor je program s velmi vysokou důvěrou. Často získává oprávnění zapisovat do systémových adresářů, vytvářet služby a měnit konfiguraci.

Proto je důležité, **odkud software pochází**.

Nejbezpečnější zdroj bývá:

- oficiální repozitář,
- důvěryhodný app store,
- web výrobce,
- interní firemní distribuční systém.

U instalátoru lze kontrolovat **digitální podpis**, který pomáhá ověřit vydavatele a integritu souboru.

U některých projektů je zveřejněn také kryptografický hash staženého souboru. Pokud vypočtený hash odpovídá oficiální hodnotě, máme další kontrolu, že se obsah cestou nezměnil.

Při instalaci je vhodné sledovat požadovaná oprávnění. Program na úpravu fotografií pravděpodobně nepotřebuje spravovat systémové účty ani automaticky otevírat síťový server.

Velké riziko představuje **supply-chain attack** — útok na dodavatelský řetězec. Útočník nemusí napadnout každého uživatele samostatně. Stačí kompromitovat aktualizační systém, vývojářský účet nebo populární knihovnu.

Bezpečnost software proto začíná ještě před jeho spuštěním: u důvěryhodnosti zdroje a způsobu distribuce.

---

## 6.3 Aktualizace, verze a životní cyklus software

Software není hotový jednou provždy. Po vydání se objevují chyby, nové požadavky i bezpečnostní zranitelnosti.

**Aktualizace** může opravovat chyby, přidávat funkce, zvyšovat kompatibilitu nebo odstraňovat zranitelnosti.

Bezpečnostní aktualizace jsou zvlášť důležité. Jakmile je chyba veřejně známá, mohou vzniknout nástroje, které ji automaticky zneužívají.

Odkládání aktualizace proto může znamenat provoz systému s veřejně známou zranitelností.

Na druhou stranu organizace nemusí každou novou verzi okamžitě nasadit do kritického provozu. Aktualizace mohou přinést regresi, změnit kompatibilitu nebo vyžadovat restart.

Profesionální správa proto kombinuje:

- sledování vydaných oprav,
- hodnocení rizika,
- testování,
- plánované nasazení,
- možnost návratu.

Důležitý je také **konec podpory — End of Life nebo End of Support**. Program může technicky dál fungovat, ale pokud už výrobce nevydává bezpečnostní opravy, jeho provoz se stává stále rizikovější.

Správa software proto musí myslet na celý životní cyklus:

**pořízení → instalace → konfigurace → aktualizace → provoz → migrace → vyřazení**

---

## 6.4 Odinstalace, konfigurace a uživatelská data

Odinstalace programu není totéž co smazání jeho hlavního spustitelného souboru.

Aplikace může během instalace a provozu vytvořit:

- programové soubory,
- systémové služby,
- konfigurační soubory,
- cache,
- databáze,
- uživatelský profil,
- dočasná data.

Korektní odinstalátor se snaží odstranit komponenty, které vlastní, ale často záměrně ponechá uživatelská data nebo konfiguraci.

To je rozumné. Uživatel může program později znovu nainstalovat a nechce přijít o své dokumenty.

Proto není cílem odinstalace za každou cenu „odstranit každou stopu“. Důležité je rozlišovat:

- programový kód,
- systémovou konfiguraci,
- cache,
- uživatelská data.

Agresivní automatické čističe mohou tuto hranici špatně odhadnout.

U firemního zařízení se navíc při vyřazení programu řeší licenční evidence a bezpečné odstranění citlivých dat.

Odinstalace je tedy součást životního cyklu software, nikoli kosmetická operace.

---

## 6.5 Záloha: ochrana proti návratu v čase

**Záloha** je kopie dat vytvořená proto, abychom mohli obnovit stav po ztrátě, poškození nebo nežádoucí změně.

Důležité je slovo **obnovit**. Záloha, kterou neumíme spolehlivě obnovit, má malou hodnotu.

Zálohy chrání například proti:

- selhání disku,
- náhodnému smazání,
- poškození souborů,
- ransomwaru,
- krádeži zařízení,
- požáru,
- některým softwarovým chybám.

Základní strategie jsou:

### Plná záloha

Obsahuje všechny vybrané soubory nebo celý systém.

Obnova je jednoduchá, ale tvorba zabírá více času a prostoru.

### Inkrementální záloha

Po výchozí plné záloze ukládá změny od poslední zálohy.

Je úsporná, ale při obnově může být potřeba celý řetězec záloh.

### Diferenciální záloha

Ukládá změny od poslední plné zálohy.

Postupně roste, ale obnova obvykle potřebuje plnou a poslední diferenciální zálohu.

Vedle souborových záloh existují **obrazy disků nebo systémů**, které mohou zachovat celý systém včetně struktury oddílů a operačního prostředí.

Moderní zálohovací systémy často používají snapshoty, deduplikaci a průběžné ukládání změn. Konkrétní implementace se liší, ale cíl je stejný: umožnit návrat k bezpečnému stavu.

---

## 6.6 Pravidlo 3–2–1 a proč jedna kopie nestačí

Známé pravidlo zálohování **3–2–1** říká zjednodušeně:

- mít alespoň tři kopie dat,
- na alespoň dvou typech úložiště nebo nezávislých systémech,
- alespoň jednu kopii mimo hlavní lokalitu.

Dnešní bezpečnostní praxe často přidává požadavek na **offline nebo immutable** kopii, kterou ransomware nemůže snadno přepsat.

Představme si notebook a externí disk, který je trvale připojený. Pokud ransomware zašifruje oba, nemáme skutečně oddělenou ochranu.

Podobně NAS ve stejné místnosti nepomůže při požáru nebo krádeži celé techniky.

Dobrá strategie proto kombinuje různé druhy selhání:

- lokální chyba disku,
- lidský omyl,
- škodlivý software,
- fyzická katastrofa,
- kompromitace účtu.

Velmi důležité je **testování obnovy**. Organizace může roky hlásit „backup successful“, ale při skutečné havárii zjistí, že záloha je neúplná nebo že nikdo nezná správný postup.

Proto je obnova součástí zálohovacího procesu stejně jako samotné kopírování.

---

## 6.7 Synchronizace, archivace, RAID a verzování

Pro bezpečnou správu dat musíme rozlišovat několik mechanismů.

**Synchronizace** udržuje data na více místech ve shodě. Výborně se hodí pro práci na více zařízeních, ale může rychle rozšířit i nežádoucí změnu.

**Záloha** umožňuje obnovit předchozí stav.

**Archivace** uchovává data dlouhodobě, často kvůli historické, právní nebo dokumentační hodnotě. Archiv může mít jinou retenční politiku než běžná záloha.

**RAID** kombinuje více disků pro výkon nebo odolnost proti selhání některých disků. Nechrání však proti všem druhům ztráty dat, a proto není náhradou zálohy.

**Verzování** ukládá starší verze souboru nebo objektu. Může významně pomoci po chybné editaci nebo ransomwarovém incidentu.

Podobný princip známe z Git repozitáře, který uchovává historii změn zdrojového kódu. Git ale není automaticky záloha celého pracovního počítače. Pokud je repozitář pouze lokálně a disk selže, historie zmizí spolu s ním.

Každý mechanismus řeší jiný typ problému. Správná správa dat je proto kombinací několika vrstev.

---

## 6.8 Správa dat jako životní cyklus

Data mají svůj životní cyklus podobně jako software.

Vznikají, mění se, kopírují, sdílejí, archivují a nakonec mají být odstraněna.

U každého významného datového souboru bychom měli vědět:

- kdo je jeho vlastníkem,
- kdo k němu má přístup,
- kde jsou jeho kopie,
- jak dlouho se má uchovávat,
- zda je zálohován,
- zda obsahuje citlivé informace,
- jak bude bezpečně odstraněn.

U osobních údajů nebo firemních dokumentů může být nekontrolované „necháme si všechno navždy“ problémem. Větší množství uložených dat znamená také větší rozsah případného úniku.

Proto se uplatňuje **minimalizace dat** a retenční pravidla.

Bezpečné odstranění navíc není vždy totéž co přetažení do koše. Na některých médiích mohou zůstat obnovitelné kopie, cloudové služby mohou mít vlastní retenční vrstvy a SSD používají interní mechanismy, které komplikují jednoduchou představu „přepsat sektor několikrát“.

Při vyřazení zařízení je proto vhodné používat postupy doporučené pro daný typ úložiště, například kryptografické vymazání nebo bezpečné resetování zařízení.

Správa programů a dat nakonec není jen technická údržba. Je to disciplína, která propojuje **dostupnost, bezpečnost, náklady, kompatibilitu a dlouhodobou udržitelnost**.

---

# Závěrečné propojení kurzu

Programy a data nejsou dvě oddělené poloviny počítače. Program je sám uložen jako data, dokud jej operační systém nenačte a nevytvoří běžící proces. Aplikace pak zpracovává další data, která mohou být uložena lokálně, v databázi, na síťovém disku nebo v cloudu.

Celou oblast lze shrnout jako několik vrstev:

**data na úložišti → souborový systém → operační systém → aplikace → uživatel**

K tomu přistupují další otázky:

**Kdo smí program používat?**  
To řeší licence.

**Jak spustíme software vytvořený pro jiné prostředí?**  
To řeší emulace, kompatibilní vrstvy a virtualizace.

**Kde budou aplikace a data provozovány?**  
Jednou možností jsou cloudové služby.

**Jak zajistíme, aby software zůstal bezpečný a data nezmizela?**  
To řeší aktualizace, řízení oprávnění, zálohy, verzování a správa životního cyklu.

Výslednou cestu lze zapsat:

**soubor → program nebo data → proces → služba → uživatelská práce → změna dat → uložení → synchronizace nebo záloha → dlouhodobá správa**

Právě toto propojení dává tématům smysl. DLL, GPL, virtuální stroj, SaaS nebo inkrementální záloha nejsou izolované zkratky. Jsou to různé odpovědi na jednu praktickou otázku: **jak dlouhodobě a bezpečně provozovat software a spravovat data v reálném výpočetním prostředí.****
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
