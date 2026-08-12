## Snímek 6.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Webové knihovny a CDN**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Knihovna** je soubor hotového kódu pro určitou oblast. Programátor ji využívá, aby nemusel znovu implementovat běžný problém — například grafy, mapy, práci s datem, animace nebo 3D scénu.

Knihovnu lze přidat jako lokální závislost přes správce balíčků, nebo ji lze načíst ze vzdáleného serveru.

**CDN — Content Delivery Network** je síť distribučních serverů, které uchovávají kopie obsahu na různých místech. Když uživatel požádá o soubor, CDN jej může obsloužit z vhodného uzlu místo jediného vzdáleného serveru.

```text
uživatel v ČR → blízký CDN uzel → soubor
```

CDN se používá pro obrázky, video, JavaScript, CSS i další statický obsah.

Ve výuce se často ukazuje přímé vložení knihovny:

```html
<script src="https://cdn.example.com/library.js"></script>
```

Je to pohodlné pro jednoduchý příklad, ale produkční projekt musí zvažovat dostupnost cizí služby, soukromí a bezpečnost. Externí JavaScript běží se schopnostmi dané stránky. U moderních projektů se proto knihovny často instalují přes npm a zahrnou do vlastního produkčního buildu.

***

## Snímek 6.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Webové frameworky**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Framework** poskytuje širší strukturu pro tvorbu aplikace. Zatímco knihovna řeší vybranou úlohu, framework často určuje způsob, jakým se jednotlivé části projektu organizují a propojují.

Na frontendu je vhodné rozlišovat různé druhy frameworků.

**Bootstrap** je CSS/UI framework. Poskytuje grid, formuláře, tlačítka, navigaci a další připravené komponenty.

**Tailwind CSS** používá jinou filozofii. Nabízí velké množství malých **utility classes**, kterými se přímo skládá výsledný vzhled:

```html
<button class="px-4 py-2 rounded font-semibold">
  Uložit
</button>
```

Tyto nástroje pomáhají především s prezentací, nikoli s kompletní aplikační logikou.

Na backendu existují frameworky jako Express, Django, Laravel, Spring nebo ASP.NET Core. Pomáhají řešit například routing, middleware, validaci, databázovou vrstvu, šablony a autentizaci.

Hranice mezi knihovnou a frameworkem není vždy ostrá. Užitečný mentální rozdíl je však:

```text
knihovna  → náš program si volá její funkce
framework → náš program se zapojuje do rámce, který řídí větší část aplikace
```

***

## Snímek 6.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Komponentový frontend**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


U rozsáhlého frontendu vzniká problém: stránka obsahuje mnoho propojených interaktivních částí a jejich ruční změny v DOM mohou být obtížně udržovatelné. **Komponentový přístup** rozděluje rozhraní na menší opakovaně použitelné celky.

Komponentou může být například:

```text
NavigationBar
SearchBox
ProductCard
LoginDialog
DataTable
```

Stránku e-shopu si můžeme představit jako strom komponent:

```text
App
├── Header
├── ProductList
│   ├── ProductCard
│   ├── ProductCard
│   └── ProductCard
└── Footer
```

Komponenta typicky přijímá vstupní data, udržuje určitý stav a vytváří část uživatelského rozhraní. Když se stav změní, nástroj zajistí odpovídající aktualizaci stránky.

Mezi známé technologie patří **React**, **Angular**, **Vue** a **Svelte**. Nejsou totožné. React se tradičně označuje jako knihovna pro UI, Angular je rozsáhlý framework a Vue či Svelte volí vlastní kombinaci principů. Pro základní orientaci je ale důležitější společná myšlenka komponent než přesná marketingová kategorie.

Komponentový nástroj nenahrazuje platformu prohlížeče. Výsledné rozhraní stále používá HTML/DOM, CSS, události a síťová API.

***

## Snímek 6.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**TypeScript a transkompilace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**TypeScript** rozšiřuje JavaScript především o statickou kontrolu typů.

```ts
function add(a: number, b: number): number {
  return a + b;
}
```

Editor a překladač mohou díky typovým informacím upozornit na chybu ještě před spuštěním:

```ts
add("5", 3); // typová chyba
```

Prohlížeče však běžně vykonávají JavaScript, nikoli zdrojový TypeScript. TypeScript se proto při přípravě projektu převádí:

```text
TypeScript → JavaScript → prohlížeč nebo Node.js
```

Takovému převodu se často říká **transkompilace**: zdrojový program se překládá do jiného, podobně vysokoúrovňového zdrojového jazyka.

