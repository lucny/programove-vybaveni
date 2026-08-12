<!--
title: Podprogramy, funkce a rozsah proměnných – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je podprogram?**

<!-- data-randomize="true" -->
[(X)] Samostatný blok kódu plnící vymezenou úlohu.
[( )] Každý zdrojový soubor bez funkcí.
[( )] Globální proměnná sdílená aplikací.
[( )] Překladač použitého jazyka.

---

**2. Které přínosy mají podprogramy?**

<!-- data-randomize="true" -->
[[X]] znovupoužitelnost
[[X]] lepší přehlednost
[[X]] snazší údržba
[[X]] oddělené testování
[[X]] rozdělení týmové práce
[[ ]] nutné opakování stejného kódu
[[ ]] povinný globální stav

---

**3. Co může funkce přijímat?**

<!-- data-randomize="true" -->
[(X)] Vstupní parametry.
[( )] Pouze globální proměnné.
[( )] Výhradně návratovou hodnotu jiné funkce.
[( )] Jen textové řetězce.

---

**4. K čemu slouží return?**

<!-- data-randomize="true" -->
[(X)] Předává výsledek funkce volajícímu kódu.
[( )] Deklaruje globální proměnnou.
[( )] Spouští cyklus od začátku.
[( )] Importuje knihovnu.

---

**5. Jaký je rozdíl mezi parametrem a argumentem?**

<!-- data-randomize="true" -->
[(X)] Parametr je jméno v definici, argument konkrétní hodnota při volání.
[( )] Argument je v definici a parametr výsledek funkce.
[( )] Jde vždy o dvě označení globální proměnné.
[( )] Parametr existuje pouze u procedur bez vstupu.

---

**6. Co označuje void u funkce v C?**

<!-- data-randomize="true" -->
[(X)] Funkce nevrací hodnotu.
[( )] Funkce nepřijímá žádný parametr za všech okolností.
[( )] Funkce nemá tělo.
[( )] Funkce je globální proměnná.

---

**7. Kde je viditelná lokální proměnná?**

<!-- data-randomize="true" -->
[(X)] Uvnitř bloku nebo funkce, kde byla deklarována.
[( )] Ve všech souborech programu.
[( )] Pouze v operačním systému.
[( )] Ve všech budoucích spuštěních aplikace.

---

**8. Jak dlouho typicky existuje lokální proměnná funkce?**

<!-- data-randomize="true" -->
[(X)] Po dobu konkrétního volání funkce.
[( )] Po celou dobu existence zdrojového souboru.
[( )] Dokud není ručně smazána z disku.
[( )] Ve všech procesech počítače.

---

**9. Jaká rizika přinášejí globální proměnné?**

<!-- data-randomize="true" -->
[[X]] nečekané změny stavu
[[X]] složitější ladění
[[X]] silnější závislosti funkcí
[[X]] konflikty názvů
[[ ]] automatická izolace funkcí
[[ ]] snazší opakované použití

---

**10. Jak lze omezit závislost na globálním stavu?**

<!-- data-randomize="true" -->
[(X)] Předávat potřebné hodnoty parametry a vracet výsledky.
[( )] Přesunout všechny lokální proměnné mimo funkce.
[( )] Používat stejné jméno v každé funkci.
[( )] Zrušit návratové hodnoty.


# 2. Interaktivní shrnutí kapitoly

## Rozdělení práce do funkcí

Podprogram řeší jednu vymezenou část problému a lze jej volat z více míst. V moderních jazycích má nejčastěji podobu [[funkce]]. Rozdělení odstraňuje duplicitu, zlepšuje orientaci a dovoluje testovat malé celky.

Dobrá funkce má srozumitelné jméno a jasné rozhraní. Nemá být pouhým náhodným výřezem kódu, ale [[ (soudržnou operací s vymezeným účelem) | úložištěm všech globálních hodnot | kopií celého programu ]].

## Vstup, výstup a volání

Parametry jsou proměnné uvedené v definici funkce. Při konkrétním volání do nich vstupují [[argumenty]]. Příkaz `return` předává výsledek zpět volajícímu kódu.

Funkce může mít více parametrů, žádný parametr nebo nemusí vracet hodnotu. V C se chybějící návratová hodnota označuje [[void]]. To neznamená, že funkce nic nedělá; může například vypsat pozdrav.

**Vyber správná tvrzení o funkcích:**

<!-- data-randomize="true" -->
[[X]] stejnou funkci lze volat z více míst
[[X]] parametr popisuje vstup v definici
[[X]] argument je konkrétní hodnota při volání
[[X]] návratová hodnota může být použita v dalším výpočtu
[[ ]] každá funkce musí měnit globální proměnnou

## Lokální stav

Lokální proměnná je viditelná jen v odpovídajícím bloku či funkci a při každém volání vzniká její nová instance. Dvě funkce tak mohou mít lokální proměnnou stejného jména bez konfliktu. Po skončení volání lokální stav obvykle [[ (zanikne) | stane se automaticky globálním | uloží se trvale na disk ]].

## Globální stav propojuje vzdálené části

Globální proměnná existuje po dobu běhu programu a může být dostupná více funkcím. Pohodlí však vytváří skryté vazby: není snadné zjistit, která část hodnotu změnila. Funkce závislá na globálním stavu se hůře testuje a znovu používá.

Proto se má globální stav omezovat a data předávat přes [[parametry]] a návratové hodnoty. Tok informací je pak z volání čitelnější a změna jedné části méně překvapí jinou.
