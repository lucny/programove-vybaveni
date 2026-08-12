<!--
title: Principy vektorové grafiky – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Jak vektorový obraz reprezentuje grafiku?**

<!-- data-randomize="true" -->
[(X)] Pomocí geometrických objektů a jejich vlastností.
[( )] Výhradně mřížkou barevných pixelů.
[( )] Pouze fotografickými texturami.
[( )] Seznamem tiskových bodů DPI.

---

**2. Které objekty mohou být součástí vektorové grafiky?**

<!-- data-randomize="true" -->
[[X]] body
[[X]] úsečky
[[X]] křivky
[[X]] text
[[X]] mnohoúhelníky
[[ ]] pouze bitmapové pixely

---

**3. Proč lze vektorový objekt dobře škálovat?**

<!-- data-randomize="true" -->
[(X)] Jeho geometrický popis není vázán na pevnou mřížku pixelů.
[( )] Vždy obsahuje nekonečný počet pixelů.
[( )] Používá pouze černou a bílou.
[( )] Každé zvětšení přidá skutečný detail fotografie.

---

**4. Co je path?**

<!-- data-randomize="true" -->
[(X)] Cesta složená z geometrických segmentů a příkazů.
[( )] Barevný profil dokumentu.
[( )] Rastrová textura.
[( )] Typ komprese SVG.

---

**5. Co znamená rasterizace?**

<!-- data-randomize="true" -->
[(X)] Převod geometrického popisu na pixely výsledného zařízení.
[( )] Převod fotografie na Bézierovy křivky.
[( )] Komprese SVG do ZIP.
[( )] Změna barevného prostoru.

---

**6. Co řeší antialiasing?**

<!-- data-randomize="true" -->
[(X)] Vyhlazuje schodovité hrany při rasterizaci.
[( )] Zvyšuje počet vektorových uzlů.
[( )] Nahrazuje dithering.
[( )] Převádí text na křivky.

---

**7. Co je vektorizace?**

<!-- data-randomize="true" -->
[(X)] Odhad geometrie z rastrového obrazu.
[( )] Převod SVG na PNG.
[( )] Změna tloušťky obrysu.
[( )] Nastavení rozlišení monitoru.

---

**8. Kde se vektorová grafika typicky používá?**

<!-- data-randomize="true" -->
[[X]] loga
[[X]] ikony
[[X]] mapy
[[X]] diagramy
[[X]] technické výkresy
[[ ]] výhradně digitální fotografie

---

**9. Co je SVG?**

<!-- data-randomize="true" -->
[(X)] Otevřený vektorový webový formát založený na XML.
[( )] Výhradně rastrový formát.
[( )] Tiskový kodek bez struktury.
[( )] Pouze proprietární formát Adobe.

---

**10. Co platí o PDF?**

<!-- data-randomize="true" -->
[(X)] Může kombinovat vektorovou grafiku, text i rastry.
[( )] Je vždy čistě vektorové.
[( )] Nemůže obsahovat text.
[( )] Je určeno jen pro CAD.


# 2. Interaktivní shrnutí kapitoly

## Objekty místo pixelové mřížky

Vektorová grafika ukládá [[geometrii]] objektů a jejich atributy, například výplň, obrys, průhlednost nebo gradient. Kružnice tak může být popsána středem a poloměrem místo milionu pixelů.

Výhodou je samostatná editovatelnost objektů a škálování bez klasické [[pixelizace]]. Dokument ale může obsahovat vložené rastry nebo efekty, takže ne každý prvek je automaticky nezávislý na rozlišení.

## Cesty a souřadnice

Vektorový objekt používá souřadnice `(x,y)`. Složitější tvar bývá popsán jako [[path]] tvořený segmenty a uzly. U SVG se lze setkat s příkazy `M`, `L`, `C` a `Z`.

Anchor point neboli [[uzel]] definuje část geometrie. Otevřená cesta se používá hlavně pro obrys, uzavřená může mít výplň.

## Rasterizace a vektorizace

Monitor je pixelové zařízení, takže vektor musí být při zobrazení [[rasterizován]]. Antialiasing zjemňuje hrany tím, že hraničním pixelům přiděluje mezilehlé hodnoty.

Dithering řeší jiný problém: napodobuje chybějící tóny nebo barvy při omezené [[paletě]].

**Vyber správná tvrzení:**

<!-- data-randomize="true" -->
[[X]] rasterizace převádí geometrii na pixely
[[X]] antialiasing vyhlazuje hrany
[[X]] vektorizace odhaduje geometrii z rastru
[[ ]] vektorizace dokonale obnoví původní geometrii fotografie

## Použití a formáty

SVG je strukturovaný XML dokument, který lze stylovat CSS a měnit pomocí JavaScriptu. [[PDF]] může kombinovat text, vektory i rastry. AI je pracovní formát Illustratoru, EPS historický PostScriptový formát a [[DXF]] výměnný formát pro CAD.

Při převodu mezi formáty se nemusí zachovat všechny vrstvy, efekty a typy [[objektů]].
