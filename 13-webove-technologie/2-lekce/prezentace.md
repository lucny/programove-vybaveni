## Snímek 2.1

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**JavaScript a ECMAScript**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


**JavaScript** vznikl v roce 1995 jako jazyk pro programování webových stránek. Dnes se používá nejen v prohlížeči, ale také na serveru, v desktopových aplikacích nebo ve vývojových nástrojích.

**ECMAScript** je standard, který popisuje základ jazyka JavaScript. Prohlížeče a další prostředí tento standard implementují a doplňují vlastní rozhraní. Například DOM nebo `fetch()` nejsou součástí samotného ECMAScriptu; poskytuje je prostředí prohlížeče.

JavaScript je dynamicky typovaný jazyk. Typ je spojen s hodnotou a proměnná může během běhu programu odkazovat na hodnoty různých typů.

```js
let value = 10;
value = "deset";
```

Takový zápis je platný, i když bývá vhodné držet význam proměnné konzistentní.

***

## Snímek 2.2

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**`let`, `const`, `var`, scope a hoisting**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 2.3

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Datové typy a jejich zvláštnosti**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


JavaScript je **dynamicky typovaný**. Typ je vlastností hodnoty a jedna proměnná může v průběhu programu obsahovat hodnoty různých typů. To přináší pružnost, ale také možnost nečekaných převodů.

Mezi primitivní typy patří `string`, `number`, `boolean`, `undefined`, `null`, `bigint` a `symbol`. Většina složitějších struktur je objektem.

### Řetězce — `string`

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

### Čísla — `number`

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

***

## Snímek 2.4

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Operátory a jejich specifika**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 2.5

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Podmínky a cykly**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 2.6

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Funkce v JavaScriptu**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

***

## Snímek 2.7

***
Zpracuj v podobě encyklopedické grafiky tuto kapitolu:
**Objekty, třídy a vestavěné objekty**
-----
Vycházej z tohoto textu, ale k vyjádření obsahu používej hlavně grafické prvky:
-----


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

# 3. Propojení JavaScriptu s webovou stránkou

***
