## Snímek 5.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Proč vzniklo „Not only SQL“**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Označení **NoSQL** se používá pro skupinu nerelačních databázových modelů. Často se vykládá jako „Not only SQL“ — nejen SQL. Neznamená zákaz relačních databází, absenci dotazovacího jazyka ani databázi bez pravidel. NoSQL systémy vznikaly pro různé potřeby: pružně se měnící dokumenty, velmi rychlý přístup podle klíče, zápis obrovského proudu událostí, distribuci mezi mnoho uzlů nebo efektivní procházení vztahů.

Ani „bezschémová databáze“ není přesný popis. Dokumentová databáze může přijmout dokumenty s rozdílnými poli, aplikace však stále očekává určitý význam, typy a povinné údaje. Schéma nezmizelo; část odpovědnosti se přesunula do aplikace, validačních pravidel a správy dat. Pružnost urychlí změnu, ale bez disciplíny může vytvořit směs nekompatibilních záznamů.

NoSQL není automaticky rychlejší. Výkon závisí na konkrétní operaci, datovém modelu, indexech, distribuci a konfiguraci. Relační databáze může být nejlepší pro účetní transakce, dokumentová pro katalog proměnlivých produktů a grafová pro hledání vazeb. Často se používají vedle sebe v jedné aplikaci, což označujeme jako **polyglot persistence**.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Dokumentové databáze**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**Dokumentová databáze** ukládá záznam jako dokument, obvykle ve struktuře podobné JSON. Dokument obsahuje pole, vnořené objekty a seznamy. MongoDB může například uložit katalogový záznam knihy spolu s autory, štítky, jazyky a různými vydáními. Dva dokumenty ve stejné kolekci nemusí mít vždy úplně stejná pole.

Základním návrhovým pravidlem je ukládat společně data, která aplikace často čte a mění společně. Detail produktu v e-shopu může obsahovat parametry, obrázky a varianty. Jediné načtení poskytne celou stránku. Vnoření však není vhodné bez omezení. Pokud se stejný autor opakuje v tisících dokumentů a jeho údaje se často mění, vznikají duplicity. Rozsáhlé vztahy mnoho ku mnoha mohou být přehlednější pomocí odkazů nebo jiného modelu.

Dokumentové databáze se hodí pro katalogy s různými vlastnostmi, profily, správu obsahu, události aplikace nebo rychle se vyvíjející webové služby. Výhodou je přirozená shoda s objekty používanými v programu a pružný vývoj schématu. Nevýhodou může být duplicita, složitější globální kontrola pravidel a nutnost navrhovat strukturu podle skutečných přístupových vzorů.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Key-value databáze**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----
**Key-value databáze** funguje jako rozsáhlý slovník. Jedinečný klíč ukazuje na hodnotu a systém ji velmi rychle uloží nebo načte. Příkladem je Redis. Webová aplikace může pod náhodným klíčem uchovat stav přihlášení, obsah krátkodobé cache nebo čítač požadavků.

Síla jednoduchého modelu je zároveň jeho omezením. Když známe klíč, je přístup velmi rychlý. Pokud se ale chceme ptát na libovolnou vlastnost ukrytou uvnitř hodnoty, systém ji nemusí umět efektivně prohledat. Datový model proto vyžaduje předem vědět, jak budou data vyhledávána.

Key-value úložiště se používají pro relace uživatelů, mezipaměť, nákupní košíky, žebříčky nebo omezení počtu požadavků. U cache musí aplikace počítat s tím, že položka zmizí nebo bude zastaralá. Mezipaměť zrychluje přístup, ale nemá se bez dalšího stát jediným důvěryhodným zdrojem důležitých dat.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Sloupcové databáze**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

**Wide-column databáze** neboli **sloupcová databáze** organizuje data do řádků a sloupcových rodin, ale není to relační tabulka s libovolnými spojeními. Apache Cassandra rozděluje data podle klíče mezi uzly a modeluje tabulky podle dotazů, které musí systém rychle obsloužit. Jeden typ informace proto může být uložen více způsoby pro různé dotazy.

Představme si miliony měření ze senzorů. Častý dotaz zní: „Vrať všechna měření daného senzoru za konkrétní den v časovém pořadí.“ Vhodný klíč spojí identitu senzoru s časovým úsekem a data uvnitř oddílu seřadí podle času. Nevhodný klíč by vytvořil jediný obrovský oddíl nebo nerovnoměrně zatížil několik uzlů.

Wide-column systémy se hodí pro telemetrii, časové řady, komunikační události a služby s velmi vysokým objemem zápisů a požadavkem na geografickou dostupnost. Výhodou je horizontální škálování a odolnost proti výpadku uzlu. Cenou bývá méně pružné dotazování a potřeba znát přístupové vzory už při návrhu. Cassandra navíc není „sloupcový datový sklad“ v analytickém smyslu; jde o distribuovaný wide-column model určený především pro jiný druh zátěže.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Grafové databáze**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

