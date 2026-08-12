<!--
title: Node.js a serverový JavaScript – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Node.js je běhové prostředí pro JavaScript mimo webový prohlížeč.**

<!-- data-randomize="true" -->
[(X)] Node.js a jeho princip
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Větší program se nerozumně neukládá do jednoho souboru.**

<!-- data-randomize="true" -->
[(X)] npm, `package.json` a moduly
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Node.js umí HTTP server vytvořit i bez frameworku, ale při tvorbě aplikací se často používá vyšší vrstva.**

<!-- data-randomize="true" -->
[(X)] Express a základ serverové aplikace
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Dynamický web nemusí vždy posílat do prohlížeče pouze JSON a celé rozhraní sestavovat JavaScriptem.**

<!-- data-randomize="true" -->
[(X)] Šablonovací systémy
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**5. Které tvrzení odpovídá tématu Node.js a jeho princip?**

<!-- data-randomize="true" -->
[(X)] Node.js je běhové prostředí pro JavaScript mimo webový prohlížeč.
[( )] Web je založen na komunikaci mezi programy.
[( )] Pojmy frontend a backend popisují dvě různé části webové aplikace.
[( )] Webový server je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi.

---

**6. Které tvrzení odpovídá tématu Šablonovací systémy?**

<!-- data-randomize="true" -->
[(X)] Dynamický web nemusí vždy posílat do prohlížeče pouze JSON a celé rozhraní sestavovat JavaScriptem.
[( )] Web je založen na komunikaci mezi programy.
[( )] Pojmy frontend a backend popisují dvě různé části webové aplikace.
[( )] Webový server je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Node.js a jeho princip
[[X]] npm, `package.json` a moduly
[[X]] Express a základ serverové aplikace
[[ ]] Klient a server
[[ ]] Frontend a backend

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Node.js a serverový JavaScript?**

<!-- data-randomize="true" -->
[(X)] Synchronní a asynchronní přístup
[( )] TypeScript a transkompilace
[( )] Nástroje a proces vývoje webu
[( )] WebAssembly

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Node.js je běhové prostředí pro JavaScript mimo webový prohlížeč.
[[X]] Větší program se nerozumně neukládá do jednoho souboru.
[[ ]] Web je založen na komunikaci mezi programy.
[[ ]] Pojmy frontend a backend popisují dvě různé části webové aplikace.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Šablonovací systémy
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

# 2. Interaktivní shrnutí kapitoly

## JavaScript na serveru

Node.js umožňuje spouštět JavaScript mimo prohlížeč. Jeho událostní model dobře obsluhuje mnoho čekajících vstupně-výstupních operací, ale dlouhý výpočet na hlavním vlákně může blokovat další práci.

Balíčky spravuje [[npm]] a soubor package.json popisuje projekt, skripty a závislosti. Zámkový soubor zachycuje konkrétní vyřešené verze, aby byla instalace reprodukovatelnější.

## Express a cesta požadavku

Express usnadňuje vytvoření HTTP serveru, rout a middleware. Route spojuje metodu a cestu s obslužnou funkcí. Middleware může požadavek zaznamenat, doplnit, ověřit nebo odmítnout ještě před cílovou obsluhou.

Odpověď musí být dokončena právě jednou. Server může vrátit HTML, JSON nebo stavový kód; nemá po odeslání odpovědi pokračovat v dalším zápisu.

## Asynchronní práce

Čtení souboru, databázový dotaz nebo síťový požadavek obvykle čekají na vnější zdroj. Promise reprezentuje budoucí výsledek a zápis async/await umožňuje tuto práci vyjádřit čitelněji.

await [[ zastaví celý serverový proces | (pozastaví danou asynchronní funkci, ne všechny ostatní úlohy) | převede operaci na synchronní výpočet ]].

**Co typicky probíhá asynchronně?**

<!-- data-randomize="true" -->
[[X]] čtení souboru
[[X]] komunikace s databází
[[X]] síťový požadavek
[[ ]] obyčejné sečtení dvou čísel v paměti

## Data a šablony

Databázové dotazy mají používat parametrizaci, ne skládání příkazu z nedůvěryhodného textu. Šablonovací systém kombinuje připravenou strukturu s daty a vytváří HTML; automatické escapování pomáhá omezit [[XSS]].

Serverová aplikace tak propojuje routing, aplikační pravidla, data a výslednou reprezentaci, ale každá vrstva má zůstat srozumitelně oddělená.
