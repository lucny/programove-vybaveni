<!--
title: Obrazové formáty, velikost a komprese – kvíz
language: cs
-->

# 1. Testovací část

Vyber správnou odpověď nebo všechny správné odpovědi. Pořadí možností se při novém načtení kvízu náhodně mění.

**1. Co určuje obrazový formát?**

<!-- data-randomize="true" -->
[(X)] Uspořádání pixelových dat, metadat a případnou kompresi.
[( )] Pouze příponu souboru.
[( )] Jen fyzickou velikost monitoru.
[( )] Výhradně počet vrstev.

---

**2. Pro jaký obsah je typicky vhodný JPEG?**

<!-- data-randomize="true" -->
[(X)] Fotografie s plynulými změnami.
[( )] Loga s průhledností a ostrými hranami.
[( )] Zdrojový kód.
[( )] Vektorové technické výkresy.

---

**3. Jaké artefakty může mít silně komprimovaný JPEG?**

<!-- data-randomize="true" -->
[[X]] blokování
[[X]] kroužkování kolem hran
[[X]] ztrátu jemných textur
[[X]] barevné rozmazání
[[ ]] automaticky vyšší bitovou hloubku

---

**4. Proč se nedoporučuje opakovaně ukládat pracovní obraz jako JPEG?**

<!-- data-randomize="true" -->
[(X)] Každé další ztrátové uložení může přidat artefakty.
[( )] JPEG se po druhém uložení stane vektorem.
[( )] Při každém uložení zdvojnásobí rozlišení.
[( )] JPEG vždy smaže metadata i při prvním uložení.

---

**5. Které formáty nebo vlastnosti odpovídají kapitole?**

<!-- data-randomize="true" -->
[[X]] PNG — bezeztrátový a vhodný pro ostré hrany
[[X]] GIF — paleta do 256 barev na snímek
[[X]] TIFF — flexibilní profesionální formát
[[X]] PSD — pracovní formát s vrstvami
[[ ]] JPEG — běžný alfa kanál

---

**6. Co je typické pro WebP?**

<!-- data-randomize="true" -->
[(X)] Podporuje ztrátovou i bezeztrátovou kompresi a průhlednost.
[( )] Je pouze nekomprimovaný formát.
[( )] Nepodporuje webové prohlížeče.
[( )] Je výhradně vektorový.

---

**7. Co je výhodou AVIF?**

<!-- data-randomize="true" -->
[(X)] Vysoká kompresní účinnost a podpora moderních vlastností obrazu.
[( )] Vždy nejrychlejší kódování.
[( )] Používá pouze 256 barev.
[( )] Neumí průhlednost.

---

**8. Kolik surových bajtů má přibližně RGB obraz 4000 × 3000 px při 8 bitech na kanál?**

<!-- data-randomize="true" -->
[(X)] 36 000 000 B
[( )] 12 000 000 B
[( )] 96 000 000 B
[( )] 288 000 000 B

---

**9. Co znamená resampling?**

<!-- data-randomize="true" -->
[(X)] Přepočet hodnot pixelů při změně pixelových rozměrů.
[( )] Pouhou změnu metadata PPI bez pixelů.
[( )] Převod rastru na vektor.
[( )] Odstranění EXIF.

---

**10. Která metoda je vhodná pro zvětšení pixel artu se zachováním tvrdých hran?**

<!-- data-randomize="true" -->
[(X)] Nearest neighbour
[( )] Bicubic
[( )] Lanczos jako jediná možnost
[( )] AI generative fill


# 2. Interaktivní shrnutí kapitoly

## Formát a pracovní soubor

Obrazový formát určuje, jak jsou v souboru uspořádána pixelová data, metadata a komprese. Pracovní formát editoru může uchovávat vrstvy a masky, zatímco exportní formát je optimalizován pro konkrétní [[použití]].

JPEG je typický distribuční formát fotografie, zatímco PSD nebo XCF uchovávají strukturu rozpracovaného dokumentu.

## JPEG a další klasické formáty

JPEG používá ztrátovou kompresi. Kvantování odstraňuje část informace a při silné kompresi se objeví [[artefakty]]. Opakované ukládání JPEG může ztrátu kumulovat.

PNG používá [[bezeztrátovou]] kompresi a podporuje průhlednost. GIF má paletu nejvýše 256 barev na snímek. TIFF je flexibilní a může používat různé kompresní režimy.

## Moderní webové formáty

[[WebP]] i AVIF mohou podporovat ztrátové i bezeztrátové režimy. AVIF nabízí vysokou kompresní účinnost, průhlednost, HDR a vyšší bitové hloubky, ale kódování může být náročnější.

**Pro efektivní webový obraz je důležité:**

<!-- data-randomize="true" -->
[[X]] vhodná pixelová velikost
[[X]] vhodný formát
[[X]] rozumná kompresní kvalita
[[X]] responsive images
[[X]] lazy loading
[[ ]] pevné metadata 72 DPI jako podmínka webu

## Velikost a resampling

Surový RGB obraz má přibližný objem **šířka × výška × počet kanálů × bitová hloubka**. Pro 4000 × 3000 px, tři kanály a 8 bitů vyjde [[36]] MB v desítkovém vyjádření.

Při změně pixelových rozměrů probíhá [[resampling]]. Nearest neighbour zachovává tvrdé pixely, bilineární a bikubická interpolace jsou vhodné pro plynulejší fotografický obraz. AI zvětšování může detail odhadnout, ale nemusí rekonstruovat skutečnost.
