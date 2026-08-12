<!--
title: Big data a datové sklady – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co nejlépe charakterizuje big data?**

<!-- data-randomize="true" -->
[(X)] Data, jejichž vlastnosti nutí změnit běžnou architekturu zpracování.
[( )] Každý soubor větší než 1 GB.
[( )] Pouze nestrukturovaná data.
[( )] Data uložená výhradně v cloudu.

---

**2. Které vlastnosti patří mezi známá „V“ big data?**

<!-- data-randomize="true" -->
[[X]] volume
[[X]] velocity
[[X]] variety
[[X]] veracity
[[X]] value
[[ ]] versioning jako povinné šesté V

---

**3. Co je datový sklad?**

<!-- data-randomize="true" -->
[(X)] Analytické úložiště sjednocující historická data z více zdrojů.
[( )] Provozní databáze pouze pro aktuální transakce.
[( )] Pouze složka se zálohami.
[( )] Jiný název pro data lake.

---

**4. Co znamená ETL?**

<!-- data-randomize="true" -->
[(X)] Extract, Transform, Load.
[( )] Evaluate, Transfer, Log.
[( )] Encode, Test, Link.
[( )] Export, Translate, List.

---

**5. Jaký je hlavní rozdíl mezi OLTP a OLAP?**

<!-- data-randomize="true" -->
[(X)] OLTP obsluhuje provozní transakce, OLAP analytické souhrny.
[( )] OLTP je grafová DB, OLAP dokumentová DB.
[( )] OLAP zapisuje jen jednotlivé objednávky.
[( )] Jde o dvě zkratky pro stejný proces.

---

**6. Co označuje drill-down?**

<!-- data-randomize="true" -->
[(X)] Přechod ze souhrnu k většímu detailu.
[( )] Komprimaci databáze.
[( )] Smazání historických dat.
[( )] Přenos do jiného cloudu.

---

**7. Co je batch processing?**

<!-- data-randomize="true" -->
[(X)] Zpracování většího celku dat najednou.
[( )] Vyhodnocování každé události okamžitě.
[( )] Pouze ruční kontrola dat.
[( )] Výhradně komprese obrázků.

---

**8. Co je stream processing?**

<!-- data-randomize="true" -->
[(X)] Průběžné zpracování přicházejících událostí.
[( )] Noční zpracování jedné dávky.
[( )] Archivace starých souborů.
[( )] Zálohování databáze.

---

**9. Jaká rizika může přinášet práce s velkými propojitelnými daty?**

<!-- data-randomize="true" -->
[[X]] znovuidentifikace osob
[[X]] profilování
[[X]] odvozování citlivých vlastností
[[X]] opakování historických nerovností modelem
[[ ]] automatická anonymita všech záznamů

---

**10. Co je pseudonymizace?**

<!-- data-randomize="true" -->
[(X)] Nahrazení přímého identifikátoru jiným, přičemž zpětné spojení může zůstat možné.
[( )] Nevratné odstranění jakékoli možnosti identifikace.
[( )] Komprese osobních údajů.
[( )] Pouze zašifrování síťového přenosu.


# 2. Interaktivní shrnutí kapitoly

## Kdy jsou data „velká“

Big data neurčuje pevná hranice velikosti. Rozhodující je, zda objem, rychlost nebo různorodost nutí změnit běžnou [[architekturu]]. Známá „V“ zahrnují volume, velocity, variety, veracity a value.

Smyslem není shromažďovat vše. Data mají mít známý účel, dobu uchování a očekávanou [[hodnotu]].

## Datový sklad a ETL

Datový sklad neboli [[DWH]] integruje historická data z více zdrojů a sjednocuje jejich význam. ETL znamená extract, transform, [[load]]. ELT přesouvá transformaci až do cílového prostředí.

Faktová tabulka obsahuje měřené události, dimenze například čas, produkt nebo zákazníka. Data lake uchovává širší množství strukturovaných i nestrukturovaných dat, ale bez katalogu a pravidel se může stát datovou [[bažinou]].

## OLTP a OLAP

[[OLTP]] obsluhuje krátké provozní transakce nad aktuálními daty. OLAP čte velká historická data a vytváří agregace. Drill-down znamená přechod do detailu, roll-up naopak do [[souhrnu]].

Oddělení provozní a analytické zátěže chrání výkon produkčního systému.

## Batch, stream a distribuované zpracování

Batch processing zpracuje větší celek najednou. [[stream]] processing vyhodnocuje události průběžně. Distribuované platformy jako Apache Spark rozdělují výpočet mezi více uzlů.

**Vyber správná použití stream processingu:**

<!-- data-randomize="true" -->
[[X]] detekce podvodu
[[X]] monitoring sítě
[[X]] řízení výroby
[[ ]] měsíční archiv uložený bez časového požadavku

## Soukromí a zneužití

Propojením velkých dat lze někdy znovu rozpoznat člověka nebo odvodit citlivé vlastnosti. [[pseudonymizace]] nahrazuje přímý identifikátor, ale možnost zpětného spojení může zůstat. Anonymizace má být nevratná a u bohatých dat je obtížná.

Profilování může ovlivňovat nabídky, úvěry nebo hodnocení rizika. Pokud historická data obsahují nerovnosti, model je může [[opakovat]]. Technická analýza proto musí řešit také soukromí, účel a spravedlivé použití.
