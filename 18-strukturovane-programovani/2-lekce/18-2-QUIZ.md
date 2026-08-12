<!--
title: Proměnné, konstanty a datové typy – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je proměnná?**

<!-- data-randomize="true" -->
[(X)] Pojmenované místo uchovávající hodnotu, která se může měnit.
[( )] Pevná hodnota bez názvu a paměti.
[( )] Funkce bez návratové hodnoty.
[( )] Typ cyklu s podmínkou.

---

**2. Co je konstanta?**

<!-- data-randomize="true" -->
[(X)] Pojmenovaná hodnota, která se po inicializaci nemá měnit.
[( )] Proměnná měněná při každém průchodu cyklu.
[( )] Výjimka vzniklá za běhu.
[( )] Dynamicky načtený modul.

---

**3. Co určuje datový typ?**

<!-- data-randomize="true" -->
[(X)] Povolené hodnoty, paměťovou reprezentaci a smysluplné operace.
[( )] Pouze název proměnné.
[( )] Pořadí funkcí ve zdrojovém souboru.
[( )] Barvu textu v editoru.

---

**4. Které typy patří mezi základní datové typy v kapitole?**

<!-- data-randomize="true" -->
[[X]] int
[[X]] float nebo double
[[X]] char
[[X]] string
[[X]] bool
[[ ]] breakpoint
[[ ]] commit

---

**5. Který typ reprezentuje logickou hodnotu?**

<!-- data-randomize="true" -->
[(X)] bool.
[( )] char.
[( )] double.
[( )] string.

---

**6. Co charakterizuje statické typování?**

<!-- data-randomize="true" -->
[(X)] Typ proměnné je určen deklarací a kontroluje se před či při překladu.
[( )] Typ lze kdykoli libovolně měnit za běhu.
[( )] Proměnné nemají žádný datový typ.
[( )] Každá hodnota musí být textový řetězec.

---

**7. Co charakterizuje dynamické typování?**

<!-- data-randomize="true" -->
[(X)] Typ je spojen s aktuální hodnotou a může se za běhu změnit.
[( )] Typ musí být vždy napsán před názvem proměnné.
[( )] Jazyk nepodporuje číselné hodnoty.
[( )] Každá chyba je zachycena kompilátorem.

---

**8. Které jazyky text uvádí jako staticky typované?**

<!-- data-randomize="true" -->
[[X]] C
[[X]] C++
[[X]] Java
[[X]] C#
[[ ]] Python
[[ ]] Ruby

---

**9. Jak se v C deklaruje konstanta?**

<!-- data-randomize="true" -->
[(X)] Pomocí klíčového slova const.
[( )] Pouze názvem velkými písmeny bez omezení.
[( )] Pomocí příkazu import.
[( )] Pomocí bloku except.

---

**10. Jak se běžně označuje konstanta v Pythonu?**

<!-- data-randomize="true" -->
[(X)] Konvenčně názvem velkými písmeny, bez technického vynucení.
[( )] Klíčovým slovem const, které změnu zakáže.
[( )] Příponou .constant.
[( )] Dekorátorem @immutable povinným v jazyce.


# 2. Interaktivní shrnutí kapitoly

## Hodnota se jménem

Proměnná je pojmenované místo pro hodnotu, která se může v průběhu programu měnit. [[Konstanta]] vyjadřuje údaj, jenž má po inicializaci zůstat stejný. Toto rozlišení zvyšuje čitelnost: z kódu je patrné, které hodnoty představují stav a které pevné pravidlo.

V C lze neměnnost vyjádřit klíčovým slovem [[const]]. Python používá konvenci názvu velkými písmeny, ale [[ technicky změnu vždy zakáže | (samotná konvence hodnotu před přepsáním neochrání) | promění hodnotu na komentář ]].

## Typ určuje význam operací

Datový typ neoznačuje jen způsob zobrazení. Vymezuje rozsah hodnot, potřebnou paměť i operace. `int` reprezentuje celá čísla, `float` či `double` desetinná, `char` znak, `string` řetězec a [[bool]] logickou pravdu nebo nepravdu.

**Vyber významově správné dvojice:**

<!-- data-randomize="true" -->
[[X]] počet studentů — celé číslo
[[X]] teplota — desetinné číslo
[[X]] příznak přihlášení — logická hodnota
[[X]] jméno — textový řetězec
[[ ]] odstavec textu — jediný znak char

Nevhodný typ může ztížit kontrolu hodnot nebo znemožnit smysluplnou operaci. Typ je tedy součástí modelu dat.

## Statická a dynamická kontrola

Ve staticky typovaných jazycích jako C, C++, Java či C# se typ proměnné deklaruje a nemění se libovolně za běhu. To umožňuje zachytit řadu neshod už při překladu. Zápis `int vek = 25;` výslovně spojuje proměnnou s typem [[int]].

Python, JavaScript nebo Ruby jsou dynamicky typované. Typ se odvozuje z přiřazené hodnoty a proměnná může později odkazovat na hodnotu jiného typu. Tento přístup je [[ (flexibilnější při psaní, ale část chyb se projeví až za běhu) | vždy rychlejší a bez možnosti typové chyby | totožný se statickou deklarací ]].

Ani jeden model automaticky nezaručuje správný program. Statická kontrola zachytí určitý druh neshod dříve, dynamika usnadňuje pružný zápis; vývojář musí v obou případech rozumět hodnotám a operacím.
