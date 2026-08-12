<!--
title: Propojení JavaScriptu s webovou stránkou – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? JavaScript lze vložit přímo do HTML: html <script console.log("Ahoj"); </script Ve větších projektech je ale lepší použít samostatný soubor: html <script src="app.js"</script Pokud…**

<!-- data-randomize="true" -->
[(X)] Jak připojit JavaScript k HTML
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? HTML soubor je text. Prohlížeč jej ale při načítání parsuje a vytváří z něj v paměti objektovou stromovou strukturu nazývanou DOM — Document Object Model.**

<!-- data-randomize="true" -->
[(X)] DOM — Document Object Model
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? DOM popisuje dokument, ale webový prohlížeč poskytuje JavaScriptu i další informace a funkce, které se netýkají přímo HTML stránky.**

<!-- data-randomize="true" -->
[(X)] BOM — Browser Object Model
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Dynamická změna stránky sama o sobě nestačí.**

<!-- data-randomize="true" -->
[(X)] Interaktivní web — události
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

---

**5. Které tvrzení odpovídá tématu Jak připojit JavaScript k HTML?**

<!-- data-randomize="true" -->
[(X)] JavaScript lze vložit přímo do HTML: html <script console.log("Ahoj"); </script Ve větších projektech je ale lepší použít samostatný soubor: html <script src="app.js"</script Pokud…
[( )] Web je založen na komunikaci mezi programy.
[( )] Pojmy frontend a backend popisují dvě různé části webové aplikace.
[( )] Webový server je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi.

---

**6. Které tvrzení odpovídá tématu Interaktivní web — události?**

<!-- data-randomize="true" -->
[(X)] Dynamická změna stránky sama o sobě nestačí.
[( )] Web je založen na komunikaci mezi programy.
[( )] Pojmy frontend a backend popisují dvě různé části webové aplikace.
[( )] Webový server je program, který přijímá požadavky protokolu HTTP nebo HTTPS a vrací odpovědi.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Jak připojit JavaScript k HTML
[[X]] DOM — Document Object Model
[[X]] BOM — Browser Object Model
[[ ]] Klient a server
[[ ]] Frontend a backend

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Propojení JavaScriptu s webovou stránkou?**

<!-- data-randomize="true" -->
[(X)] BOM — Browser Object Model
[( )] TypeScript a transkompilace
[( )] Nástroje a proces vývoje webu
[( )] WebAssembly

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] JavaScript lze vložit přímo do HTML: html <script console.log("Ahoj"); </script Ve větších projektech je ale lepší použít samostatný soubor: html <script src="app.js"</script Pokud…
[[X]] HTML soubor je text. Prohlížeč jej ale při načítání parsuje a vytváří z něj v paměti objektovou stromovou strukturu nazývanou DOM — Document Object Model.
[[ ]] Web je založen na komunikaci mezi programy.
[[ ]] Pojmy frontend a backend popisují dvě různé části webové aplikace.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Interaktivní web — události
[( )] Klient a server
[( )] Frontend a backend
[( )] Webové servery

# 2. Interaktivní shrnutí kapitoly

## Připojení skriptu

JavaScript lze vložit do HTML nebo načíst z externího souboru. Externí skript zlepšuje organizaci a opakované použití. Atribut defer zajistí, že se skript vykoná až po zpracování dokumentu, přitom se může načítat souběžně.

Modulový skript používá type="module" a umožňuje import a export. Moduly mají vlastní scope a ve výchozím stavu se chovají podobně jako skripty s [[defer]].

## DOM a BOM

DOM je objektový model dokumentu. HTML elementy reprezentuje jako uzly, které lze vyhledávat, měnit nebo vytvářet. Metoda querySelector vybírá první prvek podle CSS selektoru.

BOM popisuje rozhraní pro okolí prohlížeče, například location, history nebo rozměry okna. DOM tedy pracuje s [[dokumentem]], BOM s prostředím prohlížeče.

## Změna stránky

Text lze bezpečně měnit pomocí textContent, třídy přes classList a atributy pomocí odpovídajících vlastností nebo metod. Vkládání nedůvěryhodného textu přes innerHTML může změnit data na spustitelný kód.

**Které operace patří k práci s DOM?**

<!-- data-randomize="true" -->
[[X]] výběr elementu
[[X]] změna textového obsahu
[[X]] přidání CSS třídy
[[X]] vytvoření nového uzlu
[[ ]] přímá změna tabulky v serverové databázi

## Události

Interaktivita vzniká reakcí na události, například click, input nebo submit. Posluchač se registruje pomocí [[addEventListener]]. Objekt události obsahuje informace o tom, co se stalo, a event.preventDefault může zabránit výchozí akci, například odeslání formuláře.

Delegování událostí využívá jejich šíření: jeden posluchač na společném rodiči může obsloužit mnoho dynamicky vznikajících potomků.
