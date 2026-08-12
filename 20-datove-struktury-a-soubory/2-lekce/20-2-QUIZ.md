<!--
title: Znakové řetězce v C a Pythonu – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je znakový řetězec?**

<!-- data-randomize="true" -->
[(X)] Posloupnost znaků reprezentující text.
[( )] Vždy jediné číslo v paměti.
[( )] Pole ukazatelů na soubory.
[( )] Regulární výraz bez znaků.

---

**2. Jak je řetězec reprezentován v C?**

<!-- data-randomize="true" -->
[(X)] Jako pole char ukončené nulovým znakem.
[( )] Jako neměnný objekt typu str.
[( )] Jako seznam celých čísel bez konce.
[( )] Jako dvojice klíč-hodnota.

---

**3. Jaký význam má v C znak \0?**

<!-- data-randomize="true" -->
[(X)] Označuje konec řetězce.
[( )] Vkládá viditelnou nulu do textu.
[( )] Odděluje dva zdrojové soubory.
[( )] Mění řetězec na číslo.

---

**4. Která hlavička C obsahuje běžné řetězcové funkce?**

<!-- data-randomize="true" -->
[(X)] string.h.
[( )] stdio.py.
[( )] regex.h.
[( )] array.json.

---

**5. Co vrací strlen?**

<!-- data-randomize="true" -->
[(X)] Počet znaků před nulovým ukončením.
[( )] Velikost cílového bufferu.
[( )] Počet slov oddělených mezerou.
[( )] Adresu posledního znaku.

---

**6. K čemu slouží strcmp?**

<!-- data-randomize="true" -->
[(X)] K lexikografickému porovnání dvou řetězců.
[( )] K připojení řetězce na konec jiného.
[( )] K vyhledání jediného znaku.
[( )] K alokaci paměti pro text.

---

**7. Jaká vlastnost platí pro Python str?**

<!-- data-randomize="true" -->
[(X)] Řetězec je neměnný a úprava vytváří nový řetězec.
[( )] Řetězec je měnitelné pole char s \0.
[( )] Každý znak musí být změněn ukazatelem.
[( )] Typ str nemá vestavěné metody.

---

**8. Co v Pythonu vrátí text[-1]?**

<!-- data-randomize="true" -->
[(X)] Poslední znak řetězce.
[( )] První znak řetězce.
[( )] Délku řetězce minus jedna.
[( )] Chybu při každém použití.

---

**9. Které operace poskytují metody Python řetězce?**

<!-- data-randomize="true" -->
[[X]] upper a lower
[[X]] find
[[X]] split
[[X]] replace
[[X]] strip
[[ ]] malloc
[[ ]] fclose

---

**10. Jaké riziko je výraznější při práci s řetězci v C?**

<!-- data-randomize="true" -->
[(X)] Přetečení bufferu při zápisu bez kontroly kapacity.
[( )] Nemožnost zjistit délku řetězce.
[( )] Automatická změna typu str.
[( )] Povinné použití garbage collectoru.


# 2. Interaktivní shrnutí kapitoly

## Text jako posloupnost znaků

Řetězec reprezentuje text, ale konkrétní paměťový model se mezi jazyky liší. C používá pole prvků `char` ukončené znakem [[\0]]. Funkce pozná konec podle tohoto terminátoru, nikoli automaticky podle velikosti rezervovaného bufferu.

Zápis `"Ahoj!"` nulový znak doplní, takže je potřeba místo i pro něj. Chybějící ukončení nebo zápis za kapacitu pole může způsobit [[ (nesprávné čtení paměti či přetečení bufferu) | automatické zvětšení pole | bezpečné vytvoření nového řetězce ]].

## Funkce knihovny C

Hlavička [[string.h]] poskytuje `strlen` pro délku, `strcpy` pro kopírování, `strcat` pro připojení, `strcmp` pro porovnání a `strchr` pro hledání znaku. `strcmp` nevrací obecně logickou hodnotu; nula znamená shodu a znaménko výsledku vyjadřuje pořadí.

**Přiřaď funkce k operacím:**

<!-- data-randomize="true" -->
[[X]] strlen — délka
[[X]] strcpy — kopírování
[[X]] strcat — spojení
[[X]] strcmp — porovnání
[[X]] strchr — hledání znaku
[[ ]] malloc — převod na velká písmena

Při kopírování a spojování musí mít cílové pole dostatečnou kapacitu; nízkoúrovňová kontrola současně znamená odpovědnost.

## Pythonový objekt str

Python má samostatný typ [[str]] s indexováním, slicingem a metodami. `text[0]` vrací první znak, `text[-1]` poslední a `text[0:4]` vyřízne část. Funkce [[len]] poskytne délku.

Řetězce jsou neměnné. Metoda `replace`, `upper` nebo `strip` původní objekt neupraví, ale vytvoří nový výsledek. `split` rozdělí text na části a `find` hledá podřetězec.

## Kontrola proti pohodlí

C nabízí přímý pohled na paměť a měnitelné pole znaků, ale vyžaduje hlídat terminátor a velikost. Python spravuje paměť automaticky a nabízí vysokoúrovňové metody, ale změna znamená [[ (vytvoření nového řetězce) | přepsání znaků původního objektu | ruční posun nulového terminátoru ]]. Rozdíl ovlivňuje bezpečnost, výkon i styl programu.
