<!--
title: Vytvoření databáze a bezpečné změny dat – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Jaký je základní charakter SQL?**

<!-- data-randomize="true" -->
[(X)] Převážně deklarativní jazyk.
[( )] Výhradně procedurální assembler.
[( )] Grafický formát.
[( )] Pouze skript pro soubory.

---

**2. Do které skupiny patří CREATE TABLE?**

<!-- data-randomize="true" -->
[(X)] DDL
[( )] DCL
[( )] TCL
[( )] Pouze DML

---

**3. Do které skupiny patří INSERT, UPDATE a DELETE?**

<!-- data-randomize="true" -->
[(X)] DML
[( )] DDL
[( )] DCL
[( )] TCL

---

**4. K čemu slouží GRANT a REVOKE?**

<!-- data-randomize="true" -->
[(X)] K řízení oprávnění.
[( )] K tvorbě indexů.
[( )] K filtrování SELECT.
[( )] K záloze.

---

**5. Proč je vhodné u INSERT výslovně uvádět cílové sloupce?**

<!-- data-randomize="true" -->
[(X)] Kód není závislý na jejich fyzickém pořadí a je čitelnější.
[( )] SQL to vždy povinně vyžaduje.
[( )] Jinak nelze vložit čísla.
[( )] Kvůli indexům.

---

**6. Jaké riziko má UPDATE nebo DELETE bez WHERE?**

<!-- data-randomize="true" -->
[(X)] Může změnit nebo odstranit všechny řádky.
[( )] Příkaz se nikdy nespustí.
[( )] Změní pouze první řádek.
[( )] Automaticky provede rollback.

---

**7. Co je měkké smazání?**

<!-- data-randomize="true" -->
[(X)] Označení záznamu jako neaktivního či zrušeného místo fyzického odstranění.
[( )] Smazání jen poloviny řádku.
[( )] DELETE s LIMIT 1.
[( )] Odstranění indexu.

---

**8. Co je migrace schématu?**

<!-- data-randomize="true" -->
[(X)] Verzovaná změna struktury databáze.
[( )] Export CSV.
[( )] Přesun uživatele mezi rolemi.
[( )] Zálohování.

---

**9. O co se stará DBA?**

<!-- data-randomize="true" -->
[[X]] účty a oprávnění
[[X]] zálohy a obnova
[[X]] aktualizace
[[X]] výkon a dostupnost
[[ ]] grafický design aplikace jako hlavní role

---

**10. Jaká oprávnění má mít běžný aplikační účet?**

<!-- data-randomize="true" -->
[(X)] Pouze ta, která skutečně potřebuje.
[( )] Vždy superuživatelská.
[( )] Právo DROP na všechny databáze.
[( )] Žádná, ani pro vlastní tabulky.


# 2. Interaktivní shrnutí kapitoly

## SQL a jeho skupiny

SQL je převážně [[deklarativní]]: popisujeme, čeho chceme dosáhnout, zatímco optimalizátor volí plán provedení. DDL definuje strukturu, DML pracuje s daty, DCL s oprávněními a TCL s [[transakcemi]].

Jednotlivé databázové produkty používají vlastní dialekty a rozšíření.

## Schéma jako pravidla

`CREATE TABLE` nepopisuje pouze sloupce, ale také klíče, výchozí hodnoty a omezení. `ON DELETE CASCADE` může automaticky smazat závislé řádky, proto se musí používat [[vědomě]].

Změny schématu se v provozu verzují pomocí [[migrací]] a testují.

## Změny dat

`INSERT` přidává řádky, `UPDATE` mění a `DELETE` odstraňuje. Před rizikovou změnou je vhodné ověřit stejnou podmínku pomocí SELECT a pracovat v [[transakci]].

**Vyber správné zásady:**

<!-- data-randomize="true" -->
[[X]] u UPDATE kontrolovat WHERE
[[X]] ověřit počet dotčených řádků
[[X]] hromadný import řešit vhodným mechanismem
[[ ]] každou provozní změnu provádět jako superuser

## Server, klient a role

Databázový server ověřuje uživatele, plánuje dotazy a řídí souběh. Klient může být DBeaver, pgAdmin, příkazová řádka nebo aplikace.

DBA spravuje provoz, ale aplikační účet má dodržovat princip nejmenších [[oprávnění]].
