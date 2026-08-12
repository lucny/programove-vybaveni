<!--
title: Klient, server, frontend a backend – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Web je založen na komunikaci mezi programy.**

<!-- data-randomize="true" -->
[(X)] Klient a server
[( )] Frontend a backend
[( )] Webové servery
[( )] Frontendové technologie

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Pojmy frontend a backend popisují dvě různé části webové aplikace.**

<!-- data-randomize="true" -->
[(X)] Frontend a backend
[( )] Klient a server
[( )] Webové servery
[( )] Frontendové technologie

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Webový server je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi.**

<!-- data-randomize="true" -->
[(X)] Webové servery
[( )] Klient a server
[( )] Frontend a backend
[( )] Frontendové technologie

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Serverová část webu může být vytvořena v mnoha jazycích a prostředích.**

<!-- data-randomize="true" -->
[(X)] Serverové technologie
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**5. Které tvrzení odpovídá tématu Klient a server?**

<!-- data-randomize="true" -->
[(X)] Web je založen na komunikaci mezi programy.
[( )] JavaScript vznikl v roce 1995 jako jazyk pro programování webových stránek.
[( )] Proměnné v moderním JavaScriptu deklarujeme především pomocí const a let.
[( )] JavaScript je dynamicky typovaný.

---

**6. Které tvrzení odpovídá tématu Serverové technologie?**

<!-- data-randomize="true" -->
[(X)] Serverová část webu může být vytvořena v mnoha jazycích a prostředích.
[( )] JavaScript vznikl v roce 1995 jako jazyk pro programování webových stránek.
[( )] Proměnné v moderním JavaScriptu deklarujeme především pomocí const a let.
[( )] JavaScript je dynamicky typovaný.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Klient a server
[[X]] Frontend a backend
[[X]] Webové servery
[[ ]] JavaScript a ECMAScript
[[ ]] `let`, `const`, `var`, scope a hoisting

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Klient, server, frontend a backend?**

<!-- data-randomize="true" -->
[(X)] Webové servery
[( )] TypeScript a transkompilace
[( )] Nástroje a proces vývoje webu
[( )] WebAssembly

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Web je založen na komunikaci mezi programy.
[[X]] Pojmy frontend a backend popisují dvě různé části webové aplikace.
[[ ]] JavaScript vznikl v roce 1995 jako jazyk pro programování webových stránek.
[[ ]] Proměnné v moderním JavaScriptu deklarujeme především pomocí const a let.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Serverové technologie
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

# 2. Interaktivní shrnutí kapitoly

## Klient a server jsou role

Klient zahajuje požadavek a server na něj odpovídá. Nejčastějším klientem webu je prohlížeč, ale stejnou službu může používat mobilní aplikace nebo jiný server. Jeden počítač může podle situace plnit [[ vždy jen jednu pevnou roli | (roli klienta i serveru) | pouze roli síťového směrovače ]].

Webový server přijímá HTTP požadavky, vrací statické soubory nebo předává požadavek aplikační logice. Odpověď může obsahovat HTML, data ve formátu JSON, obrázek nebo chybovou informaci.

## Frontend a backend

Frontend běží převážně v prostředí uživatele a zajišťuje zobrazení a interakci. Tvoří jej především HTML, CSS a [[JavaScript]]. Backend běží na serveru, ověřuje pravidla, pracuje s databází a připravuje odpovědi.

Rozdělení neznamená, že klientu lze důvěřovat. Kontrola formuláře ve frontendu zlepšuje odezvu, ale bezpečnostní validace musí proběhnout také [[na serveru]].

**Která přiřazení jsou správná?**

<!-- data-randomize="true" -->
[[X]] HTML — struktura dokumentu
[[X]] CSS — vzhled a layout
[[X]] JavaScript — chování a práce s webovými API
[[X]] backend — pravidla a přístup k datům
[[ ]] databáze — přímé vykreslení stránky v prohlížeči

## Technologie tvoří vrstvy

Frontendové knihovny a frameworky pomáhají stavět uživatelské rozhraní. Serverové technologie řeší routing, autentizaci, práci s daty a generování odpovědí. Konkrétní nástroj se volí podle požadavků, týmu a provozu; samotná popularita není úplným kritériem.

Celý webový systém lze číst jako tok: uživatel → klient → HTTP požadavek → serverová aplikace → data → odpověď → aktualizované rozhraní.
