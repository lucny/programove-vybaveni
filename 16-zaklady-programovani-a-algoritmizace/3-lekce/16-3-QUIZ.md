<!--
title: Princip fungování programu v počítači – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Jaká posloupnost předchází vykonávání programu procesorem?**

<!-- data-randomize="true" -->
[(X)] Načtení z úložiště, umístění do RAM a vykonání CPU.
[( )] Překlad RAM na disk a vypnutí procesoru.
[( )] Uložení do registru bez použití paměti.
[( )] Odeslání programu na internetový server.

---

**2. Jaké kroky tvoří základní instrukční cyklus procesoru?**

<!-- data-randomize="true" -->
[(X)] Načti, dekóduj, vykonej.
[( )] Zapiš, vytiskni, smaž.
[( )] Přelož, archivuj, odešli.
[( )] Spusť, komprimuj, restartuj.

---

**3. Co při běhu programů zajišťuje operační systém?**

<!-- data-randomize="true" -->
[[X]] spouštění programů
[[X]] přidělování času procesoru
[[X]] správu paměti
[[X]] komunikaci hardwaru a softwaru
[[ ]] návrh algoritmu za programátora
[[ ]] automatickou správnost každého výpočtu

---

**4. Jaký je rozdíl mezi programem a procesem?**

<!-- data-randomize="true" -->
[(X)] Program je uložený předpis, proces jeho běžící instance.
[( )] Program je vlákno a proces zdrojový soubor.
[( )] Program je vždy aktivní, proces vždy pasivní.
[( )] Jde o dvě označení stejného souboru.

---

**5. Jak může jednojádrový procesor vytvářet dojem multitaskingu?**

<!-- data-randomize="true" -->
[(X)] Operační systém rychle přepíná mezi procesy.
[( )] Každý program dostane vlastní fyzický procesor.
[( )] Procesy se převedou na soubory v RAM.
[( )] Všechny instrukce se vykonají ve stejném okamžiku.

---

**6. Co je vlákno?**

<!-- data-randomize="true" -->
[(X)] Menší jednotka vykonávání uvnitř procesu.
[( )] Adresa souboru na disku.
[( )] Samostatný operační systém.
[( )] Typ strojového jazyka.

---

**7. Která tvrzení o vláknech jednoho procesu jsou správná?**

<!-- data-randomize="true" -->
[[X]] Sdílejí paměť procesu.
[[X]] Mohou oddělit různé činnosti programu.
[[X]] Mohou využít více jader procesoru.
[[ ]] Každé musí mít vlastní zdrojový program.
[[ ]] Nikdy nemohou běžet souběžně.

---

**8. Co uchovává ukazatel?**

<!-- data-randomize="true" -->
[(X)] Adresu místa v paměti.
[( )] Vždy přímo číselnou hodnotu objektu.
[( )] Pouze název zdrojového souboru.
[( )] Počet vláken operačního systému.

---

**9. Proč operační systém odděluje paměťové prostory procesů?**

<!-- data-randomize="true" -->
[(X)] Aby procesy nemohly nelegálně zasahovat do cizí paměti.
[( )] Aby všechny procesy sdílely každou proměnnou.
[( )] Aby nebylo nutné používat RAM.
[( )] Aby procesor nemusel dekódovat instrukce.

---

**10. Jak se často liší práce s pamětí v C a Pythonu?**

<!-- data-randomize="true" -->
[(X)] C zpřístupňuje ukazatele, Python většinu detailů skrývá běhovým prostředím.
[( )] Python vyžaduje ruční adresy, C má vždy garbage collector.
[( )] Oba jazyky zakazují dynamickou paměť.
[( )] C ani Python neukládají data do RAM.


# 2. Interaktivní shrnutí kapitoly

## Od souboru k běžícím instrukcím

Program uložený na disku je pasivní. Při spuštění operační systém načte potřebný kód a data do [[RAM]], vytvoří proces a přiděluje mu prostředky. Procesor pak opakuje cyklus [[ načti – zapiš – vytiskni | (načti – dekóduj – vykonej) | přelož – ulož – vypni ]].

Operační systém stojí mezi aplikací a hardwarem: spouští programy, plánuje čas CPU, spravuje paměť a zprostředkovává zařízení. Program tedy neběží zcela samostatně.

## Program, proces a vlákno

Program je uložený předpis, zatímco [[proces]] je jeho aktivní běžící instance. Jeden program může být spuštěn vícekrát a vytvářet několik procesů s odděleným stavem.

Multitasking znamená správu více procesů. Na jednom jádře vzniká souběžný dojem rychlým [[ přepisováním zdrojového kódu | (přepínáním přiděleného času mezi procesy) | kopírováním každého procesu na disk ]]. Multithreading dělí jeden proces na více vláken, která sdílejí jeho paměť.

**K čemu lze v jednom programu využít více vláken?**

<!-- data-randomize="true" -->
[[X]] oddělení uživatelského rozhraní od práce na pozadí
[[X]] souběžná obsluha síťových požadavků
[[X]] využití více jader pro vhodně rozdělené úlohy
[[ ]] automatická oprava každé chyby v algoritmu
[[ ]] nahrazení operační paměti diskem

## Paměť a adresy

Kód, proměnné i dočasné výsledky za běhu sídlí v adresovatelných oblastech paměti. Operační systém procesům přiděluje vlastní prostor, aby jeden proces [[ mohl libovolně měnit cizí data | (nemohl bez oprávnění zasahovat do paměti jiného) | nepotřeboval žádnou ochranu ]].

[[Ukazatel]] neuchovává přímo cílovou hodnotu, ale její adresu. V C a C++ dává programátorovi jemnou kontrolu při dynamické alokaci a práci s datovými strukturami. Vyšší jazyky jako Python nebo Java podrobnosti často skrývají a paměť spravují prostřednictvím běhového prostředí či [[garbage collectoru]]. Zjednodušení práce je vykoupeno menší přímou kontrolou nad jejím využitím.
