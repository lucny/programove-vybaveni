<!--
title: Markdown: dokument jako jednoduchý čitelný zdrojový text – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Proč Markdown vznikl?**

<!-- data-randomize="true" -->
[(X)] Aby byl zdrojový text čitelný i bez vykreslení.
[( )] Aby nahradil všechny DTP systémy.
[( )] Aby ukládal dokument jako bitmapu.
[( )] Aby zakázal HTML.

---

**2. Jak se v Markdownu běžně zapisuje nadpis první úrovně?**

<!-- data-randomize="true" -->
[(X)] # Nadpis
[( )] **Nadpis**
[( )] <title>Nadpis</title>
[( )] [Nadpis]

---

**3. Které prvky Markdown běžně umí vyjádřit?**

<!-- data-randomize="true" -->
[[X]] nadpisy
[[X]] seznamy
[[X]] odkazy
[[X]] kód
[[ ]] přesné umístění každého znaku na stránce

---

**4. Co znamená sémantika nadpisu v Markdownu?**

<!-- data-randomize="true" -->
[(X)] Úroveň nadpisu vyjadřuje hierarchii dokumentu.
[( )] Jde pouze o velikost písma.
[( )] Určuje barevný profil.
[( )] Je to příkaz k tisku.

---

**5. Co je CommonMark?**

<!-- data-randomize="true" -->
[(X)] Přesněji specifikovaná varianta základní syntaxe Markdownu.
[( )] Editor společnosti Microsoft.
[( )] Formát obrázků.
[( )] LaTeXový balíček.

---

**6. Co přidává GitHub Flavored Markdown?**

<!-- data-randomize="true" -->
[(X)] Například tabulky a task lists.
[( )] Povinnou sazbu v PDF.
[( )] Pouze matematické rovnice.
[( )] Zákaz HTML.

---

**7. Proč se Markdown dobře verzovuje v Gitu?**

<!-- data-randomize="true" -->
[(X)] Je to prostý text a změny lze přesně porovnávat.
[( )] Každý soubor je binární.
[( )] Git ukládá pouze obrázky.
[( )] Markdown nemá řádky.

---

**8. Co označuje docs as code?**

<!-- data-randomize="true" -->
[(X)] Použití postupů vývoje software také pro dokumentaci.
[( )] Automatický překlad dokumentu do strojového kódu.
[( )] Zápis dokumentu pouze v C++.
[( )] Šifrování textu.

---

**9. Co je front matter?**

<!-- data-randomize="true" -->
[(X)] Blok metadat před vlastním obsahem dokumentu.
[( )] První odstavec každé kapitoly.
[( )] Patička PDF.
[( )] Obrázek na titulní straně.

---

**10. Kdy Markdown není ideální?**

<!-- data-randomize="true" -->
[(X)] Když potřebujeme velmi přesnou a složitou stránkovou sazbu.
[( )] Při jednoduché technické dokumentaci.
[( )] Při verzování textu.
[( )] Při psaní README.


# 2. Interaktivní shrnutí kapitoly

## Zdroj, který zůstává čitelný

Markdown používá jednoduché značky, takže dokument je současně zdrojový text i dobře čitelný [[prostý]] text. Nadpis `#` vyjadřuje nejen vzhled, ale také strukturální [[úroveň]].

Obrázky, odkazy, seznamy a bloky kódu lze zapisovat přímo v textu. Alternativní text obrázku je důležitý pro [[přístupnost]].

## Varianty Markdownu

Markdown není jediný dokonale jednotný standard. [[CommonMark]] zpřesňuje základní syntaxi a GitHub Flavored Markdown přidává například tabulky, task lists a přeškrtnutí.

Proto je nutné znát cílový [[renderer]], protože různá prostředí mohou podporovat odlišná rozšíření.

## Obsah a vzhled

Markdown obvykle říká **co prvek znamená**, nikoli přesně jak má vypadat. Vzhled může dodat CSS, šablona nebo sazební systém. Jeden zdroj lze převést například do HTML, DOCX nebo [[PDF]].

Nástroj [[Pandoc]] je známý převody mezi značkovacími a publikačními formáty.

## Git a metadata

Prostý text lze přesně porovnávat v Gitu. Tento přístup se označuje jako docs as [[code]] a umožňuje commit, branch, review i automatické sestavení.

**Vyber výhody Markdownu v Gitu:**

<!-- data-randomize="true" -->
[[X]] čitelný diff
[[X]] snadné verzování
[[X]] automatizovatelný build
[[ ]] přesné ruční umístění každého prvku na stránce

Metadata bývají u některých systémů uložena ve front [[matter]], často v YAML.
