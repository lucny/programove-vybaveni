<!--
title: Datové formáty CSV, XML, JSON a YAML – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Proč se používají standardizované datové formáty?**

<!-- data-randomize="true" -->
[(X)] Usnadňují přenositelnost, parsování a spolupráci systémů.
[( )] Zaručují správnost všech uložených hodnot.
[( )] Nahrazují databáze ve všech situacích.
[( )] Odstraňují potřebu kódování textu.

---

**2. Pro jaká data je přirozené CSV?**

<!-- data-randomize="true" -->
[(X)] Pro jednoduché tabulkové záznamy v řádcích a sloupcích.
[( )] Pro hluboce vnořenou stromovou strukturu.
[( )] Pro binární obrazová data.
[( )] Pro objektový kód programu.

---

**3. Jaké omezení má CSV?**

<!-- data-randomize="true" -->
[(X)] Obtížně vyjadřuje hierarchická a vnořená data.
[( )] Nelze jej otevřít v tabulkovém procesoru.
[( )] Nepodporuje textové hodnoty.
[( )] Vždy vyžaduje XML schéma.

---

**4. Jak XML vyjadřuje strukturu?**

<!-- data-randomize="true" -->
[(X)] Hierarchií značek neboli tagů.
[( )] Pouze pořadím hodnot oddělených čárkou.
[( )] Výhradně odsazením bez značek.
[( )] Binárními hlavičkami.

---

**5. Které vlastnosti má XML?**

<!-- data-randomize="true" -->
[[X]] hierarchická struktura
[[X]] vlastní značky
[[X]] možnost validace schématem
[[X]] větší rozvláčnost
[[ ]] pouze ploché tabulky
[[ ]] nativní typ Python str

---

**6. Které hodnoty podporuje JSON?**

<!-- data-randomize="true" -->
[(X)] Objekty, pole, čísla, řetězce, boolean a null.
[( )] Pouze textové řádky bez struktury.
[( )] Libovolné binární objekty bez kódování.
[( )] Výhradně XML tagy.

---

**7. Proč je JSON častý u webových API?**

<!-- data-randomize="true" -->
[(X)] Je lehký, strukturovaný a dobře podporovaný webovými jazyky.
[( )] Je vždy menší než každý jiný formát.
[( )] Umožňuje pouze tabulková data.
[( )] Je přímo vykonáván procesorem.

---

**8. Jak YAML vyjadřuje vnoření?**

<!-- data-randomize="true" -->
[(X)] Odsazením.
[( )] Nulovým znakem.
[( )] Povinnými složenými závorkami.
[( )] Číselným indexem každého řádku.

---

**9. Jakou výhodu má YAML pro konfiguraci?**

<!-- data-randomize="true" -->
[(X)] Je čitelný pro člověka a podporuje komentáře.
[( )] Není citlivý na odsazení.
[( )] Je určen výhradně pro binární data.
[( )] Nemůže obsahovat seznamy.

---

**10. Která volba formátu je přiměřená?**

<!-- data-randomize="true" -->
[(X)] CSV pro plochý export, JSON pro webové API, YAML pro konfiguraci.
[( )] YAML pro zvuk, CSV pro strom dokumentu, JSON pro spustitelný kód.
[( )] XML pouze pro jedinou číselnou hodnotu.
[( )] Jeden formát je nejlepší pro všechny účely.


# 2. Interaktivní shrnutí kapitoly

## Formát je dohoda mezi systémy

Strukturovaný formát umožňuje programům data zapsat a znovu načíst podle společných pravidel. Přináší přenositelnost, čitelnost, [[parsovatelnost]] a interoperabilitu. Nezaručuje však, že hodnoty dávají věcný smysl; to je úloha validace a aplikačních pravidel.

## CSV pro tabulku

CSV ukládá jeden záznam na řádek a pole odděluje čárkou nebo jiným dohodnutým znakem. Je kompaktní a široce podporované, ale obtížně vyjadřuje [[hierarchii]]. Hodí se pro export tabulek, reporty či výměnu databázových záznamů.

CSV se má číst knihovnou, nikoli prostým rozdělením každého řádku podle čárky, protože skutečná data mohou obsahovat oddělovače či uvozovky.

## XML a JSON pro strukturu

XML používá značky a vytváří strom. Je rozšiřitelné, samopopisné a lze je validovat schématem, ale opakované tagy zvětšují objem. Uplatňuje se u dokumentů, konfigurací a starších integračních systémů.

JSON zapisuje objekty a pole kompaktněji. Podporuje řetězce, čísla, boolean, [[null]], objekty a pole. Je běžný ve webových API a v Pythonu se načítá modulem [[json]].

**Vyber vhodné použití formátů:**

<!-- data-randomize="true" -->
[[X]] CSV — jednoduchý tabulkový export
[[X]] XML — dokument s hierarchií a schématem
[[X]] JSON — data webového API
[[X]] YAML — čitelná konfigurace nástroje
[[ ]] CSV — složitý strom s mnoha vnořenými objekty

## YAML pro čitelnou konfiguraci

YAML omezuje počet syntaktických značek a strukturu vyjadřuje [[odsazením]]. Podporuje komentáře a je oblíbený v Dockeru, Kubernetes či CI/CD. Stejná citlivost na odsazení však může být zdrojem chyb.

## Volba podle dat a spotřebitele

Neexistuje univerzálně nejlepší formát. Rozhoduje tvar dat, velikost, čitelnost, validace a podpora v cílových systémech. CSV je ploché, XML výrazné a rozvláčné, JSON lehké pro web a YAML pohodlné pro ruční konfiguraci. Správná otázka zní [[ (kdo data vytváří, kdo je čte a jakou strukturu potřebují) | který formát má nejkratší název | který zápis obsahuje nejvíce značek ]].
