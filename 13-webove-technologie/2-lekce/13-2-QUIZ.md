<!--
title: JavaScript a jazyk ECMAScript – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? JavaScript vznikl v roce 1995 jako jazyk pro programování webových stránek.**

<!-- data-randomize="true" -->
[(X)] JavaScript a ECMAScript
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Proměnné v moderním JavaScriptu deklarujeme především pomocí const a let.**

<!-- data-randomize="true" -->
[(X)] `let`, `const`, `var`, scope a hoisting
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? JavaScript je dynamicky typovaný.**

<!-- data-randomize="true" -->
[(X)] Datové typy a jejich zvláštnosti
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Objekt sdružuje hodnoty do vlastností: js const student = { name: "Eva", age: 17, greet() { console.log(Ahoj, jsem ${this.name}.); } }; K vlastnostem přistupujeme například: js stu…**

<!-- data-randomize="true" -->
[(X)] Objekty, třídy a vestavěné objekty
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**5. Které tvrzení odpovídá tématu JavaScript a ECMAScript?**

<!-- data-randomize="true" -->
[(X)] JavaScript vznikl v roce 1995 jako jazyk pro programování webových stránek.
[( )] Web je založen na komunikaci mezi programy.
[( )] Pojmy frontend a backend popisují dvě různé části webové aplikace.
[( )] Webový server je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi.

---

**6. Které tvrzení odpovídá tématu Objekty, třídy a vestavěné objekty?**

<!-- data-randomize="true" -->
[(X)] Objekt sdružuje hodnoty do vlastností: js const student = { name: "Eva", age: 17, greet() { console.log(Ahoj, jsem ${this.name}.); } }; K vlastnostem přistupujeme například: js stu…
[( )] Web je založen na komunikaci mezi programy.
[( )] Pojmy frontend a backend popisují dvě různé části webové aplikace.
[( )] Webový server je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] JavaScript a ECMAScript
[[X]] `let`, `const`, `var`, scope a hoisting
[[X]] Datové typy a jejich zvláštnosti
[[ ]] Klient a server
[[ ]] Frontend a backend

---

**8. Které téma tvoří jednu z hlavních částí kapitoly JavaScript a jazyk ECMAScript?**

<!-- data-randomize="true" -->
[(X)] Operátory a jejich specifika
[( )] TypeScript a transkompilace
[( )] Nástroje a proces vývoje webu
[( )] WebAssembly

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] JavaScript vznikl v roce 1995 jako jazyk pro programování webových stránek.
[[X]] Proměnné v moderním JavaScriptu deklarujeme především pomocí const a let.
[[ ]] Web je založen na komunikaci mezi programy.
[[ ]] Pojmy frontend a backend popisují dvě různé části webové aplikace.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Objekty, třídy a vestavěné objekty
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

# 2. Interaktivní shrnutí kapitoly

## JavaScript a ECMAScript

JavaScript je programovací jazyk používaný v prohlížeči i mimo něj. ECMAScript je standard, který popisuje jeho syntaxi a chování; JavaScript je konkrétní implementovaný jazyk tohoto standardu.

Proměnnou s měnitelnou vazbou obvykle deklarujeme pomocí [[let]], neměnnou vazbu pomocí const. const nezaručuje neměnnost obsahu objektu, pouze brání přiřazení jiné hodnoty do stejné vazby. var má odlišný scope a kvůli hoistingu může vést k méně přehlednému chování.

## Typy a operátory

JavaScript má primitivní typy i objekty a používá dynamické typování. Hodnota null označuje záměrnou nepřítomnost, zatímco [[undefined]] často znamená, že hodnota nebyla určena.

Striktní porovnání === neprovádí automatickou konverzi typů, proto je obvykle předvídatelnější než ==. Pravdivostní převody mohou způsobit, že prázdný řetězec, nula a null se v podmínce chovají jako nepravdivé hodnoty.

## Řízení programu a funkce

Podmínky vybírají větev programu a cykly opakují kroky. Funkce uzavírá opakovatelnou logiku, může přijímat parametry a vracet hodnotu. Šipkové funkce mají stručný zápis, ale liší se mimo jiné zacházením s this.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] Funkce lze v JavaScriptu předávat jako hodnoty.
[[X]] Pole je objekt určený pro uspořádanou kolekci.
[[X]] Striktní rovnost porovnává hodnotu i typ.
[[ ]] const automaticky zmrazí všechny vlastnosti objektu.

## Objekty a třídy

Objekt sdružuje vlastnosti a metody. Třídy poskytují čitelnou syntaxi pro konstrukci objektů, ale JavaScriptové dědění stojí na [[prototypech]]. Vestavěné objekty jako Array, Date, Map nebo JSON řeší běžné úlohy, každý však má přesně vymezenou roli.
