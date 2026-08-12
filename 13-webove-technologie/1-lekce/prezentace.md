## Snímek 1.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Klient a server**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Web je založen na komunikaci mezi programy. **Klient** požaduje určitou službu a **server** na tento požadavek odpovídá. Nejčastějším webovým klientem je prohlížeč, ale stejnou službu může používat také mobilní aplikace, desktopový program nebo jiný server.

Typický průběh můžeme zjednodušit takto:

**uživatel → prohlížeč → HTTP požadavek → server → HTTP odpověď → prohlížeč**

Uživatel například zadá adresu webu. Prohlížeč odešle požadavek na server a ten vrátí HTML dokument. Dokument může odkazovat na další zdroje — CSS, JavaScript, obrázky, fonty nebo data — a prohlížeč si je následně vyžádá dalšími požadavky.

Server nemusí znamenat jeden fyzický počítač. Jednu webovou službu může ve skutečnosti zajišťovat několik serverů, databáze, cache, cloudové služby nebo reverzní proxy. Z pohledu klienta je však podstatné, že odešle požadavek na určitou adresu a obdrží odpověď.

***

## Snímek 1.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Frontend a backend**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Pojmy **frontend** a **backend** popisují dvě různé části webové aplikace.

**Frontend** je část, se kterou uživatel přímo pracuje. Patří sem obsah stránky, vzhled, formuláře, tlačítka, animace a další interakce. Ve webovém prohlížeči jej tvoří především HTML, CSS a JavaScript.

**Backend** je část, která běží na serverové straně. Zpracovává požadavky, provádí aplikační logiku, ověřuje uživatele, pracuje s databází nebo komunikuje s dalšími službami.

Například v e-shopu může frontend zobrazit katalog zboží a tlačítko „Přidat do košíku“. Backend ověří dostupnost zboží, uloží obsah košíku a při objednávce zapíše data do databáze.

Frontend a backend tedy nejsou dvě oddělené aplikace bez vazby. Společně tvoří jeden systém a komunikují přes síťové rozhraní, nejčastěji pomocí HTTP.

***

## Snímek 1.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Webové servery**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Webový server** je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi. Pojem je dobré odlišit od fyzického serveru: jeden počítač může provozovat několik serverových programů a naopak jedna webová služba může být rozložena mezi mnoho počítačů.

Nejjednodušší úlohou webového serveru je poskytování **statických souborů**. Prohlížeč požádá například o `/styles.css` a server vrátí odpovídající soubor spolu s informací o jeho typu. U dynamického webu však server často rozhoduje, zda požadavek obslouží sám, nebo jej předá aplikačnímu programu.

Zjednodušeně:

```text
prohlížeč
    ↓ HTTP/HTTPS
webový server
    ├── statické soubory: HTML, CSS, obrázky
    └── dynamické požadavky → aplikační server → databáze
```

Známými webovými servery jsou **Apache HTTP Server**, **Nginx** a **Microsoft IIS**. Jejich význam nespočívá v samotném názvu, ale v úlohách, které mohou plnit. Webový server může obsluhovat statický obsah, ukončovat šifrované spojení TLS, směrovat provoz podle adresy, zapisovat požadavky do logů nebo rozdělovat zatížení mezi více aplikačních procesů.

Častá je role **reverse proxy**. Uživatel komunikuje například s Nginxem, ale ten část požadavků předává aplikaci běžící v Node.js, Pythonu či jiném prostředí. Prohlížeč přitom nemusí vědět, kolik programů se na vyřízení požadavku podílelo.

Webový server může také provozovat více webů na jedné IP adrese. Podle požadované domény pozná, kterou konfiguraci a obsah má použít. Tento princip se označuje jako **virtual hosting**.

Je proto přesnější chápat webový server jako vstupní síťovou vrstvu webové služby než jen jako „program, který posílá stránky“.

***

## Snímek 1.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Frontendové technologie**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Frontend** je část aplikace, která vytváří uživatelské rozhraní a reaguje na uživatele. Ve webovém prohlížeči stojí na trojici HTML, CSS a JavaScript.

**HTML** určuje strukturu a význam dokumentu. Popisuje například nadpis, odstavec, formulář, tabulku nebo navigaci.

**CSS** popisuje prezentaci: barvy, písmo, rozměry, rozložení prvků, responzivní chování nebo animace.

**JavaScript** přidává programovou logiku. Reaguje na události, mění obsah stránky, provádí výpočty a komunikuje se serverem.

Praktický mentální model je:

```text
HTML        → co stránka obsahuje
CSS         → jak je obsah zobrazen
JavaScript  → jak se stránka chová
```

JavaScript ale nepracuje s webem sám. Prohlížeč mu poskytuje **Web APIs** — programová rozhraní pro práci s dokumentem, sítí, úložištěm, historií prohlížení, grafikou, zvukem a dalšími možnostmi. Patří sem například DOM API, Fetch API, Canvas nebo WebSocket API.

Nad těmito základy se používají knihovny a frameworky. React, Vue, Angular nebo Svelte pomáhají organizovat rozsáhlejší interaktivní rozhraní; Bootstrap nebo Tailwind CSS usnadňují tvorbu vzhledu; TypeScript přidává kontrolu typů. Tyto nástroje však základní webové technologie neruší. Výsledkem je stále dokument a rozhraní, které musí prohlížeč převést na DOM, aplikovat CSS a obsluhovat pomocí webových API.

***

## Snímek 1.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Serverové technologie**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Serverová část webu může být vytvořena v mnoha jazycích a prostředích. JavaScript používá **Node.js**, Python například **Django** nebo **FastAPI**, PHP **Laravel** či **Symfony**, Java **Spring** a C# **ASP.NET Core**. Tyto názvy je vhodné chápat jako příklady různých ekosystémů, nikoli jako seznam technologií, které je nutné znát nazpaměť.

Společný princip je podobný. Serverová aplikace přijme požadavek, určí, jaká část programu jej má zpracovat, ověří vstupní data a případná oprávnění, provede aplikační logiku a vytvoří odpověď.

```text
požadavek
   ↓
routing
   ↓
ověření a aplikační logika
   ↓
soubor / databáze / další služba
   ↓
odpověď
```

Server může vrátit hotové HTML, které prohlížeč rovnou zobrazí, nebo jen data — často ve formátu JSON — která zpracuje frontend. Může také přijímat soubory, posílat e-maily, generovat dokumenty nebo komunikovat s externím API.

Důležitá je hranice důvěry. Kód běžící v prohlížeči má uživatel pod kontrolou, proto backend nesmí spoléhat na to, že klientská aplikace posílá vždy správná a oprávněná data. Server musí důležitá pravidla ověřovat sám.

***