**Grafová databáze** ukládá **uzly**, **vztahy** a jejich vlastnosti. V Neo4j může být uzlem člověk, kniha nebo téma a vztah může znamenat „četl“, „napsal“ či „souvisí s“. Vztah je plnohodnotná součást modelu, nikoli jen nepřímá shoda hodnot ve dvou tabulkách.

Graf je výhodný, když otázka vede přes řetězec vazeb: Kteří lidé jsou propojeni s podezřelou transakcí? Jaké přestupy spojují dvě zastávky? Které knihy četli lidé s podobným profilem? Kdo má v podnikové síti nepřímý přístup k citlivému prostředku? Délka a tvar cesty jsou často důležitější než součet sloupce.

Použití zahrnuje sociální a znalostní sítě, doporučování, detekci podvodů, správu závislostí a síťovou bezpečnost. Grafová databáze ale není automaticky nejlepší jen proto, že data obsahují vztahy — vztahy má téměř každá databáze. Výhodu získá tehdy, když je procházení mnoha proměnlivých vazeb hlavní částí dotazů.**
------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***

## Snímek 5.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Distribuce, konzistence a volba modelu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----

Distribuovaná databáze ukládá data na více uzlech. **Replikace** vytváří kopie pro dostupnost a odolnost, **partitioning neboli sharding** rozděluje data, aby se zátěž rozložila. Když se přeruší spojení mezi uzly, systém musí rozhodnout, zda některé operace odmítne ve prospěch silnější konzistence, nebo je přijme ve prospěch dostupnosti a kopie později sladí. CAP teorém se týká právě chování při síťovém rozdělení; neříká, že si databáze jednou provždy vybere pouze dvě libovolná písmena ze tří.

**Eventual consistency — výsledná konzistence** znamená, že kopie mohou být dočasně rozdílné, ale bez dalších změn se sjednotí. Pro počet reakcí u příspěvku může být krátké zpoždění přijatelné. Pro zůstatek při převodu peněz by mohlo být nebezpečné. Některé NoSQL systémy dovolují úroveň konzistence volit podle operace a moderní produkty často podporují i transakce. Nelze tedy tvrdit, že NoSQL vždy obětuje správnost.

Při volbě se nejprve ptáme na data a dotazy: Je struktura pravidelná? Které záznamy se čtou společně? Jsou nejdůležitější vazby? Jaký objem zápisu očekáváme? Jaké chyby lze tolerovat? Jak rychle se musí systém obnovit? Teprve potom se vybírá produkt. Školní systém může použít relační databázi pro výpůjčky, dokumentový index pro katalog, key-value cache pro relace a graf pro doporučování. Více technologií však zvyšuje nároky na provoz, zálohování i znalosti týmu, proto musí mít každá jasný důvod.

**Hlavní myšlenka:** NoSQL není jedna technologie ani náhrada všech relačních databází. Dokumentový, key-value, wide-column a grafový model řeší odlišné přístupové vzory a přinášejí vlastní výhody i omezení.

------
Formát 16:9, ideálně 1600 × 900 px. Profesionální encyklopedická grafika pro středoškolskou výuku informatiky. Světlá, vzdušná kompozice s dostatkem volného prostoru; dominantní metafora může vytvářet vlastní prostor a hloubku. Výrazný tmavý titulek organicky začleněný do architektury obrazu, bez povinné horní lišty. Velké bezpatkové písmo, vysoký kontrast, bezpečné okraje. Grafické prvky mají nést hlavní výklad; text používej jen pro nezbytné přesné názvy, cesty a krátká vysvětlení.
**Obraz má vysvětlovat, ne jen zdobit.** Atraktivita musí pomáhat pochopení nebo zapamatování.
**Konkrétní příklad je cennější než obecný symbol.** Skutečná situace, objekt nebo rozhodnutí často vysvětlí téma lépe než sada ikon. **Metafora, technický model a realita se nesmějí slít.** Je-li použita metafora, musí být jasné, co představuje a kde její platnost končí. **Text je součást kompozice, nikoli povinná sada boxů.** Může být vytištěn na objektu, začleněn do prostoru, položen do negativního místa, veden podél řezu nebo tvořit součást vizuálního kontrastu. Text by měl být dobře čitelný, používej dostatečné velikosti fontů. Nepoužívej univerzální karty, opakované boxy ani dekorativní šipky; směr a vztahy vyjadřuj prostorem, světlem, měřítkem a návazností objektů. Všechny popisky jsou česky, bez pseudo-textu, falešných log a vodoznaků.
***
