<!--
title: Tabulkový procesor jako datová laboratoř – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co označuje adresa B5?**

<!-- data-randomize="true" -->
[(X)] Průsečík sloupce B a řádku 5.
[( )] Pátý list sešitu.
[( )] Rozsah pěti buněk.
[( )] Absolutní odkaz.

---

**2. Jaký je rozdíl mezi hodnotou a formátem buňky?**

<!-- data-randomize="true" -->
[(X)] Formát mění zobrazení, nikoli uloženou hodnotu.
[( )] Formát vždy mění datový typ.
[( )] Hodnota je pouze barva buňky.
[( )] Jde o totéž.

---

**3. Co znamená `$H$1` ve vzorci?**

<!-- data-randomize="true" -->
[(X)] Absolutní odkaz na sloupec H i řádek 1.
[( )] Relativní odkaz.
[( )] Textový řetězec.
[( )] Chybu vzorce.

---

**4. Co je relativní odkaz?**

<!-- data-randomize="true" -->
[(X)] Při kopírování se mění podle nové polohy.
[( )] Je vždy pevně uzamčen.
[( )] Obsahuje vždy znak `$` před sloupcem i řádkem.
[( )] Funguje jen v Excelu.

---

**5. Které funkce patří mezi základní agregační funkce tabulkového procesoru?**

<!-- data-randomize="true" -->
[[X]] SUM
[[X]] AVERAGE
[[X]] MIN
[[X]] MAX
[[X]] COUNT
[[ ]] PRINT

---

**6. K čemu slouží IF?**

<!-- data-randomize="true" -->
[(X)] Vrací různý výsledek podle splnění podmínky.
[( )] Řadí tabulku.
[( )] Vytváří graf.
[( )] Importuje JSON.

---

**7. K čemu slouží kontingenční tabulka?**

<!-- data-randomize="true" -->
[(X)] K rychlému agregovanému pohledu nad daty.
[( )] K ukládání zdrojových obrázků.
[( )] K šifrování sešitu.
[( )] K převodu dat na prostý text.

---

**8. Co se stane při filtrování?**

<!-- data-randomize="true" -->
[(X)] Některé řádky se dočasně skryjí, ale data se nesmažou.
[( )] Řádky se trvale odstraní.
[( )] Vzorce se nahradí hodnotami.
[( )] Tabulka se automaticky seřadí.

---

**9. Co XLSX může uchovávat navíc oproti CSV?**

<!-- data-randomize="true" -->
[[X]] více listů
[[X]] vzorce
[[X]] styly
[[X]] grafy
[[ ]] hierarchický JSON objekt jako základní princip

---

**10. Proč může být JSON před tabulkovou analýzou nutné rozbalit?**

<!-- data-randomize="true" -->
[(X)] Může obsahovat vnořené objekty a seznamy.
[( )] Neobsahuje text.
[( )] Je vždy binární.
[( )] Neumí reprezentovat čísla.


# 2. Interaktivní shrnutí kapitoly

## Buňka a formát

Buňka má adresu, obsah a způsob zobrazení. Hodnotu `0,25` lze zobrazit jako `25 %`, aniž se změní uložené [[číslo]]. Barva buňky proto nemá nahrazovat samostatnou datovou proměnnou.

Je vhodné oddělit list se zdrojovými [[daty]], výpočty a výsledný report.

## Vzorce a odkazy

Vzorec začíná znakem `=` a představuje opakovatelný postup. Relativní odkazy se při kopírování mění, absolutní odkaz například `[[$H$1]]` zůstává pevný.

Smíšený odkaz uzamyká pouze sloupec nebo [[řádek]].

## Funkce a analýza

SUM, AVERAGE, MIN, MAX a COUNT řeší mnoho základních úloh. Podmíněné varianty umožňují agregovat jen řádky splňující kritéria. [[IF]] rozhoduje mezi dvěma výsledky a XLOOKUP doplňuje údaje z jiné tabulky.

Kontingenční tabulka vytváří [[agregovaný]] pohled bez změny původních dat.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] filtr data nemaže
[[X]] řazení musí zachovat celé řádky pohromadě
[[X]] strukturované odkazy mohou být čitelnější než pevné rozsahy
[[ ]] samotná barva buňky je spolehlivý datový typ

## CSV, XLSX a JSON

CSV je jednoduchý [[textový]] formát tabulkových dat, XLSX uchovává celý sešit a JSON umí vnořené objekty. Volba formátu závisí na účelu výměny.
