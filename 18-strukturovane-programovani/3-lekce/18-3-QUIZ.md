<!--
title: Řídicí struktury, podmínky a cykly – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co určují řídicí struktury?**

<!-- data-randomize="true" -->
[(X)] Pořadí a podmínky vykonávání příkazů.
[( )] Datový formát souboru.
[( )] Verzi nainstalované knihovny.
[( )] Rozložení objektů v paměti.

---

**2. Jak se vykonává sekvence?**

<!-- data-randomize="true" -->
[(X)] Příkazy jdou za sebou v zapsaném pořadí.
[( )] Vždy se vybere náhodná větev.
[( )] Blok se opakuje bez podmínky.
[( )] Program skočí na konec souboru.

---

**3. K čemu slouží if-else?**

<!-- data-randomize="true" -->
[(X)] K výběru jedné ze dvou cest podle podmínky.
[( )] K vytvoření funkce se dvěma parametry.
[( )] K pevnému opakování bloku.
[( )] K ukončení každého programu.

---

**4. Kdy je vhodné elif nebo else if?**

<!-- data-randomize="true" -->
[(X)] Při postupném testování více podmínek.
[( )] Při čtení souboru po řádcích.
[( )] Při deklaraci konstanty.
[( )] Při zahrnutí hlavičkového souboru.

---

**5. K čemu slouží ternární operátor?**

<!-- data-randomize="true" -->
[(X)] Ke stručnému výběru jedné ze dvou hodnot.
[( )] K vytvoření tří nezávislých cyklů.
[( )] K zachycení libovolné výjimky.
[( )] K importu tří modulů.

---

**6. Proč se ve větvích switch v C používá break?**

<!-- data-randomize="true" -->
[(X)] Aby se zabránilo nechtěnému pokračování do další větve.
[( )] Aby se program vždy ukončil.
[( )] Aby se podmínka přepočítala dvakrát.
[( )] Aby se vytvořila lokální proměnná.

---

**7. Kdy while zkontroluje podmínku?**

<!-- data-randomize="true" -->
[(X)] Před každým průchodem těla.
[( )] Pouze po posledním průchodu.
[( )] Při překladu a potom nikdy.
[( )] Až po ukončení programu.

---

**8. Jaká vlastnost odlišuje do-while?**

<!-- data-randomize="true" -->
[(X)] Tělo proběhne alespoň jednou, protože podmínka je až na konci.
[( )] Tělo nemůže obsahovat více příkazů.
[( )] Cyklus nemá žádnou ukončovací podmínku.
[( )] Je dostupný v Pythonu přímo stejnou syntaxí jako v C.

---

**9. Kdy se typicky používá for?**

<!-- data-randomize="true" -->
[(X)] Při opakování s předem známým počtem nebo přes posloupnost.
[( )] Výhradně při zpracování výjimek.
[( )] Jen při deklaraci globálních proměnných.
[( )] Při jednorázovém rozhodnutí mezi dvěma hodnotami.

---

**10. Které rozdíly mezi C a Pythonem kapitola uvádí?**

<!-- data-randomize="true" -->
[[X]] C vymezuje bloky závorkami, Python odsazením.
[[X]] C for má explicitní inicializaci, podmínku a krok.
[[X]] Python často používá range pro číselnou posloupnost.
[[ ]] Python má přímý příkaz do-while.
[[ ]] C nepodporuje podmínky.


# 2. Interaktivní shrnutí kapitoly

## Tok začíná sekvencí

Bez rozhodování se příkazy vykonávají postupně: načíst hodnoty, provést výpočet, vypsat výsledek. Takový tok se nazývá [[sekvence]]. Pořadí je významné, protože pozdější příkaz může používat výsledek předchozího.

Řídicí struktury přidávají možnost zvolit cestu nebo opakovat blok. Neurčují, jak jsou data uložena, ale [[ (kdy a za jakých podmínek se příkazy vykonají) | jakou příponu dostane soubor | který překladač se nainstaluje ]].

## Rozhodování podle podmínky

`if` vykoná blok při pravdivé podmínce, `else` poskytne alternativu a `elif` či `else if` umožní testovat více možností. Ternární operátor stručně vybere jednu ze dvou [[hodnot]], ale pro složitou logiku může být méně čitelný.

`switch` nebo pythonovský `match` se hodí při výběru podle jedné hodnoty. V C ukončuje větev obvykle [[break]], jinak může řízení nechtěně pokračovat do další větve.

## Tři podoby opakování

`while` testuje podmínku před tělem, takže blok nemusí proběhnout ani jednou. `do...while` testuje až potom a zaručuje nejméně [[jeden]] průchod. Python jej nemá přímo, ale lze jej napodobit nekonečným cyklem s řízeným `break`.

`for` se používá, když známe počet opakování nebo procházíme posloupnost. C zapisuje inicializaci, podmínku a krok, Python často iteruje přes [[range]] či jiný iterovatelný objekt.

**Vyber vhodnou konstrukci pro situaci:**

<!-- data-randomize="true" -->
[[X]] ověření plnoletosti — if-else
[[X]] pět opakování — for
[[X]] načítání do zadání platné hodnoty — while
[[X]] nabídka podle číselné volby — switch nebo match
[[ ]] deklarace konstanty — do-while

## Podmínka musí směřovat k ukončení

Každý cyklus potřebuje promyšlenou inicializaci, podmínku a aktualizaci stavu. Pokud se stav nikdy nepřiblíží ukončení, vznikne [[nekonečný]] cyklus. Volba konstrukce má vyjádřit záměr: for pro známou posloupnost, while pro opakování řízené podmínkou a větvení pro rozdílné cesty programu.
