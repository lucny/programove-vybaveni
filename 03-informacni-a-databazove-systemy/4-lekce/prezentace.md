## Snímek 4.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Databáze, DBMS a aplikace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 4.1 Databáze, DBMS a aplikace

**Databáze** je organizovaná kolekce souvisejících dat určená k dlouhodobému používání. **Systém řízení báze dat — DBMS, Database Management System** je software, který databázi vytváří, zpřístupňuje a chrání. Zajišťuje dotazování, změny, souběžný přístup, oprávnění, integritu a obnovu. **Databázový systém** tvoří databáze, DBMS, potřebná infrastruktura, pravidla a uživatelé. Aplikace nad ním nabízí funkce konkrétního IS.

Když žák v knihovní aplikaci vyhledá titul, formulář obvykle neotevírá databázový soubor přímo. Odešle požadavek aplikační vrstvě, ta ověří identitu a oprávnění, provede dotaz přes databázový ovladač nebo API a výsledek převede do podoby stránky. Zápis výpůjčky navíc musí respektovat pravidla: výtisk je dostupný, čtenář má aktivní účet a operace se provede jako celek.

Databáze se používá proto, že běžný soubor obtížně zvládá mnoho souběžných uživatelů, vztahy mezi záznamy, řízení přístupu a spolehlivou obnovu. Tabulkový procesor je výborný pro menší analýzu, ale sdílený sešit s tisíci zákazníků není náhradou za provozní databázi. Naopak malý osobní seznam nemusí získat nic tím, že jej zbytečně přesuneme do složitého serverového DBMS.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Od předrelačních k postrelačním databázím**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 4.2 Od předrelačních k postrelačním databázím

Historické **hierarchické databáze** organizovaly záznamy jako strom rodičů a potomků. Dobře odpovídaly situacím s přirozenou a stabilní hierarchií, ale složité vztahy mezi větvemi se vyjadřovaly obtížně. Princip přetrvává v adresářových službách, souborových stromech nebo dokumentech XML a JSON, i když jejich dnešní implementace nejsou prostým pokračováním původních DBMS.

**Síťový databázový model** dovoloval záznamu více vazeb a podporoval složitější struktury. Aplikační program však často musel znát cestu, po níž daty projde. Vývojář tedy nepopisoval jen požadovaný výsledek, ale navigoval mezi konkrétními záznamy. Tato těsná vazba ztěžovala změny struktury.

**Relační model** uspořádal data do relací, prakticky zobrazovaných jako tabulky, a oddělil logický dotaz od fyzického uložení. Vazby se vyjadřují klíči a data se zpracovávají deklarativním jazykem SQL. Relační databáze, například PostgreSQL, MySQL, Microsoft SQL Server nebo SQLite, zůstávají základní volbou pro mnoho transakčních aplikací, protože dobře podporují integritu, vztahy a transakce. Podrobný návrh tabulek, normalizace a SQL však patří do samostatného okruhu.

Označení **postrelační** není jeden přesný datový model. Používá se pro přístupy, které relační model rozšiřují nebo řeší potřeby, pro něž tabulky nejsou nejpřirozenější reprezentací. Patří sem objektově-relační rozšíření, objektové databáze a především různé NoSQL databáze. Moderní systémy se navíc ovlivňují: relační DBMS ukládají JSON a NoSQL produkty mohou podporovat transakce či dotazovací jazyky podobné SQL. Důležitější než nálepka je způsob modelování a typ požadovaných dotazů.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Datové modely a různé pohledy na stejnou skutečnost**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 4.3 Datové modely a různé pohledy na stejnou skutečnost

**Datový model** určuje, z jakých stavebních prvků se data skládají, jaké vazby lze vyjádřit a jaké operace nad nimi systém provádí. Relační model používá tabulky a klíče, dokumentový model vnořené dokumenty, key-value model pár klíč–hodnota, grafový model uzly a hrany. Stejnou školní knihovnu lze popsat všemi těmito způsoby, ale každý zvýhodní jiné otázky.