TypeScript je užitečný zejména u větších projektů. Pomáhá dokumentovat strukturu dat, usnadňuje bezpečnější refaktoring a zlepšuje našeptávání editoru.

Je však důležité pochopit hranici jeho možností. Typová informace sama nezaručí, že JSON přijatý ze sítě má skutečně správný obsah. Vnější data je stále nutné za běhu validovat. TypeScript kontroluje především konzistenci kódu, který zná během vývoje.

***

## Snímek 6.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Nástroje a proces vývoje webu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


Moderní webový projekt prochází více kroky než jen „napsat soubor a otevřít jej v prohlížeči“. Zjednodušený proces může vypadat:

```text
návrh
  ↓
psaní kódu
  ↓
lokální spuštění
  ↓
kontrola a ladění
  ↓
testování
  ↓
build
  ↓
verzování a code review
  ↓
nasazení
```

V každé fázi pomáhají jiné nástroje.

**Editor nebo IDE** poskytuje zvýraznění syntaxe, dokončování, refaktoring a práci s Gitem.

**Browser DevTools** dovolují zkoumat aktuální DOM, výsledné CSS, konzoli, síťové požadavky, úložiště a výkon. Jsou jedním z nejdůležitějších diagnostických nástrojů webového vývojáře.

**npm** spravuje balíčky a spouštěcí skripty projektu.

**Vite** a podobné build nástroje poskytují vývojový server, načítání modulů, zpracování TypeScriptu a sestavení produkční verze. Build může provést například minifikaci, rozdělení kódu nebo odstranění nepoužitých částí.

**ESLint** analyzuje JavaScript či TypeScript a upozorňuje na problematické konstrukce. **Prettier** automaticky sjednocuje formátování.

**Git** ukládá historii změn a umožňuje práci ve větvích, porovnávání změn a týmovou spolupráci.

**Testovací nástroje** ověřují jednotlivé funkce, komponenty, API nebo celé uživatelské scénáře.

Smyslem toolchainu není přidat co nejvíce nástrojů. Každý by měl řešit konkrétní opakovaný problém a poskytovat rychlou zpětnou vazbu. U malého statického webu může být proces velmi jednoduchý; rozsáhlá aplikace bude mít automatizované testy, build a nasazení.

***

## Snímek 6.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**WebAssembly**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**WebAssembly — Wasm** je nízkoúrovňový binární formát a běhový model navržený pro rychlé a přenositelné vykonávání kódu. Umožňuje přinést do webového prostředí programy nebo knihovny napsané například v C, C++ nebo Rustu.

Typická cesta je:

```text
C / C++ / Rust
      ↓ překlad
WebAssembly modul
      ↓
prohlížeč
```

WebAssembly nenahrazuje HTML, CSS ani JavaScript. Je vhodné zejména pro části aplikace, kde je potřeba vysoký výpočetní výkon nebo kde už existuje rozsáhlá knihovna v jiném jazyce.

Příklady:

- zpracování obrazu a zvuku,
- kodeky,
- CAD a technické aplikace,
- emulátory,
- hry,
- vědecké výpočty.

JavaScript často zůstává „spojovacím“ jazykem. Ovládá DOM, reaguje na události a předává data WebAssembly modulu, který provede náročný výpočet.

WebAssembly tak rozšiřuje možnosti prohlížeče, ale nemění základní bezpečnostní model webu. Kód běží v sandboxu a k citlivým funkcím zařízení přistupuje pouze přes rozhraní, která mu webová platforma dovolí.

# Závěrečné propojení

Webová aplikace se skládá z několika vrstev, které spolu musí spolupracovat.

**prohlížeč → HTML/CSS/JavaScript → HTTP/API → server → aplikační logika → databáze**

JavaScript může na klientu reagovat na události a měnit DOM. Pomocí Fetch API komunikuje se serverem. Serverová aplikace může běžet například v Node.js, zpracovat požadavek, pracovat se souborem nebo databází a vrátit JSON či výsledné HTML.

Nad základními technologiemi stojí knihovny, frameworky, TypeScript a vývojové nástroje, které zjednodušují práci na rozsáhlejších projektech. WebSocket umožňuje dlouhodobou obousměrnou komunikaci a WebAssembly rozšiřuje možnosti webu o výkonné specializované výpočty.

Nejdůležitější však není zapamatovat si seznam konkrétních technologií. Podstatné je rozumět otázkám:

**Kde daný kód běží? Co je klient a co server? Jak se data přenášejí? Kdo je zpracovává? Jak se výsledek projeví v uživatelském rozhraní?**

Pokud tyto principy známe, dokážeme se mnohem snadněji zorientovat i v nových knihovnách a frameworcích, které se na webu průběžně mění.

***
