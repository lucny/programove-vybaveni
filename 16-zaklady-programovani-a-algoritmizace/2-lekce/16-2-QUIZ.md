<!--
title: Vývoj programování a úrovně jazyků – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Jak se programoval počítač ENIAC?**

<!-- data-randomize="true" -->
[(X)] Pomocí přepínačů a kabelů.
[( )] Pomocí webového prohlížeče.
[( )] Výhradně jazykem Python.
[( )] Pomocí virtuálního stroje JVM.

---

**2. Proč byl přímý zápis strojového kódu obtížný?**

<!-- data-randomize="true" -->
[(X)] Byl nepřehledný, chybový a vázaný na procesor.
[( )] Nepodporoval žádná binární čísla.
[( )] Vyžadoval připojení k internetu.
[( )] Byl příliš podobný přirozenému jazyku.

---

**3. Co přinesl assembler oproti strojovému kódu?**

<!-- data-randomize="true" -->
[(X)] Symbolické názvy instrukcí a adres.
[( )] Úplné odstranění vazby na hardware.
[( )] Automatickou tvorbu grafického rozhraní.
[( )] Zápis programů přirozenou češtinou.

---

**4. Které přínosy měly vyšší programovací jazyky?**

<!-- data-randomize="true" -->
[[X]] vyšší produktivita vývoje
[[X]] lepší čitelnost a údržba
[[X]] větší přenositelnost programů
[[ ]] povinný binární zápis
[[ ]] silnější vazba na jediný procesor

---

**5. Která vlastnost je typická pro nižší jazyky?**

<!-- data-randomize="true" -->
[(X)] Přímější kontrola hardwaru a silnější vazba na architekturu.
[( )] Úplné skrytí všech hardwarových detailů.
[( )] Použití pouze pro tvorbu dokumentů.
[( )] Stejný strojový kód na každém procesoru.

---

**6. Jaký vztah bývá mezi instrukcí assembleru a strojovou instrukcí?**

<!-- data-randomize="true" -->
[(X)] Jedna assemblerová instrukce často odpovídá jedné strojové.
[( )] Jedna assemblerová instrukce vždy vytvoří celý program.
[( )] Assembler neobsahuje instrukce procesoru.
[( )] Strojová instrukce se skládá z mnoha jazyků.

---

**7. Proč jsou vyšší jazyky obvykle produktivnější?**

<!-- data-randomize="true" -->
[(X)] Jedna srozumitelnější konstrukce může skrýt více nízkoúrovňových operací.
[( )] Programátor v nich musí zapisovat adresy každého bajtu.
[( )] Nevyžadují žádná pravidla syntaxe.
[( )] Vždy automaticky vytvoří optimální algoritmus.

---

**8. Jak kapitola hodnotí zařazení jazyků C a C++?**

<!-- data-randomize="true" -->
[(X)] Stojí do určité míry na pomezí nižší a vyšší úrovně.
[( )] Jsou čistě značkovacími jazyky.
[( )] Patří výhradně mezi databázové jazyky.
[( )] Nemohou pracovat blízko hardwaru.

---

**9. Podle kterých hledisek lze moderní jazyky rozdělovat?**

<!-- data-randomize="true" -->
[[X]] oblast použití
[[X]] programovací paradigma
[[X]] úroveň abstrakce
[[X]] syntaktická struktura
[[ ]] barva ikony editoru
[[ ]] velikost monitoru

---

**10. Co má rozhodovat o volbě programovacího jazyka?**

<!-- data-randomize="true" -->
[(X)] Účel, výkon, přenositelnost, bezpečnost a zkušenost týmu.
[( )] Pouze délka názvu jazyka.
[( )] Jen rok vzniku prvního překladače.
[( )] Výhradně počet klíčových slov.


# 2. Interaktivní shrnutí kapitoly

## Od kabelů k symbolickému zápisu

První počítače se obtížně přizpůsobovaly novým úlohám. ENIAC se programoval přepínači a kabely, později se instrukce zapisovaly přímo jako [[strojový kód]]. Takový zápis byl chybový a pevně svázaný s konkrétním procesorem.

Assembler nahradil binární posloupnosti mnemotechnickými názvy. Programátor získal čitelnější zápis, ale jazyk zůstal [[ zcela nezávislý na procesoru | (blízký konkrétní architektuře) | určený jen k úpravě textu ]].

## Vyšší úroveň znamená více abstrakce

Vyšší jazyky skrývají část hardwarových detailů a dovolují jednou konstrukcí vyjádřit více operací. Vývojář se tak může více soustředit na problém, kód bývá čitelnější a přenositelnější. K historicky významným jazykům patří Fortran, COBOL, Pascal a [[C]].

**Vyber typické vlastnosti vyšších jazyků:**

<!-- data-randomize="true" -->
[[X]] srozumitelnější zápis
[[X]] vyšší produktivita vývoje
[[X]] snazší přenos mezi platformami
[[ ]] povinné ruční zadávání binárních instrukcí
[[ ]] vždy přímá závislost na jediném procesoru

Nižší jazyky mají naopak význam tam, kde je potřeba přímá kontrola, vysoká efektivita nebo práce s hardwarem, například u ovladačů či vestavěných systémů. Rozdělení však není absolutní: C a C++ [[ patří pouze mezi nižší jazyky | (kombinují nízkoúrovňové možnosti s prvky vyšší úrovně) | nelze použít pro systémový software ]].

## Jazyky se liší účelem i paradigmatem

Jazyk lze zařadit podle oblasti použití, paradigmatu nebo úrovně abstrakce. JavaScript a PHP se používají na webu, Swift a [[Kotlin]] v mobilním vývoji, Python a R při práci s daty. SQL je doménově zaměřený na databáze a Bash na skriptování systému.

Volba proto není soutěží o jediný nejlepší jazyk. Rozhoduje problém, požadovaný výkon, bezpečnost, přenositelnost i zkušenost týmu. Vhodný jazyk je ten, jehož vlastnosti [[ (odpovídají konkrétním požadavkům) | jsou vždy nejblíže strojovému kódu | mají nejkratší syntaxi bez ohledu na úkol ]].