V relační databázi lze oddělit tituly, fyzické výtisky, čtenáře a výpůjčky. Dokumentová databáze může uložit katalogový záznam s poli, autory a seznamem štítků v jednom dokumentu. Key-value databáze se hodí pro rychlé načtení relace přihlášeného uživatele podle náhodného klíče. Grafová databáze může sledovat vazby mezi knihami, tématy, autory a doporučeními. Volba není soutěž o „nejmodernější“ typ, ale rozhodnutí podle struktury dat, dotazů, objemu a provozních požadavků.

Vedle logického modelu rozlišujeme také fyzické uspořádání. **Řádkové uložení** drží hodnoty jednoho záznamu blízko sebe a hodí se pro časté čtení či změnu celých záznamů. **Sloupcové uložení** drží pohromadě hodnoty stejného sloupce a usnadňuje analytické součty nad mnoha řádky. Sloupcový analytický DBMS ale není totéž co NoSQL wide-column databáze; podobný název označuje jiný princip.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 4.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Uživatelé databáze a hromadné operace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**## 4.4 Uživatelé databáze a hromadné operace

Databázi nepoužívá jediný „uživatel“. Běžný uživatel pracuje přes formulář a databázi vůbec nemusí vidět. **Databázový administrátor — DBA** nastavuje účty, výkon, zálohy a obnovu. Vývojář vytváří aplikaci a dotazy, datový analytik zkoumá souhrny, datový inženýr připravuje přenosy a transformace. Vlastník dat rozhoduje o významu a oprávněném použití; správce technologie pouze neřeší obsahovou odpovědnost.

Podle přístupu rozlišujeme **jednouživatelské** a **víceuživatelské** databáze. SQLite v lokální aplikaci může sloužit jednomu uživateli bez samostatného serveru. Serverové DBMS obsluhují mnoho klientů současně a musí řešit souběh. Toto rozdělení neříká, jaký datový model databáze používá; popisuje provozní způsob přístupu.

Síla databáze se projeví při hromadném zpracování. Místo tisíce ručních změn lze jedním příkazem vybrat, agregovat nebo aktualizovat celou množinu záznamů. Hromadná operace je rychlá, ale chyba má také hromadný dopad. Před změnou je nutné ověřit podmínku, zajistit oprávnění, vytvořit možnost návratu a zaznamenat, co se provedlo. Automatizace násobí správný postup i omyl.

**Hlavní myšlenka:** Databáze poskytuje organizované a sdílené uložení dat, DBMS řídí práci s nimi a aplikace z nich vytváří konkrétní službu. Datový model se vybírá podle toho, jaká data máme a jaké otázky nad nimi potřebujeme řešit.

# 5. NoSQL databáze

## 5.1 Proč vzniklo „Not only SQL“

Označení **NoSQL** se používá pro skupinu nerelačních databázových modelů. Často se vykládá jako „Not only SQL“ — nejen SQL. Neznamená zákaz relačních databází, absenci dotazovacího jazyka ani databázi bez pravidel. NoSQL systémy vznikaly pro různé potřeby: pružně se měnící dokumenty, velmi rychlý přístup podle klíče, zápis obrovského proudu událostí, distribuci mezi mnoho uzlů nebo efektivní procházení vztahů.

Ani „bezschémová databáze“ není přesný popis. Dokumentová databáze může přijmout dokumenty s rozdílnými poli, aplikace však stále očekává určitý význam, typy a povinné údaje. Schéma nezmizelo; část odpovědnosti se přesunula do aplikace, validačních pravidel a správy dat. Pružnost urychlí změnu, ale bez disciplíny může vytvořit směs nekompatibilních záznamů.

NoSQL není automaticky rychlejší. Výkon závisí na konkrétní operaci, datovém modelu, indexech, distribuci a konfiguraci. Relační databáze může být nejlepší pro účetní transakce, dokumentová pro katalog proměnlivých produktů a grafová pro hledání vazeb. Často se používají vedle sebe v jedné aplikaci, což označujeme jako **polyglot persistence**.

