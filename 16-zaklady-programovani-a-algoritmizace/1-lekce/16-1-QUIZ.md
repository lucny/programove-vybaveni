<!--
title: Základní pojmy z programování – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je počítačový program?**

<!-- data-randomize="true" -->
[(X)] Soubor instrukcí určených k vykonání počítačem.
[( )] Libovolný dokument uložený na disku.
[( )] Pouze binární soubor s příponou EXE.
[( )] Seznam hardwarových součástí počítače.

---

**2. Která vlastnost vyjadřuje konečnost algoritmu?**

<!-- data-randomize="true" -->
[(X)] Postup má jasně určený začátek a konec.
[( )] Každý krok může mít více výkladů.
[( )] Postup nesmí přijímat žádná data.
[( )] Výsledek musí být vždy číselný.

---

**3. Které způsoby lze použít pro vyjádření algoritmu?**

<!-- data-randomize="true" -->
[[X]] přirozený jazyk
[[X]] pseudokód
[[X]] vývojový diagram
[[ ]] čas procesoru
[[ ]] přípona souboru

---

**4. Jaký je rozdíl mezi syntaxí a sémantikou programovacího jazyka?**

<!-- data-randomize="true" -->
[(X)] Syntaxe určuje pravidla zápisu, sémantika význam příkazů.
[( )] Syntaxe určuje význam, sémantika pouze vzhled editoru.
[( )] Syntaxe popisuje hardware, sémantika operační systém.
[( )] Jde o dvě označení stejné vlastnosti jazyka.

---

**5. Proč se zdrojový kód vyššího jazyka překládá?**

<!-- data-randomize="true" -->
[(X)] Procesor přímo vykonává strojové instrukce.
[( )] Operační systém přijímá jen přirozený jazyk.
[( )] Překlad přidává programu vstupní data.
[( )] Překlad mění algoritmus na vývojový diagram.

---

**6. Jak obvykle pracuje kompilátor?**

<!-- data-randomize="true" -->
[(X)] Přeloží celý zdrojový kód a vytvoří spustitelný výsledek.
[( )] Vykonává pouze komentáře ve zdrojovém kódu.
[( )] Překládá vždy jediný řádek až při jeho vykonání.
[( )] Převádí strojový kód zpět do přirozeného jazyka.

---

**7. Jak obvykle pracuje interpret?**

<!-- data-randomize="true" -->
[(X)] Překládá a vykonává kód během běhu programu.
[( )] Vytváří výhradně samostatný nativní soubor.
[( )] Slouží pouze ke kreslení vývojových diagramů.
[( )] Kontroluje jen názvy proměnných bez spuštění.

---

**8. Která tvrzení o bytecode odpovídají kapitole?**

<!-- data-randomize="true" -->
[[X]] Je mezikrokem mezi zdrojovým a strojovým kódem.
[[X]] Může jej vykonávat virtuální stroj nebo interpret.
[[X]] Podporuje přenositelnost mezi platformami.
[[ ]] Je totožný s přirozeným jazykem.
[[ ]] Procesor jej vždy vykonává přímo bez prostředí.

---

**9. Které přiřazení oblasti a jazyka je v textu uvedeno správně?**

<!-- data-randomize="true" -->
[(X)] Vědecké výpočty a data – Python nebo R.
[( )] Systémové programování – HTML nebo CSS.
[( )] Mobilní aplikace pro iOS – SQL.
[( )] Webový vývoj – pouze assembler.

---

**10. Jak kapitola klasifikuje HTML a CSS?**

<!-- data-randomize="true" -->
[(X)] Jako značkovací a stylovací jazyk, nikoli plnohodnotné programovací jazyky.
[( )] Jako dva strojové jazyky procesoru.
[( )] Jako kompilátory pro JavaScript.
[( )] Jako varianty bytecode pro web.


# 2. Interaktivní shrnutí kapitoly

## Od problému k programu

Program je uspořádaný soubor instrukcí, které počítač vykonává za určitým cílem. Jeho člověkem čitelný zápis se nazývá [[zdrojový kód]]. Typický program přijme vstup, zpracuje jej podle navrženého postupu a vytvoří výstup; může počítat, řídit hardware, zpracovávat data nebo komunikovat s uživatelem.

Program a algoritmus nejsou totéž. Algoritmus popisuje řešení problému nezávisle na konkrétním jazyce, zatímco program je [[ obecná myšlenka bez zápisu | (implementace postupu v programovacím jazyce) | pouze výsledek výpočtu ]].

## Vlastnosti algoritmu

Použitelný algoritmus musí být konečný a jeho kroky jednoznačné. Může přijímat vstupy a má vytvářet výsledky. Postup lze nejprve zachytit přirozeným jazykem, [[pseudokódem]] nebo vývojovým diagramem a teprve potom převést do kódu.

**Vyber vlastnosti dobře popsaného algoritmu:**

<!-- data-randomize="true" -->
[[X]] má jasně určený postup
[[X]] po konečném počtu kroků skončí
[[X]] poskytuje výstup své činnosti
[[ ]] každý krok lze vyložit libovolně
[[ ]] musí být zapsán pouze v Pythonu

## Jazyk musí být přesný

Přirozený jazyk bývá víceznačný, programovací jazyk proto používá přesná pravidla. [[Syntaxe]] určuje, jak se příkazy zapisují, zatímco [[sémantika]] určuje jejich význam. Různé jazyky se hodí k různým úlohám: C a C++ k systémovému vývoji, Python a R k datům, Swift a Kotlin k mobilním aplikacím.

HTML a CSS se s programovacími jazyky na webu kombinují, ale plní jinou úlohu: HTML je značkovací a CSS [[ programovací | (stylovací) | strojový ]] jazyk.

## Cesta k instrukcím procesoru

Procesor nerozumí přímo vyššímu zdrojovému jazyku. [[Kompilátor]] obvykle překládá celý program do samostatného výsledku, kdežto interpret provádí překlad a vykonávání během běhu. Moderní prostředí mohou oba přístupy kombinovat.

Java se například překládá do [[bytecode]], který vykonává JVM. Podobný mezikrok používá i Python. Přenositelnost pak zajišťuje [[ stejný procesor ve všech zařízeních | (odpovídající virtuální stroj nebo interpret na cílové platformě) | přejmenování zdrojového souboru ]].
