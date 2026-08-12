<!--
title: Vznik OOP, třídy a objekty – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Na jaký problém reagovalo objektově orientované programování?**

<!-- data-randomize="true" -->
[(X)] Na obtížnou organizaci a údržbu rozsáhlých provázaných programů.
[( )] Na nemožnost počítačů provádět aritmetiku.
[( )] Na nedostatek značek v HTML.
[( )] Na absenci souborových systémů.

---

**2. Které potíže velkých procedurálních programů kapitola uvádí?**

<!-- data-randomize="true" -->
[[X]] obtížná údržba
[[X]] opakování kódu
[[X]] špatná organizace
[[X]] náchylnost změn k vedlejším chybám
[[ ]] automatické zapouzdření
[[ ]] povinná hierarchie tříd

---

**3. Jaká je hlavní změna pohledu v OOP?**

<!-- data-randomize="true" -->
[(X)] Data a operace se spojují do spolupracujících objektů.
[( )] Program se zapisuje jen jako binární posloupnost.
[( )] Každý algoritmus se nahradí databází.
[( )] Veškerý stav se přesune do globálních proměnných.

---

**4. Co je třída?**

<!-- data-randomize="true" -->
[(X)] Předpis určující atributy a metody objektů daného typu.
[( )] Konkrétní běžící instance v paměti.
[( )] Jedna hodnota atributu.
[( )] Samostatný proces operačního systému.

---

**5. Co je objekt?**

<!-- data-randomize="true" -->
[(X)] Konkrétní instance třídy s vlastním stavem v paměti.
[( )] Pouze text definice třídy.
[( )] Programovací jazyk určený pro OOP.
[( )] Vždy jediná globální proměnná.

---

**6. Co představuje atribut?**

<!-- data-randomize="true" -->
[(X)] Data nebo vlastnost objektu.
[( )] Překladač objektového jazyka.
[( )] Vztah mezi dvěma repozitáři.
[( )] Samostatný běžící proces.

---

**7. Co představuje metoda?**

<!-- data-randomize="true" -->
[(X)] Chování nebo operaci definovanou třídou.
[( )] Pouze uloženou číselnou hodnotu.
[( )] Příponu zdrojového souboru.
[( )] Přístupovou adresu v síti.

---

**8. Jaký je vztah třídy Automobil a konkrétní červené Octavie?**

<!-- data-randomize="true" -->
[(X)] Automobil je třída, konkrétní vůz její objekt.
[( )] Automobil je objekt a Octavia programovací jazyk.
[( )] Oba názvy označují pouze atribut.
[( )] Octavia je metoda třídy Automobil.

---

**9. Kde se podle kapitoly OOP používá?**

<!-- data-randomize="true" -->
[[X]] webové a desktopové aplikace
[[X]] počítačové hry
[[X]] simulace
[[X]] informační systémy
[[X]] grafika
[[ ]] jen v ovladačích procesoru
[[ ]] výhradně v textových dokumentech

---

**10. Může z jedné třídy vzniknout více objektů?**

<!-- data-randomize="true" -->
[(X)] Ano, každý může mít vlastní hodnoty atributů.
[( )] Ne, třída dovoluje právě jednu instanci.
[( )] Ano, ale všechny musí sdílet každý atribut.
[( )] Ne, objekt existuje jen ve zdrojovém textu.


# 2. Interaktivní shrnutí kapitoly

## Proč vznikl objektový pohled

S růstem aplikací se dlouhé procedurální programy s globálním stavem a mnoha vazbami obtížně měnily. Stejný kód se opakoval a zásah na jednom místě mohl poškodit jiné. OOP proto modeluje systém jako spolupráci objektů, které spojují [[data]] s operacemi nad nimi.

Objektové členění samo o sobě chyby neodstraní, ale nabízí způsob, jak rozdělit odpovědnosti do srozumitelnějších celků. Cílem není [[ vytvořit třídu pro každý řádek | (uspořádat stav a chování podle modelovaného problému) | nahradit všechny algoritmy atributy ]].

## Třída je předpis, objekt konkrétní instance

[[Třída]] určuje, jaké atributy a metody budou mít objekty daného typu. Sama je definicí. Objekt vzniká instancováním v paměti a nese skutečné hodnoty, například červenou barvu a konkrétní množství paliva.

Z jedné třídy `Automobil` může vzniknout mnoho vozů. Každý má vlastní instanční stav, ale používá chování popsané společnou třídou. Atribut reprezentuje [[vlastnost]], metoda operaci.

**Rozliš správně třídu, objekt, atribut a metodu:**

<!-- data-randomize="true" -->
[[X]] Automobil — možná třída
[[X]] konkrétní červený vůz — objekt
[[X]] množství_paliva — atribut
[[X]] zabrzdi() — metoda
[[ ]] rychlost 50 km/h — definice celé třídy

## Model skutečného problému

Ve hře mohou objekty představovat postavy a předměty, v informačním systému zákazníky či transakce, v grafice tvary a kamery. Výběr tříd má vycházet z potřeb aplikace, nikoli jen z podstatných jmen v zadání.

Objekt obsahuje stav a nabízí chování, které s ním souvisí. Model je užitečný, když [[ (pomáhá rozdělit logiku a vztahy systému) | kopíruje realitu do nejmenšího detailu | soustředí všechny operace do jedné třídy ]]. OOP je tedy paradigma návrhu programu, ne pouhá syntaxe slova `class`.