## 5.2 Dokumentové databáze

**Dokumentová databáze** ukládá záznam jako dokument, obvykle ve struktuře podobné JSON. Dokument obsahuje pole, vnořené objekty a seznamy. MongoDB může například uložit katalogový záznam knihy spolu s autory, štítky, jazyky a různými vydáními. Dva dokumenty ve stejné kolekci nemusí mít vždy úplně stejná pole.

Základním návrhovým pravidlem je ukládat společně data, která aplikace často čte a mění společně. Detail produktu v e-shopu může obsahovat parametry, obrázky a varianty. Jediné načtení poskytne celou stránku. Vnoření však není vhodné bez omezení. Pokud se stejný autor opakuje v tisících dokumentů a jeho údaje se často mění, vznikají duplicity. Rozsáhlé vztahy mnoho ku mnoha mohou být přehlednější pomocí odkazů nebo jiného modelu.

Dokumentové databáze se hodí pro katalogy s různými vlastnostmi, profily, správu obsahu, události aplikace nebo rychle se vyvíjející webové služby. Výhodou je přirozená shoda s objekty používanými v programu a pružný vývoj schématu. Nevýhodou může být duplicita, složitější globální kontrola pravidel a nutnost navrhovat strukturu podle skutečných přístupových vzorů.

## 5.3 Key-value databáze

**Key-value databáze** funguje jako rozsáhlý slovník. Jedinečný klíč ukazuje na hodnotu a systém ji velmi rychle uloží nebo načte. Příkladem je Redis. Webová aplikace může pod náhodným klíčem uchovat stav přihlášení, obsah krátkodobé cache nebo čítač požadavků.

Síla jednoduchého modelu je zároveň jeho omezením. Když známe klíč, je přístup velmi rychlý. Pokud se ale chceme ptát na libovolnou vlastnost ukrytou uvnitř hodnoty, systém ji nemusí umět efektivně prohledat. Datový model proto vyžaduje předem vědět, jak budou data vyhledávána.

Key-value úložiště se používají pro relace uživatelů, mezipaměť, nákupní košíky, žebříčky nebo omezení počtu požadavků. U cache musí aplikace počítat s tím, že položka zmizí nebo bude zastaralá. Mezipaměť zrychluje přístup, ale nemá se bez dalšího stát jediným důvěryhodným zdrojem důležitých dat.

## 5.4 Wide-column databáze

**Wide-column databáze** organizuje data do řádků a sloupcových rodin, ale není to relační tabulka s libovolnými spojeními. Apache Cassandra rozděluje data podle klíče mezi uzly a modeluje tabulky podle dotazů, které musí systém rychle obsloužit. Jeden typ informace proto může být uložen více způsoby pro různé dotazy.

Představme si miliony měření ze senzorů. Častý dotaz zní: „Vrať všechna měření daného senzoru za konkrétní den v časovém pořadí.“ Vhodný klíč spojí identitu senzoru s časovým úsekem a data uvnitř oddílu seřadí podle času. Nevhodný klíč by vytvořil jediný obrovský oddíl nebo nerovnoměrně zatížil několik uzlů.

Wide-column systémy se hodí pro telemetrii, časové řady, komunikační události a služby s velmi vysokým objemem zápisů a požadavkem na geografickou dostupnost. Výhodou je horizontální škálování a odolnost proti výpadku uzlu. Cenou bývá méně pružné dotazování a potřeba znát přístupové vzory už při návrhu. Cassandra navíc není „sloupcový datový sklad“ v analytickém smyslu; jde o distribuovaný wide-column model určený především pro jiný druh zátěže.

## 5.5 Grafové databáze

**Grafová databáze** ukládá **uzly**, **vztahy** a jejich vlastnosti. V Neo4j může být uzlem člověk, kniha nebo téma a vztah může znamenat „četl“, „napsal“ či „souvisí s“. Vztah je plnohodnotná součást modelu, nikoli jen nepřímá shoda hodnot ve dvou tabulkách.

