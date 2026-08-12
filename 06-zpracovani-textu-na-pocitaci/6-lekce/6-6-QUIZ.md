<!--
title: Publikace, předtisková příprava a elektronické dokumenty – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co znamená předtisková příprava?**

<!-- data-randomize="true" -->
[(X)] Kontrolu a přípravu dokumentu pro konkrétní tiskový proces.
[( )] Pouze napsání textu.
[( )] Automatickou publikaci na web.
[( )] Převod textu na zvuk.

---

**2. Co může být potřeba před tiskem zkontrolovat?**

<!-- data-randomize="true" -->
[[X]] rozměr stránky
[[X]] spadávku
[[X]] barevný prostor
[[X]] fonty
[[X]] rozlišení obrázků
[[ ]] pouze název souboru

---

**3. Co je spadávka?**

<!-- data-randomize="true" -->
[(X)] Přesah grafiky za finální ořez stránky.
[( )] Mezera mezi dvěma slovy.
[( )] Povinná prázdná stránka.
[( )] Typ fontu.

---

**4. Co historicky představuje PostScript?**

<!-- data-randomize="true" -->
[(X)] Stránkový popisovací jazyk důležitý pro digitální tiskový workflow.
[( )] Zvukový kodek.
[( )] Formát e-knih.
[( )] Databázový jazyk.

---

**5. Co charakterizuje reflowable e-knihu?**

<!-- data-randomize="true" -->
[(X)] Text se přizpůsobuje velikosti displeje a nastavení čtenáře.
[( )] Každá stránka má pevnou velikost jako PDF.
[( )] Neobsahuje skutečný text.
[( )] Je určena jen pro tisk.

---

**6. Který formát je typický pro reflowable e-knihy?**

<!-- data-randomize="true" -->
[(X)] EPUB
[( )] BMP
[( )] WAV
[( )] EXE

---

**7. Co podporuje přístupnost dokumentu?**

<!-- data-randomize="true" -->
[[X]] sémantické nadpisy
[[X]] alternativní text obrázků
[[X]] správné pořadí čtení
[[X]] dostatečný kontrast
[[ ]] výhradně barevné rozlišení významu

---

**8. Co znamená single source of truth v publikačním workflow?**

<!-- data-randomize="true" -->
[(X)] Jeden řízený zdroj obsahu slouží pro více výstupů.
[( )] Každý výstup se ručně přepisuje.
[( )] Používá se jediný font.
[( )] Dokument smí mít jen jednu kapitolu.

---

**9. Co je publikační pipeline?**

<!-- data-randomize="true" -->
[(X)] Řetězec kroků od zdroje přes transformace k výsledným formátům.
[( )] Pouze tiskárna připojená k PC.
[( )] Seznam fontů.
[( )] Jeden PDF soubor.

---

**10. Kdy je vhodné použít DTP místo Markdownu?**

<!-- data-randomize="true" -->
[(X)] Když potřebujeme přesnou vícesloupcovou a tiskovou sazbu.
[( )] Když chceme jednoduchý README.
[( )] Když potřebujeme snadný Git diff.
[( )] Když píšeme krátké technické poznámky.


# 2. Interaktivní shrnutí kapitoly

## Od zdroje k publikaci

Dokument nekončí uložením pracovního souboru. Pro tisk, web, e-knihu nebo archiv se připravují různé [[výstupy]]. Každý má jiné požadavky na formát, barvy, obrázky a přístupnost.

Předtisková příprava kontroluje například rozměr stránky, fonty, spadávku a barevný [[prostor]].

## Tisk a PDF

[[Spadávka]] je přesah grafiky za budoucí ořez, aby po řezání nevznikl bílý proužek. PostScript historicky sehrál důležitou roli jako stránkový popisovací jazyk a PDF se stal standardním stabilním výstupem.

Pro profesionální tisk existují profily PDF/X, pro archivaci [[PDF/A]].

## E-knihy a přístupnost

Reflowable e-kniha, typicky [[EPUB]], přizpůsobuje tok textu displeji a preferencím čtenáře. Pevná stránka PDF se naproti tomu chová jinak.

**Vyber prvky přístupného dokumentu:**

<!-- data-randomize="true" -->
[[X]] sémantické nadpisy
[[X]] alternativní text
[[X]] logické pořadí čtení
[[X]] dostatečný kontrast
[[ ]] význam vyjádřený pouze barvou

## Jeden zdroj, více výstupů

Single source of [[truth]] znamená, že jeden řízený zdroj obsahu může vytvořit více publikačních podob. Moderní pipeline může vypadat jako **Markdown → šablona → HTML/PDF/EPUB**.

Nástroj se vybírá podle cíle: Markdown pro jednoduchý strukturovaný zdroj, LaTeX pro odbornou sazbu a [[DTP]] pro přesnou stránkovou kompozici.
