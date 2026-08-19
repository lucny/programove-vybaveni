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

Stejný dotaz tedy může podle velikosti tabulek, indexů a statistik dostat jiný plán, aniž se změní jeho požadovaný výsledek. Skupiny příkazů jsou užitečná orientace, ne úplná definice všech možností produktu. Jednotlivé databázové produkty používají vlastní dialekty a rozšíření: například `LIMIT` je běžný v PostgreSQL, MySQL a SQLite, zatímco standard zná také `FETCH FIRST`. Při změně databázového systému je nutné ověřit [[dokumentaci]].

## Schéma jako pravidla

`CREATE TABLE` nepopisuje pouze sloupce, ale také klíče, výchozí hodnoty a omezení. `ON DELETE CASCADE` může automaticky smazat závislé řádky, proto se musí používat [[vědomě]].

Například tabulka účasti může po odstranění rezervace ztratit navázané řádky, zatímco použitou učebnu bez povolené kaskády nelze jednoduše odstranit. Kaskáda je užitečná jen tehdy, odpovídá-li významu vztahu; jinak může odstranit více dat, než uživatel čekal. Změny schématu se v provozu verzují pomocí [[migrací]], testují na kopii dat a nasazují s plánem návratu. I zdánlivě jednoduchý `ALTER TABLE` může nad velkou tabulkou trvat dlouho nebo blokovat práci ostatních.

## Změny dat

`INSERT` přidává řádky, `UPDATE` mění a `DELETE` odstraňuje. Před rizikovou změnou je vhodné ověřit stejnou podmínku pomocí SELECT a pracovat v [[transakci]].

U `INSERT` se vyplatí cílové sloupce psát výslovně: kód pak nezávisí na jejich fyzickém pořadí a je čitelnější. Hromadné importy patří do dávkových či specializovaných mechanismů, ne do tisíců ručně sestavených dotazů. Zapomenuté `WHERE` u `UPDATE` či `DELETE` zasáhne všechny řádky. Měkké smazání místo fyzického odstranění zachovává historii, ale komplikuje dotazy a samo nenahrazuje audit ani pravidla uchovávání údajů.

**Vyber správné zásady:**

<!-- data-randomize="true" -->
[[X]] u UPDATE kontrolovat WHERE
[[X]] ověřit počet dotčených řádků
[[X]] hromadný import řešit vhodným mechanismem
[[ ]] každou provozní změnu provádět jako superuser

## Server, klient a role

Databázový server ověřuje uživatele, plánuje dotazy a řídí souběh. Klient může být DBeaver, pgAdmin, příkazová řádka nebo aplikace.

DBA spravuje provoz, ale aplikační účet má dodržovat princip nejmenších [[oprávnění]].

Server přijímá spojení, ověřuje uživatele, plánuje dotazy, řídí souběh a ukládá data. Klient je jen nástroj, například administrační program, příkazová řádka nebo webová aplikace s ovladačem; grafické rozhraní pravidla nevynucuje. DBA se stará o účty, oprávnění, zálohy, obnovu, aktualizace, výkon i dostupnost. Název superuživatele závisí na produktu a aplikace nemá běžet s nejvyššími právy.

## Praktická bezpečnost změn

Každá změna dat má být čitelná a ověřitelná. Před příkazem, který mění či maže řádky, lze spustit `SELECT` se stejnou podmínkou, zkontrolovat počet výsledků a teprve potom pracovat v transakci. Tento postup omezuje riziko chybného zásahu, ale nenahrazuje vhodně navržená omezení schématu. Při práci ve více aplikacích jsou pravidla vložená přímo do databáze spolehlivější než kontroly ukryté jen v jednom klientovi. Bezpečný provoz proto spojuje přesné SQL, řízené změny schématu a omezená oprávnění.

Při velkém importu je vhodnější [[ dávkové vkládání nebo specializovaný mechanismus | (dávkové vkládání nebo specializovaný mechanismus) | ručně skládané jednotlivé dotazy ]]. Takový postup je čitelnější, lépe měřitelný a nezatěžuje systém zbytečným opakováním stejných kroků.