Graf je výhodný, když otázka vede přes řetězec vazeb: Kteří lidé jsou propojeni s podezřelou transakcí? Jaké přestupy spojují dvě zastávky? Které knihy četli lidé s podobným profilem? Kdo má v podnikové síti nepřímý přístup k citlivému prostředku? Délka a tvar cesty jsou často důležitější než součet sloupce.

Použití zahrnuje sociální a znalostní sítě, doporučování, detekci podvodů, správu závislostí a síťovou bezpečnost. Grafová databáze ale není automaticky nejlepší jen proto, že data obsahují vztahy — vztahy má téměř každá databáze. Výhodu získá tehdy, když je procházení mnoha proměnlivých vazeb hlavní částí dotazů.

## 5.6 Distribuce, konzistence a volba modelu

Distribuovaná databáze ukládá data na více uzlech. **Replikace** vytváří kopie pro dostupnost a odolnost, **partitioning neboli sharding** rozděluje data, aby se zátěž rozložila. Když se přeruší spojení mezi uzly, systém musí rozhodnout, zda některé operace odmítne ve prospěch silnější konzistence, nebo je přijme ve prospěch dostupnosti a kopie později sladí. CAP teorém se týká právě chování při síťovém rozdělení; neříká, že si databáze jednou provždy vybere pouze dvě libovolná písmena ze tří.

**Eventual consistency — výsledná konzistence** znamená, že kopie mohou být dočasně rozdílné, ale bez dalších změn se sjednotí. Pro počet reakcí u příspěvku může být krátké zpoždění přijatelné. Pro zůstatek při převodu peněz by mohlo být nebezpečné. Některé NoSQL systémy dovolují úroveň konzistence volit podle operace a moderní produkty často podporují i transakce. Nelze tedy tvrdit, že NoSQL vždy obětuje správnost.

Při volbě se nejprve ptáme na data a dotazy: Je struktura pravidelná? Které záznamy se čtou společně? Jsou nejdůležitější vazby? Jaký objem zápisu očekáváme? Jaké chyby lze tolerovat? Jak rychle se musí systém obnovit? Teprve potom se vybírá produkt. Školní systém může použít relační databázi pro výpůjčky, dokumentový index pro katalog, key-value cache pro relace a graf pro doporučování. Více technologií však zvyšuje nároky na provoz, zálohování i znalosti týmu, proto musí mít každá jasný důvod.

**Hlavní myšlenka:** NoSQL není jedna technologie ani náhrada všech relačních databází. Dokumentový, key-value, wide-column a grafový model řeší odlišné přístupové vzory a přinášejí vlastní výhody i omezení.

# 6. Big data a datové sklady

## 6.1 Kdy se z dat stávají big data

**Big data — velká data** nejsou určena pevným počtem gigabajtů. Jde o data, jejichž vlastnosti překračují možnosti běžné architektury a vyžadují jiné způsoby ukládání, přenosu nebo zpracování. Často se popisují pomocí „V“: **volume** označuje objem, **velocity** rychlost vzniku a příchodu, **variety** různorodost formátů. Doplňuje se **veracity**, tedy nejistá kvalita a důvěryhodnost, a **value**, skutečná hodnota pro daný účel.

Meteorologická služba přijímá proud měření ze stanic, radarů a družic; e-shop vytváří objednávky, kliknutí a provozní logy; město získává data z dopravy a senzorů. Velikost sama nestačí. Milion jednoduchých řádků může zvládnout běžný DBMS, zatímco rychlý proud různorodých událostí vyžaduje distribuované zpracování. Správná otázka tedy nezní „Kolik dat už je big data?“, ale „Která vlastnost dat nutí změnit architekturu?“

Ne všechna dostupná data je účelné shromažďovat. Uchování stojí peníze, zvětšuje bezpečnostní dopad úniku a může porušovat zásadu omezení účelu. Datová strategie má určit, proč údaj potřebujeme, jak dlouho jej uchováme a podle čeho poznáme jeho přínos.

