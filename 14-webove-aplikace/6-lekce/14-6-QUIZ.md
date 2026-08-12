<!--
title: CMS, nasazení a provoz – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? CMS — Content Management System umožňuje vytvářet, upravovat a publikovat obsah bez ručního editování HTML.**

<!-- data-randomize="true" -->
[(X)] CMS je specializovaná webová aplikace
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Progressive Web App — PWA je webová aplikace využívající schopnosti platformy tak, aby se v podporovaném prostředí chovala více jako instalovatelná aplikace.**

<!-- data-randomize="true" -->
[(X)] PWA, SPA, serverless a další architektury
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Příkaz python manage.py runserver je určen pro vývoj.**

<!-- data-randomize="true" -->
[(X)] Vývojový server není produkční server
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Současné webové aplikace stále častěji přidávají funkce založené na generativní AI: shrnutí článku, vyhledávání v přirozeném jazyce, klasifikaci, překlad nebo asistenta.**

<!-- data-randomize="true" -->
[(X)] AI jako další služba v architektuře
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

---

**5. Které tvrzení odpovídá tématu CMS je specializovaná webová aplikace?**

<!-- data-randomize="true" -->
[(X)] CMS — Content Management System umožňuje vytvářet, upravovat a publikovat obsah bez ručního editování HTML.
[( )] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[( )] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.
[( )] Klasická serverová aplikace vytvoří HTML na serveru.

---

**6. Které tvrzení odpovídá tématu AI jako další služba v architektuře?**

<!-- data-randomize="true" -->
[(X)] Současné webové aplikace stále častěji přidávají funkce založené na generativní AI: shrnutí článku, vyhledávání v přirozeném jazyce, klasifikaci, překlad nebo asistenta.
[( )] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[( )] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.
[( )] Klasická serverová aplikace vytvoří HTML na serveru.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] CMS je specializovaná webová aplikace
[[X]] PWA, SPA, serverless a další architektury
[[X]] Vývojový server není produkční server
[[ ]] Od statické stránky k systému se stavem
[[ ]] MVC a příbuzné návrhové vzory

---

**8. Které téma tvoří jednu z hlavních částí kapitoly CMS, nasazení a provoz?**

<!-- data-randomize="true" -->
[(X)] Hosting, VPS, kontejnery a PaaS
[( )] Testování a automatizovaný průchod změny
[( )] Provoz začíná po úspěšném deployi
[( )] AI jako další služba v architektuře

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] CMS — Content Management System umožňuje vytvářet, upravovat a publikovat obsah bez ručního editování HTML.
[[X]] Progressive Web App — PWA je webová aplikace využívající schopnosti platformy tak, aby se v podporovaném prostředí chovala více jako instalovatelná aplikace.
[[ ]] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[[ ]] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] AI jako další služba v architektuře
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web

# 2. Interaktivní shrnutí kapitoly

## CMS a aplikační architektury

CMS je webová aplikace specializovaná na správu a publikaci obsahu. Nabízí účty, role, editor, šablony a rozšíření. Pohodlí pluginů ale zvyšuje počet závislostí, které je potřeba aktualizovat a kontrolovat.

SPA přesouvá velkou část navigace a stavu do klienta, PWA přidává webu možnosti instalace a práce při omezeném spojení. Serverless znamená, že provoz infrastruktury přebírá poskytovatel; serverový kód a odpovědnost za data [[ mizí úplně | (zůstávají, jen se mění provozní model) | přesouvají se do CSS ]].

## Od vývojového serveru k produkci

Vývojový server je určen pro pohodlnou práci, ne pro odolný veřejný provoz. Produkční nasazení používá vhodný aplikační server, reverzní proxy, HTTPS, správu statických souborů a řízenou konfiguraci.

Hosting nabízí jednoduchý sdílený provoz, VPS větší kontrolu, kontejner přenositelné prostředí a PaaS spravovanou platformu. Volba závisí na požadavcích, týmu, ceně a potřebné míře kontroly.

## Konfigurace, testy a změna

Tajné údaje a nastavení prostředí nepatří přímo do zdrojového kódu. Produkce má mít vypnutý debug režim, omezené hostitele, bezpečné cookies a samostatné přístupové údaje.

**Co patří do řízeného nasazení?**

<!-- data-randomize="true" -->
[[X]] automatizované testy
[[X]] vytvoření a kontrola sestavení
[[X]] aplikace databázových migrací
[[X]] možnost návratu nebo opravy
[[ ]] ruční změny bez záznamu

CI průběžně ověřuje změny, CD připravuje nebo provádí jejich nasazení. Automatizace snižuje počet náhodných kroků, ale stále potřebuje pozorovatelnost a odpovědnost.

## Provoz a externí služby

Po deployi začíná monitoring, logování, zálohování, obnova a řešení incidentů. Dostupná záloha má hodnotu až tehdy, když lze ověřit její [[obnovu]].

AI služba je další závislost architektury. Aplikace musí počítat s latencí, cenou, výpadkem, ochranou vstupních dat a možností chybného výstupu. Odpověď modelu proto prochází stejnými kontrolami jako jiné nedůvěryhodné externí údaje.
