<!--
title: SELECT – od otázky k výsledku – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co dělá SELECT?**

<!-- data-randomize="true" -->
[(X)] Vytváří výslednou tabulku bez změny uložených dat.
[( )] Vždy mění řádky.
[( )] Maže duplicity ve zdroji.
[( )] Vytváří index.

---

**2. K čemu slouží WHERE?**

<!-- data-randomize="true" -->
[(X)] K filtrování jednotlivých řádků.
[( )] K filtrování už hotových skupin.
[( )] K řazení.
[( )] K přejmenování sloupce.

---

**3. K čemu slouží ORDER BY?**

<!-- data-randomize="true" -->
[(X)] K definování pořadí výsledku.
[( )] K seskupení.
[( )] K výběru zdroje.
[( )] K vytvoření cizího klíče.

---

**4. Je pořadí výsledku bez ORDER BY zaručeno?**

<!-- data-randomize="true" -->
[(X)] Ne.
[( )] Ano, vždy podle primárního klíče.
[( )] Ano, podle vložení.
[( )] Ano, abecedně.

---

**5. Jak se testuje NULL?**

<!-- data-randomize="true" -->
[(X)] IS NULL / IS NOT NULL.
[( )] = NULL.
[( )] LIKE NULL.
[( )] NULL = TRUE.

---

**6. Co dělá DISTINCT?**

<!-- data-randomize="true" -->
[(X)] Odstraní duplicitní kombinace ve výsledku.
[( )] Opraví špatný JOIN ve zdroji.
[( )] Odstraní duplicity z tabulky.
[( )] Vytvoří UNIQUE constraint.

---

**7. Co je CASE?**

<!-- data-randomize="true" -->
[(X)] Výraz umožňující vracet různé hodnoty podle podmínek.
[( )] Příkaz pro index.
[( )] Typ JOIN.
[( )] Transakční úroveň.

---

**8. Co dělá COALESCE?**

<!-- data-randomize="true" -->
[(X)] Vrátí první hodnotu, která není NULL.
[( )] Počítá řádky.
[( )] Řadí skupiny.
[( )] Vytváří CTE.

---

**9. Jaký je rozdíl mezi WHERE a HAVING?**

<!-- data-randomize="true" -->
[(X)] WHERE filtruje řádky před seskupením, HAVING skupiny po agregaci.
[( )] Jde o synonyma.
[( )] HAVING řadí.
[( )] WHERE lze použít jen s JOIN.

---

**10. Co je CTE?**

<!-- data-randomize="true" -->
[(X)] Pojmenovaný pomocný výsledek zavedený WITH pro jeden dotaz.
[( )] Trvalá tabulka.
[( )] Index.
[( )] Datový typ.


# 2. Interaktivní shrnutí kapitoly

## SELECT jako otázka

SELECT vytváří výslednou tabulku. `FROM` určuje zdroj, `WHERE` filtr, `ORDER BY` pořadí a `SELECT` výrazy, které chceme zobrazit.

Bez [[ORDER BY]] není pořadí výsledku zaručeno. V aplikacích je vhodnější vypisovat konkrétní sloupce než bezmyšlenkovitě používat `SELECT *`.

## Podmínky a NULL

SQL nabízí `AND`, `OR`, `NOT`, `IN`, `BETWEEN` a `LIKE`. `NULL` se testuje pomocí [[IS NULL]]. Závorky jsou důležité, protože operátory mají různou prioritu.

`CASE` vytváří podmíněný výraz a [[COALESCE]] hledá první nenulovou hodnotu.

## Agregace

COUNT, SUM, AVG, MIN a MAX mění úroveň detailu. `GROUP BY` vytváří skupiny. `WHERE` odstraňuje řádky před agregací, [[HAVING]] filtruje až výsledné skupiny.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] COUNT(*) počítá řádky
[[X]] COUNT(sloupec) ignoruje NULL v daném sloupci
[[X]] AVG obvykle ignoruje NULL
[[ ]] DISTINCT je správná oprava každého chybného JOINu

## Poddotazy a CTE

Poddotaz může být součástí jiného dotazu. CTE pomocí `WITH` pojmenuje pomocný výsledek a často zlepší [[čitelnost]]. Není však automaticky rychlejší.
