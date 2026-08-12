# Webové technologie

> Webová stránka dnes není jen dokument uložený na serveru. Může fungovat jako plnohodnotná aplikace: reaguje na uživatele, načítá data bez obnovování celé stránky, komunikuje s databází a někdy udržuje se serverem trvalé spojení. Abychom se v této oblasti neztratili, je důležité rozumět především rolím jednotlivých vrstev a tomu, jak mezi nimi proudí data.

## 1. Klient, server, frontend a backend

### 1.1 Klient a server

Web je založen na komunikaci mezi programy. **Klient** požaduje určitou službu a **server** na tento požadavek odpovídá. Nejčastějším webovým klientem je prohlížeč, ale stejnou službu může používat také mobilní aplikace, desktopový program nebo jiný server.

Typický průběh můžeme zjednodušit takto:

**uživatel → prohlížeč → HTTP požadavek → server → HTTP odpověď → prohlížeč**

Uživatel například zadá adresu webu. Prohlížeč odešle požadavek na server a ten vrátí HTML dokument. Dokument může odkazovat na další zdroje — CSS, JavaScript, obrázky, fonty nebo data — a prohlížeč si je následně vyžádá dalšími požadavky.

Server nemusí znamenat jeden fyzický počítač. Jednu webovou službu může ve skutečnosti zajišťovat několik serverů, databáze, cache, cloudové služby nebo reverzní proxy. Z pohledu klienta je však podstatné, že odešle požadavek na určitou adresu a obdrží odpověď.

### 1.2 Frontend a backend

Pojmy **frontend** a **backend** popisují dvě různé části webové aplikace.

**Frontend** je část, se kterou uživatel přímo pracuje. Patří sem obsah stránky, vzhled, formuláře, tlačítka, animace a další interakce. Ve webovém prohlížeči jej tvoří především HTML, CSS a JavaScript.

**Backend** je část, která běží na serverové straně. Zpracovává požadavky, provádí aplikační logiku, ověřuje uživatele, pracuje s databází nebo komunikuje s dalšími službami.

Například v e-shopu může frontend zobrazit katalog zboží a tlačítko „Přidat do košíku“. Backend ověří dostupnost zboží, uloží obsah košíku a při objednávce zapíše data do databáze.

Frontend a backend tedy nejsou dvě oddělené aplikace bez vazby. Společně tvoří jeden systém a komunikují přes síťové rozhraní, nejčastěji pomocí HTTP.

### 1.3 Webové servery

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

### 1.4 Frontendové technologie

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

### 1.5 Serverové technologie

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

## 2. JavaScript: jazyk pro web

### 2.1 JavaScript a ECMAScript

**JavaScript** vznikl v roce 1995 jako jazyk pro programování webových stránek. Dnes se používá nejen v prohlížeči, ale také na serveru, v desktopových aplikacích nebo ve vývojových nástrojích.

**ECMAScript** je standard, který popisuje základ jazyka JavaScript. Prohlížeče a další prostředí tento standard implementují a doplňují vlastní rozhraní. Například DOM nebo `fetch()` nejsou součástí samotného ECMAScriptu; poskytuje je prostředí prohlížeče.

JavaScript je dynamicky typovaný jazyk. Typ je spojen s hodnotou a proměnná může během běhu programu odkazovat na hodnoty různých typů.

```js
let value = 10;
value = "deset";
```

Takový zápis je platný, i když bývá vhodné držet význam proměnné konzistentní.

### 2.2 `let`, `const`, `var`, scope a hoisting

Proměnné v moderním JavaScriptu deklarujeme především pomocí `const` a `let`.

```js
const school = "SPŠ";
let score = 10;

score = 11;
```

`let` používáme tehdy, když se má vazba později změnit. `const` znamená, že stejné proměnné nelze přiřadit jinou hodnotu. U objektu však `const` nezmrazí jeho obsah:

```js
const user = { name: "Eva" };
user.name = "Ema";       // povoleno
// user = { name: "Jan" }; // nepovoleno
```

Pro pochopení rozdílu je důležitý pojem **scope — rozsah platnosti**. Říká, ve které části programu je konkrétní proměnná dostupná. JavaScript rozlišuje mimo jiné globální, funkční a blokový scope.

`let` a `const` mají **blokový scope**. Proměnná vytvořená uvnitř složených závorek je dostupná jen v daném bloku a jeho vnořených částech:

```js
if (true) {
  const message = "Ahoj";
  console.log(message);   // funguje
}

// console.log(message);  // ReferenceError
```

Starší `var` má **funkční scope**. Blok `if`, `for` nebo `while` sám o sobě jeho platnost neukončí:

```js
if (true) {
  var oldMessage = "Ahoj";
}

console.log(oldMessage);  // funguje
```

