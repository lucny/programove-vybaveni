<!--
title: Strukturované typy, pole, ukazatele a matice – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Jaký je rozdíl mezi skalárním a strukturovaným typem?**

<!-- data-randomize="true" -->
[(X)] Skalární drží jednu hodnotu, strukturovaný organizuje více hodnot.
[( )] Strukturovaný typ smí obsahovat pouze znaky.
[( )] Skalární typ je vždy pole stejného typu.
[( )] Liší se pouze názvem proměnné.

---

**2. Které struktury kapitola uvádí jako strukturované typy?**

<!-- data-randomize="true" -->
[[X]] pole
[[X]] záznamy
[[X]] seznamy
[[X]] slovníky
[[ ]] jediné celé číslo
[[ ]] jeden znak

---

**3. Co charakterizuje klasické pole?**

<!-- data-randomize="true" -->
[(X)] Prvky stejného typu uložené v pořadí a přístupné indexem.
[( )] Prvky různých typů bez pořadí.
[( )] Výhradně dvojice klíč-hodnota.
[( )] Vždy stromová hierarchie hodnot.

---

**4. Jaký index má první prvek pole v C?**

<!-- data-randomize="true" -->
[(X)] 0.
[( )] 1.
[( )] -1.
[( )] Podle velikosti pole.

---

**5. Proč je přístup k prvku pole podle indexu rychlý?**

<!-- data-randomize="true" -->
[(X)] Prvky leží souvisle a adresa se vypočítá z indexu.
[( )] Program musí vždy projít všechny předchozí prvky.
[( )] Pole používá regulární výraz.
[( )] Každý prvek je uložen v jiném souboru.

---

**6. Co je statické pole?**

<!-- data-randomize="true" -->
[(X)] Pole s velikostí stanovenou při deklaraci.
[( )] Pole, které se vždy automaticky zvětšuje.
[( )] Pole uložené pouze v textovém souboru.
[( )] Pole bez indexů.

---

**7. Jak se v C přiděluje a uvolňuje dynamické pole?**

<!-- data-randomize="true" -->
[(X)] Pomocí malloc a free.
[( )] Pomocí import a del.
[( )] Pomocí fopen a fclose.
[( )] Pomocí push a pull.

---

**8. Jak se v Pythonu chová list?**

<!-- data-randomize="true" -->
[(X)] Je dynamický a může se podle potřeby zvětšovat.
[( )] Má vždy pevnou velikost jako pole v C.
[( )] Může obsahovat pouze celá čísla.
[( )] Nelze k němu přistupovat indexem.

---

**9. Jaký vztah má v C název pole k ukazateli?**

<!-- data-randomize="true" -->
[(X)] V mnoha výrazech odkazuje na adresu prvního prvku.
[( )] Vždy obsahuje počet prvků pole.
[( )] Je totožný s poslední hodnotou pole.
[( )] Nemá s adresami paměti žádnou souvislost.

---

**10. Jak se přistupuje k prvku dvourozměrné matice?**

<!-- data-randomize="true" -->
[(X)] Pomocí indexu řádku a sloupce.
[( )] Pouze pomocí klíče textového slovníku.
[( )] Jedním ukazatelem bez indexu.
[( )] Regulárním výrazem nad hodnotami.


# 2. Interaktivní shrnutí kapitoly

## Jedna hodnota nebo organizovaný celek

Skalární typ reprezentuje jednu hodnotu, například věk nebo teplotu. Strukturovaný typ spojuje více hodnot podle určitého pravidla. Záznam může sdružit jméno, věk a město, [[pole]] posloupnost prvků stejného typu a slovník dvojice klíč–hodnota.

Volba struktury určuje, jak se k datům přistupuje. Nejde jen o to, kolik hodnot uložíme, ale také [[ (jak jsou uspořádány a jaké operace podporují) | jakou barvu mají v editoru | v jakém pořadí vznikl zdrojový kód ]].

## Pole a index

Klasické pole obsahuje prvky stejného typu uložené za sebou. V C začíná indexování hodnotou [[0]], takže pátý prvek má index 4. Souvislé uložení dovoluje adresu prvku vypočítat a přistoupit k němu přímo.

**Vyber správná tvrzení o poli:**

<!-- data-randomize="true" -->
[[X]] pořadí prvků je významné
[[X]] k prvku se přistupuje indexem
[[X]] klasické pole obsahuje prvky stejného typu
[[X]] index mimo platný rozsah je nebezpečný
[[ ]] první prvek v C má index 1

## Pevná a dynamická velikost

Statické pole má velikost určenou při deklaraci a za běhu ji nezmění. Dynamické pole získává paměť podle potřeby. C používá [[malloc]] k alokaci a [[free]] k uvolnění; opomenutí uvolnění může zanechat paměť obsazenou.

Pythonový `list` se zvětšuje automaticky a může obsahovat i různé typy. Modul `array` naopak poskytuje úspornější pole základních typů. Pohodlí seznamu tedy není totožné s paměťovým modelem statického pole C.

## Ukazatel a vícerozměrné pole

Ukazatel uchovává adresu. V C se název pole v mnoha výrazech chová jako ukazatel na [[první prvek]], takže aritmetika ukazatelů dovoluje přecházet mezi sousedními hodnotami. Tato kontrola je efektivní, ale vyžaduje hlídat hranice.

Matice je nejčastěji dvourozměrné pole s řádky a sloupci. Prvek se vybírá dvojicí indexů. V Pythonu ji lze znázornit vnořenými seznamy. Matice se hodí pro obraz, tabulková data nebo soustavy rovnic, protože [[ (zachovává dvourozměrné uspořádání) | převádí každý prvek na text | neumožňuje přímý přístup ]].
