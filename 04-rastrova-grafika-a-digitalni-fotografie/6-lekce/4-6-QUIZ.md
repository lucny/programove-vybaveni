<!--
title: Zpracování, publikace a důvěryhodnost digitální fotografie – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co je RAW soubor?**

<!-- data-randomize="true" -->
[(X)] Soubor s minimálně zpracovanými daty ze snímače a metadaty.
[( )] Hotový obraz totožný s JPEG.
[( )] Vždy bezeztrátově upravený tiskový soubor.
[( )] Výhradně náhled bez původních měření.

---

**2. Co ovlivňuje vyvážení bílé?**

<!-- data-randomize="true" -->
[(X)] Interpretaci barev vzhledem k barvě osvětlení.
[( )] Počet pixelů snímače.
[( )] Délku expozice.
[( )] Ohniskovou vzdálenost.

---

**3. Co znamená barevná teplota světla?**

<!-- data-randomize="true" -->
[(X)] Popis odstínu osvětlení pomocí teploty v kelvinech.
[( )] Teplotu snímače během expozice.
[( )] Počet bitů na kanál.
[( )] Jas monitoru v procentech.

---

**4. Které úpravy patří do běžného RAW workflow?**

<!-- data-randomize="true" -->
[[X]] expozice
[[X]] vyvážení bílé
[[X]] stíny a světla
[[X]] redukce šumu
[[X]] korekce objektivu
[[ ]] fyzické zvětšení snímače

---

**5. Co je EXIF?**

<!-- data-randomize="true" -->
[(X)] Metadata o pořízení fotografie a zařízení.
[( )] Ztrátový obrazový kodek.
[( )] Barevný prostor monitoru.
[( )] Typ fotografického objektivu.

---

**6. Proč metadata sama nejsou nezfalšovatelným důkazem?**

<!-- data-randomize="true" -->
[(X)] Lze je upravit nebo odstranit.
[( )] Nikdy neobsahují čas.
[( )] Jsou vždy šifrovaná.
[( )] Existují jen u RAW.

---

**7. Co je vhodné při exportu pro web?**

<!-- data-randomize="true" -->
[(X)] Přizpůsobit pixelové rozměry, formát a kompresi cílovému použití.
[( )] Vždy ponechat plné rozlišení fotoaparátu.
[( )] Vždy nastavit 72 DPI jako hlavní podmínku.
[( )] Používat pouze TIFF.

---

**8. Co je důležité při exportu pro tisk?**

<!-- data-randomize="true" -->
[(X)] Propojit pixelové rozměry s fyzickou velikostí a barevným workflow.
[( )] Ignorovat PPI.
[( )] Převést vše na GIF.
[( )] Odstranit všechny profily bez ohledu na tiskárnu.

---

**9. Které zásahy mohou vytvářet syntetický obsah?**

<!-- data-randomize="true" -->
[[X]] generativní fill
[[X]] AI outpainting
[[X]] generování detailů při některém upscalingu
[[ ]] běžné načtení EXIF
[[ ]] prosté otočení obrazu

---

**10. Co je při dokumentární nebo důkazní fotografii zásadní u AI zásahů?**

<!-- data-randomize="true" -->
[(X)] Transparentně odlišit korekci od syntézy nového obsahu.
[( )] Považovat každý AI výsledek za původní scénu.
[( )] Odstranit všechna metadata.
[( )] Vždy použít nejsilnější generativní filtr.


# 2. Interaktivní shrnutí kapitoly

## RAW a vyvážení bílé

RAW není hotová fotografie, ale soubor s relativně málo zpracovanými daty ze snímače a metadaty. Výsledný obraz vzniká až při interpretaci a [[demosaicingu]]. RAW proto nabízí větší prostor pro následné úpravy než hotový JPEG.

Vyvážení bílé upravuje interpretaci barev podle osvětlení. Barevná teplota se udává v [[kelvinech]].

## Expozice a lokální úpravy

RAW editor může měnit expozici, stíny, světla, kontrast a barvy nedestruktivně. Neznamená to, že lze obnovit libovolně přepálený nebo zcela ztracený detail; možnosti jsou omezeny zachycenými [[daty]].

Redukce šumu musí hledat kompromis mezi hladkým obrazem a zachováním detailů. Doostření zvyšuje lokální kontrast hran, ale nevytváří jistý původní detail.

## Metadata a správa fotografií

[[EXIF]] může obsahovat čas, model fotoaparátu, expoziční údaje a další informace. Metadata jsou užitečná pro organizaci a dohledání původu, ale lze je měnit a nejsou sama nezfalšovatelným důkazem.

**Vyber vhodné způsoby správy fotografií:**

<!-- data-randomize="true" -->
[[X]] smysluplná metadata
[[X]] zálohy
[[X]] katalogizace
[[X]] zachování kvalitního zdroje
[[ ]] spoléhat pouze na název souboru

## Export a důvěryhodnost

Pro web volíme vhodné pixelové rozměry, formát a kompresi. Pro tisk propojujeme pixelové rozměry, fyzickou velikost, [[PPI]] a správu barev. Pro archiv má smysl uchovat kvalitní zdroj a potřebná metadata.

Generativní AI může obraz doplnit nebo změnit způsobem, který nevychází přímo z původních fotonů. V kreativní grafice je to legitimní, ale v dokumentární a vědecké práci je zásadní rozlišit korekci od [[syntézy]] a zásah transparentně přiznat.