Dalším pojmem je **hoisting**. Při zpracování kódu JavaScript připravuje deklarace ještě před vykonáním jednotlivých příkazů. U `var` proto může být jméno proměnné použitelné ještě před řádkem deklarace, ale hodnota je zatím `undefined`:

```js
console.log(x); // undefined
var x = 5;
```

U `let` a `const` jsou deklarace také známy před samotným vykonáním jejich řádku, ale před deklarací k nim nelze přistoupit. Tato oblast se označuje jako **temporal dead zone**. Pro běžné programování není nutné mechanismus memorovat; praktické pravidlo je jednodušší:

> Proměnnou deklaruj před prvním použitím. Preferuj `const`; použij `let`, pokud potřebuješ vazbu měnit. `var` je důležité umět přečíst ve starším kódu, ale pro nový kód obvykle není první volbou.

### 2.3 Datové typy a jejich zvláštnosti

JavaScript je **dynamicky typovaný**. Typ je vlastností hodnoty a jedna proměnná může v průběhu programu obsahovat hodnoty různých typů. To přináší pružnost, ale také možnost nečekaných převodů.

Mezi primitivní typy patří `string`, `number`, `boolean`, `undefined`, `null`, `bigint` a `symbol`. Většina složitějších struktur je objektem.

**Řetězce — `string`**

Řetězec je textová hodnota:

```js
const name = "Eva";
const city = 'Opava';
```

Řetězce jsou v JavaScriptu **neměnné hodnoty**. Metoda, která například převede text na velká písmena, původní řetězec nezmění, ale vytvoří nový:

```js
const word = "web";
const upper = word.toUpperCase();

console.log(word);  // web
console.log(upper); // WEB
```

Velmi užitečné jsou **template literals** zapisované pomocí zpětných apostrofů. Umožňují snadno vkládat výrazy:

```js
const age = 17;
const text = `Eva má ${age} let.`;
```

**Čísla — `number`**

Typ `number` se používá pro běžná celá i desetinná čísla:

```js
const count = 25;
const temperature = 21.4;
```

JavaScript pro většinu čísel používá reprezentaci s plovoucí řádovou čárkou podle IEEE 754. Proto některé desetinné zlomky nelze uložit naprosto přesně:

```js
console.log(0.1 + 0.2);
// 0.30000000000000004
```

Nejde o „chybu JavaScriptu“, ale o důsledek binární reprezentace desetinných čísel. U peněz se proto často pracuje s nejmenšími celými jednotkami, například s haléři nebo centy.

Speciálními číselnými hodnotami jsou `Infinity`, `-Infinity` a `NaN`. `NaN` znamená, že číselná operace nedala použitelný číselný výsledek:

```js
Number("abc"); // NaN
```

Pro velmi velká celá čísla existuje typ `bigint`, například `12345678901234567890n`. Není však běžnou náhradou typu `number`; používá se tam, kde je skutečně potřeba přesná práce s velkými celými hodnotami.

### 2.4 Operátory a jejich specifika

Základní aritmetické operátory jsou podobné jako v jiných jazycích:

```js
+  -  *  /  %
```

Pro umocnění používá JavaScript operátor `**`:

```js
2 ** 3   // 8
```

Velmi důležité je porovnávání. Operátory `==` a `!=` mohou před porovnáním automaticky převádět typy:

```js
5 == "5"   // true
```

Naproti tomu **striktní rovnost** `===` a `!==` porovnává hodnotu bez takové implicitní konverze:

```js
5 === "5"  // false
5 !== "5"  // true
```

Proto se v moderním kódu většinou preferují `===` a `!==`. Výsledek je předvídatelnější.

Logické operátory jsou:

```js
&&   // a zároveň
||   // nebo
!    // negace
```

JavaScript navíc pracuje s pojmem **truthy** a **falsy**. Podmínka nemusí obsahovat přímo `true` nebo `false`; některé hodnoty se při logickém vyhodnocení chovají jako nepravdivé, například `false`, `0`, prázdný řetězec `""`, `null`, `undefined` a `NaN`.

```js
if ("ahoj") {
  console.log("Řetězec je truthy.");
}
```

Pro krátké rozhodnutí lze použít **ternární operátor**:

```js
const category = age >= 18 ? "dospělý" : "nezletilý";
```

Jeho struktura je:

```text
podmínka ? hodnota_při_true : hodnota_při_false
```

Pro jednoduchou volbu je přehledný. Složitější větvení je vhodnější zapisovat klasickým `if`.

### 2.5 Podmínky a cykly

Základní podmínka má podobu:

```js
if (score >= 50) {
  console.log("Úspěch");
} else {
  console.log("Neúspěch");
}
```

