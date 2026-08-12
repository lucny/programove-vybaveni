<!--
title: Rekurze, výjimky a validace vstupu – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je rekurzivní funkce?**

<!-- data-randomize="true" -->
[(X)] Funkce, která volá sama sebe s jednodušší verzí problému.
[( )] Funkce, která nesmí nic vracet.
[( )] Cyklus bez podmínky ukončení.
[( )] Funkce dostupná pouze z jiného modulu.

---

**2. Proč rekurze potřebuje ukončovací podmínku?**

<!-- data-randomize="true" -->
[(X)] Aby existoval případ řešitelný bez dalšího volání.
[( )] Aby se každé volání zdvojnásobilo.
[( )] Aby funkce vždy použila globální proměnnou.
[( )] Aby se problém při každém kroku zvětšil.

---

**3. Který problém kapitola uvádí jako přirozený pro rekurzi?**

<!-- data-randomize="true" -->
[(X)] Procházení hierarchie složek.
[( )] Jednoduché vypsání čísel 1 až 100.
[( )] Přiřazení jedné hodnoty proměnné.
[( )] Zobrazení pevného textu.

---

**4. Jaký je vztah iterace a rekurze?**

<!-- data-randomize="true" -->
[(X)] Mnoho úloh lze řešit oběma způsoby a volba závisí na povaze problému.
[( )] Rekurze je vždy rychlejší než cyklus.
[( )] Iterace nemůže opakovat výpočet.
[( )] Rekurze je syntaktický název cyklu for.

---

**5. Co je výjimka?**

<!-- data-randomize="true" -->
[(X)] Signál, že operaci nelze dokončit běžným způsobem.
[( )] Každá logická podmínka programu.
[( )] Návratová hodnota úspěšné funkce.
[( )] Komentář upozorňující na možný problém.

---

**6. Jakou úlohu má blok try?**

<!-- data-randomize="true" -->
[(X)] Obsahuje operaci, při níž může vzniknout očekávaná výjimka.
[( )] Definuje cyklus s pevným počtem opakování.
[( )] Zaručuje, že se žádná chyba nestane.
[( )] Automaticky validuje význam každé hodnoty.

---

**7. Co zachytí ValueError při převodu vstupu na int?**

<!-- data-randomize="true" -->
[(X)] Text, který nelze převést na celé číslo.
[( )] Číslo ležící mimo rozumný věkový rozsah.
[( )] Chybějící soubor na disku.
[( )] Úspěšně načtené celé číslo.

---

**8. Proč není vhodný prázdný obecný except?**

<!-- data-randomize="true" -->
[(X)] Může skrýt neočekávanou chybu bez reakce a diagnostiky.
[( )] Zachytí příliš málo druhů chyb.
[( )] Vždy ukončí program před blokem try.
[( )] Nelze jej syntakticky zapsat v Pythonu.

---

**9. Co kontroluje validace vstupu?**

<!-- data-randomize="true" -->
[(X)] Zda získaná hodnota splňuje pravidla a význam požadovaný programem.
[( )] Pouze zda překladač zná název proměnné.
[( )] Zda soubor obsahuje přesně jeden řádek.
[( )] Jen dostupnost procesoru.

---

**10. Které prvky se kombinují při opakovaném načítání známky 1 až 5?**

<!-- data-randomize="true" -->
[[X]] cyklus pro opakování
[[X]] try-except pro převod
[[X]] podmínka pro rozsah
[[X]] break po platné hodnotě
[[ ]] nekontrolovaný GOTO
[[ ]] ignorování chybného typu


# 2. Interaktivní shrnutí kapitoly

## Problém se zmenšuje až k základnímu případu

Rekurzivní funkce volá sama sebe, ale vždy s jednodušší verzí úlohy. U faktoriálu se `n!` převede na `n × (n−1)!`. [[Ukončovací podmínka]] přímo vyřeší nejjednodušší případ a zabrání nekonečnému řetězci volání.

Při návrhu je nutné ověřit dvě věci: kdy se funkce zastaví a zda se problém při každém kroku [[ (skutečně zmenšuje) | vrací beze změny | náhodně zvětšuje ]]. Bez toho program skončí chybou po příliš hluboké rekurzi.

## Rekurze nebo cyklus

Faktoriál lze vypočítat rekurzivně i iterací. Cyklus bývá přímočařejší pro běžné opakování, rekurze přirozeně vyjadřuje hierarchie, například strom složek, kde se stejný postup použije na každou podsložku.

**Vyber situace, které přirozeně podporují rekurzivní pohled:**

<!-- data-randomize="true" -->
[[X]] procházení stromu adresářů
[[X]] zpracování rodokmenu
[[X]] návštěva uzlu a jeho potomků
[[ ]] prosté vypsání čísel od 1 do 10
[[ ]] jednorázový součet dvou hodnot

Volba nemá být vedena dojmem, že rekurze je automaticky pokročilejší a lepší. Rozhoduje srozumitelnost konkrétního řešení.

## Výjimka odděluje neúspěšnou operaci

Převod textu `osmnáct` na celé číslo vyvolá [[ValueError]], chybějící soubor [[FileNotFoundError]]. Kód v `try` se pokusí operaci provést a odpovídající `except` reaguje na konkrétní očekávaný problém.

Obecné `except: pass` je nebezpečné, protože [[ (může skrýt skutečnou chybu) | vždy opraví vstup | převede výjimku na platný výsledek ]]. Zachytávat se mají situace, kterým program rozumí a na které umí reagovat.

## Formát není totéž co význam

Úspěšný převod vstupu ještě neznamená, že je hodnota přijatelná. `-300` je platné celé číslo, ale ne smysluplný věk. [[Validace]] proto kontroluje rozsah nebo další pravidla po převodu.

Robustní vstupní smyčka propojí cyklus, výjimku a podmínku: cyklus opakuje dotaz, `try-except` řeší chybný typ, podmínka ověří rozsah a `break` ukončí zadávání po platné hodnotě. Tok lze shrnout jako [[ (vstup → převod → validace → zpracování) | vstup → ignorování chyby → náhodný výsledek | validace → vstup → překlad programu ]].