## 6.2 Datový sklad sjednocuje historická data

**Datový sklad — data warehouse, DWH** je analytické úložiště, které integruje data z více zdrojů, sjednocuje jejich význam a uchovává historii. Provozní systémy školy evidují rozvrh, docházku, výsledky a provoz učeben každý po svém. Datový sklad může vytvořit společné dimenze času, třídy a předmětu, takže analytik porovnává údaje podle jedné definice.

Data se do skladu dostávají procesem **ETL — extract, transform, load**: nejprve se získají ze zdrojů, poté vyčistí a převedou a nakonec načtou do cíle. U varianty **ELT** se nejprve načtou a transformují až v cílové platformě. Ani jeden postup není automaticky lepší; volba závisí na prostředí, objemu a potřebě uchovat původní data.

Pro analytiku se často používá model faktů a dimenzí. **Faktová tabulka** obsahuje měřené události, například počet prodaných kusů a cenu. **Dimenze** popisují čas, produkt, zákazníka nebo pobočku. Takzvané hvězdicové schéma umožňuje snadno odpovídat na otázky typu „Jak se vyvíjel prodej dané kategorie podle měsíců a regionů?“ Jde o analytický model, nikoli o náhradu provozní databáze.

Vedle skladu se používá **data lake — datové jezero**, které uchovává velké množství strukturovaných i nestrukturovaných dat v méně předem upravené podobě. Je pružné pro další zpracování, ale bez katalogu, pravidel kvality a odpovědnosti se může změnit v nepřehlednou „datovou bažinu“. Moderní architektury někdy vlastnosti skladu a jezera kombinují; principem stále zůstává řízený původ, význam a kvalita dat.

## 6.3 OLTP a OLAP řeší jiné úkoly

Správná zkratka pro provozní zpracování je **OLTP — Online Transaction Processing**. OLTP obsluhuje velké množství krátkých operací nad aktuálními daty: vytvoření objednávky, změnu rezervace, výběr z účtu. Typický dotaz pracuje s několika záznamy, odezva má být krátká a změna spolehlivá.

**OLAP — Online Analytical Processing** slouží analytice. Čte velké množství historických záznamů, seskupuje je a porovnává podle více rozměrů. Vedoucí prodeje začne celkovým obratem, rozpadne jej podle regionu, přejde na měsíc a nakonec na produkt. Přechod ze souhrnu do detailu se označuje jako **drill-down**, opačný směr jako **roll-up**. Filtrování a výběr řezu dat umožňuje zkoumat stejnou skutečnost z různých úhlů.

OLTP databáze je navržena pro bezpečné změny během provozu; datový sklad a OLAP pro rozsáhlé čtení a agregaci. Pokud analytik spustí náročný souhrn přímo nad živou databází e-shopu, může zpomalit zákaznické objednávky. Oddělení zátěží proto chrání provoz a současně umožní uchovat historický stav, který se v běžném systému průběžně přepisuje.

## 6.4 Zpracování velkých dat

Velká data se často dělí mezi více počítačů. **Dávkové zpracování — batch processing** zpracuje větší celek najednou, například noční souhrn denních transakcí. Je efektivní, pokud výsledek nemusí vzniknout okamžitě. **Proudové zpracování — stream processing** vyhodnocuje události průběžně; používá se pro detekci podvodu, monitoring sítě nebo řízení výroby.

Distribuované zpracování přesouvá výpočet k částem dat a výsledky skládá. Platformy jako Apache Spark mohou provádět transformace a analýzy nad rozsáhlými datovými sadami. Sloupcové analytické databáze zase čtou jen potřebné sloupce a dobře je komprimují, takže rychle počítají souhrny. Cloud dovoluje dočasně přidat výkon, ale nezruší potřebu řídit náklady a bezpečnost.

