<!--
title: Databáze a hromadné zpracování dat – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je DBMS?**

<!-- data-randomize="true" -->
[(X)] Software pro vytváření, zpřístupnění a ochranu databáze.
[( )] Samotná sada tabulek bez software.
[( )] Pouze uživatelský formulář.
[( )] Jiný název pro tabulkový procesor.

---

**2. Co tvoří databázový systém v širším pojetí?**

<!-- data-randomize="true" -->
[(X)] Databáze, DBMS, infrastruktura, pravidla a uživatelé.
[( )] Pouze jeden databázový soubor.
[( )] Jen aplikace a monitor.
[( )] Výhradně SQL dotazy.

---

**3. Co typický DBMS zajišťuje?**

<!-- data-randomize="true" -->
[[X]] dotazování
[[X]] změny dat
[[X]] souběžný přístup
[[X]] oprávnění
[[X]] integritu a obnovu
[[ ]] grafický design webu

---

**4. Co bylo typické pro hierarchické databáze?**

<!-- data-randomize="true" -->
[(X)] Struktura stromu rodičů a potomků.
[( )] Pouze grafové hrany.
[( )] Dokumenty bez vazeb.
[( )] Výhradně sloupcové analytické uložení.

---

**5. Co přinesl relační model oproti navigačním modelům?**

<!-- data-randomize="true" -->
[(X)] Oddělení logického dotazu od fyzického uložení a práci s relacemi.
[( )] Zákaz klíčů a vazeb.
[( )] Pouze stromovou strukturu.
[( )] Nutnost procházet záznamy pevnou cestou.

---

**6. Které datové modely kapitola rozlišuje?**

<!-- data-randomize="true" -->
[[X]] relační
[[X]] dokumentový
[[X]] key-value
[[X]] grafový
[[X]] wide-column jako jiný model v další kapitole
[[ ]] barevný

---

**7. Co je výhodou řádkového uložení?**

<!-- data-randomize="true" -->
[(X)] Efektivní práce s celými záznamy.
[( )] Vždy nejrychlejší analytické součty nad jedním sloupcem.
[( )] Neobsahuje žádné indexy.
[( )] Je totožné s wide-column NoSQL.

---

**8. Co je výhodou sloupcového analytického uložení?**

<!-- data-randomize="true" -->
[(X)] Efektivní čtení vybraných sloupců při agregacích.
[( )] Vždy nejlepší pro jednotlivé transakce.
[( )] Neukládá žádné typy dat.
[( )] Je to totéž co Cassandra.

---

**9. Které role mohou pracovat s databází?**

<!-- data-randomize="true" -->
[[X]] DBA
[[X]] vývojář
[[X]] datový analytik
[[X]] datový inženýr
[[X]] vlastník dat
[[ ]] pouze koncový uživatel

---

**10. Jaké riziko mají hromadné operace?**

<!-- data-randomize="true" -->
[(X)] Chyba může zasáhnout velké množství záznamů najednou.
[( )] Nemohou změnit více než jeden řádek.
[( )] Vždy se automaticky vrátí bez transakce.
[( )] Nemají žádné požadavky na oprávnění.


# 2. Interaktivní shrnutí kapitoly

## Databáze, DBMS a aplikace

Databáze je organizovaná kolekce souvisejících dat. [[DBMS]] je software, který řídí dotazování, změny, souběh, oprávnění, integritu a obnovu. Databázový systém zahrnuje také infrastrukturu, pravidla a uživatele.

Aplikace obvykle neotevírá databázový soubor přímo, ale používá aplikační vrstvu, ověření identity a databázový [[ovladač]] nebo API.

## Vývoj databázových modelů

Hierarchický model používá strom, síťový model umožňuje více vazeb a relační model pracuje s relacemi zobrazovanými jako [[tabulky]]. SQL umožňuje deklarativně popsat, jaký výsledek chceme, bez nutnosti navigovat fyzickou cestou mezi záznamy.

Označení postrelační není jeden model; zahrnuje různé přístupy, které relační model rozšiřují nebo volí jinou reprezentaci.

## Datový model a fyzické uložení

Datový model určuje základní stavební prvky a vztahy. Dokumentový model pracuje s dokumenty, key-value s párem klíč–hodnota a grafový s uzly a [[hranami]].

Řádkové uložení je vhodné pro práci s celými záznamy, zatímco sloupcové analytické uložení pro agregace nad vybranými [[sloupci]].

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] logický datový model není totéž co fyzické uložení
[[X]] sloupcový analytický DBMS není totéž co wide-column NoSQL
[[X]] volba modelu závisí na datech a dotazech
[[ ]] každý osobní seznam musí být serverová databáze

## Role a hromadné operace

[[DBA]] spravuje účty, výkon, zálohy a obnovu. Vývojář vytváří aplikaci a dotazy, analytik zkoumá souhrny a datový inženýr připravuje datové toky.

Hromadné operace jsou silné, protože jedním příkazem změní mnoho záznamů. Stejná síla ale násobí i [[chybu]], proto je nutné ověřit podmínku, oprávnění a možnost návratu.
