<!--
title: Rastrový obraz: svět složený z pixelů – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co tvoří rastrový obraz?**

<!-- data-randomize="true" -->
[(X)] Pravidelná mřížka pixelů s číselnou informací o barvě.
[( )] Pouze matematické křivky a objekty.
[( )] Seznam textových instrukcí bez pixelů.
[( )] Výhradně trojrozměrná síť.

---

**2. Proč se při výrazném zvětšení rastru může objevit pixelizace?**

<!-- data-randomize="true" -->
[(X)] Zdrojový obraz má konečný počet vzorků.
[( )] Monitor přestane používat barvy.
[( )] Přípona souboru se změní.
[( )] Alfa kanál se automaticky vypne.

---

**3. Kolik megapixelů má obraz 4000 × 3000 px?**

<!-- data-randomize="true" -->
[(X)] 12 Mpx
[( )] 7 Mpx
[( )] 24 Mpx
[( )] 120 Mpx

---

**4. Co může ovlivnit kvalitu fotografie kromě počtu megapixelů?**

<!-- data-randomize="true" -->
[[X]] velikost snímače
[[X]] objektiv
[[X]] šum
[[X]] dynamický rozsah
[[X]] zaostření
[[ ]] pouze název souboru

---

**5. Co vyjadřuje PPI?**

<!-- data-randomize="true" -->
[(X)] Počet pixelů na palec fyzické délky.
[( )] Počet inkoustových bodů tiskárny.
[( )] Počet bitů na kanál.
[( )] Počet snímků za sekundu.

---

**6. Co vyjadřuje DPI?**

<!-- data-randomize="true" -->
[(X)] Hustotu tiskových bodů zařízení.
[( )] Pixelové rozměry obrázku.
[( )] Počet barevných kanálů.
[( )] Velikost souboru.

---

**7. Kolik hodnot má osmibitový barevný kanál?**

<!-- data-randomize="true" -->
[(X)] 256
[( )] 128
[( )] 512
[( )] 1024

---

**8. Proč se běžnému RGB obrazu se třemi osmibitovými kanály říká 24bitový?**

<!-- data-randomize="true" -->
[(X)] Tři kanály po 8 bitech dávají 24 bitů.
[( )] Má 24 milionů pixelů.
[( )] Používá 24 barev.
[( )] Obsahuje 24 vrstev.

---

**9. K čemu je alfa kanál?**

<!-- data-randomize="true" -->
[[X]] průhlednost
[[X]] částečná viditelnost
[[X]] skládání vrstev
[[X]] maskování
[[ ]] určení rozměrů obrazu

---

**10. Který formát běžně nepodporuje alfa kanál?**

<!-- data-randomize="true" -->
[(X)] JPEG
[( )] PNG
[( )] WebP
[( )] AVIF


# 2. Interaktivní shrnutí kapitoly

## Pixelový obraz

Rastrový obraz je tvořen pravidelnou mřížkou [[pixelů]]. Každý pixel nese číselnou informaci o barvě a případně průhlednosti. Rastrový princip je vhodný pro fotografie, textury, skeny a digitální malbu.

Při zvětšování editor musí vytvářet nové hodnoty. Klasický algoritmus může pouze [[ zachovat pouze původní pixely bez změny | (odhadnout chybějící mezihodnoty) | obnovit původní detail s jistotou ]]. AI super-resolution může vytvářet věrohodné struktury, ale část detailů je syntetická.

## Rozměry a megapixely

Pixelové rozměry zapisujeme jako šířka × výška. Fotografie `4000 × 3000 px` má [[12]] megapixelů. Počet Mpx ale sám neurčuje kvalitu; záleží také na snímači, objektivu, šumu a zpracování.

Ořez odstraňuje část obrazu, zatímco změna velikosti mění počet pixelů a vyžaduje [[resampling]].

## PPI a DPI

[[PPI]] vyjadřuje počet pixelů na palec výsledné délky, zatímco DPI počet tiskových bodů tiskového zařízení. Pro web jsou podstatné hlavně pixelové rozměry a CSS, nikoli metadata „72 DPI“.

Obraz široký 3000 px bude při 300 PPI široký [[10]] palců.

## Bitová hloubka a alfa

Osmibitový kanál má 256 hodnot. Běžný RGB obraz používá tři kanály a proto má 24bitovou barvu. Vyšší bitová hloubka poskytuje při úpravách více mezistupňů a omezuje riziko [[bandingu]].

**Vyber správná tvrzení o alfa kanálu:**

<!-- data-randomize="true" -->
[[X]] řídí průhlednost pixelu
[[X]] umožňuje částečnou viditelnost
[[X]] je důležitý při skládání vrstev
[[ ]] určuje počet megapixelů
[[ ]] JPEG jej běžně používá jako čtvrtý kanál

Alfa může být reprezentována jako straight nebo premultiplied [[alpha]], což může ovlivnit okraje průhledných objektů.
