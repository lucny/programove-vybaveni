<!--
title: Další datové struktury a jejich volba – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Podle čeho se má volit datová struktura?**

<!-- data-randomize="true" -->
[(X)] Podle operací, které budeme s daty nejčastěji provádět.
[( )] Pouze podle počtu písmen v názvu.
[( )] Vždy podle největší možné struktury.
[( )] Podle programovacího jazyka bez ohledu na úlohu.

---

**2. Jaké chování má zásobník?**

<!-- data-randomize="true" -->
[(X)] LIFO – poslední vložený prvek odchází první.
[( )] FIFO – první vložený odchází první.
[( )] Náhodný prvek odchází první.
[( )] Prvky nelze odebírat.

---

**3. Která úloha se hodí pro zásobník?**

<!-- data-randomize="true" -->
[(X)] Historie operací funkce Zpět.
[( )] Požadavky obsluhované v pořadí příchodu.
[( )] Vyhledání hodnoty podle klíče.
[( )] Reprezentace silniční sítě.

---

**4. Jaké chování má fronta?**

<!-- data-randomize="true" -->
[(X)] FIFO – první vložený prvek odchází první.
[( )] LIFO – poslední vložený odchází první.
[( )] Každý prvek se obslouží dvakrát.
[( )] Prvky musí být vždy seřazené podle hodnoty.

---

**5. Která úloha se hodí pro frontu?**

<!-- data-randomize="true" -->
[(X)] Tiskové úlohy čekající na zpracování.
[( )] Návrat k poslední editaci.
[( )] Ukládání unikátních ID bez duplicit.
[( )] Hierarchie adresářů.

---

**6. Co charakterizuje množinu?**

<!-- data-randomize="true" -->
[(X)] Uchovává unikátní hodnoty a podporuje rychlé ověření členství.
[( )] Přiřazuje každému klíči jednu hodnotu.
[( )] Zachovává vždy duplicitní prvky.
[( )] Vyjadřuje pouze stromovou hierarchii.

---

**7. Co ukládá slovník?**

<!-- data-randomize="true" -->
[(X)] Dvojice klíč–hodnota.
[( )] Pouze posloupnost bez názvů položek.
[( )] Výhradně unikátní hodnoty bez doprovodných údajů.
[( )] Vrcholy a hrany sítě.

---

**8. Co je kořen stromu?**

<!-- data-randomize="true" -->
[(X)] Výchozí nejvyšší uzel hierarchie.
[( )] Každý list bez potomků.
[( )] Hrana spojující dva grafy.
[( )] Poslední prvek zásobníku.

---

**9. Z čeho se skládá graf?**

<!-- data-randomize="true" -->
[(X)] Z vrcholů a hran vyjadřujících vztahy.
[( )] Pouze z jedné kořenové posloupnosti.
[( )] Z klíčů bez hodnot.
[( )] Z pevného pole stejných znaků.

---

**10. Která přiřazení struktury a úlohy jsou vhodná?**

<!-- data-randomize="true" -->
[[X]] množina — ověření unikátního ID
[[X]] slovník — body podle jména
[[X]] strom — adresářová hierarchie
[[X]] graf — trasy mezi městy
[[ ]] zásobník — pořadí první příchozí první obsloužen
[[ ]] CSV — datová struktura pro funkci Zpět


# 2. Interaktivní shrnutí kapitoly

## Nejprve otázka, potom struktura

Datová struktura není jen nádoba. Ovlivňuje, jak snadno hodnotu najdeme, přidáme, odebereme nebo projdeme. Pole je výhodné pro přímý přístup podle indexu, ale jiný problém může lépe vyjádřit zásobník, množina nebo graf.

Základní návrhová otázka zní: [[ (které operace budu provádět nejčastěji) | kolik názvů struktur znám zpaměti | která struktura je nejnovější ]]. Stejná data lze uložit více způsoby, avšak s jinými důsledky pro algoritmus.

## Posloupnost, zásobník a fronta

Seznam uchovává pořadí a lze jej rozšiřovat. Zásobník používá [[LIFO]]: poslední vložená položka odchází první, což odpovídá historii funkce Zpět nebo volání funkcí. Fronta používá [[FIFO]] a zpracovává požadavky v pořadí příchodu.

**Vyber přirozené příklady struktur:**

<!-- data-randomize="true" -->
[[X]] historie úprav — zásobník
[[X]] tiskové úlohy — fronta
[[X]] naměřené hodnoty v pořadí — seznam
[[X]] čekající požadavky serveru — fronta
[[ ]] poslední změna jako první — FIFO

## Hledání podle hodnoty a klíče

Množina uchovává unikátní hodnoty. Hodí se pro kontrolu členství, odstranění duplicit nebo průnik skupin. Slovník spojuje [[klíč]] s hodnotou, například jméno studenta s počtem bodů.

Obě struktury často používají [[hashování]], aby nemusely při hledání procházet všechny položky. To neznamená, že zachovávají stejné pořadí či stejné operace jako seznam.

## Hierarchie a obecná síť

Strom tvoří uzly ve vztahu rodič–potomek a má [[kořen]]. Přirozeně modeluje adresáře, DOM nebo organizační strukturu. Binární strom omezuje počet potomků uzlu nejvýše na dva.

Graf používá vrcholy a [[hrany]]. Nemusí mít jediný kořen a může vyjádřit silnice mezi městy, sociální vazby nebo počítačovou síť. Strom je zvláštní hierarchické uspořádání, graf obecnější síť vztahů.

## Kombinace podle skutečné úlohy

Pro funkci Zpět zvolíme zásobník, pro příchod požadavků frontu, pro existenci ID množinu, pro hodnotu podle jména slovník, pro složky strom a pro navigaci graf. Skutečný program může struktury kombinovat. Volba je součást algoritmu, protože [[ (organizace dat ovlivňuje jednoduchost i rychlost operací) | všechny struktury mají stejné chování | správný typ lze určit pouze podle počtu prvků ]].
