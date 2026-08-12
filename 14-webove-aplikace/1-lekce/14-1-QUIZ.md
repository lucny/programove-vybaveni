<!--
title: Architektura webové aplikace – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Která podkapitola nejlépe odpovídá tomuto tvrzení? Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.**

<!-- data-randomize="true" -->
[(X)] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Server-side rendering, client-side rendering a hybridní web
[( )] Projekt, aplikace a cesta požadavku

---

**2. Která podkapitola nejlépe odpovídá tomuto tvrzení? Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.**

<!-- data-randomize="true" -->
[(X)] MVC a příbuzné návrhové vzory
[( )] Od statické stránky k systému se stavem
[( )] Server-side rendering, client-side rendering a hybridní web
[( )] Projekt, aplikace a cesta požadavku

---

**3. Která podkapitola nejlépe odpovídá tomuto tvrzení? Klasická serverová aplikace vytvoří HTML na serveru.**

<!-- data-randomize="true" -->
[(X)] Server-side rendering, client-side rendering a hybridní web
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Projekt, aplikace a cesta požadavku

---

**4. Která podkapitola nejlépe odpovídá tomuto tvrzení? Klasická serverová aplikace vytvoří HTML na serveru.**

<!-- data-randomize="true" -->
[(X)] Server-side rendering, client-side rendering a hybridní web
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Projekt, aplikace a cesta požadavku

---

**5. Které tvrzení odpovídá tématu Od statické stránky k systému se stavem?**

<!-- data-randomize="true" -->
[(X)] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[( )] Django je webový framework pro Python, který spojuje routování, ORM, šablony, formuláře, autentizaci, administraci a řadu bezpečnostních mechanismů.
[( )] Django ORM — Object–Relational Mapping umožňuje popsat tabulky a vztahy pomocí tříd Pythonu.
[( )] Když do modelu přidáme pole summary, databáze se sama bezpečně nezmění jen proto, že Pythonová třída vypadá jinak.

---

**6. Které tvrzení odpovídá tématu Server-side rendering, client-side rendering a hybridní web?**

<!-- data-randomize="true" -->
[(X)] Klasická serverová aplikace vytvoří HTML na serveru.
[( )] Django je webový framework pro Python, který spojuje routování, ORM, šablony, formuláře, autentizaci, administraci a řadu bezpečnostních mechanismů.
[( )] Django ORM — Object–Relational Mapping umožňuje popsat tabulky a vztahy pomocí tříd Pythonu.
[( )] Když do modelu přidáme pole summary, databáze se sama bezpečně nezmění jen proto, že Pythonová třída vypadá jinak.

---

**7. Která témata jsou součástí této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Od statické stránky k systému se stavem
[[X]] MVC a příbuzné návrhové vzory
[[X]] Server-side rendering, client-side rendering a hybridní web
[[ ]] Projekt, aplikace a cesta požadavku
[[ ]] Model a ORM: objektový pohled na relační databázi

---

**8. Které téma tvoří jednu z hlavních částí kapitoly Architektura webové aplikace?**

<!-- data-randomize="true" -->
[(X)] MVC a příbuzné návrhové vzory
[( )] Testování a automatizovaný průchod změny
[( )] Provoz začíná po úspěšném deployi
[( )] AI jako další služba v architektuře

---

**9. Která tvrzení vycházejí z obsahu této kapitoly?**

<!-- data-randomize="true" -->
[[X]] Statický web může být tvořen soubory HTML, CSS, JavaScriptu a médii, které server vydává prakticky beze změny.
[[X]] Mnoho frameworků používá architektonické myšlenky odvozené od MVC — Model–View–Controller.
[[ ]] Django je webový framework pro Python, který spojuje routování, ORM, šablony, formuláře, autentizaci, administraci a řadu bezpečnostních mechanismů.
[[ ]] Django ORM — Object–Relational Mapping umožňuje popsat tabulky a vztahy pomocí tříd Pythonu.

---

**10. Které téma uzavírá tuto kapitolu?**

<!-- data-randomize="true" -->
[(X)] Server-side rendering, client-side rendering a hybridní web
[( )] Od statické stránky k systému se stavem
[( )] MVC a příbuzné návrhové vzory
[( )] Projekt, aplikace a cesta požadavku

# 2. Interaktivní shrnutí kapitoly

## Aplikace pracuje se stavem

Statická stránka vrací předem připravený obsah. Webová aplikace přijímá vstupy, udržuje stav, provádí pravidla a vytváří odpověď podle uživatele a dat. Stav může být v databázi, serverové relaci nebo klientském rozhraní; každé umístění má jinou životnost a důvěryhodnost.

Klientské zobrazení není autoritou pro bezpečnostní rozhodnutí. Pravidlo, které chrání data, musí být vynuceno [[ pouze skrytím tlačítka | (na důvěryhodné serverové straně) | změnou CSS třídy ]].

## Oddělení odpovědností

MVC rozděluje aplikaci na model, pohled a řídicí část. Model reprezentuje data a pravidla, view připravuje prezentaci a controller nebo obdobná vrstva koordinuje požadavek. Cílem není přesně tři soubory, ale [[oddělení]] rolí, aby se systém lépe měnil a testoval.

**Která přiřazení odpovídají MVC?**

<!-- data-randomize="true" -->
[[X]] model — data a doménová pravidla
[[X]] view — výsledná prezentace
[[X]] controller — koordinace vstupu a odpovědi
[[ ]] view — přímá správa databázových migrací

## Kde vzniká HTML

Při server-side renderingu vznikne HTML na serveru a klient dostane hotovější dokument. Při client-side renderingu získá prohlížeč skript a data a rozhraní sestavuje na klientovi. Hybridní přístup kombinuje počáteční serverový výstup s následnou interaktivitou.

Žádná varianta není nejlepší ve všech situacích. Rozhodují požadavky na první zobrazení, SEO, interaktivitu, výkon a složitost provozu. SSR a CSR tedy označují [[ databázové modely | (místo a způsob sestavení uživatelského rozhraní) | druhy šifrování hesel ]].