Z dat lze získávat popisné statistiky, hledat skupiny, neobvyklé případy a vztahy nebo vytvářet predikční modely. **Data mining — dolování dat** označuje hledání užitečných vzorů ve velkých datech pomocí statistiky, databázových metod a strojového učení. Nalezený vzor však není automaticky příčina ani trvalé pravidlo. Model se musí ověřit na datech, na nichž se neučil, a sledovat i po nasazení, protože svět se mění.

## 6.5 Jak lze data zneužít

Velké soubory dat umožňují užitečné objevy, ale také rozsáhlé zásahy do soukromí. Propojením zdánlivě nevinných údajů lze znovu rozpoznat člověka, odvodit zdravotní stav, pohyb, sociální vztahy nebo finanční situaci. **Pseudonymizace** nahrazuje přímý identifikátor jiným, ale možnost zpětného spojení může zůstat. **Anonymizace** má být nevratná, což je u bohatých propojitelných dat obtížné.

Profilování může rozhodovat, kdo uvidí nabídku, dostane úvěr nebo bude označen za rizikového. Pokud historická data obsahují nerovné zacházení, model jej může opakovat. Výsledek může být diskriminační i bez použití výslovně citlivého údaje, protože jiné proměnné fungují jako jeho zástupce. Automatické skóre proto potřebuje kontrolu účelu, kvality dat, dopadu na různé skupiny a možnost lidského přezkoumání.

Dalším rizikem je **účelový posun**: data shromážděná pro jednu službu se začnou používat k jinému cíli, který uživatel neočekával. Školní přístupový systém může být zaveden kvůli bezpečnosti, ale později použit k detailnímu sledování pohybu. Technická možnost není sama o sobě oprávněním.

Ochrana stojí na minimalizaci dat, omezení doby uchování, řízení přístupu, šifrování, auditu a transparentních pravidlech. Organizace má vědět, odkud data pocházejí, kdo za ně odpovídá a jak lze chybný záznam opravit. Etika a bezpečnost nejsou dodatek po dokončení analýzy; ovlivňují už to, co se bude sbírat a jaké rozhodnutí je přijatelné automatizovat.

**Hlavní myšlenka:** Big data vyžadují nové architektury kvůli objemu, rychlosti nebo různorodosti. Datový sklad sjednocuje historická data pro OLAP, zatímco OLTP chrání každodenní transakce. Schopnost rozsáhle analyzovat data musí doprovázet kontrola kvality, účelu, soukromí a dopadu rozhodnutí.

# Závěrečné propojení

Informační a databázový systém není totéž. Informační systém začíná potřebou organizace a zahrnuje lidi, procesy, data i techniku. Databázový systém je část infrastruktury, která data organizovaně ukládá a zpřístupňuje. Nad stejnou databází mohou pracovat provozní aplikace, manažerské přehledy i analytické nástroje, ale každý typ uživatele potřebuje jiný pohled a jiná oprávnění.

Celý okruh lze shrnout řetězcem:

**potřeba → proces → vstupní data → zpracování → provozní informace → databázový model → analytika → rozhodnutí → zpětná vazba**

Dobré řešení nezačíná otázkou „Jakou databázi použijeme?“, ale otázkami „Jaký problém řešíme, kdo bude výsledek používat a podle čeho poznáme, že systém funguje?“ Teprve potom se rozhoduje, zda postačí relační databáze, zda se hodí dokumentový, key-value, wide-column či grafový model a zda je nutný datový sklad nebo distribuované zpracování.

## Ověřené zdroje k dalšímu studiu

- [NIST Big Data Interoperability Framework: Definitions](https://www.nist.gov/publications/nist-big-data-interoperability-framework-volume-1-big-data-definitions-version-2)
- [MongoDB: Data Modeling](https://www.mongodb.com/docs/manual/data-modeling/)
- [Apache Cassandra: Architecture Overview](https://cassandra.apache.org/doc/latest/cassandra/architecture/overview.html)
- [Neo4j: What is a Graph Database](https://neo4j.com/docs/getting-started/graph-database/)
- [PostgreSQL: Transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
