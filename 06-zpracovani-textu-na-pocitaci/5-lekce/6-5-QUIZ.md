<!--
title: LaTeX: programovatelná profesionální sazba – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Na jakém systému je LaTeX postaven?**

<!-- data-randomize="true" -->
[(X)] TeX
[( )] PostScript
[( )] Markdown
[( )] HTML

---

**2. Kdo vytvořil TeX?**

<!-- data-randomize="true" -->
[(X)] Donald Knuth
[( )] Leslie Lamport
[( )] John Gruber
[( )] Tim Berners-Lee

---

**3. Co LaTeX přidává nad TeX?**

<!-- data-randomize="true" -->
[(X)] Vyšší úroveň strukturálních příkazů a dokumentových tříd.
[( )] Pouze grafické rozhraní.
[( )] Výhradně tabulky.
[( )] Kodek pro PDF.

---

**4. Jaký soubor je zdrojem LaTeXu?**

<!-- data-randomize="true" -->
[(X)] Prostý text `.tex`.
[( )] Rastrový `.png`.
[( )] Binární `.exe`.
[( )] Výhradně `.docx`.

---

**5. Které enginy kapitola zmiňuje?**

<!-- data-randomize="true" -->
[[X]] pdfLaTeX
[[X]] XeLaTeX
[[X]] LuaLaTeX
[[ ]] ChromeLaTeX

---

**6. K čemu slouží environment?**

<!-- data-randomize="true" -->
[(X)] K zápisu strukturovaných bloků jako seznam nebo rovnice.
[( )] K uložení barevného profilu.
[( )] Pouze k nastavení fontu.
[( )] K exportu obrázku.

---

**7. V čem je LaTeX zvlášť silný?**

<!-- data-randomize="true" -->
[(X)] V matematické sazbě a rozsáhlých strukturovaných dokumentech.
[( )] V ručním retušování fotografií.
[( )] Ve střihu videa.
[( )] V databázových transakcích.

---

**8. Co určuje document class?**

<!-- data-randomize="true" -->
[(X)] Základní typ a strukturu dokumentu.
[( )] Pouze jazyk textu.
[( )] Bitovou hloubku PDF.
[( )] Síťový protokol.

---

**9. Co je BibTeX/biblatex?**

<!-- data-randomize="true" -->
[(X)] Nástrojový systém pro práci s bibliografií.
[( )] Formát rastrového obrázku.
[( )] TeXový editor kódu.
[( )] Způsob komprese PDF.

---

**10. Proč se LaTeX dobře kombinuje s Gitem?**

<!-- data-randomize="true" -->
[(X)] Zdroj je prostý text a lze verzovat jeho změny.
[( )] Každá stránka je samostatný obrázek.
[( )] Git vyžaduje PDF.
[( )] LaTeX nemá zdrojový soubor.


# 2. Interaktivní shrnutí kapitoly

## TeX a LaTeX

TeX vytvořil Donald [[Knuth]] jako přesný sazební systém. LaTeX, spojený se jménem Leslie Lamport, nad TeXem nabízí vyšší úroveň strukturálních příkazů.

Autor píše například `\section{...}` a šablona rozhoduje o vzhledu. Dokument se tak podobá [[programu]]: zdroj popisuje strukturu a sazební engine vytváří výstup.

## Zdroj a kompilace

Soubor `.tex` je [[prostý]] text. Zpracovat jej mohou například pdfLaTeX, XeLaTeX nebo LuaLaTeX. XeLaTeX a LuaLaTeX jsou zajímavé pro Unicode a moderní OpenType fonty.

Příkazy začínají zpětným lomítkem a složitější bloky používají [[environmenty]].

## Matematika a moduly

LaTeX je velmi silný v matematické [[sazbě]]. Document class určuje základní typ dokumentu, například `article`, `book` nebo `beamer`. Balíčky přidávají funkce; `amsmath` rozšiřuje matematiku a `graphicx` práci s obrázky.

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] Beamer je určen pro prezentace
[[X]] CTAN distribuuje velké množství balíčků
[[X]] LaTeX může automaticky číslovat obrázky a rovnice
[[ ]] LaTeX je rastrový editor

## Reference a bibliografie

Pomocí `\label` a `\ref` lze vytvářet automatické [[reference]]. Bibliografická data lze ukládat v `.bib` souborech a zpracovat pomocí BibTeX nebo biblatex/Biber.

Protože je zdroj textový, výborně se kombinuje s [[Gitem]] a automatickým CI buildem.
