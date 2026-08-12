<!--
title: Webové prohlížeče, bezpečnost a digitální stopa – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Webová stránka nepřichází do počítače jako hotový obrázek.**

<!-- data-randomize="true" -->
[(X)] Jak prohlížeč promění kód ve stránku
[( )] ARPANET: Zárodek dnešního internetu
[( )] Internet a intranet
[( )] Přepojování okruhů a paketů

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Adresní řádek, karty, historie, profily a rozšíření vypadají jako běžné ovládací prvky, ale každý z nich souvisí se soukromím a bezpečností.**

<!-- data-randomize="true" -->
[(X)] Rozhraní a ekosystém webových prohlížečů
[( )] ARPANET: Zárodek dnešního internetu
[( )] Internet a intranet
[( )] Přepojování okruhů a paketů

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Vývojářské nástroje ukazují rozdíl mezi tím, co vidí uživatel, a tím, co prohlížeč skutečně zpracovává.**

<!-- data-randomize="true" -->
[(X)] DevTools: digitální rentgen webové stránky
[( )] ARPANET: Zárodek dnešního internetu
[( )] Internet a intranet
[( )] Přepojování okruhů a paketů

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Smazání historie odstraní seznam navštívených stránek z vašeho prohlížeče, ale nevrátí odeslaný příspěvek, nesmaže serverové logy ani kopie u jiných lidí.**

<!-- data-randomize="true" -->
[(X)] Digitální stopa a paměť webu
[( )] ARPANET: Zárodek dnešního internetu
[( )] Internet a intranet
[( )] Přepojování okruhů a paketů

---

**5. Které tvrzení odpovídá tématu Jak prohlížeč promění kód ve stránku?**

<!-- data-randomize="true" -->
[(X)] Webová stránka nepřichází do počítače jako hotový obrázek.
[( )] Představte si svět, ve kterém by jediný zničený telefonní ústřední uzel odstřihl od komunikace celý stát.
[( )] Ve škole můžete otevřít web, ale zároveň také tisknout na školní tiskárně nebo pracovat se soubory, které z domova nevidíte.
[( )] Při klasickém telefonním hovoru byla mezi dvěma účastníky po dobu spojení vyhrazena komunikační cesta.

---

**6. Které tvrzení odpovídá tématu Digitální stopa a paměť webu?**

<!-- data-randomize="true" -->
[(X)] Smazání historie odstraní seznam navštívených stránek z vašeho prohlížeče, ale nevrátí odeslaný příspěvek, nesmaže serverové logy ani kopie u jiných lidí.
[( )] Představte si svět, ve kterém by jediný zničený telefonní ústřední uzel odstřihl od komunikace celý stát.
[( )] Ve škole můžete otevřít web, ale zároveň také tisknout na školní tiskárně nebo pracovat se soubory, které z domova nevidíte.
[( )] Při klasickém telefonním hovoru byla mezi dvěma účastníky po dobu spojení vyhrazena komunikační cesta.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Jak prohlížeč promění kód ve stránku
[[X]] Rozhraní a ekosystém webových prohlížečů
[[X]] DevTools: digitální rentgen webové stránky
[[ ]] ARPANET: Zárodek dnešního internetu
[[ ]] Internet a intranet

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Webové prohlížeče, bezpečnost a digitální stopa?**

<!-- data-randomize="true" -->
[(X)] DevTools: digitální rentgen webové stránky
[( )] Internet věcí
[( )] Generativní AI a hledání informací
[( )] Internet, bezpečnost, soukromí a pravdivost

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Webová stránka nepřichází do počítače jako hotový obrázek.
[[X]] Adresní řádek, karty, historie, profily a rozšíření vypadají jako běžné ovládací prvky, ale každý z nich souvisí se soukromím a bezpečností.
[[ ]] Představte si svět, ve kterém by jediný zničený telefonní ústřední uzel odstřihl od komunikace celý stát.
[[ ]] Ve škole můžete otevřít web, ale zároveň také tisknout na školní tiskárně nebo pracovat se soubory, které z domova nevidíte.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Digitální stopa a paměť webu
[( )] ARPANET: Zárodek dnešního internetu
[( )] Internet a intranet
[( )] Přepojování okruhů a paketů

# 2. Interaktivní shrnutí kapitoly

## Od odpovědi serveru k obrazu

Prohlížeč nejprve získá HTML a vytvoří strom dokumentu [[DOM]]. Načte styly, sestaví pravidla pro vzhled, vypočítá rozložení a stránku vykreslí. JavaScript může strukturu i vzhled později měnit, takže výsledná stránka není pouhým obrazem zdrojového HTML.

Rozhraní prohlížeče zahrnuje adresní řádek, karty, historii, záložky a správu oprávnění. Vykreslovací a JavaScriptový engine naproti tomu zpracovávají obsah stránky.

## DevTools jako diagnostika

Vývojářské nástroje umožňují prohlížet DOM a CSS, sledovat síťové požadavky, pracovat s konzolí a analyzovat výkon. Změna provedená v panelu Elements je obvykle [[ trvalá změna souboru na serveru | (dočasný zásah do aktuálně načtené stránky) | úprava všech kopií daného webu ]].

Panel Network pomáhá zjistit, který požadavek selhal, jaký měl stavový kód a jak dlouho trval. Konzole zobrazuje chyby skriptů a dovoluje ověřovat výrazy.

## Bezpečnost a soukromí

Prohlížeč odděluje weby pomocí bezpečnostních pravidel a žádá o oprávnění k citlivým funkcím, například poloze nebo kameře. Uživatel má posuzovat doménu, platnost zabezpečeného spojení i smysl požadovaného oprávnění.

Soukromý režim [[ zajišťuje anonymitu vůči poskytovateli internetu | (omezuje hlavně ukládání místní historie a cookies po ukončení relace) | blokuje všechny sledovací mechanismy ]].

**Co může omezovat soukromí při prohlížení?**

<!-- data-randomize="true" -->
[[X]] cookies a další identifikátory
[[X]] přihlášení k uživatelskému účtu
[[X]] otisk vlastností prohlížeče
[[ ]] samotná existence tlačítka Zpět

## Digitální stopa

Digitální stopu tvoří vědomě publikovaný obsah i údaje vznikající používáním služeb. Smazání místní historie neodstraní kopie uložené na serverech. Rozumná ochrana proto spojuje nastavení prohlížeče, omezení oprávnění a uvážlivé rozhodování o tom, jaká data službě poskytneme.
