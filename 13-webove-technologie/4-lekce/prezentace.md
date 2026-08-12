## Snímek 4.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Node.js a jeho princip**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**Node.js** je běhové prostředí pro JavaScript mimo webový prohlížeč. Používá JavaScriptový engine V8, ale doplňuje jej o rozhraní potřebná pro serverové a systémové programování: souborový systém, síťová spojení, procesy nebo práci s operačním systémem.

Je proto důležité rozlišovat **jazyk** a **prostředí**. JavaScript je jazyk. Prohlížeč a Node.js jsou dvě různá prostředí, která tento jazyk vykonávají a poskytují mu různá API. V prohlížeči máme DOM; v Node.js máme například modul `fs` pro soubory.

Node.js je známý událostně řízenou architekturou a efektivní prací s I/O. Webový server tráví velkou část času čekáním: na databázi, soubor, síťovou službu nebo klienta. Node.js se snaží během takového čekání neblokovat zpracování jiných událostí.

To neznamená, že „Node.js umí dělat všechno současně v jednom vlákně“. JavaScriptová část programu typicky používá event loop, zatímco runtime a operační systém mohou některé operace obsluhovat jinými mechanismy. Pro základní pochopení stačí vědět, že čekání na I/O nemusí zastavit celý server.

***

## Snímek 4.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**npm, `package.json` a moduly**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 4.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Express a základ serverové aplikace**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 4.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Synchronní a asynchronní přístup**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 4.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Práce se soubory**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 4.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Propojení s databází**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 4.7

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Šablonovací systémy**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***
