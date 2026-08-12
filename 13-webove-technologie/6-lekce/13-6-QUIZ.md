<!--
title: Knihovny, frameworky a moderní vývoj webu – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Knihovna je soubor hotového kódu pro určitou oblast.**

<!-- data-randomize="true" -->
[(X)] Webové knihovny a CDN
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Framework poskytuje širší strukturu pro tvorbu aplikace.**

<!-- data-randomize="true" -->
[(X)] Webové frameworky
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? U rozsáhlého frontendu vzniká problém: stránka obsahuje mnoho propojených interaktivních částí a jejich ruční změny v DOM mohou být obtížně udržovatelné.**

<!-- data-randomize="true" -->
[(X)] Komponentový frontend
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? WebAssembly — Wasm je nízkoúrovňový binární formát a běhový model navržený pro rychlé a přenositelné vykonávání kódu.**

<!-- data-randomize="true" -->
[(X)] WebAssembly
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**5. Které tvrzení odpovídá tématu Webové knihovny a CDN?**

<!-- data-randomize="true" -->
[(X)] Knihovna je soubor hotového kódu pro určitou oblast.
[( )] Web je založen na komunikaci mezi programy.
[( )] Pojmy frontend a backend popisují dvě různé části webové aplikace.
[( )] Webový server je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi.

---

**6. Které tvrzení odpovídá tématu WebAssembly?**

<!-- data-randomize="true" -->
[(X)] WebAssembly — Wasm je nízkoúrovňový binární formát a běhový model navržený pro rychlé a přenositelné vykonávání kódu.
[( )] Web je založen na komunikaci mezi programy.
[( )] Pojmy frontend a backend popisují dvě různé části webové aplikace.
[( )] Webový server je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Webové knihovny a CDN
[[X]] Webové frameworky
[[X]] Komponentový frontend
[[ ]] Klient a server
[[ ]] Frontend a backend

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Knihovny, frameworky a moderní vývoj webu?**

<!-- data-randomize="true" -->
[(X)] Komponentový frontend
[( )] TypeScript a transkompilace
[( )] Nástroje a proces vývoje webu
[( )] WebAssembly

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Knihovna je soubor hotového kódu pro určitou oblast.
[[X]] Framework poskytuje širší strukturu pro tvorbu aplikace.
[[ ]] Web je založen na komunikaci mezi programy.
[[ ]] Pojmy frontend a backend popisují dvě různé části webové aplikace.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] WebAssembly
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

# 2. Interaktivní shrnutí kapitoly

## Knihovna, framework a CDN

Knihovna nabízí funkce, které volá aplikace. Framework určuje širší strukturu a v určených bodech volá náš kód. Rozdíl tedy spočívá hlavně v [[ barvě výsledného rozhraní | (řízení toku programu a rozsahu poskytované struktury) | podpoře pouze jednoho prohlížeče ]].

CDN distribuuje statické prostředky z více míst blízko uživatelům. Může zrychlit načítání, ale externí závislost přináší otázky dostupnosti, verzí, integrity a soukromí.

## Komponentový frontend

Komponenta spojuje strukturu, chování a stav určité části rozhraní. Data obvykle proudí do komponenty přes vlastnosti a změna stavu vyvolá aktualizaci zobrazení. Sdílený stav má být umístěn tam, kde mu rozumějí všechny části, které jej potřebují.

Framework neodstraňuje potřebu rozumět HTML, CSS a JavaScriptu. Naopak staví na jejich principech.

## TypeScript a nástroje

TypeScript přidává statickou kontrolu typů a před spuštěním se převádí na JavaScript. Typy pomáhají odhalit část chyb a dokumentují rozhraní, ale [[ dokazují úplnou správnost programu | (nenahrazují běhové kontroly a testy) | automaticky opravují síťové chyby ]].

**Co může být součástí moderního vývojového procesu?**

<!-- data-randomize="true" -->
[[X]] správce balíčků
[[X]] bundler nebo build nástroj
[[X]] linter a formátovač
[[X]] automatizované testy
[[ ]] ruční změny závislostí bez evidence verzí

## WebAssembly

WebAssembly je binární formát a běhový cíl pro výkonný kód v prohlížeči. Doplňuje JavaScript například u výpočetně náročných částí; samo neposkytuje běžnou práci s DOM. Typická aplikace proto používá [[ pouze WebAssembly bez webových API | (spolupráci JavaScriptu a WebAssembly) | WebAssembly jako náhradu HTML dokumentu ]].

Nástroje mají řešit konkrétní problém projektu. Každá nová vrstva současně přidává závislosti, konfiguraci a nároky na údržbu.
