<!--
title: Od otázky k datové sadě – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Čím má datová analýza začínat?**

<!-- data-randomize="true" -->
[(X)] Dobře formulovanou otázkou.
[( )] Výběrem typu grafu.
[( )] Otevřením Excelu.
[( )] Výpočtem průměru.

---

**2. Co označuje jedno pozorování v příkladu školy?**

<!-- data-randomize="true" -->
[(X)] Stav jedné učebny v konkrétním čase.
[( )] Celou školu za rok.
[( )] Jeden sloupec tabulky.
[( )] Pouze hodnotu teploty.

---

**3. Co jsou tidy data?**

<!-- data-randomize="true" -->
[(X)] Struktura, kde jeden řádek je záznam, sloupec proměnná a buňka hodnota.
[( )] Tabulka s libovolně sloučenými buňkami.
[( )] Graficky upravený report.
[( )] Soubor bez metadat.

---

**4. Které mohou být proměnné v projektu učeben?**

<!-- data-randomize="true" -->
[[X]] čas
[[X]] teplota
[[X]] CO₂
[[X]] obsazenost
[[X]] spotřeba energie
[[ ]] barva okraje tabulky

---

**5. Proč není vhodné ukládat `21,8 °C` jako jediný obsah buňky?**

<!-- data-randomize="true" -->
[(X)] Jednotka může způsobit, že hodnota bude interpretována jako text.
[( )] Čísla se nesmí ukládat do tabulek.
[( )] Teplotu nelze analyzovat.
[( )] Protože °C není fyzikální jednotka.

---

**6. Co je selection bias?**

<!-- data-randomize="true" -->
[(X)] Zkreslení způsobené nereprezentativním výběrem vzorku.
[( )] Chyba v grafickém formátování.
[( )] Zaokrouhlovací chyba.
[( )] Převod jednotek.

---

**7. Co musí dobrý vzorek kromě velikosti splňovat?**

<!-- data-randomize="true" -->
[(X)] Rozumně zastupovat populaci, o níž chceme mluvit.
[( )] Obsahovat jen extrémní hodnoty.
[( )] Mít vždy přesně 1000 řádků.
[( )] Být seřazený.

---

**8. Co mohou obsahovat metadata datové sady?**

<!-- data-randomize="true" -->
[[X]] význam sloupců
[[X]] jednotky
[[X]] původ dat
[[X]] časové období
[[X]] licenci
[[ ]] pouze barvu buněk

---

**9. Proč není jedna hodnota z každé učebny v různou dobu vhodná pro férové srovnání?**

<!-- data-randomize="true" -->
[(X)] Mění se současně místnost i čas měření.
[( )] Teplota se nedá měřit opakovaně.
[( )] Učebny nelze porovnávat.
[( )] Jedno měření je vždy přesnější než více.

---

**10. Jaký řetězec vystihuje datový proces?**

<!-- data-randomize="true" -->
[(X)] otázka → sběr → kontrola → struktura → analýza → interpretace → rozhodnutí
[( )] graf → barvy → tisk → data
[( )] vzorec → tabulka → otázka
[( )] API → PDF → prezentace


# 2. Interaktivní shrnutí kapitoly

## Data začínají otázkou

Dobrá analytická otázka určuje, co budeme pozorovat, které [[proměnné]] potřebujeme a jak poznáme užitečnou odpověď. Chyba ve sběru se nedá zachránit pozdějším efektním grafem.

Užitečný řetězec je **otázka → sběr → kontrola → struktura → analýza → interpretace → [[rozhodnutí]]**.

## Tidy data

V uklizené tabulce představuje jeden řádek jeden [[záznam]], jeden sloupec jednu proměnnou a jedna buňka jednu hodnotu. Jednotky je vhodné popsat názvem sloupce nebo metadaty, ne je míchat s číselnou hodnotou.

Datový typ musí odpovídat významu: číslo, kategorie, datum, čas nebo [[text]].

## Sběr a zkreslení

Data mohou vzniknout formulářem, senzorem, exportem nebo přes [[API]]. Automatický sběr ale sám nezaručuje kvalitu.

Selection bias vzniká, když vzorek nereprezentuje populaci. Důležitý je způsob výběru, ne jen [[velikost]] vzorku.

**Vyber faktory, které mohou ovlivnit kvalitu senzorových dat:**

<!-- data-randomize="true" -->
[[X]] kalibrace
[[X]] umístění senzoru
[[X]] měřicí interval
[[ ]] barva tabulky

## Metadata

Metadata jsou návod k použití dat. Popisují význam sloupců, jednotky, původ, časové období a další omezení. Krátký [[datový slovník]] pomáhá zabránit chybným interpretacím.
