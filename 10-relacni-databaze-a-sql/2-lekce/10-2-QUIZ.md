<!--
title: Od požadavků k databázovému schématu – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Čím má začít návrh databáze?**

<!-- data-randomize="true" -->
[(X)] Požadavky, uživateli a obchodními pravidly.
[( )] Tvorbou indexů.
[( )] Volbou názvů SQL funkcí.
[( )] Importem náhodné tabulky.

---

**2. Co je konceptuální návrh?**

<!-- data-randomize="true" -->
[(X)] Popis významu entit a vztahů bez vazby na konkrétní DBMS.
[( )] Nastavení konkrétních indexů.
[( )] Hotový CREATE TABLE skript.
[( )] Záloha databáze.

---

**3. Co je logický návrh?**

<!-- data-randomize="true" -->
[(X)] Převod konceptu do tabulek, atributů, klíčů a omezení.
[( )] Volba fyzického serveru.
[( )] Pouze kresba obrazovky.
[( )] Monitoring výkonu.

---

**4. Co je fyzický návrh?**

<!-- data-randomize="true" -->
[(X)] Volba konkrétních typů, indexů a provozních detailů zvoleného DBMS.
[( )] Formulace uživatelského problému.
[( )] Výběr barev ER diagramu.
[( )] Pouze pojmenování entit.

---

**5. K čemu slouží ER diagram?**

<!-- data-randomize="true" -->
[(X)] K vizualizaci entit, atributů a vztahů.
[( )] K měření výkonu SQL.
[( )] K záloze dat.
[( )] K řízení transakcí.

---

**6. Co je slabá entita?**

<!-- data-randomize="true" -->
[(X)] Entita, jejíž identita závisí na vlastníkovi.
[( )] Tabulka bez dat.
[( )] Tabulka bez cizích klíčů.
[( )] Každá vazební tabulka.

---

**7. Co řeší 1NF?**

<!-- data-randomize="true" -->
[(X)] Jednotlivé hodnoty v polích a odstranění opakujících se skupin.
[( )] Tranzitivní závislosti.
[( )] Pouze indexy.
[( )] Transakce.

---

**8. Co řeší 2NF?**

<!-- data-randomize="true" -->
[(X)] Částečné závislosti na části složeného klíče.
[( )] Všechny cizí klíče.
[( )] Pouze NULL.
[( )] Šifrování.

---

**9. Co řeší 3NF?**

<!-- data-randomize="true" -->
[(X)] Tranzitivní závislosti neklíčových atributů.
[( )] Pouze složené primární klíče.
[( )] Datové typy.
[( )] Replikaci.

---

**10. Která omezení lze zapsat přímo do schématu?**

<!-- data-randomize="true" -->
[[X]] PRIMARY KEY
[[X]] FOREIGN KEY
[[X]] UNIQUE
[[X]] NOT NULL
[[X]] CHECK
[[ ]] ORDER BY


# 2. Interaktivní shrnutí kapitoly

## Návrh před SQL

Databáze začíná otázkou, co má systém umět a která pravidla nesmí porušit. Konceptuální návrh zachycuje význam, logický návrh tabulky a [[klíče]], fyzický návrh konkrétní typy, indexy a provozní nastavení.

## ER diagram

ER diagram je mapa entit, atributů a [[vztahů]]. Notace crow's foot vyjadřuje kardinalitu a povinnost účasti. Diagram má sloužit jako nástroj diskuse ještě před vytvořením databáze.

Slabá entita nemá úplnou identitu bez svého [[vlastníka]].

## Normalizace

1NF odstraňuje opakující se skupiny a vyžaduje jednu hodnotu v jedné pozici. 2NF řeší částečné závislosti na části složeného [[klíče]]. 3NF odstraňuje tranzitivní závislosti.

Normalizace není soutěž o největší počet tabulek; cílem je omezit redundanci a anomálie.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] seznam účastníků není vhodné ukládat jako jeden textový řetězec
[[X]] denormalizace může být vědomým výkonovým kompromisem
[[X]] funkční závislosti vyjadřují, na čem údaj závisí
[[ ]] 3NF znamená, že tabulka musí mít právě tři sloupce

## Omezení

`PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL` a [[CHECK]] převádějí pravidla do databáze. Pravidlo vynucené jen ve formuláři lze jinou aplikací nebo importem obejít.
