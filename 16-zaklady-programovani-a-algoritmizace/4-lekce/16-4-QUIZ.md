<!--
title: Algoritmizace a zápis algoritmů – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je algoritmizace?**

<!-- data-randomize="true" -->
[(X)] Proces návrhu algoritmu pro řešení konkrétního problému.
[( )] Překlad hotového programu do strojového kódu.
[( )] Měření velikosti operační paměti.
[( )] Pouhé kreslení symbolů bez analýzy problému.

---

**2. Který krok má při algoritmizaci předcházet návrhu řešení?**

<!-- data-randomize="true" -->
[(X)] Analýza požadavků a cílů problému.
[( )] Optimalizace neexistujícího programu.
[( )] Volba barvy vývojového diagramu.
[( )] Instalace všech programovacích jazyků.

---

**3. Které činnosti patří do algoritmizace?**

<!-- data-randomize="true" -->
[[X]] analýza problému
[[X]] návrh logiky
[[X]] zápis postupu
[[X]] testování a optimalizace
[[ ]] náhodná změna vstupů
[[ ]] vynechání kontroly výsledku

---

**4. Co charakterizuje pseudokód?**

<!-- data-randomize="true" -->
[(X)] Strukturovaný čitelný zápis bez přísné syntaxe konkrétního jazyka.
[( )] Binární instrukce určené přímo procesoru.
[( )] Graf složený výhradně z obrázků.
[( )] Spustitelný soubor vytvořený kompilátorem.

---

**5. Jakou roli má vývojový diagram?**

<!-- data-randomize="true" -->
[(X)] Graficky znázorňuje kroky a tok řízení algoritmu.
[( )] Ukládá hodnoty proměnných do databáze.
[( )] Nahrazuje procesor při vykonávání programu.
[( )] Určuje licenci výsledné aplikace.

---

**6. Co ve vývojovém diagramu označuje ovál?**

<!-- data-randomize="true" -->
[(X)] Začátek nebo konec.
[( )] Rozhodovací podmínku.
[( )] Vstup nebo výstup.
[( )] Běžný procesní krok.

---

**7. Co ve vývojovém diagramu označuje kosočtverec?**

<!-- data-randomize="true" -->
[(X)] Rozhodovací bod.
[( )] Začátek algoritmu.
[( )] Běžný výpočet bez větvení.
[( )] Uložení souboru na disk.

---

**8. Co ve vývojovém diagramu označuje paralelogram?**

<!-- data-randomize="true" -->
[(X)] Vstup nebo výstup.
[( )] Pouze konec programu.
[( )] Deklaraci funkce.
[( )] Překlad zdrojového kódu.

---

**9. Jakou funkci mají šipky ve vývojovém diagramu?**

<!-- data-randomize="true" -->
[(X)] Ukazují směr toku řízení.
[( )] Označují typ proměnné.
[( )] Měří časovou složitost.
[( )] Nahrazují všechny rozhodovací symboly.

---

**10. Které algoritmy text uvádí jako ustálená řešení běžných úloh?**

<!-- data-randomize="true" -->
[[X]] bubble sort
[[X]] quicksort
[[X]] binární vyhledávání
[[X]] Dijkstrův algoritmus
[[ ]] JVM
[[ ]] HTML


# 2. Interaktivní shrnutí kapitoly

## Nejprve porozumět problému

Algoritmizace nezačíná psaním syntaxe. Nejprve je nutné určit požadavky, vstupy, očekávané výstupy a podmínky správného řešení. Teprve potom vzniká logika kroků. Tento proces se nazývá [[algoritmizace]].

Úplná cesta vede od analýzy přes návrh a zápis až k [[ (testování a optimalizaci) | okamžitému překladu bez kontroly | výběru přípony souboru ]]. Testování ověřuje správnost, optimalizace hledá vhodnější provedení.

## Pseudokód jako most

Pseudokód připomíná programovací jazyk, ale není svázán jeho přesnou syntaxí. Umožňuje soustředit se na podmínky, opakování a pořadí kroků. Je proto [[ výsledným strojovým programem | (mostem mezi návrhem řešení a zdrojovým kódem) | náhradou všech testů ]].

U rekurzivního faktoriálu musí například zápis rozlišit jednoduchý případ a krok, který problém zmenší. Konkrétní závorky či klíčová slova Pythonu nebo C přicházejí až při implementaci.

## Vývojový diagram ukazuje tok

Vývojový diagram vyjadřuje logiku prostorově. [[Ovál]] označuje začátek nebo konec, obdélník běžný procesní krok, [[kosočtverec]] rozhodnutí a paralelogram vstup či výstup. Šipky propojují symboly ve směru vykonávání.

**Přiřaď významy, které do vývojového diagramu patří:**

<!-- data-randomize="true" -->
[[X]] obdélník — zpracování nebo výpočet
[[X]] kosočtverec — rozdělení toku podle podmínky
[[X]] paralelogram — načtení nebo vypsání hodnoty
[[X]] šipka — návaznost kroků
[[ ]] ovál — datový typ proměnné

## Zápis není řešení samo o sobě

Přirozený jazyk, pseudokód i diagram mohou popsat stejný algoritmus. Volba zápisu má pomoci pochopení a následné implementaci, nikoli změnit podstatu řešení. Pro běžné problémy navíc existují známé algoritmy, například bubble sort, quicksort, [[binární vyhledávání]] nebo Dijkstrův algoritmus. Jejich použití však stále vyžaduje pochopit podmínky a cíl konkrétní úlohy.
