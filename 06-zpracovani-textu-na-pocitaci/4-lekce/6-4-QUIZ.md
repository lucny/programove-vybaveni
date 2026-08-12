<!--
title: Struktura dokumentu, styly a automatizace – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Proč nestačí nadpis jen ručně zvětšit?**

<!-- data-randomize="true" -->
[(X)] Systém pak nemusí poznat jeho sémantickou roli.
[( )] Velké písmo je zakázané.
[( )] Nadpis nesmí být tučný.
[( )] Ruční velikost vždy poškodí PDF.

---

**2. Co je styl?**

<!-- data-randomize="true" -->
[(X)] Pojmenovaná sada vlastností formátování.
[( )] Jeden konkrétní font.
[( )] Obrázek v záhlaví.
[( )] Typ souboru.

---

**3. Jaké výhody přinášejí styly?**

<!-- data-randomize="true" -->
[[X]] konzistenci
[[X]] globální změnu vzhledu
[[X]] podporu automatického obsahu
[[X]] lepší přístupnost
[[ ]] nutnost ručního formátování každého nadpisu

---

**4. Co je šablona?**

<!-- data-randomize="true" -->
[(X)] Definice základní struktury a stylů dokumentu.
[( )] Pouze prázdný soubor.
[( )] Záloha dokumentu.
[( )] Databázová tabulka.

---

**5. Co umožní správně strukturované nadpisy?**

<!-- data-randomize="true" -->
[(X)] Automatický obsah.
[( )] Automatický převod na obrázek.
[( )] Zrušení číslování.
[( )] Povinný tisk.

---

**6. Proč jsou křížové reference lepší než ručně napsaná čísla?**

<!-- data-randomize="true" -->
[(X)] Po změnách se mohou automaticky přepočítat.
[( )] Vždy vypadají barevněji.
[( )] Nemají vazbu na objekt.
[( )] Fungují pouze v LaTeXu.

---

**7. Které nástroje podporují spolupráci na dokumentech?**

<!-- data-randomize="true" -->
[[X]] komentáře
[[X]] sledování změn
[[X]] historie verzí
[[X]] Git diff
[[ ]] ruční přepis bez historie

---

**8. Co je mail merge?**

<!-- data-randomize="true" -->
[(X)] Hromadné generování personalizovaných dokumentů ze šablony a dat.
[( )] Spojení dvou e-mailových účtů.
[( )] Komprese dokumentu.
[( )] Převod PDF na obrázek.

---

**9. Jaká je vhodná role AI při tvorbě dokumentů?**

<!-- data-randomize="true" -->
[(X)] Navrhovat či transformovat obsah, který člověk a nástroje ověří.
[( )] Automaticky garantovat faktickou správnost.
[( )] Nahrazovat strukturu dokumentu.
[( )] Ignorovat zdroje.

---

**10. Proč je deterministické sestavení dokumentu užitečné?**

<!-- data-randomize="true" -->
[(X)] Odděluje generování obsahu od spolehlivé šablony a validace.
[( )] Zajišťuje náhodný vzhled každé verze.
[( )] Odstraňuje potřebu kontroly.
[( )] Je možné pouze u PDF.


# 2. Interaktivní shrnutí kapitoly

## Sémantická struktura

Dokument má logickou hierarchii: kapitoly, podkapitoly, odstavce, seznamy, tabulky a další prvky. Skutečný nadpis má být označen jako [[nadpis]], nikoli jen ručně zvětšen.

To je důležité pro obsah, převod formátů, vyhledávání i [[přístupnost]].

## Styly a šablony

[[Styl]] je pojmenovaná sada vlastností. Změníme-li styl Nadpis 2, mohou se změnit všechny odpovídající nadpisy najednou. Šablona navíc definuje společnou strukturu, barvy, záhlaví a další pravidla.

Stejnou myšlenku používá CSS a publikační workflow založené na Markdownu nebo [[LaTeXu]].

## Automatické reference

Správná struktura umožňuje generovat obsah, seznam obrázků i křížové [[reference]]. Ručně napsané číslo obrázku se po změně dokumentu může stát chybným.

**Vyber výhody automatických referencí:**

<!-- data-randomize="true" -->
[[X]] přečíslování po vložení objektu
[[X]] menší riziko neaktuálních odkazů
[[X]] lepší práce s rozsáhlým dokumentem
[[ ]] nutnost ručně přepsat každé číslo

## Spolupráce a generování

Textové procesory používají komentáře a sledování změn, Git pracuje s commity a [[diffem]]. Hromadná korespondence propojuje šablonu s datovým zdrojem.

AI může pomoci s návrhem a transformací textu, ale nemá být považována za automatický [[fakt-checker]]. Bezpečný workflow odděluje obsah, šablonu, generátor a validaci.
