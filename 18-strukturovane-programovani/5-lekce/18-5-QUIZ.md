<!--
title: Modularita, knihovny a hlavičkové soubory – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je modulární program?**

<!-- data-randomize="true" -->
[(X)] Program rozdělený do logicky souvisejících částí s jasnými rolemi.
[( )] Program uložený v jediném dlouhém souboru.
[( )] Program bez funkcí a knihoven.
[( )] Pouze binární modul operačního systému.

---

**2. Které výhody přináší modularita?**

<!-- data-randomize="true" -->
[[X]] lepší organizace
[[X]] znovupoužitelnost
[[X]] týmová spolupráce
[[X]] snazší údržba
[[X]] oddělené testování
[[ ]] povinné propojení každé části se všemi ostatními
[[ ]] odstranění rozhraní

---

**3. Co je programová knihovna?**

<!-- data-randomize="true" -->
[(X)] Kolekce předpřipravených funkcí, tříd a dalších konstrukcí.
[( )] Seznam názvů zdrojových souborů.
[( )] Pouze dokumentace bez kódu.
[( )] Paměťový prostor běžícího procesu.

---

**4. Jaký je rozdíl mezi standardní a externí knihovnou?**

<!-- data-randomize="true" -->
[(X)] Standardní je dodána s jazykem, externí pochází od třetí strany.
[( )] Externí je vždy součástí procesoru.
[( )] Standardní nelze v programu použít.
[( )] Liší se pouze příponou komentářů.

---

**5. Jak se v Pythonu připojuje modul?**

<!-- data-randomize="true" -->
[(X)] Příkazem import.
[( )] Direktivou #include.
[( )] Klíčovým slovem return.
[( )] Operací merge.

---

**6. Jak se v C připojuje hlavičkový soubor?**

<!-- data-randomize="true" -->
[(X)] Direktivou #include.
[( )] Příkazem import.
[( )] Blokem try-except.
[( )] Dekorátorem @property.

---

**7. Co typicky obsahuje hlavičkový soubor .h?**

<!-- data-randomize="true" -->
[(X)] Deklarace funkcí, typů a konstant tvořící rozhraní.
[( )] Pouze výstup z běžícího programu.
[( )] Historii commitů projektu.
[( )] Data uživatele načtená za běhu.

---

**8. Proč se odděluje deklarace a implementace v C?**

<!-- data-randomize="true" -->
[(X)] Rozhraní lze sdílet mezi více částmi a implementaci udržet v .c souboru.
[( )] Aby funkce nemohly mít parametry.
[( )] Aby program nepoužíval knihovny.
[( )] Aby se zrušila kontrola typů.

---

**9. K čemu slouží include guard?**

<!-- data-randomize="true" -->
[(X)] Brání vícenásobnému vložení stejného hlavičkového souboru.
[( )] Zakazuje použití standardní knihovny.
[( )] Automaticky zašifruje zdrojový kód.
[( )] Spouští implementaci při každém importu.

---

**10. Co je modul v Pythonu?**

<!-- data-randomize="true" -->
[(X)] Soubor .py s definicemi funkcí, tříd a proměnných.
[( )] Povinně zkompilovaný soubor .h.
[( )] Samostatný operační systém.
[( )] Výhradně externí knihovna stažená z internetu.


# 2. Interaktivní shrnutí kapitoly

## Program jako sada spolupracujících částí

Modularita rozděluje rostoucí program do logických celků. Každý [[modul]] seskupuje související funkce či typy a zpřístupňuje potřebné rozhraní. Díky tomu lze jednu část změnit nebo testovat bez detailní znalosti všech ostatních.

Rozdělení také podporuje týmovou práci a opětovné použití. Neznamená však vytvořit co nejvíce souborů; hranice mají odpovídat [[ (funkčním odpovědnostem) | náhodnému počtu řádků | názvům jednotlivých proměnných ]].

## Knihovna poskytuje hotové stavební prvky

Knihovna je kolekce připravených funkcí, tříd a konstrukcí. Standardní knihovna je dodána s jazykem a řeší například matematiku, řetězce, soubory či vstup a výstup. Externí knihovnu vytváří třetí strana pro specializovanou oblast.

**Vyber správná přiřazení knihoven jazyka C:**

<!-- data-randomize="true" -->
[[X]] stdio.h — vstup a výstup
[[X]] math.h — matematické funkce
[[X]] string.h — práce s řetězci
[[X]] stdlib.h — malloc, free a další obecné funkce
[[ ]] stdio.h — správa větví Gitu

Použití otestované knihovny omezuje opakované vymýšlení běžných řešení, ale programátor musí rozumět jejímu rozhraní a podmínkám použití.

## Rozhraní a implementace v C

Hlavičkový soubor s příponou [[.h]] obsahuje deklarace, tedy to, co je dostupné. Zdrojový soubor `.c` nese implementaci. Direktivou [[#include]] se rozhraní zpřístupní dalším souborům.

Standardní hlavičky se zapisují v lomených závorkách, vlastní obvykle v uvozovkách. Kombinace `#ifndef`, `#define` a `#endif` tvoří [[include guard]], který brání vícenásobnému zahrnutí stejné hlavičky.

## Pythonový modul

V Pythonu je modulem běžný soubor `.py`. Celý se připojí `import matematika`, případně lze vybrat konkrétní jméno pomocí `from matematika import secti`. První zápis ponechává viditelné, z kterého modulu funkce pochází; druhý ji zpřístupní přímo.

V obou jazycích je společná hlavní myšlenka: [[ (oddělit veřejné rozhraní od vnitřního uspořádání) | spojit všechen kód do jediného globálního prostoru | zrušit závislosti mezi soubory bez náhrady ]].