Pro více možností lze použít `else if` nebo `switch`.

```js
switch (role) {
  case "admin":
    console.log("Administrátor");
    break;
  case "editor":
    console.log("Editor");
    break;
  default:
    console.log("Uživatel");
}
```

JavaScript podporuje několik typů cyklů:

```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

```js
while (condition) {
  // opakovaný kód
}
```

Pro procházení hodnot pole je často přirozené:

```js
for (const item of items) {
  console.log(item);
}
```

`for...in` se používá především pro vlastnosti objektu, nikoli jako běžná náhrada `for...of` při procházení pole.

### 2.6 Funkce v JavaScriptu

JavaScript podporuje několik způsobů zápisu funkcí.

Deklarovaná funkce:

```js
function add(a, b) {
  return a + b;
}
```

Anonymní funkce uložená do proměnné:

```js
const add = function (a, b) {
  return a + b;
};
```

Arrow function:

```js
const add = (a, b) => {
  return a + b;
};
```

Krátkou arrow function lze zapsat:

```js
const square = x => x * x;
```

Funkce jsou v JavaScriptu hodnoty. Lze je předávat jako argumenty jiným funkcím, ukládat do proměnných nebo vracet jako výsledky.

To je důležité například při práci s událostmi:

```js
button.addEventListener("click", () => {
  console.log("Kliknutí");
});
```

Arrow functions mají některá specifika, například vlastní chování klíčového slova `this`. Pro základní práci ale stačí chápat, že jde o stručnější syntaxi často používanou u krátkých funkcí a callbacků.

## 2.7 Objekty, třídy a vestavěné objekty

Objekt sdružuje hodnoty do vlastností:

```js
const student = {
  name: "Eva",
  age: 17,
  greet() {
    console.log(`Ahoj, jsem ${this.name}.`);
  }
};
```

K vlastnostem přistupujeme například:

```js
student.name
student["age"]
```

JavaScript je založen na prototypovém objektovém modelu. Moderní syntaxe `class` však umožňuje zapisovat objektově orientovaný kód přehledněji:

```js
class Student {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Ahoj, jsem ${this.name}.`);
  }
}
```

JavaScript obsahuje také mnoho vestavěných objektů. Například `Array` pro pole, `Date` pro datum a čas, `Math` pro matematické funkce, `JSON` pro převod mezi objekty a JSON, `Map` a `Set` pro další datové struktury a `Promise` pro práci s budoucím výsledkem asynchronní operace.

## 3. Propojení JavaScriptu s webovou stránkou

### 3.1 Jak připojit JavaScript k HTML

JavaScript lze vložit přímo do HTML:

```html
<script>
  console.log("Ahoj");
</script>
```

Ve větších projektech je ale lepší použít samostatný soubor:

```html
<script src="app.js"></script>
```

Pokud skript pracuje s prvky stránky, je vhodné zajistit, aby HTML bylo nejprve načteno. Jednou z možností je atribut `defer`:

```html
<script src="app.js" defer></script>
```

Moderní moduly lze načíst:

```html
<script type="module" src="app.js"></script>
```

Moduly podporují `import` a `export` a mají vlastní scope.

```js
// math.js
export function add(a, b) {
  return a + b;
}
```

```js
// app.js
import { add } from "./math.js";
console.log(add(2, 3));
```

### 3.2 DOM — Document Object Model

HTML soubor je text. Prohlížeč jej ale při načítání **parsuje** a vytváří z něj v paměti objektovou stromovou strukturu nazývanou **DOM — Document Object Model**.

Máme-li například:

```html
<body>
  <h1>Webové technologie</h1>
  <p id="info">Úvodní text</p>
</body>
```

můžeme si část DOM představit:

```text
document
└── html
    └── body
        ├── h1
        └── p#info
```

Každá část dokumentu je reprezentována uzlem. HTML elementy jsou jedním druhem uzlů; dalšími mohou být například textové uzly. Objekt `document` představuje vstupní bod k právě načtenému dokumentu.

JavaScript může element vyhledat:

```js
const paragraph = document.querySelector("#info");
```

`querySelector()` přijímá CSS selektor a vrátí první odpovídající element. Pro více prvků existuje `querySelectorAll()`:

```js
const items = document.querySelectorAll("li.active");
```

Důležité je rozlišovat **zdrojový HTML soubor** a **aktuální DOM**. JavaScript může DOM po načtení změnit, aniž by se tím přepsal původní HTML soubor na serveru. Vývojářské nástroje prohlížeče proto mohou ukazovat jinou strukturu, než jaká byla původně zapsána ve zdrojovém kódu.

DOM není pouze „seznam tagů“. Je to programové rozhraní. Elementy mají vlastnosti a metody:

```js
paragraph.textContent = "Nový text";
paragraph.classList.add("important");
```

Lze také vytvářet nové elementy:

```js
const item = document.createElement("li");
item.textContent = "Nová položka";

document.querySelector("ul").append(item);
```

Užitečné je také rozlišovat **atribut v HTML** a **vlastnost objektu DOM**. Často spolu souvisejí, ale nejsou vždy totožné. Například `<input value="A">` obsahuje atribut s výchozí hodnotou, zatímco vlastnost `input.value` se může během práce uživatele měnit.

DOM tak vytváří most mezi statickou strukturou HTML a programovým chováním JavaScriptu.

### 3.3 BOM — Browser Object Model

DOM popisuje dokument, ale webový prohlížeč poskytuje JavaScriptu i další informace a funkce, které se netýkají přímo HTML stránky. Tradičně se pro ně používá označení **BOM — Browser Object Model**.

Na rozdíl od DOM není BOM jedním přesně uzavřeným modelem s jedinou standardní specifikací. Je to spíše historické a didakticky užitečné označení pro objekty prohlížeče mimo samotný dokument.

V běžném skriptu je nejdůležitější globální objekt **`window`**. Reprezentuje okno nebo kontext prohlížeče a zpřístupňuje mnoho dalších API. Například:

```js
window.location
window.history
window.navigator
window.document
```

V prohlížeči lze často `window.` vynechat:

```js
console.log(location.href);
```

**`location`** obsahuje informace o aktuální URL a umožňuje navigaci:

```js
console.log(location.hostname);
```

**`history`** poskytuje práci s historií aktuálního tabu. Moderní aplikace jej mohou využívat například ke změně URL bez úplného načtení nové stránky.

**`navigator`** poskytuje informace a vybrané možnosti prostředí prohlížeče. Přes související Web APIs lze například zjišťovat stav připojení nebo po svolení uživatele využít některé schopnosti zařízení.

Objekt **`screen`** popisuje vlastnosti obrazovky, i když pro responzivní návrh stránky se obvykle neřídíme přímo fyzickým rozlišením monitoru, ale velikostí dostupného viewportu a CSS media queries.

Rozdíl mezi DOM a BOM lze zjednodušit takto:

```text
DOM → dokument a jeho elementy
BOM → prostředí prohlížeče kolem dokumentu
```

V současné dokumentaci se častěji mluví konkrétně o jednotlivých **Web APIs** než o BOM jako jednom celku. Pojem BOM je přesto užitečný pro pochopení, proč například `document` pracuje se stránkou, zatímco `location` nebo `history` pracují s prohlížečem a navigací.

### 3.4 Dynamický web — změna elementů

Za **dynamický** označujeme web, jehož obsah nebo stav se může měnit podle dat, času nebo činnosti uživatele. JavaScript k tomu na klientské straně používá především DOM.

Může změnit text:

```js
const heading = document.querySelector("h1");
heading.textContent = "Nový nadpis";
```

může upravit CSS třídy:

```js
heading.classList.add("highlight");
heading.classList.remove("hidden");
```

může změnit atribut:

```js
const image = document.querySelector("img");
image.alt = "Schéma klient–server";
```

a může vytvořit nebo odstranit celý element:

```js
const item = document.createElement("li");
item.textContent = "Nová položka";

document.querySelector("ul").append(item);
```

Změna DOM se projeví při dalším vykreslení stránky, aniž by prohlížeč musel načíst nový HTML dokument ze serveru.

Při vkládání obsahu je důležité rozlišovat `textContent` a `innerHTML`. `textContent` vloží obyčejný text:

```js
message.textContent = userInput;
```

`innerHTML` naopak řetězec interpretuje jako HTML:

```js
message.innerHTML = "<strong>Důležité</strong>";
```

Pokud do `innerHTML` vložíme neověřený text od uživatele nebo z nedůvěryhodného zdroje, může se stát součástí stránky i škodlivý kód. Proto se pro běžný text preferuje `textContent` nebo bezpečné vytváření elementů přes DOM API.

### 3.5 Interaktivní web — události

Dynamická změna stránky sama o sobě nestačí. Aby web reagoval na člověka, potřebuje **události — events**. Událost oznamuje, že se něco stalo: uživatel klikl, stiskl klávesu, změnil hodnotu formuláře, odeslal formulář nebo se dokončilo načtení určitého zdroje.

Na událost lze připojit **event listener**, tedy funkci, která se má při dané události vykonat:

```js
const button = document.querySelector("#send");

button.addEventListener("click", () => {
  console.log("Uživatel klikl.");
});
```

Listener může získat **objekt události** s podrobnostmi:

```js
button.addEventListener("click", event => {
  console.log(event.target);
});
```

`event.target` ukazuje prvek, na němž událost vznikla.

U formuláře může JavaScript zachytit odeslání:

```js
form.addEventListener("submit", event => {
  event.preventDefault();
  console.log("Odeslání převzal JavaScript.");
});
```

`preventDefault()` zabrání výchozí akci prohlížeče. U formuláře to typicky znamená, že se neprovede klasická navigace podle atributů `action` a `method`. Skript pak může například data zkontrolovat a odeslat přes Fetch API.

Události se mohou ve stromu DOM **šířit**. Často vzniknou na konkrétním elementu a následně „probublávají“ k jeho předkům. Díky tomu lze například jeden listener na seznamu použít pro mnoho položek uvnitř. Tomuto přístupu se říká **event delegation**.

Interaktivní frontend lze proto chápat jako opakující se cyklus:

```text
událost → obslužná funkce → změna stavu nebo dat → změna DOM → nový obraz stránky
```

## 4. Node.js a JavaScript na serveru

### 4.1 Node.js a jeho princip

**Node.js** je běhové prostředí pro JavaScript mimo webový prohlížeč. Používá JavaScriptový engine V8, ale doplňuje jej o rozhraní potřebná pro serverové a systémové programování: souborový systém, síťová spojení, procesy nebo práci s operačním systémem.

Je proto důležité rozlišovat **jazyk** a **prostředí**. JavaScript je jazyk. Prohlížeč a Node.js jsou dvě různá prostředí, která tento jazyk vykonávají a poskytují mu různá API. V prohlížeči máme DOM; v Node.js máme například modul `fs` pro soubory.

Node.js je známý událostně řízenou architekturou a efektivní prací s I/O. Webový server tráví velkou část času čekáním: na databázi, soubor, síťovou službu nebo klienta. Node.js se snaží během takového čekání neblokovat zpracování jiných událostí.

To neznamená, že „Node.js umí dělat všechno současně v jednom vlákně“. JavaScriptová část programu typicky používá event loop, zatímco runtime a operační systém mohou některé operace obsluhovat jinými mechanismy. Pro základní pochopení stačí vědět, že čekání na I/O nemusí zastavit celý server.

### 4.2 Správa modulů

Větší program se nerozumně neukládá do jednoho souboru. JavaScript proto podporuje **moduly**, které rozdělují program na části s jasně určenými vstupy a výstupy.

Vlastní modul:

```js
// math.js
export function add(a, b) {
  return a + b;
}
```

Použití v jiném souboru:

```js
import { add } from "./math.js";
```

Tento soubor je **interní modul** projektu. Node.js obsahuje také **vestavěné moduly**, například `fs`, `path` nebo `http`.

Vedle nich používá většina projektů **externí balíčky**. Ty vytvářejí jiní vývojáři a instalují se ze správce balíčků. Nejpoužívanějším nástrojem v ekosystému Node.js je **npm**.

```bash
npm install express
```

Soubor **`package.json`** popisuje projekt. Uchovává například jeho název, spouštěcí skripty a seznam závislostí:

```json
{
  "name": "demo-server",
  "type": "module",
  "scripts": {
    "start": "node app.js"
  },
  "dependencies": {
    "express": "..."
  }
}
```

Po instalaci vznikají soubory a adresáře, které dovolují přesněji reprodukovat použité závislosti. Externí balíček je přitom skutečný cizí kód, který se stává součástí projektu. Proto je třeba závislosti udržovat, aktualizovat a nepřidávat je bez důvodu.

### 4.3 Express jako základ serverové aplikace

Node.js umí HTTP server vytvořit i bez frameworku, ale při tvorbě aplikací se často používá vyšší vrstva. **Express** je známý minimalistický webový framework pro Node.js.

Základní server může vypadat:

```js
import express from "express";

const app = express();

app.get("/", (req, res) => {
  res.send("Ahoj ze serveru");
});

app.listen(3000);
```

Řádek:

```js
app.get("/", ...)
```

definuje **route — obslužnou cestu**. Říká: „Když přijde požadavek metodou GET na cestu `/`, spusť tuto funkci.“

Funkce dostane dva důležité objekty:

- `req` reprezentuje příchozí **request** — požadavek,
- `res` reprezentuje **response** — odpověď, kterou server vytváří.

Jiná route může vrátit JSON:

```js
app.get("/api/user", (req, res) => {
  res.json({
    name: "Eva",
    age: 17
  });
});
```

**Routing** je tedy mechanismus, který podle HTTP metody a cesty rozhoduje, která část programu požadavek obslouží. Skutečná aplikace navíc řeší validaci dat, autentizaci, chyby, logování a práci s databází. Framework množství opakovaného kódu snižuje, ale nenahrazuje porozumění HTTP.

### 4.4 Synchronní a asynchronní zpracování

Při **synchronním** zpracování program dokončí jednu operaci a teprve potom pokračuje další:

```text
operace A → konec A → operace B → konec B
```

To je přirozené u rychlých výpočtů. Problém může vzniknout u operace, která hlavně čeká — například na síť, databázi nebo pomalý soubor. Kdyby server během čekání blokoval celý hlavní tok programu, mohl by zbytečně zdržovat další klienty.

**Asynchronní** přístup umožňuje operaci zahájit a na její výsledek čekat neblokujícím způsobem. JavaScript k tomu používá mimo jiné `Promise`.

```js
const promise = fetch("https://example.com/data");
```

Promise si můžeme představit jako objekt reprezentující výsledek, který ještě nemusí být k dispozici. Syntaxe `async` a `await` umožňuje s Promisy pracovat čitelněji:

```js
async function loadData() {
  const response = await fetch("https://example.com/data");
  const data = await response.json();
  return data;
}
```

`await` pozastaví pokračování **dané asynchronní funkce**, ale nemusí blokovat celý runtime. Node.js může mezitím obsloužit jiné události.

Důležitý je pojem **event loop**. Zjednodušeně sleduje, zda je možné spustit další připravenou úlohu. Když asynchronní I/O dokončí svou práci, pokračování se zařadí k pozdějšímu vykonání.

```text
spuštění operace → čekání mimo hlavní tok → dokončení
                                      ↓
                               pokračování funkce
```

Asynchronní přístup je vhodný hlavně pro I/O. Dlouhý čistý výpočet na hlavním vlákně může event loop naopak blokovat.

### 4.5 Práce se soubory

Na serveru je běžné pracovat se souborovým systémem. Node.js k tomu poskytuje vestavěný modul `fs`.

Asynchronní načtení textového souboru:

```js
import { readFile } from "node:fs/promises";

const text = await readFile("data.txt", "utf8");
console.log(text);
```

Server může soubory načítat, zapisovat nebo vytvářet. V praxi se to používá například pro:

- konfigurační soubory,
- importy a exporty,
- zpracování uploadovaných souborů,
- generování dokumentů,
- ukládání logů.

Je však důležité rozlišovat **souborové úložiště** a **databázi**. Uložit několik nastavení do JSON souboru může být přiměřené. Spravovat tímto způsobem tisíce současně měněných uživatelských účtů už obvykle vhodné není. Databáze nabízí nástroje pro vyhledávání, souběžný přístup, transakce a další vlastnosti, které prostý soubor sám neposkytuje.

### 4.6 Propojení s databází

Backend často potřebuje trvale ukládat strukturovaná data. K tomu slouží databáze.

Typický tok je:

```text
prohlížeč
   ↓ HTTP
Node.js aplikace
   ↓ databázový dotaz
databáze
   ↓ výsledek
Node.js aplikace
   ↓ HTTP odpověď
prohlížeč
```

Serverová aplikace může používat například PostgreSQL, MySQL, SQLite nebo databázi jiného typu. Komunikuje s ní pomocí databázového ovladače, knihovny nebo ORM.

Při práci s relační databází není bezpečné vytvářet SQL dotaz prostým slepením textu od uživatele. Vstupy se předávají pomocí **parametrizovaných dotazů** nebo přes knihovny, které správné oddělení dat od SQL zajistí.

Důležitá architektonická zásada je, že webový frontend se obvykle nepřipojuje přímo k databázi. Klient posílá požadavek backendu a backend rozhoduje, která data může uživatel číst nebo měnit. Tím se odděluje veřejné rozhraní aplikace od interního datového úložiště.

### 4.7 Šablonovací systémy

Dynamický web nemusí vždy posílat do prohlížeče pouze JSON a celé rozhraní sestavovat JavaScriptem. Server může vytvořit HTML ještě před odesláním. K tomu se používají **šablonovací systémy — template engines**.

Šablona obsahuje pevnou strukturu a místa pro proměnná data:

```html
<h1>{{ title }}</h1>
<p>{{ text }}</p>
```

Server jí předá například:

```text
title = "Novinky"
text = "Dnes vyšel nový článek."
```

a výsledkem je hotové HTML.

V prostředí Node.js existují například EJS, Pug nebo Handlebars. Přesná syntaxe se liší, princip zůstává:

```text
data + šablona → výsledný HTML dokument
```

Šablonování se hodí pro obsahové weby, administrační rozhraní nebo aplikace, kde je jednodušší sestavit stránku na serveru. Nevylučuje JavaScript na klientu — výsledné HTML lze dále doplnit o interaktivní chování.

## 5. Webové API a AJAX

### 5.1 Webové API

**API — Application Programming Interface** je rozhraní, přes které jeden program využívá funkce nebo data jiného programu. **Webové API** zpřístupňuje takové rozhraní přes síť, nejčastěji pomocí HTTP.

Je užitečné si představit API jako smlouvu. Klient musí vědět:

- na jakou adresu má požadavek poslat,
- jakou HTTP metodu použít,
- jaká data má přiložit,
- jakou odpověď může očekávat,
- jak jsou hlášeny chyby,
- zda je nutná autentizace.

Webové API je užitečné proto, že odděluje **způsob zobrazení** od **způsobu zpracování dat**. Stejný backend pak může používat webový frontend, mobilní aplikace nebo jiný server.

API může být **interní**, určené pro části jednoho systému, nebo **veřejné**, určené pro cizí vývojáře. Může používat různé styly a protokoly. Běžně se setkáme s REST API, GraphQL, RPC rozhraními nebo s dlouhodobou komunikací pomocí WebSocketu.

Samotná existence API neříká, kdo má právo jej používat. Přístup může být veřejný, omezený přihlášením, tokenem, API klíčem nebo jiným způsobem autentizace.

### 5.2 AJAX a Fetch API

Původní web fungoval převážně tak, že každá důležitá akce načetla nový HTML dokument. **AJAX — Asynchronous JavaScript and XML** přinesl možnost, aby JavaScript poslal požadavek na pozadí, získal data a změnil jen potřebnou část stránky.

Historický název obsahuje XML, ale dnešní aplikace velmi často používají JSON. Starší API `XMLHttpRequest` je stále dostupné, pro nový kód se však běžně používá **Fetch API**.

Jednoduché načtení:

```js
const response = await fetch("/api/articles");

if (!response.ok) {
  throw new Error(`HTTP ${response.status}`);
}

const articles = await response.json();
```

Objekt `response` nejprve reprezentuje HTTP odpověď. Teprve volání `response.json()` přečte její tělo a převede JSON na JavaScriptové hodnoty.

Odeslání JSON dat může vypadat:

```js
const response = await fetch("/api/articles", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    title: "Nový článek"
  })
});
```

Fetch se používá například pro živé vyhledávání, průběžné filtrování, ukládání formuláře bez reloadu, načítání další stránky výsledků nebo aktualizaci dashboardu.

Důležitá zvláštnost: `fetch()` obvykle neodmítne Promise jen proto, že server odpověděl stavem 404 nebo 500. Síťové spojení proběhlo a server odpověděl; klient proto musí stav zkontrolovat přes `response.ok` nebo `response.status`.

Při komunikaci s jiným originem může prohlížeč uplatnit **CORS**. Jde o pravidla určující, zda smí skript z jedné webové origin číst odpověď jiné služby. CORS není náhradou autentizace backendu.

### 5.3 REST API

**REST — Representational State Transfer** je architektonický styl pro síťové aplikace. V praxi se tím často myslí HTTP API, které pracuje se **zdroji — resources**. Zdrojem může být článek, uživatel, produkt nebo objednávka.

Zdroj je dostupný přes endpoint. Například:

```text
/api/articles
/api/articles/42
```

První cesta označuje kolekci článků, druhá konkrétní článek. Identifikátor `42` je součástí cesty a často se označuje jako **path parameter**.

Akci nad zdrojem vyjadřuje HTTP metoda:

```text
GET     /api/articles       načtení seznamu
GET     /api/articles/42    načtení jednoho článku
POST    /api/articles       vytvoření nového článku
PATCH   /api/articles/42    částečná změna článku
DELETE  /api/articles/42    odstranění článku
```

Pro filtrování nebo doplňující volby se často používají **query parameters**:

```text
GET /api/articles?published=true&page=2
```

REST API běžně přenáší reprezentaci zdroje jako JSON:

```json
{
  "id": 42,
  "title": "Webové technologie",
  "published": true
}
```

HTTP stavový kód oznamuje základní výsledek požadavku:

```text
200 OK             úspěch
201 Created        zdroj byl vytvořen
400 Bad Request    neplatný požadavek
401 Unauthorized   chybí platné přihlášení / autentizace
403 Forbidden      identita je známa, ale nemá oprávnění
404 Not Found      zdroj nebyl nalezen
500 Internal Server Error  chyba na straně serveru
```

Dobře navržené API používá metody, cesty a stavy konzistentně. Klient pak nemusí znát vnitřní strukturu backendu; spoléhá na veřejný kontrakt API.

**API klíče a přístupové tokeny**

Některé služby vyžadují **API klíč**. Ten identifikuje aplikaci nebo odběratele služby a může sloužit například k měření spotřeby nebo omezení přístupu.

Jiné systémy používají **access token**, který může reprezentovat konkrétního přihlášeného uživatele a jeho oprávnění. Pojmy nejsou totožné, i když se oba v požadavku často posílají v HTTP hlavičce.

Například:

```text
Authorization: Bearer <token>
```

Citlivý tajný klíč nelze bezpečně schovat do veřejného JavaScriptu v prohlížeči. Uživatel má kód frontendu pod kontrolou. Tajemství proto obvykle uchovává backend a klient komunikuje přes něj.

REST není jediný správný návrh API. Jeho hlavní síla spočívá v jednoduchém modelu zdrojů a v dobrém využití vlastností HTTP.

### 5.4 REST API v praxi

REST API umožňuje oddělit zdroj dat od aplikace, která je zobrazuje.

**Počasí**

Frontend může požádat meteorologickou službu:

```text
GET /api/weather?city=Opava
```

a získat:

```json
{
  "temperature": 22.4,
  "condition": "cloudy"
}
```

**E-shop**

```text
GET  /api/products
GET  /api/products/125
POST /api/orders
```

Webový frontend i mobilní aplikace mohou používat stejné produktové a objednávkové API.

**Školní systém**

```text
GET  /api/classes/3A/students
GET  /api/students/125
POST /api/grades
```

Backend přitom musí kontrolovat oprávnění. To, že frontend zná endpoint pro známky, neznamená, že každý uživatel smí známku vytvořit.

**Služby třetích stran**

REST API se používá také pro mapy, překlady, platební služby, cloudová úložiště nebo informační systémy. Při použití cizího API je třeba číst dokumentaci: popisuje endpointy, parametry, metody, formát dat, autentizaci, limity počtu požadavků a chybové odpovědi.

Důležitou dovedností proto není naučit se konkrétní URL zpaměti, ale umět z dokumentace pochopit kontrakt služby a sestavit správný požadavek.

### 5.5 GraphQL

**GraphQL** je jiný způsob zpřístupnění dat přes API. Zatímco REST často nabízí více endpointů pro různé zdroje, GraphQL obvykle poskytuje jednotné rozhraní se **schématem**, které popisuje dostupné typy a vztahy.

Klient v dotazu přesně uvede, která pole potřebuje:

```graphql
{
  article(id: 42) {
    title
    author {
      name
    }
  }
}
```

Server může vrátit například jen požadovaná data:

```json
{
  "data": {
    "article": {
      "title": "Webové technologie",
      "author": {
        "name": "Eva Nováková"
      }
    }
  }
}
```

Výhodou je flexibilita klienta. Mobilní aplikace může chtít menší množství polí než desktopové rozhraní a nemusí kvůli tomu vznikat nový REST endpoint.

Tato pružnost má cenu. Server musí řídit schéma, validovat dotazy, řešit autorizaci a hlídat, aby klient nevytvořil nepřiměřeně náročný dotaz. GraphQL proto není „lepší REST“, ale jiný návrhový přístup vhodný zejména pro systémy s bohatě propojenými daty a různými klienty.

### 5.6 WebSocket a Socket.IO

Běžná komunikace přes HTTP je založena na modelu **požadavek → odpověď**. Klient se zeptá a server odpoví. U chatu, multiplayerové hry nebo společné editace ale server často potřebuje poslat zprávu okamžitě, aniž by klient pokaždé předem vytvořil nový požadavek.

**WebSocket** umožňuje po úvodním navázání vytvořit dlouhodobý obousměrný komunikační kanál:

```text
klient ⇄ server
```

Klient může spojení vytvořit:

```js
const socket = new WebSocket("wss://example.com/socket");
```

Poté může reagovat na příchozí zprávy:

```js
socket.addEventListener("message", event => {
  console.log(event.data);
});
```

A může také zprávy posílat:

```js
socket.send("Ahoj");
```

WebSocket je vhodný například pro:

- chat,
- online hry,
- živé sledování stavu,
- společnou editaci,
- okamžité notifikace.

Nad touto oblastí existují knihovny s vyšší úrovní abstrakce. Známým příkladem je **Socket.IO**. Nabízí pohodlný událostní model, opětovné připojení, místnosti a další funkce užitečné pro aplikace v reálném čase.

Socket.IO není totéž jako samotný standard WebSocket. Je to knihovna a vlastní komunikační vrstva, která může WebSocket využívat. Toto rozlišení je důležité při propojování klientů a serverů různých technologií.

## 6. Knihovny a frameworky

### 6.1 Webové knihovny a CDN

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

### 6.2 Webové frameworky

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

### 6.3 Komponentový frontend

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

### 6.4 TypeScript a transkompilace

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

### 6.5 Nástroje a proces vývoje webu

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

### 6.6 WebAssembly

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
