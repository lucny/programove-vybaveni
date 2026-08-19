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

Bez [[ORDER BY]] není pořadí výsledku zaručeno, i když se při několika spuštěních tváří stejně. V aplikacích je vhodnější vypisovat konkrétní sloupce než bezmyšlenkovitě používat `SELECT *`: výsledek je stabilnější, srozumitelnější a nepřenáší zbytečná data. Omezení počtu řádků pomocí `LIMIT` nebo `FETCH FIRST` potřebuje řazení; jinak není ani stránkování stabilní. Při shodě hodnot musí dotaz určit, podle čeho se řádky dále [[řadí]].

## Podmínky a NULL

SQL nabízí `AND`, `OR`, `NOT`, `IN`, `BETWEEN` a `LIKE`. `NULL` se testuje pomocí [[IS NULL]]. Závorky jsou důležité, protože operátory mají různou prioritu.

`CASE` vytváří podmíněný výraz a [[COALESCE]] hledá první nenulovou hodnotu.

Výrazy mohou počítat délku rezervace, spojovat text nebo vytvářet kategorie. Výpočet s `NULL` obvykle vrací `NULL`, protože výsledek s neznámou hodnotou nelze určit. `COALESCE` se hodí pro náhradní popisek, nesmí však bezmyšlenkovitě zaměnit neznámou kapacitu za nulu — tyto stavy mají jiný význam. Logické pořadí dotazu začíná zdrojem `FROM` a `JOIN`, potom filtruje `WHERE`; proto alias vzniklý v `SELECT` obvykle nelze použít ve `WHERE` stejné úrovně.

## Agregace

COUNT, SUM, AVG, MIN a MAX mění úroveň detailu. `GROUP BY` vytváří skupiny. `WHERE` odstraňuje řádky před agregací, [[HAVING]] filtruje až výsledné skupiny.

Ve výběru seskupeného dotazu mohou být zpravidla jen seskupovací sloupce a agregované výrazy, jinak by nebylo jasné, kterou hodnotu ze skupiny vrátit. `COUNT(*)` počítá všechny řádky, kdežto `COUNT(sloupec)` jen řádky, v nichž daný sloupec není `NULL`. Také `AVG` neznámé hodnoty obvykle ignoruje. Výpočet může být technicky správný, přesto je nutné ověřit jeho [[interpretaci]], zejména když údaje chybějí jen určité skupině.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] COUNT(*) počítá řádky
[[X]] COUNT(sloupec) ignoruje NULL v daném sloupci
[[X]] AVG obvykle ignoruje NULL
[[ ]] DISTINCT je správná oprava každého chybného JOINu

## Poddotazy a CTE

Poddotaz může být součástí jiného dotazu. CTE pomocí `WITH` pojmenuje pomocný výsledek a často zlepší [[čitelnost]]. Není však automaticky rychlejší.

Poddotaz může například zjistit průměrnou kapacitu a vnější dotaz vybrat učebny nad tímto průměrem. CTE platí jen pro jeden dotaz a pomáhá rozdělit delší postup na pojmenované kroky. Optimalizátor ho podle produktu a verze může začlenit přímo do plánu, nebo pomocný výsledek samostatně materializovat. Srozumitelnější zápis tedy není příslibem vyššího výkonu, ale usnadňuje kontrolu správnosti otázky i odpovědi.

## Od otázky k důvěryhodnému výsledku

Dotaz má nejprve přesně určit, jaká data potřebuje, podle čeho je filtruje a jak se budou řadit. Teprve potom má smysl zvažovat omezení počtu výsledků nebo agregaci. `DISTINCT` odstraňuje opakované kombinace pouze ve výsledku; nemá maskovat chybu ve zdroji či budoucím spojení tabulek. Také průměr, minimum nebo počet je třeba interpretovat v kontextu chybějících hodnot. SQL dokáže operace provést správně, ale nemůže samo rozhodnout, zda výsledek odpovídá otázce, kterou uživatel skutečně položil.

Filtr skupin patří do [[ WHERE | (HAVING) | ORDER BY ]], protože se vyhodnocuje až po seskupení. Jasně pojmenované kroky a vhodně zvolená podmínka usnadní ověřit, zda dotaz vrací požadovaný výsledek.
