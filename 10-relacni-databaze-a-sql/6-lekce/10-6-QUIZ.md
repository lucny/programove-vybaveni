<!--
title: Transakce, výkon, bezpečnost a provoz – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je transakce?**

<!-- data-randomize="true" -->
[(X)] Logický celek operací potvrzený nebo vrácený jako celek.
[( )] Jeden SELECT bez výjimky.
[( )] Pouze záloha databáze.
[( )] Datový typ.

---

**2. Co znamená atomicita v ACID?**

<!-- data-randomize="true" -->
[(X)] Všechno, nebo nic.
[( )] Každá transakce je okamžitá.
[( )] Data jsou vždy šifrovaná.
[( )] Každý řádek má atomický typ.

---

**3. Co dělá ROLLBACK?**

<!-- data-randomize="true" -->
[(X)] Vrátí nepotvrzené změny transakce.
[( )] Potvrdí změny.
[( )] Vytvoří index.
[( )] Zálohuje databázi.

---

**4. Co je deadlock?**

<!-- data-randomize="true" -->
[(X)] Kruhové čekání transakcí na prostředky držené jinými transakcemi.
[( )] Chybějící index.
[( )] SQL injection.
[( )] Výpadek disku.

---

**5. Co je index?**

<!-- data-randomize="true" -->
[(X)] Pomocná datová struktura urychlující některá vyhledávání.
[( )] Kopie celé databáze.
[( )] Bezplatné zrychlení bez režie.
[( )] Povinný cizí klíč.

---

**6. Jaká je cena indexu?**

<!-- data-randomize="true" -->
[(X)] Zabírá místo a zpomaluje některé zápisy kvůli údržbě.
[( )] Nemá žádnou.
[( )] Zmenšuje tabulku.
[( )] Zakazuje UPDATE.

---

**7. K čemu slouží EXPLAIN?**

<!-- data-randomize="true" -->
[(X)] K zobrazení plánu provedení dotazu.
[( )] K vytvoření dokumentace tabulky.
[( )] K rollbacku.
[( )] K přidání oprávnění.

---

**8. Jaká je základní obrana proti SQL injection?**

<!-- data-randomize="true" -->
[(X)] Parametrizované dotazy a oddělení kódu od dat.
[( )] Ruční spojování vstupu do SQL řetězce.
[( )] Pouhé odstranění apostrofů.
[( )] Spouštění jako superuser.

---

**9. Proč replikace není záloha?**

<!-- data-randomize="true" -->
[(X)] Chybné smazání se může rychle přenést i na repliku.
[( )] Replika nikdy neobsahuje data.
[( )] Záloha musí být vždy CSV.
[( )] Replikace je pouze index.

---

**10. Co patří k bezpečnému provozu databáze?**

<!-- data-randomize="true" -->
[[X]] princip nejmenších oprávnění
[[X]] testované zálohy
[[X]] monitoring
[[X]] parametrizované dotazy
[[X]] správa tajných údajů mimo zdrojový kód
[[ ]] hesla uživatelů v čitelné podobě


# 2. Interaktivní shrnutí kapitoly

## Transakce a ACID

Transakce sdružuje operace do jednoho celku. `COMMIT` změny potvrdí, [[ROLLBACK]] je vrátí. ACID znamená atomicitu, konzistenci, izolaci a trvalost.

Atomicita je princip „[[všechno nebo nic]]“. Izolace řeší souběžné transakce a může mít různé úrovně.

Deadlock je kruhové čekání; databáze jednu transakci obvykle zruší a aplikace musí umět některé operace bezpečně [[opakovat]].

## Indexy a výkon

Index je podobný [[rejstříku]]. Pomáhá určitým dotazům, ale zabírá místo a musí se aktualizovat při zápisech. Pořadí sloupců ve složeném indexu je významné.

`EXPLAIN` ukáže plán a `EXPLAIN ANALYZE` v řadě systémů dotaz také skutečně provede.

## Bezpečnost

SQL injection vzniká, když aplikace skládá příkaz s nedůvěryhodným vstupem. Obrana používá [[parametrizované]] dotazy.

**Vyber správné zásady:**

<!-- data-randomize="true" -->
[[X]] aplikační účet má jen potřebná oprávnění
[[X]] tajné údaje nepatří do zdrojového kódu
[[X]] hesla se ukládají jako odolné solené hashe
[[X]] přenos citlivých dat se chrání
[[ ]] každý uživatel databáze má být superuser

## Záloha a provoz

Replika zvyšuje dostupnost, ale není [[záloha]]. Obnova se musí pravidelně testovat. Monitoring sleduje výkon, zámky, úložiště, chyby a stav záloh.

Aplikace obvykle používá omezený pool [[připojení]] a ORM může pomáhat s mapováním objektů, ale neodstraňuje potřebu rozumět SQL, transakcím a výkonu.
